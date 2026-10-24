# mvl

Website company profile CV. Mitra Viktory Logam — https://mitraviktorylogam.com

- `build.py` — generator situs statis (HTML, sitemap, JSON-LD) dari `data/products.json`
- `imgproc.py`, `admin/` — panel admin (Flask) di `/admin` untuk produk & foto website
- `data/` — data produk & override foto, disalin dari server (server adalah sumber kebenaran)
- `site/` — salinan webroot yang sedang live, termasuk foto upload klien
- `raw/`, `raw2/`, `cut/`, `gen/` — foto sumber (asli klien, potongan rembg, aset hero)

Deploy di Lightsail: kode di `/opt/mvl`, webroot `/var/www/mitraviktorylogam`,
service systemd `mvl-admin`. `data/admin.json` (login admin) sengaja tidak ada di repo.
