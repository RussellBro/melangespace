// Melange Space. Small and dependency-free: the day and night toggle,
// scroll reveals, a little hero parallax, and a nav that steps aside on scroll down.
(function () {
  var root = document.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Day and night toggle. The first paint is handled inline in <head>.
  var toggle = document.querySelector('.mode');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = root.dataset.mode === 'night' ? 'day' : 'night';
      root.dataset.mode = next;
      try { localStorage.setItem('mode', next); } catch (e) {}
    });
  }
  // Follow the system if the visitor has not chosen
  if (window.matchMedia) {
    var mq = matchMedia('(prefers-color-scheme: dark)');
    var follow = function (e) {
      var chosen = null;
      try { chosen = localStorage.getItem('mode'); } catch (err) {}
      if (!chosen) root.dataset.mode = e.matches ? 'night' : 'day';
    };
    if (mq.addEventListener) mq.addEventListener('change', follow);
  }

  // Reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    reveals.forEach(function (el) { io.observe(el); });
  }

  if (reduce) return;

  var nav = document.getElementById('nav');
  var heroCopy = document.querySelector('.hero-copy');
  var lastY = window.scrollY;
  var ticking = false;

  function frame() {
    ticking = false;
    var y = window.scrollY;
    var vh = window.innerHeight;
    if (heroCopy && y < vh * 1.2) heroCopy.style.setProperty('--copy-y', (y * -0.18).toFixed(1) + 'px');
    if (y > vh * 0.35 && y > lastY + 4) nav.classList.add('is-hidden');
    else if (y < lastY - 4 || y < vh * 0.35) nav.classList.remove('is-hidden');
    lastY = y;
  }

  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(frame); }
  }, { passive: true });
  frame();
})();
