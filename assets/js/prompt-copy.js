/* Copy buttons on .prompt blocks.
   Reads the rendered text rather than a data attribute so what lands on the
   clipboard is exactly what the reader sees in the box. */
(function () {
  'use strict';

  function flash(btn, message) {
    var label = btn.querySelector('.prompt-copy-text');
    var original = label ? label.getAttribute('data-original') || label.textContent : null;
    if (label) {
      label.setAttribute('data-original', original);
      label.textContent = message;
    }
    btn.classList.add('is-copied');
    window.setTimeout(function () {
      if (label && original !== null) { label.textContent = original; }
      btn.classList.remove('is-copied');
    }, 1600);
  }

  /* execCommand is deprecated, but it's the only thing that works when the page
     isn't in a secure context — someone serving the site over plain http on a
     classroom machine, for instance. Chrome keeps transient user activation
     alive for a few seconds, so this still works when called from the timeout
     below rather than directly in the click handler. */
  function legacyCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.top = '0';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    return ok;
  }

  /* writeText() can sit unsettled when the clipboard permission is pending,
     which would leave the button doing nothing visible at all. Racing it
     guarantees the reader always gets an answer. */
  function withTimeout(promise, ms) {
    return new Promise(function (resolve, reject) {
      var settled = false;
      var timer = window.setTimeout(function () {
        if (!settled) { settled = true; reject(new Error('clipboard timeout')); }
      }, ms);
      promise.then(
        function (value) {
          if (!settled) { settled = true; window.clearTimeout(timer); resolve(value); }
        },
        function (err) {
          if (!settled) { settled = true; window.clearTimeout(timer); reject(err); }
        }
      );
    });
  }

  document.addEventListener('click', function (event) {
    var btn = event.target.closest('[data-prompt-copy]');
    if (!btn) { return; }

    var block = btn.closest('.prompt');
    var code = block && block.querySelector('.prompt-text code');
    if (!code) { return; }

    var text = code.innerText;

    var fallback = function () {
      flash(btn, legacyCopy(text) ? 'Copied' : 'Select and copy');
    };

    if (navigator.clipboard && window.isSecureContext) {
      withTimeout(navigator.clipboard.writeText(text), 600).then(
        function () { flash(btn, 'Copied'); },
        fallback
      );
    } else {
      fallback();
    }
  });
})();
