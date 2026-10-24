"""Admin panel for mitraviktorylogam.com (products only).

Runs behind nginx at /admin. Products live in DATA (JSON). After every change the
static site is rebuilt by build.py so pages stay fast and indexable.
"""
import fcntl
import hashlib
import hmac
import json
import os
import re
import secrets
import subprocess
import sys
import tempfile
import time
from collections import defaultdict
from functools import wraps
from html import escape

from flask import Flask, abort, redirect, request, session

import ui

BASE = os.environ.get('MVL_BASE', '/opt/mvl')
DATA = os.path.join(BASE, 'data', 'products.json')
AUTH = os.path.join(BASE, 'data', 'admin.json')
LOCK = os.path.join(BASE, 'data', '.lock')
WEBROOT = os.environ.get('MVL_OUT', '/var/www/mitraviktorylogam')
PY = sys.executable
SITE = 'https://mitraviktorylogam.com'
MATERIALS = ['Kuningan', 'Bronze', 'Kuningan / Bronze']

app = Flask(__name__)
app.secret_key = json.load(open(AUTH))['secret']
app.config.update(SESSION_COOKIE_SECURE=True, SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE='Lax',
                  SESSION_COOKIE_PATH='/admin', PERMANENT_SESSION_LIFETIME=60 * 60 * 24 * 30,
                  MAX_CONTENT_LENGTH=60 * 1024 * 1024)
FAILS = defaultdict(list)


# ---------- helpers ----------
def load_auth():
    return json.load(open(AUTH))


def check_pw(pw, a):
    h = hashlib.pbkdf2_hmac('sha256', pw.encode(), bytes.fromhex(a['salt']), a['iter']).hex()
    return hmac.compare_digest(h, a['hash'])


def set_pw(pw):
    a = load_auth()
    a['salt'] = secrets.token_hex(16)
    a['iter'] = 310000
    a['hash'] = hashlib.pbkdf2_hmac('sha256', pw.encode(), bytes.fromhex(a['salt']), a['iter']).hex()
    tmp = AUTH + '.tmp'
    json.dump(a, open(tmp, 'w'))
    os.replace(tmp, AUTH)


def load():
    return json.load(open(DATA, encoding='utf-8'))


def save_and_build(products):
    tmp = DATA + '.tmp'
    json.dump(products, open(tmp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    os.replace(tmp, DATA)
    env = dict(os.environ, MVL_DATA=DATA, MVL_OUT=WEBROOT)
    r = subprocess.run([PY, os.path.join(BASE, 'build.py')], env=env, capture_output=True, text=True, timeout=120)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-800:])


class Locked:
    def __enter__(self):
        self.f = open(LOCK, 'w')
        fcntl.flock(self.f, fcntl.LOCK_EX)

    def __exit__(self, *a):
        fcntl.flock(self.f, fcntl.LOCK_UN)
        self.f.close()


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-') or 'produk'


def process_photo(file_storage, base_rel, remove_bg):
    """Save upload to a temp file and render catalog variants in a separate process (frees RAM after)."""
    fd, tmp = tempfile.mkstemp(suffix='.img', dir=os.path.join(BASE, 'tmp'))
    os.close(fd)
    try:
        file_storage.save(tmp)
        out_base = os.path.join(WEBROOT, 'img', base_rel)
        r = subprocess.run([PY, os.path.join(BASE, 'admin', 'process_image.py'), tmp, out_base,
                            os.path.join(WEBROOT, 'img', 'logo.png'), '1' if remove_bg else '0'],
                           capture_output=True, text=True, timeout=300)
        if r.returncode != 0:
            raise RuntimeError('Foto tidak bisa diproses. Pastikan file berupa gambar JPG atau PNG.')
    finally:
        os.remove(tmp)


def csrf_token():
    if 'csrf' not in session:
        session['csrf'] = secrets.token_hex(16)
    return session['csrf']


def check_csrf():
    if not hmac.compare_digest(request.form.get('csrf', ''), session.get('csrf', '')):
        abort(400)


def login_required(f):
    @wraps(f)
    def w(*a, **k):
        if not session.get('user'):
            return redirect('/admin/login')
        if request.method == 'POST':
            check_csrf()
        return f(*a, **k)
    return w


@app.after_request
def headers(r):
    r.headers['X-Robots-Tag'] = 'noindex, nofollow'
    r.headers['X-Frame-Options'] = 'DENY'
    r.headers['Cache-Control'] = 'no-store'
    return r


# ---------- layout ----------
def page(title, body, active=''):
    flashes = [(k, session.pop('flash_' + k)) for k in ('ok', 'err') if session.get('flash_' + k)]
    return ui.shell(title, body, active, flashes, os.path.exists(os.path.join(BASE, 'data', 'feature_foto.on')))


def flash(kind, m):
    session['flash_' + kind] = m


# ---------- auth ----------
@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    err = ''
    if request.method == 'POST':
        ip = request.headers.get('X-Real-IP', request.remote_addr)
        FAILS[ip] = [t for t in FAILS[ip] if t > time.time() - 900]
        if len(FAILS[ip]) >= 6:
            err = 'Terlalu banyak percobaan. Coba lagi 15 menit lagi.'
        else:
            a = load_auth()
            if hmac.compare_digest(request.form.get('user', '').strip().lower(), a['user']) and check_pw(request.form.get('password', ''), a):
                session.clear()
                session.permanent = True
                session['user'] = a['user']
                return redirect('/admin/')
            FAILS[ip].append(time.time())
            err = 'Username atau password salah.'
    return ui.login_page(err)


@app.route('/admin/logout')
def logout():
    session.clear()
    return redirect('/admin/login')


@app.route('/admin/password', methods=['GET', 'POST'])
@login_required
def password():
    if request.method == 'POST':
        a = load_auth()
        new = request.form.get('new', '')
        if not check_pw(request.form.get('old', ''), a):
            flash('err', 'Password lama salah.')
        elif len(new) < 8:
            flash('err', 'Password baru minimal 8 karakter.')
        elif new != request.form.get('new2', ''):
            flash('err', 'Konfirmasi password baru tidak sama.')
        else:
            set_pw(new)
            flash('ok', 'Password berhasil diganti.')
            return redirect('/admin/')
        return redirect('/admin/password')
    return page('Akun', ui.password_page(csrf_token()), 'akun')


# ---------- products ----------
@app.route('/admin/')
@login_required
def index():
    return page('Produk', ui.products_page(load(), csrf_token()), 'produk')


def form_html(p, is_new):
    return ui.product_form(p, is_new, csrf_token())


def apply_form(p):
    f = request.form
    p['name'] = f.get('name', '').strip()[:80]
    p['material'] = f.get('material', 'Kuningan').strip()[:40]
    p['short'] = f.get('short', '').strip()[:160]
    p['intro'] = [t.strip() for t in re.split(r'\n\s*\n', f.get('intro', '').replace('\r', '')) if t.strip()]
    p['uses'] = [t.strip() for t in f.get('uses', '').replace('\r', '').split('\n') if t.strip()]
    for k, lim in (('h1', 90), ('title', 90), ('desc', 170)):
        p[k] = f.get(k, '').strip()[:lim]
    if not p['name'] or not p['short']:
        raise ValueError('Nama produk dan deskripsi singkat wajib diisi.')


def handle_photos(p, remove_bg):
    ph = request.files.get('photo')
    if ph and ph.filename:
        rel = f"p/{p['id']}-v{secrets.token_hex(3)}"  # new name so browsers do not show the cached old photo
        process_photo(ph, rel, remove_bg)
        p['image'] = rel
    for ex in request.files.getlist('extra'):
        if ex and ex.filename:
            rel = f"p/{p['id']}-x{secrets.token_hex(3)}"
            process_photo(ex, rel, remove_bg)
            p.setdefault('gallery', []).append(rel)


@app.route('/admin/produk/baru', methods=['GET', 'POST'])
@login_required
def new():
    if request.method == 'POST':
        with Locked():
            ps = load()
            p = {'faq': [], 'gallery': []}
            try:
                apply_form(p)
                base = slugify(p['name'])
                pid = base
                n = 2
                while any(x['id'] == pid for x in ps):
                    pid = f'{base}-{n}'
                    n += 1
                p['id'] = pid
                p['image'] = f'p/{pid}'
                p['page'] = f'{pid}-medan.html'
                handle_photos(p, request.form.get('remove_bg') == '1')
                ps.append(p)
                save_and_build(ps)
            except Exception as e:
                flash('err', str(e) if isinstance(e, ValueError) else f'Gagal menyimpan: {e}')
                return page('Tambah produk', form_html(p, True), 'baru')
        flash('ok', f'Produk "{p["name"]}" berhasil ditambahkan.')
        return redirect('/admin/')
    return page('Tambah produk', form_html({'material': 'Kuningan'}, True), 'baru')


@app.route('/admin/produk/<pid>', methods=['GET', 'POST'])
@login_required
def edit(pid):
    ps = load()
    p = next((x for x in ps if x['id'] == pid), None)
    if not p:
        abort(404)
    if request.method == 'POST':
        with Locked():
            ps = load()
            p = next(x for x in ps if x['id'] == pid)
            try:
                apply_form(p)
                handle_photos(p, request.form.get('remove_bg') == '1')
                save_and_build(ps)
            except Exception as e:
                flash('err', str(e) if isinstance(e, ValueError) else f'Gagal menyimpan: {e}')
                return redirect(f'/admin/produk/{pid}')
        flash('ok', f'Produk "{p["name"]}" berhasil disimpan.')
        return redirect('/admin/')
    return page('Edit produk', form_html(p, False), 'produk')


@app.route('/admin/produk/<pid>/hapus', methods=['POST'])
@login_required
def delete(pid):
    with Locked():
        ps = load()
        p = next((x for x in ps if x['id'] == pid), None)
        if not p:
            abort(404)
        if len(ps) <= 1:
            flash('err', 'Minimal harus ada 1 produk.')
            return redirect('/admin/')
        ps.remove(p)
        save_and_build(ps)
    flash('ok', f'Produk "{p["name"]}" sudah dihapus.')
    return redirect('/admin/')


@app.route('/admin/produk/<pid>/<direction>', methods=['POST'])
@login_required
def move(pid, direction):
    if direction not in ('naik', 'turun'):
        abort(404)
    with Locked():
        ps = load()
        i = next((k for k, x in enumerate(ps) if x['id'] == pid), None)
        if i is None:
            abort(404)
        j = i - 1 if direction == 'naik' else i + 1
        if 0 <= j < len(ps):
            ps[i], ps[j] = ps[j], ps[i]
            save_and_build(ps)
    return redirect('/admin/')


@app.route('/admin/produk/<pid>/foto-hapus/<int:idx>', methods=['POST'])
@login_required
def delete_photo(pid, idx):
    with Locked():
        ps = load()
        p = next((x for x in ps if x['id'] == pid), None)
        if not p or idx >= len(p.get('gallery', [])):
            abort(404)
        p['gallery'].pop(idx)
        save_and_build(ps)
    flash('ok', 'Foto tambahan dihapus.')
    return redirect(f'/admin/produk/{pid}')


# ---------- site photos ----------
SITEIMG = os.path.join(BASE, 'data', 'site_images.json')
FEATURE_FLAG = os.path.join(BASE, 'data', 'feature_foto.on')


@app.before_request
def _foto_gate():
    if request.path.startswith('/admin/foto') and not os.path.exists(FEATURE_FLAG):
        abort(404)


def site_slots():
    import importlib.util
    src = open(os.path.join(BASE, 'build.py'), encoding='utf-8').read()
    i = src.index('SITE_SLOTS = ['); j = src.index(']\n', i) + 1
    ns = {}
    exec(src[i:j], ns)
    return ns['SITE_SLOTS']


def load_siteimg():
    try:
        return json.load(open(SITEIMG, encoding='utf-8'))
    except Exception:
        return {}


def save_siteimg(d):
    tmp = SITEIMG + '.tmp'
    json.dump(d, open(tmp, 'w', encoding='utf-8'), indent=1)
    os.replace(tmp, SITEIMG)


@app.route('/admin/foto')
@login_required
def site_photos():
    return page('Foto website', ui.site_photos_page(site_slots(), load_siteimg(), csrf_token()), 'foto')


@app.route('/admin/foto/<slot>', methods=['POST'])
@login_required
def site_photo_upload(slot):
    slots = {k: d for k, _, _, d in site_slots()}
    if slot not in slots:
        abort(404)
    f = request.files.get('photo')
    if not f or not f.filename:
        flash('err', 'Pilih foto dulu.')
        return redirect('/admin/foto')
    from PIL import Image, ImageOps
    try:
        from pillow_heif import register_heif_opener
        register_heif_opener()
    except Exception:
        pass
    with Locked():
        try:
            im = ImageOps.exif_transpose(Image.open(f.stream)).convert('RGB')
            im.thumbnail((2000, 2000) if slot == 'hero' else (1600, 1600))
            os.makedirs(os.path.join(WEBROOT, 'img', 's'), exist_ok=True)
            rel = f's/{slot}-{secrets.token_hex(3)}.jpg'
            im.save(os.path.join(WEBROOT, 'img', rel), quality=85, optimize=True, progressive=True)
            d = load_siteimg()
            d[slot] = rel
            save_siteimg(d)
            save_and_build(load())
        except Exception as e:
            flash('err', f'Foto tidak bisa diproses: {e}')
            return redirect('/admin/foto')
    flash('ok', 'Foto berhasil diganti.')
    return redirect('/admin/foto')


@app.route('/admin/foto/<slot>/reset', methods=['POST'])
@login_required
def site_photo_reset(slot):
    with Locked():
        d = load_siteimg()
        d.pop(slot, None)
        save_siteimg(d)
        save_and_build(load())
    flash('ok', 'Foto dikembalikan ke foto awal.')
    return redirect('/admin/foto')


@app.route('/admin')
def root():
    return redirect('/admin/')
