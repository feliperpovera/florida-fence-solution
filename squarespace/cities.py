# City landing pages for Squarespace (one code block per page). Reuses the scoped CSS from block-a.html.
import re, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
B = 'https://feliperpovera.github.io/florida-fence-solution/'
css = open('block-a.html').read()
css = css[:css.index('</style>') + 8]
# city pages have no Squarespace form/map blocks; keep code blocks full width
css = css.replace('</style>', '.fe-block:has(.ffs){order:0!important}\n.ffs .city-hero{min-height:72svh}\n.ffs .near a{display:inline-block;margin:4px 6px 4px 0;padding:8px 14px;border-radius:999px;background:var(--light-2);font-weight:600;font-size:.92rem;text-decoration:none}\n.ffs .near a:hover{background:var(--accent)}\n.ffs .prose p{color:var(--muted);margin-bottom:14px;max-width:70ch}\n.ffs .price li{margin:0 0 8px 18px;color:var(--muted)}\n</style>')

IMG = {
 'pvc': 'img/white-pvc-privacy-fence-backyard-pool', 'wood': 'img/horizontal-pine-wood-fence',
 'alley': 'img/horizontal-louvered-pvc-fence-alley', 'chain': 'img/black-chain-link-fence-garden',
 'louver': 'img/louvered-pvc-privacy-panels', 'crew': 'img/florida-fence-solution-crew', 'alu': 'img/aluminum-horizontal-durafence'}

C = [
 dict(slug='hollywood', name='Hollywood', hero='alley', hoods='Hollywood Lakes, Emerald Hills, Driftwood, Hollywood Hills and the neighborhoods west of I-95',
      angle='Hollywood is our home base. Our shop is on N 70th Way, so most Hollywood estimates happen the same week you call.',
      local='Near the beach, salt air eats through untreated steel and cheap hardware fast. East of US-1 we usually recommend aluminum or PVC with stainless fasteners; west of I-95, wood and shadowbox privacy fences are just as popular.',
      faq=[('Do I need a permit for a fence in Hollywood, FL?','Yes. Most new fences in Hollywood need a permit from the city\'s building department. We prepare the drawings, file the permit and schedule the final inspection for you.'),
           ('How fast can you start in Hollywood?','Hollywood is our home base, so estimates are usually within a few days. Install starts once the permit is approved.')]),
 dict(slug='fort-lauderdale', name='Fort Lauderdale', hero='louver', hoods='Victoria Park, Coral Ridge, Rio Vista, Tarpon River, Imperial Point and Riverland',
      angle='From waterfront homes on the canals to commercial lots off Broward Blvd, we build fences that pass inspection and handle coastal weather.',
      local='Many Fort Lauderdale homes sit on canals and close to the ocean, so we favor aluminum, Durafence and PVC that won\'t rust, and we set posts deeper in sandy soil.',
      faq=[('What fence holds up best near the water in Fort Lauderdale?','Aluminum and Durafence don\'t rust and handle salt air. PVC vinyl is also a good low-maintenance option for privacy.'),
           ('Do you install pool fences in Fort Lauderdale?','Yes. We install pool safety fences and self-closing gates built to Florida pool barrier requirements.')]),
 dict(slug='pembroke-pines', name='Pembroke Pines', hero='pvc', hoods='Chapel Trail, Silver Lakes, Pembroke Falls, Pembroke Lakes and Towngate',
      angle='Pembroke Pines has a lot of HOA communities. We work with your HOA guidelines from the start so your fence gets approved the first time.',
      local='Most Pembroke Pines HOAs specify fence height, color and style. White PVC privacy fences and aluminum are the most common approved options here.',
      faq=[('Can you help with HOA approval in Pembroke Pines?','Yes. We give you the specs, drawings and material samples your HOA asks for, and we build exactly to the approved design.'),
           ('What is the most popular fence in Pembroke Pines?','White PVC privacy fence, followed by aluminum around pools.')]),
 dict(slug='miramar', name='Miramar', hero='pvc', hoods='Silver Shores, Monarch Lakes, Sunset Lakes, Riviera Isles and Historic Miramar',
      angle='Miramar is minutes from our Hollywood shop. We install privacy, pool and security fences for homes and businesses across the city.',
      local='Newer Miramar communities usually have HOA rules on fence style and color; older neighborhoods east of University Dr often need chain-link or wood replacements.',
      faq=[('Do you replace old chain-link fences in Miramar?','Yes. We remove the old fence and install new chain-link, wood, PVC or aluminum, depending on what you need.'),
           ('Do you handle the Miramar permit?','Yes. We file the permit and schedule the inspection.')]),
 dict(slug='davie', name='Davie', hero='wood', hoods='Long Lake Ranches, Shenandoah, Pine Island Ridge, Ivanhoe and the ranch properties west of Flamingo Rd',
      angle='Davie has larger lots and horse properties. We build long runs of ranch-style fence, wood privacy fences and gates for driveways and paddocks.',
      local='For bigger Davie lots we often combine ranch-style or aluminum fencing along the front with wood or PVC privacy in the back.',
      faq=[('Do you install ranch-style fences in Davie?','Yes. We build ranch-style and post-and-rail fences, plus driveway and paddock gates.'),
           ('Can you fence a large property?','Yes. We quote long runs by the linear foot and plan gate locations with you on site.')]),
 dict(slug='weston', name='Weston', hero='louver', hoods='Weston Hills, Savanna, Bonaventure, The Ridges, Windmill Ranch and Isles of Weston',
      angle='Weston communities have strict HOA standards. We install clean, high-end fences such as horizontal aluminum, Durafence and PVC that fit the look of the neighborhood.',
      local='Weston buyers usually want low-maintenance, modern styles. Horizontal Durafence and aluminum pool fences are our most requested jobs here.',
      faq=[('Do Weston HOAs allow horizontal fences?','It depends on the community. We check your HOA guidelines and submit the design for approval before installing.'),
           ('What does a pool fence in Weston need?','A pool barrier with self-closing, self-latching gates. We build to Florida pool safety requirements.')]),
 dict(slug='coral-springs', name='Coral Springs', hero='chain', hoods='Eagle Trace, Ramblewood, Turtle Run, Cypress Run, The Isles and Maplewood',
      angle='We install privacy, pool and security fences across Coral Springs, built to code and to your community\'s rules.',
      local='Coral Springs has many families with pets and pools, so privacy fences with dig-proof bottoms and pool-safe gates are common requests.',
      faq=[('Can you build a pet-friendly fence in Coral Springs?','Yes. We set panels close to the ground and can add gates that latch securely for dogs.'),
           ('Do you install aluminum pool fences in Coral Springs?','Yes, in black or white, with self-closing gates.')]),
 dict(slug='plantation', name='Plantation', hero='wood', hoods='Plantation Acres, Jacaranda, Central Park, Plantation Isles and Park East',
      angle='From the large lots of Plantation Acres to gated communities near Central Park, we build fences that fit the property and the neighborhood.',
      local='Plantation Acres properties often need long fence runs and wide driveway gates; inside the gated communities, PVC and aluminum are the norm.',
      faq=[('Do you install driveway gates in Plantation?','Yes. We build single and double driveway gates in wood, aluminum and PVC.'),
           ('Do you work in Plantation Acres?','Yes. We regularly fence large lots in Plantation Acres.')]),
 dict(slug='miami-gardens', name='Miami Gardens', hero='chain', hoods='Andover, Norwood, Carol City, Rolling Oaks and Lake Lucerne',
      angle='Just south of the Broward line, Miami Gardens is close to our Hollywood shop. We install security, privacy and chain-link fences for homes and businesses.',
      local='Security is the top request in Miami Gardens: black chain-link, aluminum and solid privacy fences with lockable gates.',
      faq=[('Do you serve Miami Gardens even though it is in Miami-Dade?','Yes. Miami Gardens is close to our Hollywood shop and we serve it regularly.'),
           ('Do you install commercial fences in Miami Gardens?','Yes. We install chain-link and security fences for businesses and lots.')]),
]

def img(key, cls='', sizes='100vw', eager=False):
    base = IMG[key]
    big = {'crew': 900, 'louver': 674}.get(key, 1200)
    mid = '' if key in ('louver', 'crew') else f', {B}{base}-800.webp 800w'
    return f'<img src="{B}{base}-480.webp" srcset="{B}{base}-480.webp 480w{mid}, {B}{base}.webp {big}w" sizes="{sizes}" alt="" {"fetchpriority=\"high\"" if eager else "loading=\"lazy\""} width="1200" height="900">'

HCALL = '<a class="btn btn-glass h-call" href="tel:+17542089268"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.6a1 1 0 0 1-.25 1z"/></svg><span class="long">(754) 208-9268</span><span class="short">Call</span></a>'

HEAD = f'''<header class="site-header"><div class="wrap"><a class="logo" href="/" aria-label="Florida Fence Solution, home"><img src="{B}img/logo.png" alt="Florida Fence Solution" width="69" height="44"></a>
<nav aria-label="Main"><ul><li><a href="/residential-fence-solutions">Fences</a></li><li><a href="/fence-company-reviews">Reviews</a></li><li><a href="/fence-installation-process">Process</a></li><li><a href="/service-areas">Areas</a></li><li><a href="/fence-faq">FAQ</a></li><li><a href="/blog">Blog</a></li></ul></nav>
<div class="h-right">{HCALL}<a class="btn btn-accent" href="/#estimate">Free estimate</a></div></div></header>'''

SVC_NAV = [('vinyl-pvc-fence-installation', 'Vinyl &amp; PVC fences'), ('aluminum-pool-fence-installation', 'Aluminum &amp; pool fences'),
 ('wood-fence-installation', 'Wood fences'), ('chain-link-fence-installation', 'Chain-link fences'), ('fence-repair', 'Fence repair')]
SVC_LINKS = ''.join(f'<a href="/{u}">{t}</a>' for u, t in SVC_NAV)

def foot(wa):
    return f'''<div class="ffs-foot"><div class="wrap">
<div><a class="logo" href="/" aria-label="Back to home"><img src="{B}img/logo.png" alt="Florida Fence Solution" width="69" height="44" loading="lazy"></a><p>Family-owned fence contractor in Broward County, FL.<br>1331 N 70th Way, Hollywood, FL 33024. Hablamos espa&#241;ol.</p></div>
<div><h4>Contact</h4><a href="tel:+17542089268">(754) 208-9268</a><a href="https://wa.me/17542089268" target="_blank" rel="noopener">WhatsApp</a><a href="mailto:floresfloridafencing@gmail.com">Email</a></div>
<div><h4>Services</h4>{SVC_LINKS}</div>
<div><h4>Hours</h4><p>Mon&#8211;Sat<br>8 AM&#8211;6 PM</p></div>
<div class="copy">&#169; 2026 Florida Fence Solution LLC</div></div></div>
<a class="wa-float" href="{wa}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><svg width="30" height="30" viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3C8.8 3 3 8.7 3 15.8c0 2.3.6 4.5 1.8 6.5L3 29l6.9-1.8c1.9 1 4 1.6 6.1 1.6 7.2 0 13-5.7 13-12.8S23.2 3 16 3z"/></svg></a>
<nav class="mobile-bar" aria-label="Quick contact"><a href="tel:+17542089268">Call</a><a href="{wa}" target="_blank" rel="noopener">WhatsApp</a></nav>'''

def page(c):
    n = c['name']
    others = [x for x in C if x is not c]
    near = ''.join(f'<a href="/fence-company-{x["slug"]}-fl">Fence company in {x["name"]}</a>' for x in others)
    faqs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in c['faq'] + [
        ('Are you licensed and insured?', 'Yes. Florida Fence Solution is licensed and insured, family-owned and based in Hollywood, FL.'),
        ('How much does a fence cost in ' + n + '?', 'It depends on material, height and length. We give you a free written estimate after measuring on site.')])
    wa = "https://wa.me/17542089268?text=" + ("Hi! I'd like a free fence estimate in " + n + ".").replace(' ', '%20')
    alt = f'Fence installed by Florida Fence Solution in {n}, FL'
    return f'''<div class="ffs">
{HEAD}
<section class="hero city-hero">{img(c['hero'], eager=True).replace('alt=""', f'alt="{alt}"')}
<div class="wrap"><div class="hero-copy">
<span class="kicker">Fence contractor &#183; {n}, FL</span>
<h1>Fence company in {n}, FL <em>built for Florida weather.</em></h1>
<p class="sub">{c['angle']}</p>
<div class="ctas"><a class="btn btn-accent" href="/#estimate">Get a free estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-glass" href="tel:+17542089268">Call (754) 208-9268</a></div>
<a class="rating" href="/#reviews"><b>5.0</b><span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>17 Google reviews</span></a>
</div></div></section>

<section id="fences"><div class="wrap">
<div class="head"><div><span class="kicker">Fences in {n}</span><h2>What we install in {n}</h2></div>
<p class="lead">Every job is measured, permitted and built by our own crew. Serving {c['hoods']}.</p></div>
<div class="bento" data-carousel>
<article class="card photo b-big">{img('pvc','', '(max-width:767px) 84vw, 600px').replace('alt=""', f'alt="White PVC privacy fence in {n}, FL"')}<span class="tag">Vinyl</span><h3>PVC vinyl fences</h3><p>Privacy without painting. Hose it off.</p><a class="stretch" href="/#catalog-pvc"><span>See catalog &#8594;</span></a></article>
<article class="card photo b-wide">{img('wood','', '(max-width:767px) 84vw, 600px').replace('alt=""', f'alt="Horizontal wood fence in {n}, FL"')}<span class="tag">Wood</span><h3>Wood fences</h3><p>Horizontal, board-on-board, shadowbox, stockade.</p><a class="stretch" href="/#catalog-wood"><span>See catalog &#8594;</span></a></article>
<article class="card photo">{img('chain','', '(max-width:767px) 84vw, 300px').replace('alt=""', f'alt="Black chain-link fence in {n}, FL"')}<span class="tag">Coated steel</span><h3>Chain-link</h3><p>Black or galvanized security.</p><a class="stretch" href="/#catalog-chain-link"><span>See catalog &#8594;</span></a></article>
<article class="card accent"><span class="tag">Aluminum</span><h3>Aluminum &amp; Durafence</h3><p>Won't rust. Built for hurricane season.</p><a class="stretch" href="/#catalog-aluminum"><span>See catalog &#8594;</span></a></article>
</div></div></section>

<section class="why dark"><div class="wrap">
<div class="why-img">{img('crew','', '(max-width:1024px) 100vw, 45vw').replace('alt=""', 'alt="Florida Fence Solution crew"')}</div>
<div class="prose"><span class="kicker">Local know-how</span><h2>Fencing {n} properties the right way</h2>
<p>{c['local']}</p>
<p>We handle the permit with the city, follow your HOA rules and build to Florida code, including pool barrier requirements. Free on-site estimates, written quotes and a final walkthrough with you.</p>
<ol class="reasons"><li><span class="n" aria-hidden="true">1</span><div><h3>Licensed and insured</h3><p>Family-owned, based in Hollywood, FL.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><h3>Permits and HOA, handled</h3><p>We file with {n} and build to code.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><h3>Our own crew</h3><p>No random subs. We clean up before we leave.</p></div></li></ol>
</div></div></section>

<section id="faq" class="dark" style="padding-top:0"><div class="wrap faq-grid">
<div><span class="kicker">FAQ</span><h2>Fence questions in {n}</h2></div>
<div class="faq">{faqs}</div></div></section>

<section class="estimate"><div class="wrap">
<div><span class="kicker">Free estimate</span><h2>Get your {n} fence quote</h2><p class="lead">Takes a minute. We answer the same day. Hablamos espa&#241;ol.</p>
<div class="ctas" style="margin-top:24px"><a class="btn btn-accent" href="/#estimate">Request an estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-dark" href="tel:+17542089268">Call (754) 208-9268</a><a class="btn btn-dark" href="{wa}" target="_blank" rel="noopener">WhatsApp</a></div></div>
<div class="near"><span class="kicker">Nearby areas</span><h3 style="margin-bottom:12px">We also build fences in</h3>{near}<a href="/#areas">All of Broward County</a></div>
</div></section>

{foot(wa)}
</div>'''

os.makedirs('cities', exist_ok=True)
meta = []
for c in C:
    html = css + '\n' + page(c)
    html = html.encode('ascii', 'xmlcharrefreplace').decode()
    assert html.count('<div') == html.count('</div'), c['slug']
    open(f'cities/{c["slug"]}.html', 'w').write(html)
    meta.append(dict(slug=f'fence-company-{c["slug"]}-fl', title=f'Fence Company in {c["name"]}, FL | Florida Fence Solution',
        desc=f'Licensed & insured fence contractor in {c["name"]}, FL. Wood, PVC vinyl, aluminum, chain-link & Durafence. Permits & HOA handled. Free estimate: (754) 208-9268.'))
json.dump(meta, open('cities/meta.json', 'w'), indent=1)
open('cities/preview.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+open('cities/hollywood.html').read()+'</body></html>')
print([len(open(f'cities/{c["slug"]}.html').read()) for c in C])
exec(open('services.py').read())
exec(open('pages.py').read())
