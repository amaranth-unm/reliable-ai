/* One Markdown <section> per slide. Reveal owns navigation and speaker notes;
   Jekyll renders the Markdown so the deck needs no client-side Markdown plugin. */
(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  Reveal.initialize({
    width: 1280,
    height: 720,
    margin: 0.045,
    minScale: 0.15,
    maxScale: 2,
    center: false,
    display: 'grid',
    hash: true,
    hashOneBasedIndex: true,
    controls: true,
    controlsTutorial: false,
    progress: true,
    slideNumber: 'c/t',
    transition: reducedMotion ? 'none' : 'fade',
    backgroundTransition: 'none',
    // Keep the same presentation on phones. The full tutorial is the reading view.
    scrollActivationWidth: null,
    pdfSeparateFragments: false,
    totalTime: 45 * 60,
    plugins: [RevealNotes]
  });

  document.querySelector('[data-deck-overview]').addEventListener('click', function () {
    Reveal.toggleOverview();
  });
})();
