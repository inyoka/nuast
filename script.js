/**
 * NUAST Computer Science — Homepage Script
 *
 * What this file does:
 *  1. Mobile navigation toggle (hamburger menu)
 *  2. Closes the mobile nav when a link inside it is clicked
 *
 * This file is intentionally kept minimal.
 * No libraries or build step required.
 */

(function () {
  'use strict';

  /* ── Mobile navigation toggle ───────────────────────────── */
  var toggle = document.querySelector('.nav-toggle');
  var nav    = document.getElementById('main-nav');

  if (toggle && nav) {

    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('is-open');
      // Update aria-expanded so screen readers announce the state correctly
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close the menu when any nav link is activated
    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });

    // Close the menu when the user presses Escape
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus(); // return focus to the button
      }
    });
  }

})();
