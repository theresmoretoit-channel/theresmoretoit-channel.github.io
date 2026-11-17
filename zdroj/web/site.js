// There's More To It — drobnosti webu: přehrávač až po kliknutí, časy kapitol,
// časová osa podél textu a hledání v seznamu videí. Bez JS web funguje taky:
// náhled i časy jsou obyčejné odkazy na YouTube.
(function () {
  var player = document.querySelector('.player');
  var klidne = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function prehraj(t) {
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + player.dataset.id +
      '?autoplay=1&rel=0' + (t ? '&start=' + t : '') + (player.dataset.params || '');
    f.title = player.dataset.title;
    f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
    f.allowFullscreen = true;
    player.replaceChildren(f);
    f.focus();
  }

  if (player) {
    player.querySelector('.player-box').addEventListener('click', function (e) {
      e.preventDefault();
      prehraj(0);
    });
    document.querySelectorAll('a[data-t]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        e.preventDefault();
        prehraj(+a.dataset.t);
        player.scrollIntoView({ behavior: klidne ? 'auto' : 'smooth', block: 'center' });
      });
    });
  }

  var text = document.querySelector('.transcript');
  var fill = document.querySelector('.rail-fill');
  if (text && fill) {
    var hlavy = Array.prototype.slice.call(text.querySelectorAll('.ch h2'));
    var ceka = false;
    var obnov = function () {
      ceka = false;
      var r = text.getBoundingClientRect();
      var cara = window.innerHeight * 0.45;
      var p = Math.min(1, Math.max(0, (cara - r.top) / r.height));
      fill.style.transform = 'scaleY(' + p + ')';
      hlavy.forEach(function (h) { h.classList.toggle('passed', h.getBoundingClientRect().top < cara); });
    };
    var naplanuj = function () { if (!ceka) { ceka = true; requestAnimationFrame(obnov); } };
    window.addEventListener('scroll', naplanuj, { passive: true });
    window.addEventListener('resize', naplanuj);
    obnov();
  }

  var q = document.getElementById('q');
  if (q) {
    var polozky = Array.prototype.slice.call(document.querySelectorAll('.all .vlist li'));
    var prazdno = document.querySelector('.empty');
    var norm = function (s) { return s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase(); };
    polozky.forEach(function (li) { li.dataset.q = norm(li.textContent); });
    q.addEventListener('input', function () {
      var v = norm(q.value.trim()), n = 0;
      polozky.forEach(function (li) {
        var ok = !v || li.dataset.q.indexOf(v) >= 0;
        li.hidden = !ok;
        if (ok) n++;
      });
      prazdno.hidden = n > 0;
    });
  }
})();
