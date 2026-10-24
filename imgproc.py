"""Product photo processing shared by the local build and the admin panel.

Turns a raw workshop photo into catalog images on a light studio backdrop:
  <base>-sq.jpg   900x900   (catalog card, product page)
  <base>-lt.jpg   1200x900  (home bento small/tall cells)
  <base>-wide.jpg 1500x640  (home bento wide cells)
"""
import os
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps
try:  # iPhone HEIC photos
    from pillow_heif import register_heif_opener
    register_heif_opener()
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
_session = None


def remove_bg(rgb):
    """Return an RGBA cutout. Imports rembg lazily (heavy)."""
    global _session
    from rembg import remove, new_session
    if _session is None:
        _session = new_session('isnet-general-use')
    return remove(rgb, session=_session).convert('RGBA')


def clean_cutout(cut, erode=3, keep_frac=0.05):
    """Drop stray fragments (wires, twigs) that are not part of the main object."""
    import numpy as np
    from scipy import ndimage
    a = np.array(cut.getchannel('A'))
    m = a > 40
    if not m.any():
        return cut
    er = ndimage.binary_erosion(m, iterations=erode) if erode else m
    lab, k = ndimage.label(er)
    if k > 1:
        sizes = ndimage.sum(er, lab, range(1, k + 1))
        keep = np.isin(lab, [i + 1 for i, s in enumerate(sizes) if s > sizes.max() * keep_frac])
        keep = ndimage.binary_dilation(keep, iterations=erode + 2) & m
        a = np.where(keep, a, 0).astype('uint8')
    a = Image.fromarray(a).filter(ImageFilter.GaussianBlur(0.8))
    out = cut.copy()
    out.putalpha(a)
    return out


def polish(rgb):
    rgb = ImageOps.autocontrast(rgb, cutoff=1)
    rgb = ImageEnhance.Color(rgb).enhance(1.15)
    rgb = ImageEnhance.Contrast(rgb).enhance(1.06)
    rgb = ImageEnhance.Brightness(rgb).enhance(1.04)
    r, g, b = rgb.split()
    rgb = Image.merge('RGB', (r.point(lambda v: min(255, int(v * 1.03))), g, b.point(lambda v: int(v * 0.97))))
    return rgb.filter(ImageFilter.UnsharpMask(radius=1.5, percent=60, threshold=2))


def backdrop(W, H):
    top, mid, bot = (226, 228, 231), (242, 243, 245), (214, 216, 220)
    bg = Image.new('RGB', (W, H))
    d = ImageDraw.Draw(bg)
    for y in range(H):
        t = y / H
        if t < 0.6:
            c = tuple(int(top[i] + (mid[i] - top[i]) * (t / 0.6)) for i in range(3))
        else:
            c = tuple(int(mid[i] + (bot[i] - mid[i]) * ((t - 0.6) / 0.4)) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    v = Image.new('L', (W, H), 0)
    ImageDraw.Draw(v).ellipse((W * 0.12, H * 0.05, W * 0.88, H * 0.8), fill=255)
    v = v.filter(ImageFilter.GaussianBlur(min(W, H) * 0.18))
    return Image.composite(Image.new('RGB', (W, H), (250, 250, 251)), bg, v.point(lambda a: int(a * 0.6)))


def watermark(im, logo_path):
    if not logo_path or not os.path.exists(logo_path):
        return im
    logo = Image.open(logo_path).convert('RGBA')
    lw = int(min(im.width, im.height * 1.3) * 0.40)
    lg = logo.resize((lw, int(lw * logo.height / logo.width)), Image.LANCZOS)
    a = lg.getchannel('A').point(lambda v: int(v * 0.10))
    grey = ImageOps.grayscale(lg.convert('RGB')).convert('RGB')
    out = im.convert('RGBA')
    out.alpha_composite(Image.merge('RGBA', (*grey.split(), a)), ((im.width - lg.width) // 2, (im.height - lg.height) // 2))
    return out.convert('RGB')


def compose_cutout(cut, W, H, fw, fh, logo_path):
    cut = cut.crop(cut.getbbox())
    r = min(int(W * fw) / cut.width, int(H * fh) / cut.height)
    cut = cut.resize((max(1, int(cut.width * r)), max(1, int(cut.height * r))), Image.LANCZOS)
    bg = backdrop(W, H)
    x = (W - cut.width) // 2
    y = (H - cut.height) // 2 - int(H * 0.03)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse((x + cut.width * 0.06, y + cut.height * 0.95, x + cut.width * 0.94, y + cut.height * 1.07), fill=(40, 40, 45, 110))
    sh = sh.filter(ImageFilter.GaussianBlur(22))
    sh2 = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    sh2.paste((30, 30, 35, 255), (x + int(cut.width * 0.02), y + int(cut.height * 0.04)), cut.getchannel('A').point(lambda v: int(v * 0.28)))
    sh2 = sh2.filter(ImageFilter.GaussianBlur(24))
    out = bg.convert('RGBA')
    out.alpha_composite(sh2)
    out.alpha_composite(sh)
    out.alpha_composite(cut, (x, y))
    return watermark(out.convert('RGB'), logo_path)


def compose_photo(rgb, W, H, logo_path, centering=(0.5, 0.5)):
    return watermark(ImageOps.fit(polish(rgb), (W, H), Image.LANCZOS, centering=centering), logo_path)


SIZES = {'sq': (900, 900, 0.80, 0.74), 'lt': (1200, 900, 0.62, 0.66), 'wide': (1500, 640, 0.55, 0.72)}


def make_variants(out_base, logo_path, cutout=None, photo=None):
    """Write <out_base>-sq/-lt/-wide.jpg from either an RGBA cutout or a plain RGB photo."""
    os.makedirs(os.path.dirname(out_base), exist_ok=True)
    for key, (W, H, fw, fh) in SIZES.items():
        if cutout is not None:
            im = compose_cutout(cutout, W, H, fw, fh, logo_path)
        else:
            im = compose_photo(photo, W, H, logo_path)
        im.save(f'{out_base}-{key}.jpg', quality=86, optimize=True, progressive=True)


def process_upload(src_path, out_base, logo_path, remove_background=True):
    """Full pipeline for an uploaded photo. Falls back to a plain crop if cutout fails."""
    rgb = ImageOps.exif_transpose(Image.open(src_path)).convert('RGB')
    rgb.thumbnail((1600, 1600))
    if remove_background:
        try:
            cut = clean_cutout(remove_bg(rgb))
            if cut.getbbox():
                rgba = polish(cut.convert('RGB')).convert('RGBA')
                rgba.putalpha(cut.getchannel('A'))
                make_variants(out_base, logo_path, cutout=rgba)
                return 'cutout'
        except Exception:
            pass
    make_variants(out_base, logo_path, photo=rgb)
    return 'photo'
