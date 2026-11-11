Mapping with AI: data files
Reliable AI series, Amaranth, University of New Mexico
https://amaranth.unm.edu/reliable-ai/sessions/mapping-with-ai/

These are the files attached to the prompts in the recorded runs of
11 November 2026. Files marked "AI output" were produced by an earlier
step and checked as the page describes; they are here so you can repeat a
later step without repeating the earlier one.

STEP 2: GHOST TOWNS

nm-ghost-towns-wikipedia-2026-11-11.tsv
  The table copied from Wikipedia's "List of ghost towns in New Mexico",
  https://en.wikipedia.org/wiki/List_of_ghost_towns_in_New_Mexico,
  on 11 November 2026. Text by Wikipedia contributors, CC BY-SA 4.0.

nm-ghost-towns.csv
  AI output: that table as a CSV (66 rows). Derived from Wikipedia,
  CC BY-SA 4.0.

gnis-nm-populated-places.txt
  The 1,601 "Populated Place" records from the USGS Geographic Names
  Information System (GNIS) file for New Mexico, pipe-delimited. US
  government data, public domain. The full state file (all feature
  classes) is at
  https://prd-tnm.s3.amazonaws.com/StagedProducts/GeographicNames/DomesticNames/DomesticNames_NM_Text.zip

nm-ghost-towns-gnis.csv
  AI output: nm-ghost-towns.csv with GNIS IDs, coordinates and match
  notes added. 46 towns matched, 20 left blank.

STEP 3: PHOTOGRAPHS

marrakech-cats-sample.zip
  20 of the 208 phone photographs of cats in Marrakech taken by Jonathan
  Seyfried in March 2026, shared with his permission. All 208 are in his
  repository:
  https://github.com/jeseyfried/cats-of-marrakech/tree/main/assets/images/marrakech-cats

STEP 4: COUNTY POPULATION

nm-county-population-2020-2024.csv
  New Mexico's rows (the state and 33 counties) from the Census Bureau's
  Vintage 2024 county population estimates, co-est2024-alldata.csv,
  trimmed to the population columns. Public domain. Also used in step 6.

us-county-population-2020-2024.csv
  All 3,195 rows of the same file (states and counties), trimmed to
  name, FIPS and the 2020 and 2024 estimates. The full file is at
  https://www2.census.gov/programs-surveys/popest/datasets/2020-2024/counties/totals/co-est2024-alldata.csv

County boundaries (steps 4 and 6) are the Census Bureau's 2023
cartographic boundary file, not included here because of its size
(12 MB):
  https://www2.census.gov/geo/tiger/GENZ2023/shp/cb_2023_us_county_500k.zip

STEP 5: THE 1910 CENSUS

census-1910-nm-cities-table.png
  The table on page 158 of Thirteenth Census of the United States,
  Volume 3: Population (1913), cropped from the IPUMS scan:
  https://usa.ipums.org/usa/resources/voliii/pubdocs/1910/Vol3/36894832v3ch2.pdf
  Public domain.

nm-cities-1860-1910.csv
  AI output: the transcription of that table, checked against the scan.

nm-city-coordinates-gnis.csv
  GNIS records for Albuquerque, Raton, Roswell and Santa Fe.

nm-counties-1900-1910.txt
  The county names in the 1900 and 1910 censuses, compiled from the
  1910 report.
