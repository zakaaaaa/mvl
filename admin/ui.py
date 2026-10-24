"""Admin UI: page shell, styles, and templates.

Design read: product admin for a non-technical owner, mostly used on a phone.
Calm utility UI on the brand tokens of mitraviktorylogam.com (Archivo + IBM Plex Sans,
one brass accent, light theme). Shape rule: panels 16px, controls 10px, chips full pill.
Icons: Phosphor (same family as the public site). Motion only for feedback.
"""
import time
from html import escape

SITE = 'https://mitraviktorylogam.com'
MATERIALS = ['Kuningan', 'Bronze', 'Kuningan / Bronze']

CSS = r'''
:root{
  --bg:#f4f5f7;--panel:#fff;--sunken:#eef0f3;--line:rgba(20,24,30,.10);--line-2:rgba(20,24,30,.18);
  --text:#15181c;--text-2:#4a515b;--text-3:#6b727c;
  --brass:#d4a93c;--brass-2:#e2b94c;--brass-t:#7d5a0c;--brass-soft:rgba(212,169,60,.14);--on-brass:#1a1405;
  --danger:#b42318;--danger-soft:#fdecea;--ok:#146c2e;--ok-soft:#e9f6ec;
  --r-panel:16px;--r-ctl:10px;
  --shadow:0 1px 2px rgba(20,24,30,.05),0 8px 24px rgba(20,24,30,.06);
  --ease:cubic-bezier(.16,1,.3,1);
  --font-d:"Archivo",system-ui,sans-serif;--font-b:"IBM Plex Sans",system-ui,sans-serif;
}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:15.5px/1.55 var(--font-b);-webkit-font-smoothing:antialiased}
a{color:inherit}
img{display:block;max-width:100%}
h1,h2,h3{font-family:var(--font-d);letter-spacing:-.015em;margin:0;line-height:1.15}
:focus-visible{outline:2px solid var(--brass-t);outline-offset:2px}
.ph{font-size:1.15em;line-height:1}

/* shell */
.shell{min-height:100dvh;display:grid;grid-template-columns:minmax(0,1fr)}
.shell > div{min-width:0}
.side{display:none}
.topbar{position:sticky;top:0;z-index:20;height:60px;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:0 16px;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font:700 1rem var(--font-d)}
.brand img{height:36px;width:auto}
.brand small{display:block;font:500 .75rem var(--font-b);color:var(--text-3);letter-spacing:0}
.main{padding:20px 16px calc(150px + env(safe-area-inset-bottom));max-width:1120px;width:100%;margin:0 auto}
.tabbar{position:fixed;left:0;right:0;bottom:0;z-index:20;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));height:calc(64px + env(safe-area-inset-bottom));background:#fff;border-top:1px solid var(--line);padding:4px 6px env(safe-area-inset-bottom)}
.tabbar.t3{grid-template-columns:repeat(3,minmax(0,1fr))}
.tabbar a{display:flex;flex-direction:column;align-items:center;gap:2px;padding:6px 0;border-radius:var(--r-ctl);text-decoration:none;font:600 .72rem var(--font-b);color:var(--text-3)}
.tabbar a .ph{font-size:1.4rem}
.tabbar a[aria-current]{color:var(--brass-t)}
.tabbar a.cta .ph{background:var(--brass);color:var(--on-brass);border-radius:999px;padding:6px;font-size:1.25rem}
@media (min-width:1024px){
  .shell{grid-template-columns:248px minmax(0,1fr)}
  .side{display:flex;flex-direction:column;gap:4px;position:sticky;top:0;height:100dvh;padding:20px 14px;background:#fff;border-right:1px solid var(--line)}
  .side .brand{padding:4px 8px 18px;font-size:.95rem}
  .side nav{display:grid;gap:2px}
  .side nav a,.side .bottom a{display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:var(--r-ctl);text-decoration:none;font-weight:600;color:var(--text-2);transition:background .2s,color .2s}
  .side nav a:hover,.side .bottom a:hover{background:var(--sunken);color:var(--text)}
  .side nav a[aria-current],.side .bottom a[aria-current]{background:var(--brass-soft);color:var(--brass-t)}
  .side .bottom{margin-top:auto;display:grid;gap:2px}
  .topbar,.tabbar{display:none}
  .main{padding:36px 40px 60px}
}

/* buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:44px;padding:0 18px;border-radius:var(--r-ctl);border:1px solid var(--line-2);background:#fff;color:var(--text);font:600 .95rem var(--font-d);cursor:pointer;text-decoration:none;white-space:nowrap;transition:transform .15s var(--ease),background .2s,border-color .2s}
.btn:hover{border-color:var(--text-3)}
.btn:active{transform:scale(.98)}
.btn.primary{background:var(--brass);border-color:var(--brass);color:var(--on-brass)}
.btn.primary:hover{background:var(--brass-2);border-color:var(--brass-2)}
.btn.danger{color:var(--danger);border-color:rgba(180,35,24,.35)}
.btn.danger:hover{background:var(--danger-soft)}
.btn.icon{width:40px;height:40px;padding:0}
.btn.sm{height:38px;padding:0 14px;font-size:.88rem}
.btn[disabled]{opacity:.55;pointer-events:none}

/* page header */
.ph-head{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:22px}
.ph-head h1{font-size:clamp(1.5rem,3vw,2rem)}
.ph-head p{margin:6px 0 0;color:var(--text-2);max-width:60ch}
.back{display:inline-flex;align-items:center;gap:6px;margin-bottom:10px;color:var(--text-2);text-decoration:none;font-weight:600;font-size:.9rem}
.back:hover{color:var(--text)}

/* toolbar + product grid */
.toolbar{display:flex;gap:10px;margin-bottom:18px}
.search{position:relative;flex:1;max-width:420px}
.search .ph{position:absolute;left:13px;top:50%;transform:translateY(-50%);color:var(--text-3);z-index:1;pointer-events:none}
.search input[type=search]{padding-left:42px}
.pgrid{display:grid;gap:14px;grid-template-columns:minmax(0,1fr)}
@media (min-width:640px){.pgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1440px){.pgrid{grid-template-columns:repeat(3,minmax(0,1fr))}}
.pcard{display:grid;grid-template-columns:96px minmax(0,1fr);gap:14px;padding:12px;background:var(--panel);border:1px solid var(--line);border-radius:var(--r-panel);box-shadow:var(--shadow);transition:border-color .2s}
.pcard:hover{border-color:var(--line-2)}
.pcard .thumb{width:96px;height:96px;border-radius:12px;overflow:hidden;background:var(--sunken)}
.pcard .thumb img{width:100%;height:100%;object-fit:cover}
.pcard h3{font-size:1.02rem;overflow-wrap:anywhere}
.pcard .meta{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0 10px}
.chip{display:inline-flex;align-items:center;gap:5px;height:24px;padding:0 10px;border-radius:999px;background:var(--sunken);color:var(--text-2);font:600 .75rem var(--font-b)}
.chip.home{background:var(--brass-soft);color:var(--brass-t)}
.pcard .acts{display:flex;align-items:center;gap:6px}
.pcard .acts .spacer{flex:1}
.pcard .acts form{display:contents}
.empty{display:grid;justify-items:start;gap:10px;padding:32px;background:var(--panel);border:1px dashed var(--line-2);border-radius:var(--r-panel);color:var(--text-2)}
.empty .ph{font-size:2rem;color:var(--brass-t)}

/* forms */
.layout{display:grid;gap:18px;grid-template-columns:minmax(0,1fr)}
.layout > *{min-width:0}
@media (min-width:1024px){.layout{grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);align-items:start}.layout .aside{position:sticky;top:24px}}
.panel{background:var(--panel);border:1px solid var(--line);border-radius:var(--r-panel);box-shadow:var(--shadow);padding:20px}
.panel + .panel{margin-top:18px}
.panel h2{font-size:1.08rem;margin-bottom:4px}
.panel .sub{color:var(--text-2);font-size:.9rem;margin:0 0 6px}
.field{display:grid;gap:6px;margin-top:16px}
.field label,.lbl{font-weight:600;font-size:.92rem;display:flex;justify-content:space-between;gap:8px}
.count{font-weight:500;color:var(--text-3);font-variant-numeric:tabular-nums}
.count.over{color:var(--danger)}
input[type=text],input[type=password],input[type=search],textarea,select{width:100%;min-height:46px;padding:11px 13px;border:1px solid var(--line-2);border-radius:var(--r-ctl);background:#fff;color:var(--text);font:inherit;transition:border-color .2s,box-shadow .2s}
textarea{min-height:120px;resize:vertical}
input::placeholder,textarea::placeholder{color:var(--text-3)}
input:focus,textarea:focus,select:focus{outline:none;border-color:var(--brass-t);box-shadow:0 0 0 3px var(--brass-soft)}
.help{font-size:.84rem;color:var(--text-3)}
.seg{display:flex;flex-wrap:wrap;gap:8px}
.seg label{display:inline-flex;align-items:center;gap:8px;min-height:40px;padding:0 14px;border:1px solid var(--line-2);border-radius:999px;cursor:pointer;font-weight:600;font-size:.9rem;color:var(--text-2)}
.seg input{position:absolute;opacity:0;pointer-events:none}
.seg label:has(input:checked){border-color:var(--brass);background:var(--brass-soft);color:var(--brass-t)}
.seg label:has(input:focus-visible){outline:2px solid var(--brass-t);outline-offset:2px}

/* upload */
.drop{position:relative;display:grid;place-items:center;gap:6px;text-align:center;aspect-ratio:1;border:1.5px dashed var(--line-2);border-radius:14px;background:var(--sunken);color:var(--text-2);cursor:pointer;overflow:hidden;transition:border-color .2s,background .2s}
.drop:hover,.drop.over{border-color:var(--brass-t);background:var(--brass-soft)}
.drop input{position:absolute;inset:0;opacity:0;cursor:pointer}
.drop .ph{font-size:2rem;color:var(--brass-t)}
.drop img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.drop .swap{position:absolute;left:10px;bottom:10px;display:none;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:999px;background:rgba(255,255,255,.95);color:var(--text);font:600 .8rem var(--font-b);box-shadow:var(--shadow)}
.drop.has-img .swap{display:inline-flex}
.drop.has-img .hint{display:none}
.spgrid{display:grid;gap:16px;grid-template-columns:minmax(0,1fr)}
@media (min-width:900px){.spgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
.sp .drop.wide{aspect-ratio:16/10;margin-top:12px}
.sp-acts{display:flex;gap:8px;margin-top:12px}
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:10px}
.gal figure{position:relative;margin:0;aspect-ratio:1;border-radius:12px;overflow:hidden;background:var(--sunken)}
.gal figure img{width:100%;height:100%;object-fit:cover}
.gal figure .del{position:absolute;top:6px;right:6px}
.gal figure .btn.icon{width:32px;height:32px;background:rgba(255,255,255,.95);border-color:transparent;color:var(--danger)}
.gal .add{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;aspect-ratio:1;border:1.5px dashed var(--line-2);border-radius:12px;color:var(--text-2);font:600 .8rem var(--font-b);cursor:pointer;background:var(--sunken)}
.gal .add:hover{border-color:var(--brass-t);background:var(--brass-soft)}
.gal .add input{position:absolute;inset:0;opacity:0;cursor:pointer}
.gal .add .ph{font-size:1.4rem;color:var(--brass-t)}
.gal .pending{outline:2px solid var(--brass);outline-offset:-2px}

/* switch */
.switch{display:flex;gap:12px;align-items:flex-start;margin-top:16px;cursor:pointer}
.switch input{position:absolute;opacity:0}
.switch .track{flex:none;width:44px;height:26px;border-radius:999px;background:var(--line-2);position:relative;transition:background .2s;margin-top:2px}
.switch .track::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.2);transition:transform .2s var(--ease)}
.switch input:checked + .track{background:var(--brass)}
.switch input:checked + .track::after{transform:translateX(18px)}
.switch input:focus-visible + .track{outline:2px solid var(--brass-t);outline-offset:2px}
.switch b{display:block;font-size:.92rem}
.switch span.d{display:block;font-size:.84rem;color:var(--text-3)}

details.adv summary{list-style:none;cursor:pointer;display:flex;align-items:center;justify-content:space-between;font:700 1.02rem var(--font-d)}
details.adv summary::-webkit-details-marker{display:none}
details.adv summary .ph{transition:transform .2s var(--ease);color:var(--text-3)}
details.adv[open] summary .ph{transform:rotate(180deg)}

.savebar{position:sticky;bottom:calc(72px + env(safe-area-inset-bottom));z-index:30;display:flex;gap:10px;justify-content:flex-end;margin-top:18px;padding:12px;background:rgba(255,255,255,.95);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid var(--line);border-radius:var(--r-panel);box-shadow:var(--shadow)}
.savebar .btn.primary{flex:1;max-width:260px}
@media (min-width:1024px){.savebar{bottom:16px}}
.danger-zone{border-color:rgba(180,35,24,.25)}

/* toast + progress */
.toasts{position:fixed;top:72px;left:50%;transform:translateX(-50%);z-index:40;display:grid;gap:8px;width:min(520px,calc(100% - 32px))}
@media (min-width:1024px){.toasts{top:20px}}
.toast{display:flex;align-items:flex-start;gap:10px;padding:12px 14px;border-radius:12px;background:#fff;border:1px solid var(--line);box-shadow:0 10px 30px rgba(20,24,30,.12);font-weight:500;animation:in .35s var(--ease)}
.toast.ok .ph{color:var(--ok)}.toast.err .ph{color:var(--danger)}
.toast.err{border-color:rgba(180,35,24,.3)}
.toast button{margin-left:auto;border:0;background:none;color:var(--text-3);cursor:pointer;font-size:1.1rem}
@keyframes in{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
.busy{position:fixed;inset:0;z-index:50;display:none;place-items:center;padding:20px;background:rgba(244,245,247,.86);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
.busy.on{display:grid}
.busy .box{width:min(420px,100%);padding:24px;background:#fff;border:1px solid var(--line);border-radius:var(--r-panel);box-shadow:0 20px 50px rgba(20,24,30,.14)}
.busy h2{font-size:1.15rem}
.busy p{color:var(--text-2);margin:6px 0 16px}
.bar{height:6px;border-radius:999px;background:var(--sunken);overflow:hidden}
.bar i{display:block;height:100%;width:40%;border-radius:999px;background:var(--brass);animation:slide 1.4s var(--ease) infinite}
@keyframes slide{from{transform:translateX(-100%)}to{transform:translateX(260%)}}
.steps{display:grid;gap:8px;margin-top:16px;font-size:.9rem;color:var(--text-3)}
.steps div{display:flex;align-items:center;gap:8px}
.steps .now{color:var(--text);font-weight:600}
.steps .done{color:var(--ok)}

dialog{border:0;padding:0;border-radius:var(--r-panel);width:min(420px,calc(100% - 32px));box-shadow:0 20px 50px rgba(20,24,30,.2)}
dialog::backdrop{background:rgba(20,24,30,.35)}
dialog .in{padding:22px}
dialog h2{font-size:1.15rem}
dialog p{color:var(--text-2);margin:8px 0 18px}
dialog .row{display:flex;gap:10px;justify-content:flex-end}

/* login */
.auth{min-height:100dvh;display:grid;grid-template-columns:1fr}
.auth .art{display:none;position:relative;overflow:hidden;background:#15181c}
.auth .art img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.8}
.auth .art::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(21,24,28,.15),rgba(21,24,28,.85))}
.auth .art .cap{position:absolute;left:44px;right:44px;bottom:44px;z-index:1;color:#f6f3ec}
.auth .art .cap img{height:64px;width:auto;margin-bottom:18px}
.auth .art h2{font-size:1.9rem;max-width:18ch}
.auth .art p{color:rgba(246,243,236,.8);margin:10px 0 0;max-width:42ch}
.auth .form{display:grid;place-items:center;padding:28px 18px}
.auth .card{width:min(400px,100%)}
.auth .card .brand{margin-bottom:28px}
.auth h1{font-size:1.7rem}
.auth .card > p{color:var(--text-2);margin:8px 0 6px}
.pw{position:relative}
.pw button{position:absolute;right:6px;top:50%;transform:translateY(-50%);width:36px;height:36px;border:0;background:none;color:var(--text-3);cursor:pointer;border-radius:8px}
.alert{display:flex;gap:10px;align-items:flex-start;margin-top:16px;padding:12px 14px;border-radius:12px;background:var(--danger-soft);color:var(--danger);font-weight:500;font-size:.92rem}
@media (min-width:900px){.auth{grid-template-columns:1.1fr 1fr}.auth .art{display:block}}

body:has(.savebar) .tabbar{display:none}
body:has(.savebar) .savebar{bottom:calc(12px + env(safe-area-inset-bottom))}
body:has(.savebar) .main{padding-bottom:calc(40px + env(safe-area-inset-bottom))}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
'''

JS = r'''
(function(){
  // toasts: auto-hide success
  document.querySelectorAll('.toast').forEach(t=>{
    t.querySelector('button')?.addEventListener('click',()=>t.remove());
    if(t.classList.contains('ok')) setTimeout(()=>t.remove(),4500);
  });
  // character counters
  document.querySelectorAll('[data-count]').forEach(el=>{
    const out=document.getElementById(el.dataset.count), max=+el.getAttribute('maxlength')||0;
    const upd=()=>{out.textContent=el.value.length+(max?' / '+max:'');out.classList.toggle('over',max&&el.value.length>=max)};
    el.addEventListener('input',upd);upd();
  });
  // main photo preview
  document.querySelectorAll('.drop').forEach(d=>{
    const inp=d.querySelector('input');
    ['dragenter','dragover'].forEach(e=>d.addEventListener(e,()=>d.classList.add('over')));
    ['dragleave','drop'].forEach(e=>d.addEventListener(e,()=>d.classList.remove('over')));
    inp.addEventListener('change',()=>{
      const f=inp.files[0]; if(!f) return;
      let img=d.querySelector('img'); if(!img){img=document.createElement('img');d.prepend(img)}
      img.src=URL.createObjectURL(f); d.classList.add('has-img');
    });
  });
  // extra photo previews
  document.querySelectorAll('[data-extra]').forEach(inp=>{
    inp.addEventListener('change',()=>{
      const gal=inp.closest('.gal'); gal.querySelectorAll('.pending').forEach(x=>x.remove());
      [...inp.files].forEach(f=>{const fg=document.createElement('figure');fg.className='pending';const i=document.createElement('img');i.src=URL.createObjectURL(f);i.alt='';fg.append(i);gal.insertBefore(fg,inp.closest('.add'))});
    });
  });
  // search filter
  const q=document.getElementById('q');
  if(q){const cards=[...document.querySelectorAll('.pcard')],none=document.getElementById('none');
    q.addEventListener('input',()=>{const v=q.value.trim().toLowerCase();let n=0;
      cards.forEach(c=>{const hit=c.dataset.name.includes(v);c.hidden=!hit;n+=hit});none.hidden=n>0;});}
  // busy overlay on save, with honest step hints
  document.querySelectorAll('form[data-busy]').forEach(f=>f.addEventListener('submit',()=>{
    const b=document.querySelector('.busy'); if(!b) return;
    const photos=[...f.querySelectorAll('input[type=file]')].reduce((n,i)=>n+i.files.length,0);
    const rb=f.querySelector('[name=remove_bg]')?.checked;
    b.querySelector('[data-est]').textContent = photos ? (rb ? 'Sekitar '+photos+' menit untuk '+photos+' foto. Jangan tutup halaman ini.' : 'Sebentar lagi selesai.') : 'Sebentar lagi selesai.';
    if(!photos) b.querySelector('[data-step=photo]').remove();
    b.classList.add('on');
    const steps=[...b.querySelectorAll('[data-step]')]; let i=0;
    const tick=()=>{steps.forEach((s,k)=>{s.className=k<i?'done':k===i?'now':''});};
    tick(); if(steps.length>1) setTimeout(()=>{i=1;tick()}, photos? Math.max(4000, photos*(rb?55000:3000)) : 800);
  }));
  // confirm dialogs
  document.querySelectorAll('[data-confirm]').forEach(btn=>btn.addEventListener('click',e=>{
    e.preventDefault(); const d=document.getElementById(btn.dataset.confirm); d.showModal();
  }));
  document.querySelectorAll('dialog [data-close]').forEach(b=>b.addEventListener('click',()=>b.closest('dialog').close()));
  // show/hide password
  document.querySelectorAll('.pw button').forEach(b=>b.addEventListener('click',()=>{
    const i=b.parentElement.querySelector('input');const s=i.type==='password';i.type=s?'text':'password';
    b.innerHTML=s?'<i class="ph ph-eye-slash"></i>':'<i class="ph ph-eye"></i>';b.setAttribute('aria-label',s?'Sembunyikan password':'Tampilkan password');
  }));
})();
'''

HEAD = '''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow"><meta name="theme-color" content="#ffffff"><title>{title} | Admin Mitra Viktory Logam</title>
<link rel="icon" href="/img/logo.png"><link rel="apple-touch-icon" href="/img/logo.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/fill/style.css">
<style>{css}</style></head><body>'''


def _toasts(flashes):
    out = ''
    for kind, msg in flashes:
        icon = 'ph-fill ph-check-circle' if kind == 'ok' else 'ph-fill ph-warning-circle'
        out += f'<div class="toast {kind}" role="status"><i class="{icon}"></i><span>{escape(msg)}</span><button type="button" aria-label="Tutup">&times;</button></div>'
    return f'<div class="toasts">{out}</div>' if out else ''


def shell(title, body, active, flashes, foto=False):
    def nav_link(href, icon, label, key, cls=''):
        cur = ' aria-current="page"' if key == active else ''
        return f'<a href="{href}" class="{cls}"{cur}><i class="ph {icon}"></i><span>{label}</span></a>'
    side = f'''<aside class="side"><a class="brand" href="/admin/"><img src="/img/logo.png" alt=""><span>Mitra Viktory Logam<small>Panel admin</small></span></a>
<nav>{nav_link('/admin/', 'ph-package', 'Produk', 'produk')}{nav_link('/admin/produk/baru', 'ph-plus-circle', 'Tambah produk', 'baru')}
{nav_link('/admin/foto', 'ph-images', 'Foto website', 'foto') if foto else ''}<a href="{SITE}" target="_blank" rel="noopener"><i class="ph ph-arrow-square-out"></i><span>Lihat website</span></a></nav>
<div class="bottom">{nav_link('/admin/password', 'ph-key', 'Ganti password', 'akun')}<a href="/admin/logout"><i class="ph ph-sign-out"></i><span>Keluar</span></a></div></aside>'''
    top = f'''<header class="topbar"><a class="brand" href="/admin/"><img src="/img/logo.png" alt=""><span>Admin MVL</span></a>
<a class="btn sm" href="{SITE}" target="_blank" rel="noopener"><i class="ph ph-arrow-square-out"></i>Website</a></header>'''
    tab = f'''<nav class="tabbar{'' if foto else ' t3'}" aria-label="Menu">{nav_link('/admin/', 'ph-package', 'Produk', 'produk')}{nav_link('/admin/produk/baru', 'ph-plus', 'Tambah', 'baru', 'cta')}{nav_link('/admin/foto', 'ph-images', 'Foto', 'foto') if foto else ''}{nav_link('/admin/password', 'ph-user-circle', 'Akun', 'akun')}</nav>'''
    busy = '''<div class="busy" role="alertdialog" aria-live="polite" aria-label="Sedang menyimpan"><div class="box"><h2>Menyimpan perubahan</h2><p data-est>Sebentar lagi selesai.</p>
<div class="bar"><i></i></div><div class="steps"><div data-step="photo"><i class="ph ph-image"></i>Mengolah foto dan menghapus background</div><div data-step="site"><i class="ph ph-globe-simple"></i>Memperbarui website</div></div></div></div>'''
    return (HEAD.format(title=escape(title), css=CSS) + f'<div class="shell">{side}<div>{top}<main class="main">{body}</main></div></div>'
            + tab + busy + _toasts(flashes) + f'<script>{JS}</script></body></html>')


def login_page(err):
    alert = f'<div class="alert" role="alert"><i class="ph-fill ph-warning-circle"></i><span>{escape(err)}</span></div>' if err else ''
    return HEAD.format(title='Masuk', css=CSS) + f'''<div class="auth">
<div class="art"><img class="bg" src="/img/hero-pour-v3.jpg" alt=""><div class="cap"><img src="/img/logo.png" alt="Logo CV. Mitra Viktory Logam">
<h2>Kelola produk website Anda sendiri.</h2><p>Tambah produk baru, ganti foto, dan atur urutan. Perubahan langsung tampil di mitraviktorylogam.com.</p></div></div>
<div class="form"><div class="card"><a class="brand" href="{SITE}"><img src="/img/logo.png" alt=""><span>Mitra Viktory Logam<small>Panel admin</small></span></a>
<h1>Masuk</h1><p>Gunakan username dan password yang diberikan.</p>{alert}
<form method="post" autocomplete="on"><div class="field"><label for="u">Username</label><input id="u" name="user" type="text" autocomplete="username" autocapitalize="none" required></div>
<div class="field"><label for="p">Password</label><div class="pw"><input id="p" name="password" type="password" autocomplete="current-password" required><button type="button" aria-label="Tampilkan password"><i class="ph ph-eye"></i></button></div></div>
<button class="btn primary" type="submit" style="width:100%;margin-top:22px">Masuk</button></form></div></div></div><script>{JS}</script></body></html>'''


def products_page(ps, tok):
    if not ps:
        grid = '<div class="empty"><i class="ph ph-package"></i><b>Belum ada produk</b><span>Tambahkan produk pertama, lengkap dengan foto dan penjelasannya.</span><a class="btn primary" href="/admin/produk/baru"><i class="ph ph-plus"></i>Tambah produk</a></div>'
    else:
        cards = ''
        t = int(time.time())
        for i, p in enumerate(ps):
            pid = escape(p['id'])
            up = '' if i == 0 else f'<form method="post" action="/admin/produk/{pid}/naik"><input type="hidden" name="csrf" value="{tok}"><button class="btn icon" type="submit" aria-label="Pindah ke atas" title="Pindah ke atas"><i class="ph ph-arrow-up"></i></button></form>'
            down = '' if i == len(ps) - 1 else f'<form method="post" action="/admin/produk/{pid}/turun"><input type="hidden" name="csrf" value="{tok}"><button class="btn icon" type="submit" aria-label="Pindah ke bawah" title="Pindah ke bawah"><i class="ph ph-arrow-down"></i></button></form>'
            home = '<span class="chip home"><i class="ph ph-house-simple"></i>Tampil di beranda</span>' if i < 7 else ''
            photos = 1 + len(p.get('gallery', []))
            cards += f'''<article class="pcard" data-name="{escape(p['name'].lower())}"><a class="thumb" href="/admin/produk/{pid}"><img src="/img/{escape(p['image'])}-sq.jpg?t={t}" alt="" loading="lazy"></a>
<div><h3>{escape(p['name'])}</h3><div class="meta"><span class="chip">{escape(p['material'])}</span><span class="chip"><i class="ph ph-image"></i>{photos} foto</span>{home}</div>
<div class="acts"><a class="btn sm" href="/admin/produk/{pid}"><i class="ph ph-pencil-simple"></i>Edit</a><a class="btn icon" href="{SITE}/{escape(p['page'])}" target="_blank" rel="noopener" aria-label="Lihat di website" title="Lihat di website"><i class="ph ph-arrow-square-out"></i></a><span class="spacer"></span>{up}{down}</div></div></article>'''
        grid = f'''<div class="toolbar"><div class="search"><i class="ph ph-magnifying-glass"></i><input id="q" type="search" placeholder="Cari produk" aria-label="Cari produk"></div></div>
<div class="pgrid">{cards}</div><div id="none" class="empty" hidden><i class="ph ph-magnifying-glass"></i><b>Produk tidak ditemukan</b><span>Coba kata lain, misalnya bushing atau stuffing.</span></div>'''
    return f'''<div class="ph-head"><div><h1>Produk</h1><p>{len(ps)} produk. Urutan di sini sama dengan di website, dan 7 produk teratas tampil di beranda.</p></div>
<a class="btn primary" href="/admin/produk/baru"><i class="ph ph-plus"></i>Tambah produk</a></div>{grid}'''


def product_form(p, is_new, tok):
    pid = escape(p.get('id', ''))
    t = int(time.time())
    cur_mat = p.get('material', 'Kuningan')
    mats = list(MATERIALS) + ([cur_mat] if cur_mat not in MATERIALS else [])
    seg = ''.join(f'<label><input type="radio" name="material" value="{escape(m)}"{" checked" if m == cur_mat else ""}>{escape(m)}</label>' for m in mats)
    intro = escape('\n\n'.join(p.get('intro', [])))
    uses = escape('\n'.join(p.get('uses', [])))
    main = '' if is_new else f'<img src="/img/{escape(p["image"])}-sq.jpg?t={t}" alt="Foto utama saat ini">'
    gal = ''
    side_forms = ''
    for i, g in enumerate(p.get('gallery', [])):
        gal += f'''<figure><img src="/img/{escape(g)}-sq.jpg?t={t}" alt=""><span class="del"><button class="btn icon" type="submit" form="fdel-{i}" aria-label="Hapus foto ini" title="Hapus foto ini"><i class="ph ph-trash"></i></button></span></figure>'''
        side_forms += f'<form id="fdel-{i}" method="post" action="/admin/produk/{pid}/foto-hapus/{i}" hidden><input type="hidden" name="csrf" value="{tok}"></form>'
    action = '/admin/produk/baru' if is_new else f'/admin/produk/{pid}'
    title = 'Tambah produk' if is_new else escape(p.get('name', 'Edit produk'))
    view = '' if is_new else f'<a class="btn" href="{SITE}/{escape(p["page"])}" target="_blank" rel="noopener"><i class="ph ph-arrow-square-out"></i>Lihat di website</a>'
    delete = '' if is_new else f'''<div class="panel danger-zone"><h2>Hapus produk</h2><p class="sub">Produk dan halamannya akan dihapus dari website.</p>
<button class="btn danger" type="button" data-confirm="del" style="margin-top:8px"><i class="ph ph-trash"></i>Hapus produk ini</button></div>
<dialog id="del"><div class="in"><h2>Hapus "{escape(p.get('name', ''))}"?</h2><p>Halaman produk ini akan hilang dari website. Tindakan ini tidak bisa dibatalkan.</p>
<div class="row"><button class="btn" type="button" data-close>Batal</button><button class="btn danger" type="submit" form="fdel-product">Ya, hapus</button></div></div></dialog>'''
    return f'''<a class="back" href="/admin/"><i class="ph ph-arrow-left"></i>Semua produk</a>
<div class="ph-head"><div><h1>{title}</h1><p>{'Isi data produk dan upload fotonya. Halaman produk dan data Google dibuat otomatis.' if is_new else 'Ubah data atau foto, lalu simpan. Website langsung diperbarui.'}</p></div>{view}</div>
<form method="post" action="{action}" enctype="multipart/form-data" data-busy><input type="hidden" name="csrf" value="{tok}">
<div class="layout"><div>
<section class="panel"><h2>Informasi produk</h2><p class="sub">Tampil di kartu produk dan judul halaman.</p>
<div class="field"><label for="name">Nama produk <span class="count" id="c-name"></span></label><input id="name" name="name" type="text" value="{escape(p.get('name', ''))}" maxlength="80" required data-count="c-name" placeholder="Contoh: Impeller"></div>
<div class="field"><span class="lbl">Bahan</span><div class="seg" role="radiogroup" aria-label="Bahan">{seg}</div></div>
<div class="field"><label for="short">Deskripsi singkat <span class="count" id="c-short"></span></label><input id="short" name="short" type="text" value="{escape(p.get('short', ''))}" maxlength="160" required data-count="c-short" placeholder="Satu kalimat, misalnya untuk apa produk ini dipakai"></div></section>
<section class="panel"><h2>Isi halaman produk</h2><p class="sub">Boleh dikosongkan, nanti dibuat otomatis.</p>
<div class="field"><label for="intro">Penjelasan</label><textarea id="intro" name="intro" rows="6" placeholder="Jelaskan produknya. Pisahkan paragraf dengan baris kosong.">{intro}</textarea></div>
<div class="field"><label for="uses">Dipakai untuk</label><textarea id="uses" name="uses" rows="4" placeholder="Satu kegunaan per baris">{uses}</textarea><span class="help">Contoh: Pompa air, Mesin pabrik kelapa sawit</span></div></section>
<section class="panel"><details class="adv"><summary>Pengaturan Google<i class="ph ph-caret-down"></i></summary>
<p class="sub" style="margin-top:6px">Opsional. Kosongkan untuk dibuat otomatis. Sebutkan nama produk dan Medan supaya mudah ditemukan.</p>
<div class="field"><label for="h1">Judul di halaman produk <span class="count" id="c-h1"></span></label><input id="h1" name="h1" type="text" value="{escape(p.get('h1', ''))}" maxlength="90" data-count="c-h1"></div>
<div class="field"><label for="title">Judul di hasil Google <span class="count" id="c-title"></span></label><input id="title" name="title" type="text" value="{escape(p.get('title', ''))}" maxlength="90" data-count="c-title"></div>
<div class="field"><label for="desc">Deskripsi di hasil Google <span class="count" id="c-desc"></span></label><textarea id="desc" name="desc" rows="3" maxlength="170" data-count="c-desc">{escape(p.get('desc', ''))}</textarea></div></details></section>
</div>
<div class="aside"><section class="panel"><h2>Foto</h2><p class="sub">{'Wajib ada foto utama.' if is_new else 'Klik foto untuk mengganti.'}</p>
<div class="field"><span class="lbl">Foto utama</span><label class="drop{' has-img' if main else ''}">{main}<span class="hint"><i class="ph ph-image-square"></i><br><b>Pilih foto</b><br><span class="help">atau seret ke sini</span></span><span class="swap"><i class="ph ph-arrows-clockwise"></i>Ganti foto</span>
<input name="photo" type="file" accept="image/*" aria-label="Foto utama" {'required' if is_new else ''}></label></div>
<div class="field"><span class="lbl">Foto tambahan</span><div class="gal">{gal}<label class="add"><i class="ph ph-plus"></i><span>Tambah</span><input data-extra name="extra" type="file" accept="image/*" multiple aria-label="Foto tambahan"></label></div><span class="help">Tampil di halaman produk. Boleh pilih beberapa sekaligus.</span></div>
<label class="switch"><input type="checkbox" name="remove_bg" value="1" checked><span class="track"></span><span><b>Hapus background otomatis</b><span class="d">Latar putih rapi seperti katalog. Matikan untuk produk yang masih menempel di mesin.</span></span></label>
</section>{delete}</div></div>
<div class="savebar"><a class="btn" href="/admin/">Batal</a><button class="btn primary" type="submit"><i class="ph ph-check"></i>Simpan</button></div></form>{side_forms}{'' if is_new else f'<form id="fdel-product" method="post" action="/admin/produk/{pid}/hapus" hidden><input type="hidden" name="csrf" value="{tok}"></form>'}'''


def password_page(tok):
    return f'''<div class="ph-head"><div><h1>Akun</h1><p>Ganti password untuk masuk ke panel admin.</p></div></div>
<form method="post" class="panel" style="max-width:520px"><input type="hidden" name="csrf" value="{tok}"><h2>Ganti password</h2>
<div class="field"><label for="o">Password lama</label><div class="pw"><input id="o" name="old" type="password" autocomplete="current-password" required><button type="button" aria-label="Tampilkan password"><i class="ph ph-eye"></i></button></div></div>
<div class="field"><label for="n">Password baru</label><div class="pw"><input id="n" name="new" type="password" autocomplete="new-password" minlength="8" required><button type="button" aria-label="Tampilkan password"><i class="ph ph-eye"></i></button></div><span class="help">Minimal 8 karakter.</span></div>
<div class="field"><label for="n2">Ulangi password baru</label><div class="pw"><input id="n2" name="new2" type="password" autocomplete="new-password" required><button type="button" aria-label="Tampilkan password"><i class="ph ph-eye"></i></button></div></div>
<div style="display:flex;gap:10px;margin-top:22px"><button class="btn primary" type="submit">Simpan password</button><a class="btn" href="/admin/">Batal</a></div></form>
<div class="panel" style="max-width:520px"><h2>Keluar</h2><p class="sub">Keluar dari panel admin di perangkat ini.</p><a class="btn" href="/admin/logout" style="margin-top:8px"><i class="ph ph-sign-out"></i>Keluar</a></div>'''


def site_photos_page(slots, current, tok):
    t = int(time.time())
    cards = ''
    for key, title, where, default in slots:
        src = current.get(key) or default
        reset = f'<button class="btn sm" type="submit" form="reset-{key}"><i class="ph ph-arrow-counter-clockwise"></i>Foto awal</button>' if key in current else ''
        cards += (f'<form class="panel sp" method="post" action="/admin/foto/{key}" enctype="multipart/form-data" data-busy>'
                  f'<input type="hidden" name="csrf" value="{tok}"><h2>{escape(title)}</h2><p class="sub">Tampil di: {escape(where)}</p>'
                  f'<label class="drop wide has-img"><img src="/img/{escape(src)}?t={t}" alt="{escape(title)}"><span class="hint"></span>'
                  f'<span class="swap"><i class="ph ph-arrows-clockwise"></i>Pilih foto baru</span>'
                  f'<input name="photo" type="file" accept="image/*" required aria-label="Foto baru untuk {escape(title)}"></label>'
                  f'<div class="sp-acts"><button class="btn primary sm" type="submit"><i class="ph ph-check"></i>Simpan</button>{reset}</div></form>')
    resets = ''.join(f'<form id="reset-{k}" method="post" action="/admin/foto/{k}/reset" hidden><input type="hidden" name="csrf" value="{tok}"></form>' for k, *_ in slots if k in current)
    return ('<div class="ph-head"><div><h1>Foto website</h1><p>Ganti foto di beranda dan halaman lain. Foto produk diatur di menu Produk.</p></div></div>'
            f'<div class="spgrid">{cards}</div>{resets}')
