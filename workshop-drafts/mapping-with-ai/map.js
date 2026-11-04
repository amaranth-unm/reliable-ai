'use strict';
const collection = JSON.parse(document.getElementById('collection-data').textContent);
const records = collection.records;
const $ = id => document.getElementById(id);
const node = (tag, text, className) => { const el = document.createElement(tag); if (text !== undefined) el.textContent = text; if (className) el.className = className; return el; };
const located = r => Number.isFinite(r.lat) && Number.isFinite(r.lon);
function link(text, url) {
  const a = node('a', text);
  try { const u = new URL(url); if (!['https:', 'http:'].includes(u.protocol)) return node('span', text); a.href = u.href; } catch { return node('span', text); }
  a.target = '_blank'; a.rel = 'noopener noreferrer'; return a;
}
$('description').textContent = collection.description;
$('provenance').textContent = collection.provenance;
if (collection.kind === 'monuments') {
  $('category-label').firstChild.textContent = 'Commemoration';
  $('photo-footer').append(link('Photo reuse: National Park Service disclaimer.', 'https://www.nps.gov/aboutus/disclaimer.htm'));
}
[...new Set(records.map(r => r.category))].sort().forEach(c => { const o = node('option', c); o.value = c; $('category').append(o); });
let map = null, layer = null;
if (typeof L !== 'undefined') {
  try {
    map = L.map('map', {scrollWheelZoom: false}).setView(collection.kind === 'research' ? [37,-98] : [38.892,-77.039], collection.kind === 'research' ? 3 : 14);
    layer = L.layerGroup().addTo(map);
    const tiles = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {maxZoom:19, attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
    tiles.on('tileerror', () => { $('map-status').textContent = 'Some background tiles could not load. Use the collection list and source links.'; });
    $('map-status').textContent = 'Select a point or use the list. Numbers on points count references or sites sharing that location.';
  } catch { $('map-status').textContent = 'The map could not start. All records remain available below.'; map = null; }
} else { $('map-status').textContent = 'The map library could not load. All records remain available in the list.'; }
function content(r, popup=false) {
  const box = node('div');
  box.append(node(popup ? 'h3' : 'h2', r.title));
  box.append(node('span', r.category, 'badge'));
  if (!located(r)) box.append(node('span', 'Unlocated', 'badge unknown'));
  if (collection.kind === 'research') {
    box.append(node('p', `${r.source_id} · ${r.date} · ${r.id}`, 'meta'));
    box.append(node('blockquote', r.quote));
    box.append(node('p', `Source wording: ${r.wording}`, 'meta'));
  } else {
    box.append(node('p', r.description));
    box.append(node('p', `Dedication date: ${r.date || 'Not supplied in this sample'}`, 'meta'));
    if (!popup) {
      (collection.photographs || []).filter(p => p.monument_id === r.id).forEach(p => {
        const f = node('figure'), a = link('', p.url), img = node('img');
        img.src = p.url; img.alt = p.alt; img.loading = 'lazy';
        img.addEventListener('error', () => { img.hidden = true; a.textContent = 'Photograph could not load. Open original image.'; });
        a.append(img); const cap = node('figcaption', `${p.id} · ${p.credit}. `);
        cap.append(link('Photo source', p.source_url)); cap.append(node('p', p.rights_note)); f.append(a, cap); box.append(f);
      });
    }
    box.append(link(r.source_label, r.source_url));
  }
  box.append(node('p', r.location_note, 'meta'));
  return box;
}
let visible = records;
function render() {
  const query = $('search').value.trim().toLocaleLowerCase();
  visible = records.filter(r => {
    const photos = (collection.photographs || []).filter(p => p.monument_id === r.id);
    return (!$('category').value || r.category === $('category').value) &&
      (!$('located').value || located(r) === ($('located').value === 'yes')) &&
      JSON.stringify([r, photos]).toLocaleLowerCase().includes(query);
  });
  $('results').replaceChildren();
  const groups = new Map();
  visible.filter(located).forEach(r => { const key = `${r.lat},${r.lon}`; if (!groups.has(key)) groups.set(key, []); groups.get(key).push(r); });
  const n = visible.length, unlocated = visible.filter(r => !located(r)).length;
  const photoCount = (collection.photographs || []).filter(p => visible.some(r => r.id === p.monument_id)).length;
  $('count').textContent = `${n} of ${records.length} ${collection.kind === 'research' ? 'references' : 'monuments'} · ${groups.size} map locations · ${unlocated} unlocated${collection.kind === 'monuments' ? ` · ${photoCount} photographs` : ''}`;
  if (map) { map.closePopup(); layer.clearLayers(); }
  if (!n) $('results').append(node('p', 'No records match. Clear the search or reset the filters.', 'empty'));
  visible.forEach(r => {
    const article = node('article', undefined, 'record'); article.id = `record-${r.id}`; article.append(content(r));
    if (map && located(r)) {
      const b = node('button', 'Show on map'); b.type = 'button'; b.setAttribute('aria-label', `Show ${r.title}, ${r.id}, on map`);
      b.onclick = () => { map.setView([r.lat,r.lon], collection.kind === 'research' ? 8 : 16); L.popup().setLatLng([r.lat,r.lon]).setContent(content(r,true)).openOn(map); $('map').scrollIntoView({block:'center', behavior:'smooth'}); };
      article.append(b);
    }
    $('results').append(article);
  });
  if (map) {
    const points = [];
    groups.forEach(group => {
      const r = group[0], popup = node('div');
      group.forEach(item => { popup.append(content(item,true)); const a = node('a','Read collection entry'); a.href=`#record-${item.id}`; popup.append(a); });
      L.marker([r.lat,r.lon], {title: group.map(item=>item.title).join('; '),alt:group.map(item=>item.title).join('; '),icon:L.divIcon({className:'pin',html:String(group.length),iconSize:[30,30]})}).bindPopup(popup).addTo(layer);
      points.push([r.lat,r.lon]);
    });
    if (points.length) map.fitBounds(points, {padding:[30,30],maxZoom:collection.kind === 'research' ? 8 : 15});
  }
}
['search','category','located'].forEach(id => $(id).addEventListener(id === 'search' ? 'input' : 'change', render));
$('reset').onclick = () => { $('search').value=''; $('category').value=''; $('located').value=''; render(); };
$('download').onclick = () => {
  const url = URL.createObjectURL(new Blob([JSON.stringify(collection,null,2)+'\n'],{type:'application/json'}));
  const a = node('a'); a.href=url; a.download=collection.kind === 'research' ? 'research-reviewed.json' : 'monuments.json'; a.click(); setTimeout(()=>URL.revokeObjectURL(url),1000);
};
render();
