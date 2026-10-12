(() => {
  const search = document.getElementById('guide-search');
  if (!search) return;
  const theme = document.getElementById('guide-theme');
  const type = document.getElementById('guide-type');
  const items = [...document.querySelectorAll('.guide-item')];
  function update() {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;
    items.forEach(item => {
      const matches = item.textContent.toLocaleLowerCase().includes(query)
        && (!theme.value || item.dataset.themes.split('|').includes(theme.value))
        && (!type.value || item.dataset.type === type.value);
      item.hidden = !matches;
      if (matches) visible += 1;
    });
    document.getElementById('guide-count').textContent = `${visible} of ${items.length} source files shown.`;
    document.getElementById('guide-empty').hidden = visible !== 0;
  }
  search.addEventListener('input', update);
  theme.addEventListener('change', update);
  type.addEventListener('change', update);
  document.getElementById('guide-clear').addEventListener('click', () => {
    search.value = ''; theme.value = ''; type.value = ''; update(); search.focus();
  });
  update();
})();
