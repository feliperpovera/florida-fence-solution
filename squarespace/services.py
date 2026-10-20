# Service landing pages (one per Google Ads ad group). Run via cities.py, which defines css, img, HEAD, foot, C, SVC_NAV.
CAT = B + 'img/catalog/'
S = [
 dict(slug='vinyl-pvc-fence-installation', ag='Vinyl & PVC Fence', hero='pvc', tag='PVC vinyl',
      title='Vinyl & PVC Fence Installation in Broward County | Florida Fence Solution',
      desc='PVC vinyl privacy fence installation in Broward County, FL. White or tan, horizontal, louvered and shadowbox. Permits & HOA handled. Free estimate: (754) 208-9268.',
      h1='Vinyl &amp; PVC fence installation <em>in Broward County.</em>',
      sub='Privacy without painting. We measure, pull the permit and install white or tan PVC vinyl fences with our own crew.',
      h2='PVC vinyl fences built for South Florida',
      body=['PVC vinyl is the most requested privacy fence in Broward County. It does not rot, peel or need paint, and a garden hose is all it takes to keep it clean. That makes it the go-to choice for HOA communities in Pembroke Pines, Miramar, Weston and Coral Springs.',
            'We install standard privacy, horizontal, louvered and shadowbox styles in white or tan, with matching single and double gates. Posts are set in concrete and reinforced where gates hang, so the fence stays straight through hurricane season.'],
      styles=['Standard privacy', 'Horizontal PVC', 'Louvered PVC', 'Shadowbox PVC', 'White or tan', 'Single &amp; double gates'],
      gal=[('pvc/pvc-standard-privacy-pvc-04', 'Standard privacy PVC'), ('pvc/pvc-horizontal-pvc-with-gates-03', 'Horizontal PVC with gates'), ('pvc/pvc-louvered-pvc-tan-02', 'Tan louvered PVC'), ('pvc/pvc-shadowbox-pvc-05', 'Shadowbox PVC'), ('pvc/pvc-tan-pvc-double-gate-01', 'Tan PVC double gate'), ('pvc/pvc-louvered-pvc-07', 'Louvered PVC')],
      cost=['Linear feet and height (4, 5 or 6 ft)', 'Style: standard, horizontal, louvered or shadowbox', 'Number and size of gates', 'Removal of an old fence, if any'],
      faq=[('How long does a PVC vinyl fence last in Florida?', 'A quality PVC fence lasts 20+ years in South Florida. It does not rot or rust and only needs an occasional rinse.'),
           ('Does vinyl fence turn yellow in the sun?', 'We install UV-stabilized panels made for Florida sun, so white PVC stays white.'),
           ('Will my HOA approve a PVC fence?', 'Most Broward HOAs approve white or tan PVC. We give you the specs and drawings for the application.'),
           ('How long does installation take?', 'Most residential PVC fences are installed in 1 to 3 days once the permit is approved.')]),
 dict(slug='aluminum-pool-fence-installation', ag='Aluminum & Pool Fence', hero='alu', tag='Aluminum',
      title='Aluminum, Durafence & Pool Fence Installation in Broward | Florida Fence Solution',
      desc='Aluminum, Durafence and pool fence installation in Broward County, FL. Rust-proof, hurricane-ready, built to Florida pool code. Free estimate: (754) 208-9268.',
      h1='Aluminum, Durafence &amp; pool fences <em>that never rust.</em>',
      sub='Rust-proof fencing for salt air and hurricane season. Pool barriers built to Florida code, with self-closing gates.',
      h2='Aluminum and Durafence for coastal Broward',
      body=['Aluminum is the smart choice near the water. It does not rust, never needs paint and stands up to salt air from Hollywood to Fort Lauderdale. We install 4 ft. picket aluminum in black or white, horizontal slat aluminum and custom metal gates.',
            'Durafence is an aluminum privacy fence with the look of PVC or wood and the strength of metal. We install standard, horizontal and shadowbox Durafence, one of the most popular modern styles in Weston and on waterfront homes.',
            'For pools, we build barriers that meet the Florida Residential Pool Safety Act: the right height, no climbable gaps and self-closing, self-latching gates that open away from the pool.'],
      styles=['Durafence', 'Horizontal Durafence', 'Shadowbox Durafence', 'Horizontal slat aluminum', '4 ft. pool fence', 'Custom metal gates'],
      gal=[('aluminum/aluminum-horizontal-durafence-04', 'Horizontal Durafence'), ('aluminum/aluminum-white-durafence-01', 'White Durafence'), ('aluminum/aluminum-4-ft-aluminum-black-13', '4 ft. black aluminum'), ('aluminum/aluminum-4-ft-aluminum-lakefront-15', 'Lakefront aluminum'), ('aluminum/aluminum-horizontal-slat-gate-11', 'Horizontal slat gate'), ('aluminum/aluminum-custom-metal-double-gate-06', 'Custom metal double gate')],
      cost=['Linear feet and height', 'Picket aluminum vs. Durafence privacy panels', 'Pool gates and self-closing hardware', 'Color: black, white or bronze'],
      faq=[('What is Durafence?', 'Durafence is an aluminum privacy fence system. It looks like a solid privacy fence but is metal, so it won\'t rot, warp or rust and handles high winds.'),
           ('What does a pool fence need in Florida?', 'A barrier at least 4 ft. tall with no climbable openings and self-closing, self-latching gates. We build to the Florida pool safety code and pass inspection.'),
           ('Is aluminum good near the beach?', 'Yes. Powder-coated aluminum does not rust, which makes it the best option for coastal and canal homes.'),
           ('Do you install aluminum gates?', 'Yes. Walk gates, double driveway gates and custom metal gates.')]),
 dict(slug='wood-fence-installation', ag='Wood & Chain Link Fence', hero='wood', tag='Wood',
      title='Wood Fence Installation in Broward County | Florida Fence Solution',
      desc='Wood fence installation in Broward County, FL: horizontal, shadowbox, board-on-board, ranch style. Pressure-treated pine. Free estimate: (754) 208-9268.',
      h1='Wood fence installation <em>built on site by our crew.</em>',
      sub='Warm, natural pine fences: horizontal, shadowbox, board-on-board and ranch style. Measured, permitted and installed in Broward.',
      h2='Wood fences that hold up in Florida',
      body=['Wood is still the most affordable way to get a full privacy fence. We build with pressure-treated pine rated for ground contact, set every post in concrete and use galvanized or stainless fasteners so the fence does not bleed rust.',
            'Popular styles in Broward include modern horizontal wood, shadowbox (good-neighbor on both sides), board-on-board for full privacy and ranch style for large lots in Davie and Plantation Acres.'],
      styles=['Horizontal wood', 'Shadowbox', 'Board-on-board', 'Notch picket', 'Ranch style', 'Capped &amp; custom'],
      gal=[('wood/wood-horizontal-wood-01', 'Horizontal wood'), ('wood/wood-shadowbox-with-gate-03', 'Shadowbox with gate'), ('wood/wood-board-on-board-04', 'Board-on-board'), ('wood/wood-ranch-style-05', 'Ranch style'), ('wood/wood-custom-capped-wood-06', 'Custom capped wood'), ('wood/wood-board-on-board-with-gate-02', 'Board-on-board with gate')],
      cost=['Linear feet and height', 'Style: horizontal, shadowbox, board-on-board or ranch', 'Gates and hardware', 'Stain or sealer, if wanted'],
      faq=[('How long does a wood fence last in South Florida?', 'Pressure-treated pine lasts 10 to 15 years here with sealing every couple of years. Posts set in concrete last the longest.'),
           ('Is wood cheaper than PVC?', 'Yes, wood usually costs less up front. PVC costs more but needs almost no maintenance.'),
           ('Do you stain or seal wood fences?', 'Yes, we can seal or stain the fence after installation to protect it from sun and rain.'),
           ('Do you build horizontal wood fences?', 'Yes. Horizontal wood is one of our most requested modern styles.')]),
 dict(slug='chain-link-fence-installation', ag='Wood & Chain Link Fence', hero='chain', tag='Chain-link',
      title='Chain Link Fence Installation in Broward County | Florida Fence Solution',
      desc='Black and galvanized chain-link fence installation in Broward County, FL, with privacy slats. Residential & commercial. Free estimate: (754) 208-9268.',
      h1='Chain-link fence installation <em>for homes and businesses.</em>',
      sub='Black vinyl-coated or galvanized chain-link, with optional privacy slats. Fast, secure and budget-friendly.',
      h2='Secure, affordable chain-link fencing',
      body=['Chain-link is the most cost-effective way to secure a yard, a pool equipment area or a commercial lot. Black vinyl-coated chain-link blends into landscaping and resists corrosion better than plain galvanized.',
            'We install residential and commercial chain-link with walk gates, double drive gates and privacy slats when you want to block the view. We also replace old, rusted chain-link fences across Miramar, Miami Gardens and Hollywood.'],
      styles=['Black vinyl-coated', 'Galvanized', 'Privacy slats', 'Walk &amp; drive gates', 'Commercial lots', 'Old fence replacement'],
      gal=[('chain-link/chain-link-black-chain-link-02', 'Black chain-link'), ('chain-link/chain-link-black-chain-link-with-privacy-slats-01', 'Black chain-link with privacy slats'), ('chain-link/chain-link-black-chain-link-with-privacy-slats-03', 'Privacy slats'), ('chain-link/chain-link-galvanized-chain-link-04', 'Galvanized chain-link')],
      cost=['Linear feet and height', 'Black coated vs. galvanized', 'Privacy slats', 'Gates and removal of the old fence'],
      faq=[('Black or galvanized chain-link?', 'Black vinyl-coated looks better and resists rust longer. Galvanized is the most economical.'),
           ('Can you add privacy to chain-link?', 'Yes. We add privacy slats in several colors to new or existing chain-link.'),
           ('Do you install commercial chain-link?', 'Yes. We fence lots, warehouses and businesses, with drive gates and security options.'),
           ('Can you replace my old chain-link fence?', 'Yes. We remove and haul away the old fence and install the new one.')]),
 dict(slug='fence-repair', ag='Fence Repair', hero='alley', tag='Repair',
      title='Fence Repair in Broward County | Florida Fence Solution',
      desc='Fence repair in Broward County, FL: storm damage, leaning posts, broken panels and gates for wood, PVC, aluminum and chain-link. Call (754) 208-9268.',
      h1='Fence repair <em>after storms, wear or accidents.</em>',
      sub='Leaning posts, broken panels, sagging gates and storm damage. We repair wood, PVC, aluminum and chain-link fences.',
      h2='Fix it right instead of replacing it all',
      body=['Most damaged fences don\'t need a full replacement. After a storm or years of sun and rain, the usual problems are a few broken panels, rotten or leaning posts and gates that no longer close. We replace only what is needed and match the existing material.',
            'We repair wood, PVC vinyl, aluminum, Durafence and chain-link fences, reset posts in concrete and rehang or replace gates and hardware. If a repair won\'t last, we tell you and quote a replacement instead.'],
      styles=['Storm damage', 'Leaning or rotten posts', 'Broken panels &amp; pickets', 'Sagging gates', 'Gate hardware &amp; latches', 'Pool gate repairs'],
      gal=[('wood/wood-shadowbox-with-gate-03', 'Wood gate rebuilt'), ('pvc/pvc-standard-pvc-gate-06', 'PVC gate'), ('aluminum/aluminum-durafence-with-gate-03', 'Durafence with gate'), ('chain-link/chain-link-black-chain-link-02', 'Chain-link')],
      cost=['Number of posts and panels to replace', 'Material: wood, PVC, aluminum or chain-link', 'Gate repair or replacement', 'Matching discontinued styles'],
      faq=[('Do you repair fences you didn\'t install?', 'Yes. We repair any wood, PVC, aluminum or chain-link fence.'),
           ('Can you fix a leaning fence?', 'Yes. We reset or replace the posts in concrete so the fence stands straight again.'),
           ('Do you repair storm damage?', 'Yes. After hurricanes and storms we repair panels, posts and gates and can document the damage for your insurance.'),
           ('Repair or replace: how do I know?', 'If most posts are rotten or the fence is past its life, replacing is cheaper long term. We tell you honestly after seeing it.')]),
]

def spage(s):
    wa = "https://wa.me/17542089268?text=" + ("Hi! I'd like a free estimate for " + s['tag'].lower() + " fence work.").replace(' ', '%20')
    gal = ''.join(f'<figure class="slide"><a href="{CAT}{f}.webp" target="_blank" rel="noopener"><img src="{CAT}{f}-sm.webp" alt="{cap} by Florida Fence Solution in Broward County" loading="lazy" width="640" height="480"></a><figcaption>{cap}</figcaption></figure>' for f, cap in s['gal'])
    chips = ''.join(f'<li>{x}</li>' for x in s['styles'])
    faqs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in s['faq'] + [
        ('Are you licensed and insured?', 'Yes. Florida Fence Solution is licensed and insured, family-owned and based in Hollywood, FL.')])
    others = ''.join(f'<a href="/{u}">{t}</a>' for u, t in SVC_NAV if u != s['slug'])
    cities = ''.join(f'<a href="/fence-company-{c["slug"]}-fl">{c["name"]}</a>' for c in C)
    body = ''.join(f'<p>{p}</p>' for p in s['body'])
    cost = ''.join(f'<li>{x}</li>' for x in s['cost'])
    return f'''<div class="ffs">
{HEAD}
<section class="hero city-hero">{img(s['hero'], eager=True).replace('alt=""', f'alt="{s["tag"]} fence installed by Florida Fence Solution in Broward County"')}
<div class="wrap"><div class="hero-copy">
<span class="kicker">{s['tag']} fences &#183; Broward County, FL</span>
<h1>{s['h1']}</h1>
<p class="sub">{s['sub']}</p>
<div class="ctas"><a class="btn btn-accent" href="/#estimate">Get a free estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-glass" href="tel:+17542089268">Call (754) 208-9268</a></div>
<a class="rating" href="/#reviews"><b>5.0</b><span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>17 Google reviews</span></a>
</div></div></section>

<section id="fences"><div class="wrap">
<div class="head"><div><span class="kicker">{s['tag']}</span><h2>{s['h2']}</h2></div>
<div class="prose">{body}</div></div>
<ul class="chips" style="margin:8px 0 28px">{chips}</ul>
<div class="cat-grid">{gal}</div>
</div></section>

<section class="why dark"><div class="wrap">
<div class="why-img">{img('crew','', '(max-width:1024px) 100vw, 45vw').replace('alt=""', 'alt="Florida Fence Solution crew"')}</div>
<div class="prose"><span class="kicker">Pricing</span><h2>What affects the price</h2>
<ul class="price">{cost}</ul>
<p>Every estimate is free and in writing, after we measure on site. No surprises: permit, materials, labor and cleanup are included in the quote.</p>
<ol class="reasons"><li><span class="n" aria-hidden="true">1</span><div><h3>Licensed and insured</h3><p>Family-owned, based in Hollywood, FL.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><h3>Permits and HOA, handled</h3><p>We file with your city and build to Florida code.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><h3>Our own crew</h3><p>No random subs. We clean up before we leave.</p></div></li></ol>
</div></div></section>

<section id="faq" class="dark" style="padding-top:0"><div class="wrap faq-grid">
<div><span class="kicker">FAQ</span><h2>{s['tag']} fence questions</h2></div>
<div class="faq">{faqs}</div></div></section>

<section class="estimate"><div class="wrap">
<div><span class="kicker">Free estimate</span><h2>Get your {s['tag'].lower()} fence quote</h2><p class="lead">Takes a minute. We answer the same day. Hablamos espa&#241;ol.</p>
<div class="ctas" style="margin-top:24px"><a class="btn btn-accent" href="/#estimate">Request an estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-dark" href="tel:+17542089268">Call (754) 208-9268</a><a class="btn btn-dark" href="{wa}" target="_blank" rel="noopener">WhatsApp</a></div></div>
<div class="near"><span class="kicker">More services</span><h3 style="margin-bottom:12px">We also install</h3>{others}<h3 style="margin:20px 0 12px">Areas we serve</h3>{cities}</div>
</div></section>

{foot(wa)}
</div>'''

os.makedirs('services', exist_ok=True)
smeta = []
for s in S:
    html = (css + '\n' + spage(s)).encode('ascii', 'xmlcharrefreplace').decode()
    assert html.count('<div') == html.count('</div'), s['slug']
    open(f'services/{s["slug"]}.html', 'w').write(html)
    smeta.append(dict(slug=s['slug'], ad_group=s['ag'], title=s['title'], desc=s['desc']))
json.dump(smeta, open('services/meta.json', 'w'), indent=1)
open('services/preview.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+open('services/aluminum-pool-fence-installation.html').read()+'</body></html>')
print([len(open(f'services/{s["slug"]}.html').read()) for s in S])
