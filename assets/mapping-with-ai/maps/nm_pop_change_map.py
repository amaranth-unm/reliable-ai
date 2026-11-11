#!/usr/bin/env python3
"""
Choropleth of percent population change, 2020-2024, for New Mexico counties.

Inputs (every number on the map comes from these files):
  * nm-county-population-2020-2024.csv  - Census Bureau Vintage 2024 estimates
  * cb_2023_us_county_500k.zip          - 2023 cartographic boundary file

Outputs: <out>.png (300 dpi) and <out>.pdf, both exactly 6.5 inches wide.

PROJECTION: Albers Equal-Area Conic on the NAD83 datum, fitted to New Mexico
(standard parallels 32.3 N and 36.0 N, origin 34.0 N, central meridian
106.0 W, units metres). An equal-area projection is used so that the area of
shading on the choropleth is proportional to the true area of each county.
The source shapefile is in geographic NAD83 (EPSG:4269) and is reprojected.

Usage:
  python nm_pop_change_map.py
  python nm_pop_change_map.py --csv path/to.csv --boundaries path/to.zip --out figs/nm_pop
"""

import argparse
import sys
from pathlib import Path

import geopandas as gpd
import matplotlib

matplotlib.use("Agg")  # file output only; no display needed
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Patch, Rectangle
from shapely.geometry import box
from shapely.ops import polylabel

# ---------------------------------------------------------------------------
# Design settings (choices about presentation, not data)
# ---------------------------------------------------------------------------
PROJ = (
    "+proj=aea +lat_0=34 +lon_0=-106 +lat_1=32.3 +lat_2=36 "
    "+x_0=0 +y_0=0 +datum=NAD83 +units=m +no_defs"
)

# Interior class breaks in percent. 0 is a break so that every class is
# either all loss or all gain. The outer class limits are the data min/max.
BREAKS = [-3.0, -1.5, 0.0, 1.5, 3.0]

# One colour per class, lowest to highest. Lightness falls steadily from the
# first to the last colour, so the classes stay in order when printed in
# grayscale; the hue change (orange -> blue) marks the switch from loss to gain
# for colour readers. Gray-value check is printed when the script runs.
COLORS = ["#fff1d6", "#fcc98a", "#e8924a", "#4a7fbf", "#2f5f9e", "#0f2f5c"]
MIN_LIGHTNESS_STEP = 10  # minimum CIE L* difference between adjacent classes

FIG_WIDTH_IN = 6.5
FIG_HEIGHT_IN = 5.9
DPI = 300
SOURCE = (
    "Source: U.S. Census Bureau, Vintage 2024 county population estimates; "
    "county boundaries from the 2023 cartographic boundary file"
)

LABEL_SIZES = [6.5, 5.5]  # try the larger size first, then the smaller
MINUS = "−"           # typographic minus sign

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "pdf.fonttype": 42,  # embed TrueType so text stays editable in the PDF
        "ps.fonttype": 42,
    }
)


# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
def load_population(csv_path, base_col):
    # Read everything as text so FIPS codes keep their leading zeros.
    df = pd.read_csv(csv_path, dtype=str, encoding="utf-8")
    end_col = "POPESTIMATE2024"
    for col in (base_col, end_col):
        if col not in df.columns:
            sys.exit(f"Column {col!r} not found in {csv_path}")
        df[col] = pd.to_numeric(df[col], errors="raise")

    df["pct_change"] = (df[end_col] - df[base_col]) / df[base_col] * 100.0

    state = df[df["SUMLEV"] == "040"]
    counties = df[df["SUMLEV"] == "050"].copy()
    counties["GEOID"] = counties["STATE"].str.zfill(2) + counties["COUNTY"].str.zfill(3)
    counties["label"] = counties["CTYNAME"].str.replace(r" County$", "", regex=True)

    state_pct = state["pct_change"].iloc[0] if len(state) else None
    state_fips = counties["STATE"].str.zfill(2).unique()
    if len(state_fips) != 1:
        sys.exit(f"Expected one state in the CSV, found {list(state_fips)}")
    return counties, state_fips[0], state_pct


def load_boundaries(boundary_path, state_fips):
    path = str(boundary_path)
    if path.lower().endswith(".zip"):
        path = f"zip://{Path(path).resolve()}"
    gdf = gpd.read_file(path)
    gdf = gdf[gdf["STATEFP"] == state_fips].copy()
    return gdf.to_crs(PROJ)


def classify(values, breaks):
    """Class index for each value. Classes are [lo, hi), last one closed."""
    return np.digitize(values, breaks, right=False)


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------
def fmt(v, signed=True):
    s = f"{abs(v):.1f}"
    if round(v, 1) == 0:
        return "0.0"
    if v < 0:
        return MINUS + s
    return ("+" if signed else "") + s


def relative_luminance(hex_color):
    rgb = np.array(matplotlib.colors.to_rgb(hex_color))
    lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    return float(lin @ [0.2126, 0.7152, 0.0722])


def lightness(hex_color):
    """CIE L* (0 = black, 100 = white): roughly how light the colour prints in gray."""
    y = relative_luminance(hex_color)
    return 116 * y ** (1 / 3) - 16 if y > 0.008856 else 903.3 * y


def text_color_for(hex_color):
    return "white" if lightness(hex_color) < 50 else "black"


# ---------------------------------------------------------------------------
# Map elements
# ---------------------------------------------------------------------------
def place_labels(ax, fig, gdf):
    """Label each county only if its name fits inside the county polygon."""
    renderer = fig.canvas.get_renderer()
    to_data = ax.transData.inverted()
    skipped = []

    for _, row in gdf.iterrows():
        geom = row.geometry
        # Candidate anchor points: the centroid (if it falls inside the county)
        # and the "pole of inaccessibility", the interior point farthest from
        # the boundary, which suits irregular shapes such as Hidalgo's bootheel.
        main_part = max(getattr(geom, "geoms", [geom]), key=lambda g: g.area)
        anchors = []
        if geom.contains(geom.centroid):
            anchors.append(geom.centroid)
        anchors.append(polylabel(main_part, tolerance=500))

        name = row["label"]
        candidates = [name]
        if " " in name:  # also try breaking a two-word name onto two lines
            candidates.append(name.replace(" ", "\n", 1))

        color = text_color_for(row["fill"])
        halo = "black" if color == "white" else "white"
        placed = False
        # Shrink the polygon a little so labels don't touch the boundary.
        inner = geom.buffer(-1500)
        attempts = [(s, txt, a) for s in LABEL_SIZES for txt in candidates for a in anchors]
        for size, text, anchor in attempts:
            t = ax.text(
                anchor.x, anchor.y, text, ha="center", va="center",
                fontsize=size, color=color, linespacing=0.95, zorder=5,
                path_effects=[pe.withStroke(linewidth=1.2, foreground=halo, alpha=0.35)],
            )
            bb = t.get_window_extent(renderer).transformed(to_data)
            if inner.contains(box(bb.x0, bb.y0, bb.x1, bb.y1)):
                placed = True
                break
            t.remove()
        if not placed:
            skipped.append(name)
    return skipped


def add_scale_bar(ax, x0, y0, km_len=100, mi_len=50, height=4000):
    """Two-unit scale bar drawn in projected metres (true near map centre)."""
    style = dict(fontsize=6.5, va="top", ha="center")

    # Kilometres, alternating black/white segments
    seg = km_len / 2 * 1000
    for i in range(2):
        ax.add_patch(Rectangle((x0 + i * seg, y0), seg, height,
                               facecolor="black" if i == 0 else "white",
                               edgecolor="black", linewidth=0.6, zorder=6))
    for i, v in enumerate([0, km_len / 2, km_len]):
        ax.text(x0 + i * seg, y0 - 2500, f"{v:g}" + (" km" if i == 2 else ""),
                **style, zorder=6)

    # Miles, directly beneath
    y1 = y0 - 22000
    mseg = mi_len / 2 * 1609.344
    for i in range(2):
        ax.add_patch(Rectangle((x0 + i * mseg, y1), mseg, height,
                               facecolor="black" if i == 0 else "white",
                               edgecolor="black", linewidth=0.6, zorder=6))
    for i, v in enumerate([0, mi_len / 2, mi_len]):
        ax.text(x0 + i * mseg, y1 - 2500, f"{v:g}" + (" mi" if i == 2 else ""),
                **style, zorder=6)


def build_legend_handles(values, breaks, colors):
    lo, hi = float(np.min(values)), float(np.max(values))
    edges = [min(lo, breaks[0])] + list(breaks) + [max(hi, breaks[-1])]
    cls = classify(values, breaks)
    handles = []
    for i, c in enumerate(colors):
        n = int(np.sum(cls == i))
        label = f"{fmt(edges[i])} to {fmt(edges[i + 1])}   ({n})"
        handles.append(Patch(facecolor=c, edgecolor="#333333", linewidth=0.5, label=label))
    return handles[::-1]  # highest class at top


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    here = Path.cwd()
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[1].strip())
    ap.add_argument("--csv", default=here / "nm-county-population-2020-2024.csv", type=Path)
    ap.add_argument("--boundaries", default=here / "cb_2023_us_county_500k.zip", type=Path,
                    help="Zipped shapefile, .shp, or any file geopandas can read")
    ap.add_argument("--out", default=here / "nm_population_change_2020_2024", type=Path,
                    help="Output path without extension")
    ap.add_argument("--base", choices=["july2020", "april2020"], default="july2020",
                    help="Starting population: July 1, 2020 estimate (default) or the "
                         "April 1, 2020 estimates base")
    args = ap.parse_args()

    if len(COLORS) != len(BREAKS) + 1:
        sys.exit("COLORS must have exactly one more entry than BREAKS")
    lstar = [lightness(c) for c in COLORS]
    if any(a - b < MIN_LIGHTNESS_STEP for a, b in zip(lstar, lstar[1:])):
        sys.exit("COLORS must get darker from first to last by at least "
                 f"{MIN_LIGHTNESS_STEP} L* per step to stay distinct in grayscale")
    print("Class lightness (CIE L*):", ", ".join(f"{v:.0f}" for v in lstar))

    base_col = "POPESTIMATE2020" if args.base == "july2020" else "ESTIMATESBASE2020"
    base_desc = "July 1, 2020" if args.base == "july2020" else "April 1, 2020 (estimates base)"

    pop, state_fips, state_pct = load_population(args.csv, base_col)
    shapes = load_boundaries(args.boundaries, state_fips)

    gdf = shapes.merge(pop[["GEOID", "label", "pct_change"]], on="GEOID", how="outer",
                       indicator=True)
    unmatched = gdf[gdf["_merge"] != "both"]
    if len(unmatched):
        sys.exit("CSV and boundary file do not match for GEOIDs: "
                 + ", ".join(unmatched["GEOID"].astype(str)))
    gdf = gpd.GeoDataFrame(gdf.drop(columns="_merge"), geometry="geometry", crs=shapes.crs)

    gdf["cls"] = classify(gdf["pct_change"].to_numpy(), BREAKS)
    gdf["fill"] = [COLORS[i] for i in gdf["cls"]]

    # ---- figure layout (fixed size; not using bbox_inches="tight" so the
    # saved width is exactly FIG_WIDTH_IN) ----
    fig = plt.figure(figsize=(FIG_WIDTH_IN, FIG_HEIGHT_IN), dpi=DPI)
    ax = fig.add_axes([0.01, 0.07, 0.66, 0.84])
    ax.set_axis_off()

    gdf.plot(ax=ax, color=gdf["fill"], edgecolor="#4d4d4d", linewidth=0.35, zorder=2)
    gdf.dissolve().boundary.plot(ax=ax, color="black", linewidth=0.9, zorder=3)

    xmin, ymin, xmax, ymax = gdf.total_bounds
    pad = 0.02 * (xmax - xmin)
    ax.set_xlim(xmin - pad, xmax + pad)
    ax.set_ylim(ymin - pad, ymax + pad)
    ax.set_aspect("equal")
    fig.canvas.draw()  # fix the transforms before measuring label sizes

    skipped = place_labels(ax, fig, gdf)

    # Scale bar in the empty strip below the southern border, east of the
    # bootheel (the state's southern edge there is ~0.6 degrees above ymin).
    add_scale_bar(ax, xmin + 0.45 * (xmax - xmin), ymin + 0.065 * (ymax - ymin))

    # ---- title ----
    fig.text(0.01, 0.975, "Population change in New Mexico counties, 2020–2024",
             fontsize=10.5, fontweight="bold", va="top", ha="left")
    fig.text(0.01, 0.938, f"Percent change in resident population, {base_desc} to July 1, 2024",
             fontsize=7.5, va="top", ha="left", color="#333333")

    # ---- legend ----
    handles = build_legend_handles(gdf["pct_change"].to_numpy(), BREAKS, COLORS)
    leg = fig.legend(
        handles=handles, loc="upper left", bbox_to_anchor=(0.685, 0.86),
        title="Percent change\n(number of counties)", title_fontsize=7.5, fontsize=7,
        frameon=False, alignment="left", handlelength=2.2, handleheight=1.6,
        labelspacing=0.35, borderaxespad=0,
    )
    leg.get_title().set_linespacing(1.2)

    notes = []
    if state_pct is not None:
        notes.append(f"New Mexico overall: {fmt(state_pct)}%")
    notes.append("Classes include the lower limit\nand exclude the upper limit.")
    if skipped:
        notes.append("Not labeled (too small):\n" + ", ".join(sorted(skipped)))
    fig.text(0.69, 0.53, "\n\n".join(notes), fontsize=6.5, va="top", ha="left",
             color="#222222", linespacing=1.25)

    # ---- source line ----
    fig.text(0.01, 0.02, SOURCE, fontsize=6, va="bottom", ha="left", color="#333333")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".png"), dpi=DPI)
    fig.savefig(out.with_suffix(".pdf"))
    plt.close(fig)

    print(f"Wrote {out.with_suffix('.png')} and {out.with_suffix('.pdf')}")
    if skipped:
        print("Counties not labeled because the name did not fit:", ", ".join(sorted(skipped)))


if __name__ == "__main__":
    main()
