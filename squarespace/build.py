# Builds Squarespace Basic-plan blocks (no JS) from ../index.html.
# Output: block-a.html (styles + page up to the estimate section), block-b.html (footer + floats).
# A native Squarespace Form block sits between them.
import re, os
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/..')
B = 'https://feliperpovera.github.io/florida-fence-solution/'
s = open('index.html').read()
css = s[s.index('<style>') + 7:s.index('</style>')]
body = s[s.index('<body>') + 6:s.index('</body>')]

# ---------- CSS ----------
css = re.sub(r'\bfooter\b', '.ffs-foot', css)
css = css.replace('.slide button', '.slide a').replace('.tabs button', '.tabs a')

def scope(css):
    out = []; i = 0
    def sel(x):
        parts = []
        for p in x.split(','):
            p = p.strip()
            if p in (':root', 'html', 'body'): parts.append('.ffs')
            elif p.startswith(':root'): parts.append('.ffs' + p[5:])
            else: parts.append('.ffs ' + p)
        return ','.join(parts)
    while i < len(css):
        j = css.find('{', i)
        if j < 0: break
        pre = re.sub(r'/\*.*?\*/', '', css[i:j], flags=re.S).strip()
        if pre.startswith(('@media', '@supports', '@keyframes')):
            depth = 1; k = j + 1
            while depth: depth += {'{': 1, '}': -1}.get(css[k], 0); k += 1
            out.append(pre + '{' + (css[j+1:k-1] if pre.startswith('@keyframes') else scope(css[j+1:k-1])) + '}'); i = k; continue
        k = css.index('}', j)
        if pre: out.append(sel(pre) + '{' + css[j+1:k] + '}')
        i = k + 1
    return '\n'.join(out)

css = scope(css)
css = re.sub(r'url\((?!["\']?(https?:|data:))["\']?([^)"\']+)["\']?\)', lambda m: f'url({B}{m.group(2)})', css)

extra = '''
/* --- Squarespace host --- */
#header,.header,#footer-sections,.sqs-announcement-bar-dropzone{display:none!important}
.page-section:has(.ffs){padding:0!important;min-height:0!important}
.page-section:has(.ffs) .section-background{display:none}
.page-section:has(.ffs) .content-wrapper{padding:0!important;max-width:none!important}
.fluid-engine:has(.ffs){display:flex!important;flex-direction:column!important;padding:0!important;background:#fff}
.fe-block:has(.ffs){grid-area:auto!important;height:auto!important;width:100%!important}
.fe-block:has(.ffs .hero){order:1}
.fe-block:has(.sqs-block-map),.fe-block:has(.sqs-block-map-content),.fe-block:has([class*=sqs-block-map]){order:2}
.fe-block:has(.ffs .map-over){order:3}
.fe-block:has(.sqs-block-form){order:4}
.fe-block:has(.ffs .ffs-foot){order:5}
.sqs-block-code{padding:0!important}
.ffs h1,.ffs h2,.ffs h3,.ffs h4{font-family:var(--f)!important;font-weight:800!important;text-transform:none!important;color:inherit;margin-top:0}
.ffs h1{letter-spacing:-.035em!important;line-height:1.05!important}
.ffs h2{letter-spacing:-.035em!important;line-height:1.05!important}
.ffs h3,.ffs h4{letter-spacing:-.02em!important;line-height:1.2!important}
.ffs p,.ffs li,.ffs a,.ffs span,.ffs small,.ffs summary,.ffs b,.ffs figcaption,.ffs blockquote{font-family:var(--f)}
.ffs p{margin:0}
.ffs a{text-decoration:none}
.ffs .hero h1,.ffs .dark h2,.ffs .dark h3,.ffs .ffs-foot h4,.ffs .card.photo h3,.ffs .county.home h3,.ffs .review.more b{color:#fff!important}
.ffs .hero h1 em{color:var(--accent)!important}
/* header always solid (no scroll JS) */
.ffs .site-header{background:rgba(17,17,17,.88);backdrop-filter:blur(14px) saturate(1.4);-webkit-backdrop-filter:blur(14px) saturate(1.4);border-color:rgba(255,255,255,.08)}
/* catalog: CSS-only modal + tabs via :target (no JS) */
.ffs .catalog-sec{display:none}
.ffs .catalog-sec:has(.panel:target){display:block;position:fixed;inset:0;z-index:1000;overflow-y:auto;overscroll-behavior:contain;background:rgba(10,10,10,.72);backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px);padding:16px}
.ffs .catalog-sec > .wrap{background:#fff;border-radius:var(--r-lg);max-width:1180px;margin:24px auto;padding:clamp(18px,3vw,36px)}
.ffs .catalog-sec .head{margin-bottom:16px;align-items:start;flex-wrap:nowrap}
.ffs .catalog-sec .head h2{font-size:clamp(1.6rem,1.3rem + 1.2vw,2.4rem);margin:0}
.ffs .cm-x{flex:none;width:52px;height:52px;border-radius:50%;background:var(--dark);color:#fff!important;display:grid;place-items:center;font-size:1.2rem;text-decoration:none;transition:transform .2s var(--ease),background .2s}
.ffs .cm-x:hover{background:var(--accent);color:var(--dark)!important;transform:rotate(90deg)}
.ffs .catalog-sec .tabs a{text-decoration:none}
.ffs .catalog-sec .panel{display:none;scroll-margin-top:260px}
.ffs .catalog-sec:has(.panel:target) .cm-x{position:fixed;top:28px;right:28px;z-index:5;box-shadow:0 10px 30px -10px rgba(0,0,0,.6)}
.ffs .catalog-sec .panel:target{display:block}
.ffs .catalog-sec:has(#catalog-aluminum:target) .tabs a[href="#catalog-aluminum"],
.ffs .catalog-sec:has(#catalog-wood:target) .tabs a[href="#catalog-wood"],
.ffs .catalog-sec:has(#catalog-pvc:target) .tabs a[href="#catalog-pvc"],
.ffs .catalog-sec:has(#catalog-chain-link:target) .tabs a[href="#catalog-chain-link"]{background:var(--dark);color:#fff;border-color:var(--dark)}
.ffs .catalog-sec .panel-head{margin:20px 0}
.ffs .cat-grid .slide a{display:block;border-radius:var(--r);overflow:hidden;aspect-ratio:4/3;cursor:zoom-in}
.ffs .cat-grid .slide a img{width:100%;height:100%;object-fit:cover;transition:transform .7s var(--ease)}
.ffs .cat-grid .slide a:hover img{transform:scale(1.06)}
@media (max-width:767px){.ffs .catalog-sec:has(.panel:target){padding:0}.ffs .catalog-sec > .wrap{margin:0;border-radius:0;min-height:100%}.ffs .cat-grid{grid-template-columns:1fr 1fr;gap:10px}.ffs .catalog-sec .tabs{flex-wrap:nowrap;overflow-x:auto}.ffs .cm-x{width:46px;height:46px}}
/* map: native Squarespace Map block + overlay card */
.ffs .map-static{display:block;position:relative;margin-top:16px;border-radius:24px;overflow:hidden;height:420px;background:#e8e4dd}
.ffs .map-static img{width:100%;height:100%;object-fit:cover;display:block}
.ffs .map-static .osm{position:absolute;left:10px;bottom:8px;font-size:11px;background:rgba(255,255,255,.85);padding:2px 6px;border-radius:4px;color:#333}
.ffs .map-over .map-card{bottom:56px!important}
@media (max-width:767px){.ffs .map-static{height:300px;border-radius:24px 24px 0 0}}

.ffs #areas{padding-bottom:16px}
.fe-block:has([class*=sqs-block-map]){box-sizing:border-box!important;width:calc(min(1280px,100%) - 2*clamp(20px,4vw,48px))!important;height:420px!important;margin:0 auto!important;border-radius:24px;overflow:hidden;padding:0!important}
.fe-block:has([class*=sqs-block-map]) .sqs-block,.fe-block:has([class*=sqs-block-map]) .sqs-block-content,.fe-block:has([class*=sqs-block-map]) .sqs-block-map{height:100%!important;padding:0!important}
.fe-block:has(.ffs .map-over){position:relative!important;z-index:20!important;overflow:visible!important}
.fe-block:has(.ffs .map-over) .sqs-block,.fe-block:has(.ffs .map-over) .sqs-block-content{overflow:visible!important}
.fe-block:has([class*=sqs-block-map]){position:relative;z-index:1!important}
.ffs .map-over{position:relative;z-index:3;height:0}
.ffs .map-over .wrap{position:relative;height:0}
.ffs .map-over .map-card{position:absolute;right:calc(var(--pad) + 24px);bottom:40px;max-width:320px}
.ffs .map-after{height:clamp(72px,9vw,128px)}
@media (max-width:767px){
.fe-block:has([class*=sqs-block-map]){height:300px!important;border-radius:24px 24px 0 0}
.ffs .map-over,.ffs .map-over .wrap{height:auto}
.ffs .map-over .map-card{position:static;max-width:none;box-shadow:none;border-radius:0 0 24px 24px;border:1px solid var(--line);border-top:0}
}
/* estimate: info left, native form block on the right (desktop) */
.ffs .estimate{padding-bottom:96px}
.ffs .quote-slot{min-height:980px}
.fe-block:has(.sqs-block-form){position:relative!important;z-index:30!important;box-sizing:border-box!important;background:#111;color:#fff;border-radius:24px;padding:clamp(24px,3vw,40px)!important;
  width:calc((min(1280px,100%) - 2*clamp(20px,4vw,48px) - clamp(40px,6vw,96px))*6/11)!important;
  margin:calc(-980px - 96px) 0 96px calc((100% - min(1280px,100%))/2 + clamp(20px,4vw,48px) + (min(1280px,100%) - 2*clamp(20px,4vw,48px) - clamp(40px,6vw,96px))*5/11 + clamp(40px,6vw,96px))!important;
  min-height:980px}
@media (max-width:1024px){
.ffs .quote-slot{display:none}
.ffs .estimate{padding-bottom:32px}
.fe-block:has(.sqs-block-form){width:calc(100% - 2*clamp(20px,4vw,48px))!important;margin:0 auto 72px!important;min-height:0}
}
/* native Squarespace form styled as the dark quote card */
.fe-block:has(.sqs-block-form) .sqs-block-form{padding:0!important;background:transparent!important;
--tweak-form-block-field-fill-color:#1b1a19;--tweak-form-block-field-fill-color-on-background:#1b1a19;--tweak-form-block-field-fill-color-hsl:30,4%,10%;--tweak-form-block-field-fill-color-on-background-hsl:30,4%,10%;
--tweak-form-block-field-input-color:#fff;--tweak-form-block-field-input-color-on-background:#fff;--tweak-form-block-field-input-color-hsl:0,0%,100%;--tweak-form-block-field-input-color-on-background-hsl:0,0%,100%;
--tweak-form-block-field-border-color:#5a544e;--tweak-form-block-field-border-color-on-background:#5a544e;--tweak-form-block-field-border-color-hsl:30,7%,33%;--tweak-form-block-field-border-color-on-background-hsl:30,7%,33%;
--tweak-form-block-title-color:#fff;--tweak-form-block-title-color-on-background:#fff;--tweak-form-block-caption-color:#b9b2a8;--tweak-form-block-caption-color-on-background:#b9b2a8;--tweak-form-block-description-color:#b9b2a8;--tweak-form-block-description-color-on-background:#b9b2a8;
--tweak-form-block-field-accessory-color:#fff;--tweak-form-block-field-accessory-color-on-background:#fff;--tweak-form-block-option-color:#fff;--tweak-form-block-option-color-on-background:#fff;
--tweak-form-block-button-background-color:#f0ad3d;--tweak-form-block-button-background-color-on-background:#f0ad3d;--tweak-form-block-button-text-color:#111;--tweak-form-block-button-text-color-on-background:#111;
--tweak-form-block-field-accent-color:#f0ad3d;--tweak-form-block-field-accent-color-on-background:#f0ad3d}
.fe-block:has(.sqs-block-form) *{font-family:'Plus Jakarta Sans',system-ui,sans-serif}
.fe-block:has(.sqs-block-form) .sqs-block-content::before{content:"Request your estimate";display:block;font-weight:800;font-size:clamp(1.5rem,1.3rem + .8vw,2rem);letter-spacing:-.02em;line-height:1.2;color:#fff;margin-bottom:4px}
.fe-block:has(.sqs-block-form) .form-wrapper::before{content:"Fields marked (required) must be filled in.";display:block;color:#b9b2a8;font-size:.95rem;margin-bottom:16px}
.fe-block:has(.sqs-block-form) label,.fe-block:has(.sqs-block-form) legend,.fe-block:has(.sqs-block-form) .title{color:#fff!important;font-weight:600}
.fe-block:has(.sqs-block-form) input,.fe-block:has(.sqs-block-form) select,.fe-block:has(.sqs-block-form) textarea{border-radius:12px!important;min-height:52px}
.fe-block:has(.sqs-block-form) button[type=submit],.fe-block:has(.sqs-block-form) input[type=submit]{width:100%!important;background:#f0ad3d!important;color:#111!important;border:0!important;border-radius:999px!important;min-height:52px;font-weight:700!important;font-size:1rem!important}
.fe-block:has(.sqs-block-form) .sqs-block-content::after{content:"No spam. No obligation.";display:block;text-align:center;color:#b9b2a8;font-size:.85rem;margin-top:10px}
'''
css = open('squarespace/fontface.css').read().strip() + '\n' + extra + css
css = re.sub(r'[^\x00-\x7f]', lambda m: '\\%x ' % ord(m.group(0)), css)
# minify
css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
css = re.sub(r'\s*\n\s*', '\n', css)
css = re.sub(r'\s*([{};,])\s*', r'\1', css)

# ---------- HTML ----------
h = body
h = re.sub(r'<script>.*?</script>', '', h, flags=re.S)
h = re.sub(r'<a class="btn btn-accent" href="#top" style="position:absolute;left:-9999px.*?</a>', '', h, flags=re.S)
h = re.sub(r'<span class="lang".*?</span>\s*', '', h, flags=re.S)
h = h.replace('<header class="site-header" id="header">', '<header class="site-header">')
h = h.replace('<main id="top">', '').replace('</main>', '')
h = h.replace('<footer>', '<div class="ffs-foot">').replace('</footer>', '</div>')
h = re.sub(r'<dialog class="lightbox".*?</dialog>', '', h, flags=re.S)
# catalog dialog -> inline section with :target tabs
h = re.sub(r'<dialog class="catalog-modal" id="catalog" aria-labelledby="cm-title">\s*<div class="cm-head">\s*<div>(.*?)</div>.*?</div>',
           r'<section class="catalog-sec" id="catalog" role="dialog" aria-label="Our catalogs"><div class="wrap"><div class="head"><div>\1<p class="lead">Real jobs by our crew. Pick a fence type and tap any photo to see it big.</p></div><a class="cm-x" href="#fences" aria-label="Close catalogs">&#10005;</a></div>', h, count=1, flags=re.S)
h = h.replace('</dialog>', '</div></section>')
h = re.sub(r'<button type="button" role="tab" id="tab-([\w-]+)"[^>]*>(.*?)</button>', r'<a href="#catalog-\1">\2</a>', h)
h = h.replace(' role="tablist"', '').replace(' hidden>', '>')
h = re.sub(r'<button type="button"><img ([^>]*?)data-full="([^"]+)"([^>]*)></button>', r'<a href="\2" target="_blank" rel="noopener"><img \1\3></a>', h)
# map iframe -> card only
h = re.sub(r'<iframe title="Map:.*?</iframe>\s*', '', h, flags=re.S)
m = re.search(r'<div class="map-block reveal">\s*(<div class="map-card">.*?</a>\s*</div>)\s*</div>', h, flags=re.S)
STATIC = ('<a class="map-static" href="https://maps.google.com/?cid=273622298774698385" target="_blank" rel="noopener" aria-label="Open Florida Fence Solution in Google Maps">'
          '<picture><source media="(max-width:767px)" srcset="img/map-hollywood-mobile.webp">'
          '<img src="img/map-hollywood.webp" srcset="img/map-hollywood.webp 1280w, img/map-hollywood-2560.webp 2560w" sizes="(max-width:1280px) 100vw, 1280px" width="1280" height="420" loading="lazy" alt="Map: Florida Fence Solution, 1331 N 70th Way, Hollywood, FL 33024"></picture>'
          '<span class="osm">&#169; OpenStreetMap contributors</span></a>')
card = m.group(1); h = h[:m.start()] + STATIC + h[m.end():]
h = h.replace('<section id="faq"', '@@CUT@@<div class="map-over"><div class="wrap">' + card + '</div></div><div class="map-after"></div><section id="faq"', 1)
# remove JS form (native Squarespace form replaces it)
h = re.sub(r'\s*<!-- TODO: to receive leads.*?-->', '', h, flags=re.S)
h = re.sub(r'<form class="quote.*?</form>', '<div class="quote-slot" aria-hidden="true"></div>', h, flags=re.S)
h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
h = re.sub(r' data-ev="[^"]*"', '', h)
h = re.sub(r'(src|href|srcset)="(?!https?:|tel:|mailto:|#)([^"]+)"', lambda m: f'{m.group(1)}="' + ', '.join((B + u.strip()) for u in m.group(2).split(', ')) + '"' if m.group(1) == 'srcset' else f'{m.group(1)}="{B}{m.group(2)}"', h)
h = h.encode('ascii', 'xmlcharrefreplace').decode()
h = re.sub(r'\n\s*\n+', '\n', h)

cut = h.index('<div class="ffs-foot">')
a, b = h[:cut], h[cut:]
a1, a2 = a.split('@@CUT@@')
for part in (a1, a2): assert part.count('<div') == part.count('</div'), (part.count('<div'), part.count('</div'))
open('squarespace/block-a.html', 'w').write(f'<style>\n{css}\n</style>\n<div class="ffs">{a1}</div>\n')
open('squarespace/block-a2.html', 'w').write(f'<div class="ffs">{a2}</div>\n')
a = a1 + '<div style="width:calc(min(1280px,100%) - 80px);height:420px;margin:0 auto;border-radius:24px;background:#cfd8dc;display:grid;place-items:center">[Squarespace map block]</div>' + a2
open('squarespace/block-b.html', 'w').write(f'<div class="ffs">{b}</div>\n')
fe = lambda x: f'<div class="fe-block">{x}</div>'
fake_form = '<div class="sqs-block-form"><div class="sqs-block-content"><div class="form-wrapper">' + ''.join(f'<label style="display:block;margin:14px 0 6px">{l}</label><input style="width:100%;box-sizing:border-box;background:#1b1a19;border:1.5px solid #5a544e;color:#fff">' for l in ['Name (required)','Email (required)','Phone (required)','City (required)','Fence type','Project details']) + '<button type="submit" style="margin-top:20px">Get My Free Estimate</button></div></div></div>'
open('squarespace/preview.html', 'w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0"><div class="page-section"><div class="fluid-engine">' + fe(open('squarespace/block-a.html').read()) + fe('<div class="sqs-block-map" style="background:#cfd8dc;display:grid;place-items:center">[Squarespace map block]</div>') + fe(open('squarespace/block-a2.html').read()) + fe(fake_form) + fe(open('squarespace/block-b.html').read()) + '</div></div></body></html>')
print('A', len(open('squarespace/block-a.html').read()), 'B', len(b))
