# Assembles site/*.html from shared header/footer + per-page bodies.
import os
OUT = os.environ.get('MVL_OUT') or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')
WA_AGE = 'https://wa.me/6281262936355'
WA_VIK = 'https://wa.me/6281228413881'
WA_MSG = WA_AGE + '?text=' + 'Halo%20CV.%20Mitra%20Viktory%20Logam%2C%20saya%20ingin%20menanyakan%20pembuatan%20'
FB = 'https://www.facebook.com/kuli.logam.2025'
IG = 'https://www.instagram.com/cvmitraviktorylogam/'
TT = 'https://www.tiktok.com/@cv.mitra.viktory'
ADDR = 'Jl. Andansari Gg. Bersama, Terjun, Hamparan Perak, Kab. Deli Serdang, Sumatera Utara'
MAPS_Q = 'Jl.+Andansari,+Terjun,+Hamparan+Perak,+Deli+Serdang,+Sumatera+Utara'
MAPS_URL = 'https://www.google.com/maps/search/?api=1&query=' + MAPS_Q
MAPS_EMBED = 'https://www.google.com/maps?q=' + MAPS_Q + '&z=16&output=embed'

NAV = [('index.html', 'Beranda'), ('tentang.html', 'Tentang'), ('produk.html', 'Produk'),
       ('proses.html', 'Proses & Fasilitas'), ('galeri.html', 'Galeri'), ('kontak.html', 'Kontak')]

SITE = 'https://mitraviktorylogam.com'

def head(title, desc):
    return f'''<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="__CANONICAL__">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="ID-SU">
<meta name="geo.placename" content="Hamparan Perak, Deli Serdang">
<meta name="theme-color" content="#d4a93c">
<meta property="og:type" content="website">
<meta property="og:locale" content="id_ID">
<meta property="og:site_name" content="CV. Mitra Viktory Logam">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="__CANONICAL__">
<meta property="og:image" content="__OGIMAGE__">
<meta property="og:image:width" content="__OGW__">
<meta property="og:image:height" content="__OGH__">
<meta property="og:image:alt" content="CV. Mitra Viktory Logam, pengecoran kuningan dan bronze">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="__OGIMAGE__">
<link rel="icon" type="image/png" href="img/logo.png">
<link rel="apple-touch-icon" href="img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">
<link rel="stylesheet" href="css/style.css?v=10">
<!--SCHEMA-->
</head>
<body>
'''

def header(current):
    links = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    return f'''<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="CV. Mitra Viktory Logam, ke beranda">
      <img src="img/logo.png" alt="Logo CV. Mitra Viktory Logam" width="56" height="45">
      <span>Mitra Viktory Logam</span>
    </a>
    <nav class="nav-links" aria-label="Navigasi utama">{links}</nav>
    <a class="btn btn-primary nav-cta" href="{WA_MSG}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a>
    <button class="nav-toggle" aria-label="Buka menu" aria-expanded="false"><i class="ph ph-list"></i></button>
  </div>
  <div class="mobile-menu">
    {links}
    <a class="btn btn-primary" href="{WA_MSG}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a>
  </div>
</header>
<main>
'''

FOOTER = f'''</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="index.html"><img src="img/logo.png" alt="Logo CV. Mitra Viktory Logam"></a>
        <p>Jasa pengecoran kuningan dan bronze untuk sparepart kapal, pabrik kelapa sawit, dan kebutuhan industri lainnya. Pengerjaan cepat dengan harga bersaing.</p>
      </div>
      <div>
        <h4>Halaman</h4>
        <ul>
          <li><a href="tentang.html">Tentang Kami</a></li>
          <li><a href="produk.html">Produk</a></li>
          <li><a href="proses.html">Proses & Fasilitas</a></li>
          <li><a href="galeri.html">Galeri</a></li>
          <li><a href="kontak.html">Kontak</a></li>
        </ul>
      </div>
      <div>
        <h4>Hubungi Kami</h4>
        <ul>
          <li><i class="ph ph-whatsapp-logo"></i><a href="{WA_AGE}" target="_blank" rel="noopener">0812-6293-6355 (Age)</a></li>
          <li><i class="ph ph-whatsapp-logo"></i><a href="{WA_VIK}" target="_blank" rel="noopener">0812-2841-3881 (Viktor)</a></li>
          <li><i class="ph ph-facebook-logo"></i><a href="{FB}" target="_blank" rel="noopener">Mitra Viktory Logam</a></li>
          <li><i class="ph ph-instagram-logo"></i><a href="{IG}" target="_blank" rel="noopener">@cvmitraviktorylogam</a></li>
          <li><i class="ph ph-tiktok-logo"></i><a href="{TT}" target="_blank" rel="noopener">@cv.mitra.viktory</a></li>
          <li><i class="ph ph-map-pin"></i><a href="{MAPS_URL}" target="_blank" rel="noopener">{ADDR}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 CV. Mitra Viktory Logam. Hak cipta dilindungi.</span>
    </div>
  </div>
</footer>
<a class="wa-float" href="{WA_MSG}" target="_blank" rel="noopener" aria-label="Chat WhatsApp"><i class="ph-fill ph-whatsapp-logo"></i><span>Chat WhatsApp</span></a>
<script src="js/main.js"></script>
</body>
</html>
'''

import json as _json, re as _re
DATA = os.environ.get('MVL_DATA') or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'products.json')
PROD = _json.load(open(DATA, encoding='utf-8'))

def _slugify(s):
    return _re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

for _p in PROD:  # fill anything the admin left empty
    _p.setdefault('gallery', [])
    _p['h1'] = _p.get('h1') or _p['name']
    _p['page'] = _p.get('page') or (_slugify(_p['h1']) + '-medan.html')
    _p['title'] = _p.get('title') or f"{_p['h1']} Medan | Mitra Viktory Logam"
    _p['short'] = _p.get('short') or f"{_p['name']} dari {_p['material'].lower()}, dicor dan dibubut sesuai ukuran."
    _p['desc'] = _p.get('desc') or (f"Pembuatan {_p['name'].lower()} di Medan dan Deli Serdang oleh CV. Mitra Viktory Logam. " + _p['short'])[:158]
    _p['intro'] = [t for t in _p.get('intro', []) if t.strip()] or [_p['short'], 'Dikerjakan dengan cor dan bubut di workshop kami di Hamparan Perak, Deli Serdang. Ukuran mengikuti sampel atau gambar teknik dari Anda.']
    _p['uses'] = [t for t in _p.get('uses', []) if t.strip()]
    _p['faq'] = _p.get('faq', [])

PRODUCTS = [(_p['image'], _p['name'], _p['material'], _p['short']) for _p in PROD]

# ---------- site photos (editable in admin "Foto Website") ----------
SITE_SLOTS = [
    ('hero', 'Foto utama beranda', 'Foto besar paling atas di beranda', 'hero-pour-v3.jpg'),
    ('peleburan', 'Proses: Peleburan', 'Beranda, halaman Proses, Galeri', 'proses-peleburan.jpg'),
    ('cetak', 'Proses: Cetakan Pasir', 'Beranda, halaman Proses, Galeri', 'proses-cetak-pasir-1.jpg'),
    ('penuangan', 'Proses: Penuangan', 'Beranda, halaman Proses, Tentang, Galeri', 'proses-cetak-pasir-2.jpg'),
    ('bubut', 'Proses: Pembubutan', 'Beranda, halaman Proses, Galeri', 'proses-bubut-2.jpg'),
    ('alasan', 'Foto "Kenapa pelanggan kembali"', 'Beranda, halaman Tentang, Proses, Galeri', 'proses-bubut-1.jpg'),
]
_SI = os.environ.get('MVL_SITEIMG') or os.path.join(os.path.dirname(os.path.abspath(DATA)), 'site_images.json')
try:
    _SITEIMG = _json.load(open(_SI, encoding='utf-8'))
except Exception:
    _SITEIMG = {}

def IMG(slot):
    for k, _, _, d in SITE_SLOTS:
        if k == slot:
            return _SITEIMG.get(slot) or d
    raise KeyError(slot)


# ---------- SEO: product detail pages + FAQ ----------
import json, html as _html

# key = product name in PRODUCTS
PDETAIL = {_p['name']: _p for _p in PROD}

SHARED_FAQ = [
 ('Di mana lokasi workshop dan apakah melayani Medan?', 'Workshop kami ada di Jl. Andansari Gg. Bersama, Terjun, Hamparan Perak, Deli Serdang, dekat Medan. Kami melayani Medan, Belawan, Deli Serdang, dan wilayah Sumatera Utara lainnya.'),
 ('Bagaimana cara pesan dan mengetahui harganya?', 'Kirim foto sampel beserta ukuran, atau gambar teknik, lewat WhatsApp. Kami balas dengan estimasi harga dan waktu pengerjaan.'),
 ('Apakah bisa dikirim ke luar kota?', 'Bisa. Pesanan bisa diambil di workshop atau dikirim lewat ekspedisi ke lokasi Anda.'),
]

HOME_FAQ = [
 SHARED_FAQ[0],
 ('Produk apa saja yang bisa dibuat?', ', '.join(n for _, n, _, _ in PRODUCTS) + ', serta komponen custom lain dari kuningan atau bronze.'),
 ('Apakah bisa pesan satuan?', 'Bisa. Kami melayani pesanan satu buah untuk penggantian darurat hingga jumlah banyak untuk stok pabrik.'),
 ('Bahan apa yang dipakai, kuningan atau bronze?', 'Keduanya. Kuningan untuk komponen mesin umum yang ekonomis, bronze untuk bagian yang menahan beban berat atau terkena air laut.'),
 SHARED_FAQ[1],
 SHARED_FAQ[2],
]

def faq_html(items):
    return ''.join(f'''
      <details>
        <summary>{q}<i class="ph ph-plus"></i></summary>
        <p>{a}</p>
      </details>''' for q, a in items)

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>'

def faq_schema(items):
    return {'@context': 'https://schema.org', '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in items]}


def bento_html():
    cells = [('wide tall', 'lt'), ('', 'lt'), ('', 'lt'), ('', 'lt'), ('', 'lt'), ('wide', 'wide'), ('wide', 'wide')]
    out = ''
    for (cls, var), (img, name, mat, short) in zip(cells, PRODUCTS):
        d = PDETAIL[name]
        out += f'''
      <a class="bento-item {cls} reveal" href="{d['page']}"><img src="img/{img}-{var}.jpg" alt="{d['h1']}" loading="lazy"><span class="cap">{name}</span></a>'''
    return out


# ---------- INDEX ----------
index = head('Pengecoran Kuningan & Bronze Medan | CV. Mitra Viktory Logam',
             'Jasa pengecoran kuningan dan bronze di Medan dan Deli Serdang. Cutless bearing, stuffing box, bushing, shaft, sparepart kapal dan PKS sesuai ukuran.') + header('index.html') + f'''
<section class="hero">
  <img class="hero-bg" src="img/{IMG('hero')}" alt="Penuangan logam cair di workshop pengecoran kuningan dan bronze" width="1600" height="897" fetchpriority="high">
  <div class="container hero-content">
    <h1 class="h-display">Pengecoran kuningan dan bronze di Medan untuk sparepart kapal dan industri</h1>
    <p class="lead">Bushing, stuffing box, cutless bearing, shaft, dan komponen custom. Dicor dan dibubut sendiri di Deli Serdang, selesai cepat, harga bersaing.</p>
    <div class="hero-actions">
      <a class="btn btn-primary" href="{WA_MSG}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a>
      <a class="btn btn-ghost" href="produk.html">Lihat Produk<i class="ph ph-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h-section">Industri yang kami layani</h2>
    </div>
    <div class="industry-grid">
      <div class="industry-item reveal">
        <i class="ph ph-boat"></i>
        <div><h3>Perkapalan</h3><p>Cutless bearing, stuffing box, sleeve, dan shaft bronze yang tahan air laut untuk kapal kayu maupun besi.</p></div>
      </div>
      <div class="industry-item reveal">
        <i class="ph ph-factory"></i>
        <div><h3>Pabrik Kelapa Sawit</h3><p>Bushing dan bantalan kuningan untuk mesin press, conveyor, dan peralatan pengolahan sawit.</p></div>
      </div>
      <div class="industry-item reveal">
        <i class="ph ph-gear"></i>
        <div><h3>Industri Umum</h3><p>Komponen custom dari sampel atau gambar teknik untuk pompa, bengkel, dan mesin produksi.</p></div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h-section">Produk yang sering kami kerjakan</h2>
      <p class="lead">Semua produk dicor dari bahan kuningan atau bronze, lalu dibubut hingga ukuran akhir. Ukuran mengikuti sampel atau gambar dari Anda.</p>
    </div>
    <div class="bento">{bento_html()}
    </div>
    <div style="margin-top:28px" class="reveal">
      <a class="btn btn-ghost" href="produk.html">Semua Produk<i class="ph ph-arrow-right"></i></a>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h-section">Dari logam cair sampai komponen siap pasang</h2>
      <p class="lead">Seluruh tahap dikerjakan di workshop kami sendiri, jadi ukuran dan waktu pengerjaan ada dalam kendali kami.</p>
    </div>
    <div class="steps">
      <div class="step reveal"><img src="img/{IMG('peleburan')}" alt="Peleburan kuningan di tungku" loading="lazy"><h3>Peleburan</h3><p>Bahan kuningan atau bronze dilebur di tungku hingga suhu cor.</p></div>
      <div class="step reveal"><img src="img/{IMG('cetak')}" alt="Pembuatan cetakan pasir" loading="lazy"><h3>Cetakan Pasir</h3><p>Cetakan dibuat mengikuti sampel atau pola sesuai gambar teknik.</p></div>
      <div class="step reveal"><img src="img/{IMG('penuangan')}" alt="Penuangan logam ke cetakan" loading="lazy"><h3>Penuangan</h3><p>Logam cair dituang ke cetakan, didinginkan, lalu dibongkar dan dibersihkan.</p></div>
      <div class="step reveal"><img src="img/{IMG('bubut')}" alt="Pembubutan hasil cor" loading="lazy"><h3>Pembubutan</h3><p>Hasil cor dibubut hingga diameter dan toleransi yang diminta, siap dipasang.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="split-media reveal"><img src="img/{IMG('alasan')}" alt="Operator membubut komponen bronze" loading="lazy"></div>
    <div class="reveal">
      <h2 class="h-section">Kenapa pelanggan kembali ke kami</h2>
      <div class="points">
        <div class="point"><i class="ph ph-lightning"></i><div><h3>Pengerjaan cepat</h3><p>Cor dan bubut dalam satu workshop, tanpa menunggu antrian vendor lain.</p></div></div>
        <div class="point"><i class="ph ph-tag"></i><div><h3>Harga langsung dari pengrajin</h3><p>Tidak ada perantara, harga mengikuti berat bahan dan tingkat kerumitan.</p></div></div>
        <div class="point"><i class="ph ph-ruler"></i><div><h3>Mengikuti sampel atau gambar</h3><p>Cukup kirim foto sampel dengan ukuran, atau gambar teknik. Kami buatkan sesuai itu.</p></div></div>
        <div class="point"><i class="ph ph-package"></i><div><h3>Satuan maupun batch</h3><p>Melayani pesanan satu buah untuk penggantian darurat hingga jumlah banyak untuk stok.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container faq-wrap">
    <div class="reveal">
      <h2 class="h-section">Pertanyaan yang sering diajukan</h2>
      <p class="lead" style="margin-top:14px">Workshop kami di Hamparan Perak, Deli Serdang, melayani pesanan dari Medan, Belawan, dan seluruh Sumatera Utara.</p>
    </div>
    <div class="faq reveal">{faq_html(HOME_FAQ)}</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>Punya sampel atau gambar teknik? Kirim lewat WhatsApp.</h2>
        <p>Kami balas dengan estimasi harga dan waktu pengerjaan.</p>
      </div>
      <div class="actions">
        <a class="btn btn-primary" href="{WA_MSG}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a>
        <a class="btn btn-ghost" href="kontak.html">Semua Kontak</a>
      </div>
    </div>
  </div>
</section>
''' + FOOTER

# ---------- TENTANG ----------
tentang = head('Tentang CV. Mitra Viktory Logam | Workshop Cor Kuningan Deli Serdang',
               'CV. Mitra Viktory Logam adalah workshop pengecoran kuningan dan bronze yang melayani sparepart kapal, pabrik kelapa sawit, dan industri umum.') + header('tentang.html') + f'''
<section class="page-hero">
  <img class="bg" src="img/banner-workshop.jpg" alt="">
  <div class="container">
    <h1>Workshop pengecoran kuningan dan bronze</h1>
    <p class="lead">CV. Mitra Viktory Logam mengerjakan sparepart logam non-besi dari peleburan sampai pembubutan, di workshop sendiri.</p>
  </div>
</section>

<section>
  <div class="container split">
    <div class="reveal">
      <h2 class="h-section">Tentang Mitra Viktory Logam</h2>
      <p class="muted" style="margin-top:18px">Kami adalah usaha pengecoran logam yang fokus pada dua bahan: kuningan dan bronze. Produk utama kami adalah sparepart kapal seperti cutless bearing, stuffing box, dan shaft bronze, serta bushing dan bantalan untuk pabrik kelapa sawit.</p>
      <p class="muted" style="margin-top:14px">Setiap pesanan dimulai dari sampel atau gambar yang Anda kirim. Kami buat cetakan, cor, lalu bubut hingga ukuran akhir. Karena semua tahap ada di satu tempat, waktu pengerjaan bisa kami jaga tetap singkat dan harga tetap masuk akal.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{WA_MSG}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a>
      </div>
    </div>
    <div class="about-grid reveal">
      <img src="img/{IMG('alasan')}" alt="Operator membubut komponen bronze" loading="lazy">
      <img src="img/{IMG('penuangan')}" alt="Pekerja menyiapkan cetakan pasir" loading="lazy">
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="section-head reveal"><h2 class="h-section">Cara kami bekerja</h2></div>
    <div class="values">
      <div class="value reveal"><h3>Cepat</h3><p>Tidak ada vendor perantara. Peleburan, pencetakan, dan pembubutan dikerjakan tim kami sendiri sehingga pesanan tidak menunggu antrian pihak lain.</p></div>
      <div class="value reveal"><h3>Harga bersaing</h3><p>Harga dihitung dari berat bahan dan kerumitan bentuk. Pesanan dalam jumlah banyak mendapat harga lebih baik.</p></div>
      <div class="value reveal"><h3>Sesuai ukuran</h3><p>Kirim sampel lama atau gambar teknik dengan ukuran. Kami ikuti diameter, panjang, dan toleransi yang diminta.</p></div>
      <div class="value reveal"><h3>Terbuka untuk diskusi</h3><p>Belum yakin bahan apa yang cocok, kuningan atau bronze? Hubungi kami, kami bantu pilih sesuai pemakaian.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container split reverse">
    <div class="split-media reveal"><img src="img/produk-bushing-batch-lt.jpg" alt="Bushing kuningan" loading="lazy"></div>
    <div class="reveal">
      <h2 class="h-section">Dua bahan, banyak kegunaan</h2>
      <p class="muted" style="margin-top:18px"><strong class="accent">Kuningan</strong> dipakai untuk bushing, ring, dan komponen mesin umum karena mudah dibubut dan harganya ekonomis.</p>
      <p class="muted" style="margin-top:12px"><strong class="accent">Bronze</strong> lebih tahan gesekan dan korosi air laut, sehingga menjadi pilihan untuk cutless bearing, stuffing box, dan sleeve poros kapal.</p>
      <div class="hero-actions"><a class="btn btn-ghost" href="produk.html">Lihat Produk<i class="ph ph-arrow-right"></i></a></div>
    </div>
  </div>
</section>
''' + FOOTER

# ---------- PRODUK ----------
cards = ''
for slug, name, mat, desc in PRODUCTS:
    q = WA_AGE + '?text=' + ('Halo%20CV.%20Mitra%20Viktory%20Logam%2C%20saya%20ingin%20menanyakan%20pembuatan%20' + name.replace(' ', '%20').replace('&', '%26'))
    pg = PDETAIL[name]['page']
    cards += f'''
      <article class="product reveal">
        <a href="{pg}"><img src="img/{slug}-sq.jpg" alt="{PDETAIL[name]['h1']} buatan CV. Mitra Viktory Logam" loading="lazy" width="800" height="800"></a>
        <div class="product-body">
          <span class="tag">{mat}</span>
          <h3><a href="{pg}">{name}</a></h3>
          <p>{desc}</p>
          <div class="product-links"><a href="{pg}">Lihat detail<i class="ph ph-arrow-right"></i></a><a href="{q}" target="_blank" rel="noopener">Tanya via WA</a></div>
        </div>
      </article>'''

produk = head('Produk Cor Kuningan & Bronze Medan | Bushing, Cutless Bearing, Stuffing Box',
              'Katalog sparepart cor kuningan dan bronze buatan CV. Mitra Viktory Logam, Medan: cutless bearing, stuffing box, shaft, bushing, bantalan belah, flange. Bisa custom ukuran.') + header('produk.html') + f'''
<section class="page-hero">
  <img class="bg" src="img/produk-shaft-bronze.jpg" alt="">
  <div class="container">
    <h1>Produk cor kuningan dan bronze di Medan</h1>
    <p class="lead">Berikut jenis komponen yang paling sering kami buat. Tidak ada di daftar? Kirim sampel atau gambar, kami tetap bisa kerjakan.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="catalog">{cards}
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="section-head reveal">
      <h2 class="h-section">Pilih bahan sesuai pemakaian</h2>
    </div>
    <div class="materials">
      <div class="material reveal">
        <h3>Kuningan</h3>
        <p>Paduan tembaga dan seng. Mudah dibubut, hasil permukaan halus, dan harganya lebih ekonomis.</p>
        <ul>
          <li><i class="ph ph-check"></i>Bushing dan ring mesin umum</li>
          <li><i class="ph ph-check"></i>Komponen pabrik kelapa sawit</li>
          <li><i class="ph ph-check"></i>Pesanan batch dalam jumlah banyak</li>
        </ul>
      </div>
      <div class="material reveal">
        <h3>Bronze</h3>
        <p>Paduan tembaga dan timah. Lebih tahan aus dan korosi air asin, cocok untuk bagian yang terus bergesekan.</p>
        <ul>
          <li><i class="ph ph-check"></i>Cutless bearing dan stuffing box</li>
          <li><i class="ph ph-check"></i>Shaft dan sleeve poros kapal</li>
          <li><i class="ph ph-check"></i>Bantalan beban berat</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="cta-band reveal">
      <div>
        <h2>Butuh ukuran khusus? Kirim foto sampel beserta ukurannya.</h2>
        <p>Kami balas dengan estimasi harga dan lama pengerjaan.</p>
      </div>
      <div class="actions">
        <a class="btn btn-primary" href="{WA_MSG}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a>
      </div>
    </div>
  </div>
</section>
''' + FOOTER

# ---------- PROSES ----------
proses = head('Proses Pengecoran Logam & Fasilitas Workshop | CV. Mitra Viktory Logam',
              'Tahapan produksi pengecoran kuningan dan bronze di CV. Mitra Viktory Logam: peleburan, cetakan pasir, penuangan, dan pembubutan di workshop sendiri.') + header('proses.html') + f'''
<section class="page-hero">
  <img class="bg" src="img/hero-pour-v2.jpg" alt="">
  <div class="container">
    <h1>Proses produksi dan fasilitas workshop</h1>
    <p class="lead">Empat tahap utama, semua dikerjakan di tempat kami. Ini yang membuat waktu pengerjaan tetap terkendali.</p>
  </div>
</section>

<section>
  <div class="container">
    <div class="steps">
      <div class="step reveal"><img src="img/{IMG('peleburan')}" alt="Peleburan kuningan di tungku" loading="lazy"><h3>Peleburan</h3><p>Bahan kuningan atau bronze dilebur di tungku. Komposisi disesuaikan dengan jenis produk yang dipesan.</p></div>
      <div class="step reveal"><img src="img/{IMG('cetak')}" alt="Pembuatan cetakan pasir" loading="lazy"><h3>Cetakan Pasir</h3><p>Pola dibuat mengikuti sampel atau gambar, lalu dicetak ke pasir cetak dengan tambahan ukuran untuk pembubutan.</p></div>
      <div class="step reveal"><img src="img/{IMG('penuangan')}" alt="Penuangan logam cair ke cetakan" loading="lazy"><h3>Penuangan</h3><p>Logam cair dituang ke cetakan, didinginkan, dibongkar, lalu dibersihkan dari sisa pasir dan saluran cor.</p></div>
      <div class="step reveal"><img src="img/{IMG('bubut')}" alt="Pembubutan hasil cor" loading="lazy"><h3>Pembubutan</h3><p>Hasil cor dibubut hingga diameter dalam, diameter luar, dan panjang sesuai permintaan. Diperiksa sebelum dikirim.</p></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="container">
    <div class="section-head reveal"><h2 class="h-section">Fasilitas</h2></div>
    <div class="facilities">
      <div class="facility reveal"><img src="img/{IMG('peleburan')}" alt="Tungku peleburan" loading="lazy"><div><h3>Tungku peleburan</h3><p>Untuk kuningan dan bronze.</p></div></div>
      <div class="facility reveal"><img src="img/{IMG('penuangan')}" alt="Area cetakan pasir" loading="lazy"><div><h3>Area cetak pasir</h3><p>Pembuatan pola dan cetakan manual.</p></div></div>
      <div class="facility reveal"><img src="img/{IMG('alasan')}" alt="Mesin bubut" loading="lazy"><div><h3>Mesin bubut</h3><p>Finishing komponen hingga ukuran akhir.</p></div></div>
    </div>
  </div>
</section>

<section>
  <div class="container split">
    <div class="reveal">
      <h2 class="h-section">Cara memesan</h2>
      <div class="points">
        <div class="point"><i class="ph ph-chat-circle-text"></i><div><h3>Kirim kebutuhan via WhatsApp</h3><p>Foto sampel beserta ukuran, atau gambar teknik. Sebutkan bahan jika sudah tahu.</p></div></div>
        <div class="point"><i class="ph ph-receipt"></i><div><h3>Terima estimasi</h3><p>Kami balas dengan harga dan perkiraan lama pengerjaan.</p></div></div>
        <div class="point"><i class="ph ph-hammer"></i><div><h3>Produksi</h3><p>Setelah disepakati, komponen dicor dan dibubut. Kami kabari saat selesai.</p></div></div>
        <div class="point"><i class="ph ph-truck"></i><div><h3>Ambil atau kirim</h3><p>Bisa diambil di workshop atau dikirim lewat ekspedisi ke lokasi Anda.</p></div></div>
      </div>
      <div class="hero-actions"><a class="btn btn-primary" href="{WA_MSG}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a></div>
    </div>
    <div class="split-media reveal"><img src="img/produk-stuffing-box-lt.jpg" alt="Stuffing box bronze" loading="lazy"></div>
  </div>
</section>
''' + FOOTER

# ---------- GALERI ----------
FEATURE_FOTO = os.path.exists(os.path.join(os.path.dirname(os.path.abspath(DATA)), 'feature_foto.on'))
if FEATURE_FOTO:
    _gal_items = [(IMG(k), t.split(': ')[-1].strip('"')) for k, t, _, _ in SITE_SLOTS if k != 'hero']
    for _p in PROD:
        _gal_items.append((_p['image'] + '-sq.jpg', _p['name']))
        _gal_items += [(g + '-sq.jpg', _p['name']) for g in _p.get('gallery', [])]
else:  # old fixed gallery (until the Foto Website feature is announced)
    _gal_items = [(s + '.jpg', c) for s, c in [
        ('produk-flange-ring', 'Flange dan ring kuningan'), ('proses-peleburan', 'Peleburan logam'),
        ('produk-cutless-bearing', 'Cutless bearing non-rubber'), ('produk-shaft-bronze', 'Shaft bronze'),
        ('proses-bubut-1', 'Pembubutan komponen'), ('produk-stuffing-box', 'Stuffing box'),
        ('produk-bushing-kuningan-stack', 'Bushing kuningan'), ('proses-cetak-pasir-1', 'Area cetakan pasir'),
        ('produk-ring-bushing', 'Bushing bronze'), ('produk-bantalan-belah', 'Bantalan belah'),
        ('proses-cetak-pasir-2', 'Penyiapan cetakan'), ('produk-bushing-batch', 'Produksi batch bushing'),
        ('produk-sleeve-shaft', 'Sleeve ukuran besar'), ('proses-bubut-2', 'Mesin bubut'),
        ('produk-bushing-berlubang', 'Bushing berlubang')]]
gal = ''.join(f'\n      <a href="img/{s}" data-lightbox data-caption="{c}"><img src="img/{s}" alt="{c}" loading="lazy"></a>' for s, c in _gal_items)
galeri = head('Galeri Produk Cor Kuningan & Bronze | CV. Mitra Viktory Logam',
              'Foto produk dan proses produksi pengecoran kuningan dan bronze di workshop CV. Mitra Viktory Logam.') + header('galeri.html') + f'''
<section class="page-hero">
  <img class="bg" src="img/produk-bushing-batch.jpg" alt="">
  <div class="container">
    <h1>Galeri produk dan workshop</h1>
    <p class="lead">Hasil pengecoran dan suasana produksi. Klik foto untuk memperbesar.</p>
  </div>
</section>
<section>
  <div class="container">
    <div class="masonry">{gal}
    </div>
  </div>
</section>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Pratinjau foto">
  <button type="button" aria-label="Tutup"><i class="ph ph-x"></i></button>
  <figure style="margin:0"><img src="" alt=""><figcaption></figcaption></figure>
</div>
''' + FOOTER

# ---------- KONTAK ----------
kontak = head('Kontak & Lokasi | CV. Mitra Viktory Logam, Hamparan Perak, Deli Serdang',
              'Alamat workshop CV. Mitra Viktory Logam di Jl. Andansari, Terjun, Hamparan Perak, Deli Serdang, dekat Medan. Pesan sparepart cor kuningan dan bronze via WhatsApp.') + header('kontak.html') + f'''
<section class="page-hero">
  <img class="bg" src="img/produk-ring-bushing.jpg" alt="">
  <div class="container">
    <h1>Hubungi kami</h1>
    <p class="lead">Cara tercepat adalah WhatsApp. Kirim foto sampel atau gambar teknik, kami balas dengan estimasi.</p>
  </div>
</section>

<section>
  <div class="container contact-grid">
    <div class="reveal">
      <h2 class="h-section">Kontak langsung</h2>
      <div class="contact-cards">
        <a class="contact-card" href="{WA_AGE}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i><div><strong>0812-6293-6355</strong><span>WhatsApp, Age</span></div></a>
        <a class="contact-card" href="{WA_VIK}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i><div><strong>0812-2841-3881</strong><span>WhatsApp, Viktor</span></div></a>
        <a class="contact-card" href="{FB}" target="_blank" rel="noopener"><i class="ph ph-facebook-logo"></i><div><strong>Mitra Viktory Logam</strong><span>Facebook</span></div></a>
        <a class="contact-card" href="{IG}" target="_blank" rel="noopener"><i class="ph ph-instagram-logo"></i><div><strong>@cvmitraviktorylogam</strong><span>Instagram</span></div></a>
        <a class="contact-card" href="{TT}" target="_blank" rel="noopener"><i class="ph ph-tiktok-logo"></i><div><strong>@cv.mitra.viktory</strong><span>TikTok</span></div></a>
        <a class="contact-card" href="{MAPS_URL}" target="_blank" rel="noopener"><i class="ph ph-map-pin"></i><div><strong>Workshop</strong><span>{ADDR}</span></div></a>
      </div>
      <div class="map-embed">
        <iframe src="{MAPS_EMBED}" title="Peta lokasi workshop CV. Mitra Viktory Logam" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
      </div>
    </div>
    <div class="reveal">
      <form class="form" id="wa-form">
        <div>
          <h2 class="h-card">Kirim kebutuhan Anda</h2>
          <p class="muted" style="font-size:0.95rem;margin-top:6px">Isi form ini, lalu pesan akan terbuka di WhatsApp untuk Anda kirim.</p>
        </div>
        <div class="field">
          <label for="nama">Nama</label>
          <input id="nama" name="nama" type="text" required autocomplete="name">
        </div>
        <div class="field">
          <label for="perusahaan">Perusahaan atau kapal (opsional)</label>
          <input id="perusahaan" name="perusahaan" type="text" autocomplete="organization">
        </div>
        <div class="field">
          <label for="kebutuhan">Jenis komponen</label>
          <select id="kebutuhan" name="kebutuhan" required>
            <option value="Cutless bearing">Cutless bearing</option>
            <option value="Stuffing box">Stuffing box</option>
            <option value="Shaft / sleeve bronze">Shaft / sleeve bronze</option>
            <option value="Bushing kuningan">Bushing kuningan</option>
            <option value="Bushing / ring bronze">Bushing / ring bronze</option>
            <option value="Bantalan belah">Bantalan belah</option>
            <option value="Komponen custom lainnya">Komponen custom lainnya</option>
          </select>
        </div>
        <div class="field">
          <label for="pesan">Detail pesanan</label>
          <textarea id="pesan" name="pesan" rows="4" required placeholder="Contoh: bushing bronze, diameter luar 80 mm, diameter dalam 60 mm, panjang 100 mm, 4 pcs"></textarea>
          <small>Sertakan ukuran dan jumlah. Foto sampel bisa dikirim setelah chat terbuka.</small>
        </div>
        <button class="btn btn-primary" type="submit"><i class="ph ph-whatsapp-logo"></i>Lanjut ke WhatsApp</button>
      </form>
    </div>
  </div>
</section>
''' + FOOTER


# ---------- SEO: structured data ----------
BUSINESS_ID = SITE + '/#business'
BUSINESS = {
    '@context': 'https://schema.org',
    '@type': 'LocalBusiness',
    '@id': BUSINESS_ID,
    'name': 'CV. Mitra Viktory Logam',
    'alternateName': ['Mitra Viktory Logam', 'MVL'],
    'description': 'Pengecoran kuningan dan bronze untuk sparepart kapal, pabrik kelapa sawit, dan industri di Medan dan Deli Serdang.',
    'url': SITE + '/',
    'logo': SITE + '/img/logo.png',
    'image': [SITE + '/img/' + IMG('hero'), SITE + '/img/produk-cutless-bearing-lt-sq.jpg'],
    'telephone': '+62-812-6293-6355',
    'address': {'@type': 'PostalAddress', 'streetAddress': 'Jl. Andansari Gg. Bersama, Terjun',
                'addressLocality': 'Hamparan Perak', 'addressRegion': 'Sumatera Utara', 'addressCountry': 'ID'},
    'geo': {'@type': 'GeoCoordinates', 'latitude': 3.7089, 'longitude': 98.6212},
    'hasMap': MAPS_URL,
    'areaServed': [{'@type': 'City', 'name': n} for n in ['Medan', 'Belawan', 'Deli Serdang', 'Binjai']] + [{'@type': 'State', 'name': 'Sumatera Utara'}],
    'contactPoint': [
        {'@type': 'ContactPoint', 'telephone': '+62-812-6293-6355', 'contactType': 'sales', 'areaServed': 'ID', 'availableLanguage': 'Indonesian'},
        {'@type': 'ContactPoint', 'telephone': '+62-812-2841-3881', 'contactType': 'sales', 'areaServed': 'ID', 'availableLanguage': 'Indonesian'}],
    'sameAs': [FB, IG, TT],
    'knowsAbout': ['pengecoran kuningan', 'pengecoran bronze', 'cutless bearing', 'stuffing box', 'bushing bronze', 'sparepart kapal', 'sparepart PKS'],
}
WEBSITE = {'@context': 'https://schema.org', '@type': 'WebSite', '@id': SITE + '/#website', 'url': SITE + '/',
           'name': 'CV. Mitra Viktory Logam', 'inLanguage': 'id-ID', 'publisher': {'@id': BUSINESS_ID}}

def crumbs(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList',
            'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + '/' + u}
                                for i, (n, u) in enumerate(items)]}

# ---------- SEO: product detail pages ----------
def product_page(slug, name, mat, desc):
    d = PDETAIL[name]
    q = WA_AGE + '?text=' + ('Halo%20CV.%20Mitra%20Viktory%20Logam%2C%20saya%20ingin%20menanyakan%20pembuatan%20' + d['h1'].replace(' ', '%20').replace('&', '%26'))
    names = [n for _, n, _, _ in PRODUCTS]
    i = names.index(name)
    related = [PRODUCTS[(i + k) % len(PRODUCTS)] for k in (1, 2, 3)]
    rel_html = ''.join(f'''
      <article class="product reveal">
        <a href="{PDETAIL[n]['page']}"><img src="img/{s}-sq.jpg" alt="{PDETAIL[n]['h1']}" loading="lazy" width="800" height="800"></a>
        <div class="product-body">
          <span class="tag">{m}</span>
          <h3><a href="{PDETAIL[n]['page']}">{n}</a></h3>
          <p>{dd}</p>
        </div>
      </article>''' for s, n, m, dd in related)
    uses = ''.join(f'<li><i class="ph ph-check"></i>{u}</li>' for u in d['uses'])
    faqs = d['faq'] + SHARED_FAQ
    gallery_html = ''
    if d.get('gallery'):
        gi = ''.join(f'<a href="img/{g}-sq.jpg" data-lightbox data-caption="{d['h1']}"><img src="img/{g}-sq.jpg" alt="{d['h1']} buatan CV. Mitra Viktory Logam" loading="lazy" width="900" height="900"></a>' for g in d['gallery'])
        gallery_html = f'''<section style="padding-top:0">
  <div class="container">
    <h2 class="h-card" style="margin-bottom:16px">Foto lainnya</h2>
    <div class="pd-gallery">{gi}</div>
  </div>
</section>
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Pratinjau foto"><button type="button" aria-label="Tutup"><i class="ph ph-x"></i></button><figure style="margin:0"><img src="" alt=""><figcaption></figcaption></figure></div>

'''
    intro = ''.join(f'<p class="muted" style="margin-top:14px">{t}</p>' for t in d['intro'])
    body = head(d['title'], d['desc']) + header('produk.html') + f'''
<section class="product-detail">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Beranda</a><span>/</span><a href="produk.html">Produk</a><span>/</span><span aria-current="page">{name}</span></nav>
    <div class="split">
      <div class="pd-media reveal"><img src="img/{slug}-sq.jpg" alt="{d['h1']} buatan CV. Mitra Viktory Logam, Medan" width="900" height="900"></div>
      <div class="reveal">
        <span class="tag">{mat}</span>
        <h1 class="h-section" style="margin-top:8px">{d['h1']}</h1>
        {intro}
        <h2 class="h-card" style="margin-top:28px">Dipakai untuk</h2>
        <ul class="pd-uses">{uses}</ul>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{q}" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo"></i>Minta Penawaran</a>
          <a class="btn btn-ghost" href="produk.html">Semua Produk</a>
        </div>
      </div>
    </div>
  </div>
</section>

{gallery_html}<section class="band">
  <div class="container faq-wrap">
    <div class="reveal">
      <h2 class="h-section">Pertanyaan seputar {name.lower()}</h2>
      <p class="lead" style="margin-top:14px">Dibuat di workshop kami di Hamparan Perak, Deli Serdang. Melayani Medan, Belawan, dan Sumatera Utara.</p>
    </div>
    <div class="faq reveal">{faq_html(faqs)}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head reveal"><h2 class="h-section">Produk lainnya</h2></div>
    <div class="catalog catalog-3">{rel_html}
    </div>
  </div>
</section>
''' + FOOTER
    schema = [crumbs([('Beranda', ''), ('Produk', 'produk.html'), (name, d['page'])]),
              {'@context': 'https://schema.org', '@type': 'Product', 'name': d['h1'], 'description': d['desc'],
               'image': [SITE + f'/img/{slug}-sq.jpg'] + [SITE + f'/img/{g}-sq.jpg' for g in d.get('gallery', [])], 'material': mat, 'category': 'Sparepart cor ' + mat.lower(),
               'brand': {'@type': 'Brand', 'name': 'Mitra Viktory Logam'}, 'manufacturer': {'@id': BUSINESS_ID},
               'url': SITE + '/' + d['page']},
              faq_schema(faqs)]
    return d['page'], body, schema, 'img/og-logo.jpg'

# ---------- 404 ----------
notfound = head('Halaman tidak ditemukan | CV. Mitra Viktory Logam', 'Halaman yang Anda cari tidak ada.').replace(
    '<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex"><base href="/">') + header('') + f'''
<section>
  <div class="container" style="text-align:center;padding:40px 0">
    <h1 class="h-section">Halaman tidak ditemukan</h1>
    <p class="lead" style="margin:14px auto 0">Halaman yang Anda cari mungkin sudah dipindah. Silakan kembali ke beranda atau lihat produk kami.</p>
    <div class="hero-actions" style="justify-content:center">
      <a class="btn btn-primary" href="/index.html">Ke Beranda</a>
      <a class="btn btn-ghost" href="/produk.html">Lihat Produk</a>
    </div>
  </div>
</section>
''' + FOOTER

# ---------- write everything ----------
pages = [
    ('index.html', index, [BUSINESS, WEBSITE, faq_schema(HOME_FAQ)], 'img/og-logo.jpg', '1.0'),
    ('produk.html', produk, [crumbs([('Beranda', ''), ('Produk', 'produk.html')]),
        {'@context': 'https://schema.org', '@type': 'ItemList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'url': SITE + '/' + PDETAIL[n]['page'], 'name': PDETAIL[n]['h1']}
            for i, (_, n, _, _) in enumerate(PRODUCTS)]}], 'img/og-logo.jpg', '0.9'),
    ('tentang.html', tentang, [crumbs([('Beranda', ''), ('Tentang', 'tentang.html')])], 'img/og-logo.jpg', '0.6'),
    ('proses.html', proses, [crumbs([('Beranda', ''), ('Proses & Fasilitas', 'proses.html')])], 'img/og-logo.jpg', '0.6'),
    ('galeri.html', galeri, [crumbs([('Beranda', ''), ('Galeri', 'galeri.html')])], 'img/og-logo.jpg', '0.5'),
    ('kontak.html', kontak, [BUSINESS, crumbs([('Beranda', ''), ('Kontak', 'kontak.html')])], 'img/og-logo.jpg', '0.8'),
]
for slug, name, mat, desc in PRODUCTS:
    pg, body, schema, ogimg = product_page(slug, name, mat, desc)
    pages.append((pg, body, schema, ogimg, '0.8'))

import datetime
today = datetime.date.today().isoformat()
sitemap = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for name, html, schema, ogimg, prio in pages:
    url = SITE + '/' if name == 'index.html' else SITE + '/' + name
    ogw, ogh = ('1200', '630') if ogimg.endswith('og-logo.jpg') else ('900', '900')
    html = (html.replace('__CANONICAL__', url).replace('__OGIMAGE__', SITE + '/' + ogimg).replace('__OGW__', ogw).replace('__OGH__', ogh)
                .replace('<!--SCHEMA-->', '\n'.join(ld(s) for s in schema)))
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(html)
    sitemap.append(f'  <url><loc>{url}</loc><lastmod>{today}</lastmod><priority>{prio}</priority></url>')
    print('wrote', name)
# remove product pages that no longer exist (deleted or renamed in the admin)
_manifest = os.path.join(OUT, '.product-pages.json')
_now = [PDETAIL[n]['page'] for _, n, _, _ in PRODUCTS]
try:
    _prev = _json.load(open(_manifest, encoding='utf-8'))
except Exception:
    _prev = []
for _old in set(_prev) - set(_now):
    try:
        os.remove(os.path.join(OUT, _old)); print('removed', _old)
    except FileNotFoundError:
        pass
_json.dump(_now, open(_manifest, 'w', encoding='utf-8'))
sitemap.append('</urlset>')
with open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(sitemap) + '\n')
with open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(f'User-agent: *\nAllow: /\nDisallow: /admin\n\nSitemap: {SITE}/sitemap.xml\n')
with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
    f.write(notfound.replace('__CANONICAL__', SITE + '/404.html').replace('__OGIMAGE__', SITE + '/img/og-logo.jpg').replace('__OGW__', '1200').replace('__OGH__', '630').replace('<!--SCHEMA-->', ''))
print('wrote sitemap.xml, robots.txt, 404.html')
