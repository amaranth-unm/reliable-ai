(() => {
  const workspace = document.getElementById('workspace');
  if (!workspace) return;
  const stages = [...workspace.querySelectorAll('[data-audit-stage]')];
  const files = [...workspace.querySelectorAll('[data-audit-file]')];
  const panels = [...workspace.querySelectorAll('[data-file-panel]')];
  let currentStage = 1;
  function selectFile(id) {
    files.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.auditFile === id)));
    panels.forEach(panel => {
      panel.hidden = panel.dataset.filePanel !== id;
      panel.open = !panel.hidden;
    });
  }
  function selectStage(stage) {
    currentStage = stage;
    stages.forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.auditStage) === stage)));
    workspace.querySelectorAll('[data-stage-note]').forEach(note => { note.hidden = Number(note.dataset.stageNote) !== stage; });
    files.forEach(button => { button.hidden = Number(button.dataset.created) > stage; });
    const newest = files.find(button => Number(button.dataset.created) === stage);
    if (newest) selectFile(newest.dataset.auditFile);
  }
  stages.forEach(button => button.addEventListener('click', () => selectStage(Number(button.dataset.auditStage))));
  files.forEach(button => button.addEventListener('click', () => {
    if (Number(button.dataset.created) <= currentStage) selectFile(button.dataset.auditFile);
  }));
  workspace.classList.add('is-enhanced');
  selectStage(1);
})();
