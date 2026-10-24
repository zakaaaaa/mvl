(function () {
  // Mobile nav
  var toggle = document.querySelector('.nav-toggle');
  var menu = document.querySelector('.mobile-menu');
  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      var open = menu.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.querySelector('i').className = open ? 'ph ph-x' : 'ph ph-list';
    });
  }

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && items.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Lightbox (gallery)
  var lb = document.querySelector('.lightbox');
  if (lb) {
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('figcaption');
    document.querySelectorAll('[data-lightbox]').forEach(function (a) {
      a.addEventListener('click', function (ev) {
        ev.preventDefault();
        lbImg.src = a.getAttribute('href');
        lbImg.alt = a.getAttribute('data-caption') || '';
        lbCap.textContent = a.getAttribute('data-caption') || '';
        lb.classList.add('open');
        document.body.style.overflow = 'hidden';
      });
    });
    function close() { lb.classList.remove('open'); document.body.style.overflow = ''; }
    lb.querySelector('button').addEventListener('click', close);
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  }

  // Contact form -> WhatsApp
  var form = document.querySelector('#wa-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var msg = 'Halo CV. Mitra Viktory Logam,%0A%0A' +
        'Nama: ' + encodeURIComponent(f.get('nama')) + '%0A' +
        'Perusahaan: ' + encodeURIComponent(f.get('perusahaan') || '-') + '%0A' +
        'Kebutuhan: ' + encodeURIComponent(f.get('kebutuhan')) + '%0A%0A' +
        encodeURIComponent(f.get('pesan'));
      window.open('https://wa.me/6281262936355?text=' + msg, '_blank', 'noopener');
    });
  }
})();
