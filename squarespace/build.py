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
.fe-block:has(.sqs-block-form){order:2}
.fe-block:has(.ffs .ffs-foot){order:3}
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
/* catalog: CSS tabs via :target (no JS) */
.ffs .catalog-sec{background:var(--light-2)}
.ffs .catalog-sec .tabs a{text-decoration:none}
.ffs .catalog-sec .panel{display:none}
.ffs .catalog-sec .panel:target{display:block}
.ffs .catalog-sec:not(:has(.panel:target)) #catalog-aluminum{display:block}
.ffs .catalog-sec:not(:has(.panel:target)) .tabs a[href="#catalog-aluminum"],
.ffs .catalog-sec:has(#catalog-aluminum:target) .tabs a[href="#catalog-aluminum"],
.ffs .catalog-sec:has(#catalog-wood:target) .tabs a[href="#catalog-wood"],
.ffs .catalog-sec:has(#catalog-pvc:target) .tabs a[href="#catalog-pvc"],
.ffs .catalog-sec:has(#catalog-chain-link:target) .tabs a[href="#catalog-chain-link"]{background:var(--dark);color:#fff;border-color:var(--dark)}
.ffs .catalog-sec .panel-head{margin:28px 0 20px}
.ffs .cat-grid .slide a{display:block;border-radius:var(--r);overflow:hidden;aspect-ratio:4/3;cursor:zoom-in}
.ffs .cat-grid .slide a img{width:100%;height:100%;object-fit:cover;transition:transform .7s var(--ease)}
.ffs .cat-grid .slide a:hover img{transform:scale(1.06)}
@media (max-width:767px){.ffs .cat-grid{grid-template-columns:1fr 1fr;gap:10px}.ffs .catalog-sec .tabs{flex-wrap:nowrap;overflow-x:auto}}
/* map: card only (Basic plan blocks iframes) */
.ffs .map-block{min-height:0;background:var(--dark);padding:clamp(24px,4vw,48px);display:flex;justify-content:space-between;align-items:center;gap:24px;flex-wrap:wrap}
.ffs .map-card{position:static;max-width:none;background:none;box-shadow:none;padding:0;color:#fff}
.ffs .map-card h3{color:#fff!important}
.ffs .map-card p{color:var(--muted-dark)}
/* estimate: info on top, native form block below */
.ffs .estimate{padding-bottom:40px}
.ffs .estimate .wrap{grid-template-columns:1fr;max-width:900px}
.ffs .estimate .contact-list{grid-template-columns:1fr 1fr}
@media (max-width:767px){.ffs .estimate .contact-list{grid-template-columns:1fr}}
/* native Squarespace form styled as the dark quote card */
.fe-block:has(.sqs-block-form){box-sizing:border-box!important;width:min(820px,calc(100% - 32px))!important;margin:0 auto 96px!important;background:#fff;border:1px solid #e6e1d9;border-top:6px solid #f0ad3d;border-radius:24px;padding:clamp(24px,3vw,40px)!important;box-shadow:0 30px 60px -30px rgba(17,17,17,.35)}
.fe-block:has(.sqs-block-form) .sqs-block-form{padding:0!important}
.fe-block:has(.sqs-block-form) *{font-family:'Plus Jakarta Sans',system-ui,sans-serif}
.fe-block:has(.sqs-block-form) .sqs-block-content::before{content:"Request your estimate";display:block;font-weight:800;font-size:clamp(1.5rem,1.3rem + .8vw,2rem);letter-spacing:-.02em;line-height:1.2;color:#111;margin-bottom:4px}
.fe-block:has(.sqs-block-form) label,.fe-block:has(.sqs-block-form) legend,.fe-block:has(.sqs-block-form) .title,.fe-block:has(.sqs-block-form) .description,.fe-block:has(.sqs-block-form) span{color:#111!important}
.fe-block:has(.sqs-block-form) input,.fe-block:has(.sqs-block-form) select,.fe-block:has(.sqs-block-form) textarea{color:#111!important;border:1.5px solid #5a544e!important;border-radius:12px!important;min-height:52px}
.fe-block:has(.sqs-block-form) input:focus,.fe-block:has(.sqs-block-form) select:focus,.fe-block:has(.sqs-block-form) textarea:focus{border-color:#f0ad3d!important;box-shadow:0 0 0 3px rgba(240,173,61,.3)!important}
.fe-block:has(.sqs-block-form) button[type=submit],.fe-block:has(.sqs-block-form) input[type=submit]{width:100%!important;background:#f0ad3d!important;color:#111!important;border:0!important;border-radius:999px!important;min-height:52px;font-weight:700!important;font-size:1rem!important}
.fe-block:has(.sqs-block-form) .sqs-block-content::after{content:"No spam. No obligation.";display:block;text-align:center;color:#57524c;font-size:.85rem;margin-top:10px}
'''
css = '@import url(\'https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap\');\n' + extra + css
css = re.sub(r'[^\x00-\x7f]', lambda m: '\\%x ' % ord(m.group(0)), css)

# ---------- HTML ----------
h = body
h = re.sub(r'<script>.*?</script>', '', h, flags=re.S)
h = re.sub(r'<a class="btn btn-accent" href="#top" style="position:absolute;left:-9999px.*?</a>', '', h, flags=re.S)
h = re.sub(r'<span class="lang".*?</span>\s*', '', h, flags=re.S)
h = h.replace('<header class="site-header" id="header">', '<header class="site-header">')
h = h.replace('<main id="top">', '<div id="top">').replace('</main>', '</div>')
h = h.replace('<footer>', '<div class="ffs-foot">').replace('</footer>', '</div>')
h = re.sub(r'<dialog class="lightbox".*?</dialog>', '', h, flags=re.S)
# catalog dialog -> inline section with :target tabs
h = re.sub(r'<dialog class="catalog-modal" id="catalog" aria-labelledby="cm-title">\s*<div class="cm-head">\s*<div>(.*?)</div>.*?</div>',
           r'<section class="catalog-sec" id="catalog"><div class="wrap"><div class="head"><div>\1<p class="lead">Real jobs by our crew. Pick a fence type and tap any photo to see it big.</p></div></div>', h, count=1, flags=re.S)
h = h.replace('</dialog>', '</div></section>')
h = re.sub(r'<button type="button" role="tab" id="tab-([\w-]+)"[^>]*>(.*?)</button>', r'<a href="#catalog-\1">\2</a>', h)
h = h.replace(' role="tablist"', '').replace(' hidden>', '>')
h = re.sub(r'<button type="button"><img ([^>]*?)data-full="([^"]+)"([^>]*)></button>', r'<a href="\2" target="_blank" rel="noopener"><img \1\3></a>', h)
# map iframe -> card only
h = re.sub(r'<iframe title="Map:.*?</iframe>\s*', '', h, flags=re.S)
# remove JS form (native Squarespace form replaces it)
h = re.sub(r'\s*<!-- TODO: to receive leads.*?-->', '', h, flags=re.S)
h = re.sub(r'<form class="quote.*?</form>', '', h, flags=re.S)
h = re.sub(r'<!--.*?-->', '', h, flags=re.S)
h = re.sub(r' data-ev="[^"]*"', '', h)
h = re.sub(r'(src|href|srcset)="(?!https?:|tel:|mailto:|#)([^"]+)"', lambda m: f'{m.group(1)}="' + ', '.join((B + u.strip()) for u in m.group(2).split(', ')) + '"' if m.group(1) == 'srcset' else f'{m.group(1)}="{B}{m.group(2)}"', h)
h = h.encode('ascii', 'xmlcharrefreplace').decode()
h = re.sub(r'\n\s*\n+', '\n', h)

cut = h.index('<div class="ffs-foot">')
a, b = h[:cut], h[cut:]
assert a.count('<div') - a.count('</div') == 0, (a.count('<div'), a.count('</div'))
open('squarespace/block-a.html', 'w').write(f'<style>\n{css}\n</style>\n<div class="ffs">{a}</div>\n')
open('squarespace/block-b.html', 'w').write(f'<div class="ffs">{b}</div>\n')
open('squarespace/preview.html', 'w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">' + open('squarespace/block-a.html').read() + '<div style="max-width:820px;margin:0 auto 96px;background:#111;color:#fff;border-radius:24px;padding:40px">[Squarespace form block here]</div>' + open('squarespace/block-b.html').read() + '</body></html>')
print('A', len(open('squarespace/block-a.html').read()), 'B', len(b))
