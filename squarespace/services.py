# Service landing pages (one per Google Ads ad group). Run via cities.py, which defines css, img, HEAD, foot, C, SVC_NAV.
CAT = B + 'img/catalog/'
S = [
 dict(slug='vinyl-pvc-fence-installation', ag='Vinyl & PVC Fence', hero='pvc', tag='PVC vinyl', label='Vinyl',
      title='Vinyl Fence & PVC Fence Installation in Broward County, FL',
      desc='Vinyl fence and PVC fence installation in Broward County: privacy, horizontal, louvered & shadowbox, plus vinyl fence gates. Free estimate: (754) 208-9268.',
      kicker='Vinyl fencing &#183; Broward County, FL',
      h1='Vinyl fence &amp; PVC fence installation <em>in Broward County.</em>',
      sub='White or tan vinyl privacy fences and matching gates, measured, permitted and installed by our own crew.',
      h2='Vinyl fencing for Broward homes',
      body=['Vinyl fence and PVC fence are two names for the same material. A vinyl fence gives you full privacy without painting or staining: it does not rot, and a garden hose and mild soap keep it clean. That is why it is a common choice for HOA communities in Pembroke Pines, Miramar, Weston and Coral Springs.',
            '<h3>Vinyl fence styles we install</h3>',
            table(['Style', 'Privacy', 'Good for'], [
              ['Standard privacy', 'Full', 'Backyards, pools and shared property lines'],
              ['Horizontal PVC', 'Full', 'Modern homes'],
              ['Louvered PVC', 'High, lets air through', 'Windy lots and equipment areas'],
              ['Shadowbox PVC', 'High, looks the same from both sides', 'Neighbors who share the fence']]),
            'All four come in white or tan. See real jobs in the photos below.',
            '<h3>Vinyl fence gates</h3>',
            'We install single walk gates and double drive gates that match the fence. Gates carry more weight than any other part of a vinyl fence, so tell us how you will use yours (people, mowers, a boat or a car) and we will size it on site. If the gate is part of a pool barrier, it has to be self-closing and self-latching. See <a href="/pool-fence-requirements-florida">pool fence requirements in Florida</a>.',
            '<h3>How much does a vinyl fence cost?</h3>',
            'The price depends on total length, height, style, number of gates and whether an old fence has to come out first. Vinyl usually costs more than wood up front and needs far less upkeep after. We measure and give you the price in writing, free. Compare it with <a href="/wood-vs-vinyl-vs-aluminum-fence-florida">wood and aluminum</a>.',
            '<h3>Permits and HOA approval</h3>',
            'Most Broward cities require a permit for a new fence, and many HOAs limit height, color and style. We file the permit and give you the drawings and specs for your HOA. Read <a href="/fence-permit-broward-county">do you need a fence permit in Broward County?</a>'],
      styles=['Vinyl privacy fence', 'Horizontal PVC', 'Louvered PVC', 'Shadowbox PVC', 'White or tan', 'Vinyl fence gates'],
      gal=[('pvc/pvc-standard-privacy-pvc-04', 'Vinyl privacy fence'), ('pvc/pvc-horizontal-pvc-with-gates-03', 'Horizontal vinyl fence with gates'), ('pvc/pvc-louvered-pvc-tan-02', 'Tan louvered vinyl fence'), ('pvc/pvc-shadowbox-pvc-05', 'Shadowbox vinyl fence'), ('pvc/pvc-tan-pvc-double-gate-01', 'Tan vinyl double gate'), ('pvc/pvc-standard-pvc-gate-06', 'Vinyl fence gate')],
      cost=['Linear feet and height', 'Style: standard, horizontal, louvered or shadowbox', 'Number and size of gates', 'Removal of an old fence, if any'],
      faq=[('Is a vinyl fence the same as a PVC fence?', 'Yes. PVC is the plastic a vinyl fence is made of, and people use both names for the same fence.'),
           ('Do you install vinyl fence gates?', 'Yes. Single walk gates and double drive gates that match the fence, in white or tan.'),
           ('Does a vinyl fence turn yellow in the sun?', 'Vinyl panels made for outdoor use have UV protection that slows yellowing. Ask us about the panel and its warranty when we quote.'),
           ('Will my HOA approve a vinyl fence?', 'White and tan vinyl are common choices in Broward HOAs, but each one sets its own rules. We give you the specs and drawings for the application.'),
           ('How long does installation take?', 'Most homes take 1 to 3 days once the permit is approved.')]),
 dict(slug='aluminum-pool-fence-installation', ag='Aluminum & Pool Fence', hero='alu', tag='Aluminum', label='Metal and aluminum',
      title='Metal, Aluminum & Pool Fences in Broward County, FL',
      desc='Metal fence installation in Broward: aluminum, sheet metal privacy panels, galvanized chain-link (wire mesh) and pool fences. Free estimate: (754) 208-9268.',
      kicker='Metal fencing &#183; Broward County, FL',
      h1='Metal fence &amp; aluminum fence installation <em>in Broward County.</em>',
      sub='Aluminum and pool fences, sheet metal privacy panels and galvanized chain-link, measured, permitted and installed by our own crew.',
      h2='Metal fencing in Broward: which type do you need?',
      body=['&#8220;Metal fence&#8221; can mean very different things: a see-through aluminum fence around a pool, solid sheet metal panels for privacy, or a galvanized wire fence for security. Here is how the metal fences we install compare.',
            table(['Metal fence', 'Privacy', 'Good for'], [
              ['Aluminum picket', 'Open', 'Pools, front yards, waterfront lots'],
              ['Horizontal slat aluminum', 'Partial', 'Modern homes and gates'],
              ['Durafence sheet metal panels', 'Full', 'Backyard privacy with a modern look'],
              ['Galvanized or black chain-link (wire mesh)', 'Open, or partial with slats', 'Security, pets, lots and businesses'],
              ['Custom metal gates', 'Open to full', 'Driveways and walkways']]),
            '<h3>Aluminum fence</h3>',
            'Aluminum does not rust, which makes it the metal of choice near the ocean and the canals from Hollywood to Fort Lauderdale. We install 4 ft. aluminum fence in black or white, horizontal slat aluminum and matching gates.',
            '<h3>Sheet metal privacy fence (Durafence)</h3>',
            'If you are looking for a sheet metal fence, this is it: solid ribbed metal panels set between metal posts, with no gaps to see through. A sheet metal privacy fence comes in standard, horizontal and shadowbox Durafence. Photos of our jobs are below.',
            '<h3>Wire fence, wire mesh and galvanized fence</h3>',
            'Most people who search for wire fencing or a mesh fence need chain-link: steel wire woven into a diamond mesh. A galvanized fence has a zinc coating that protects the steel and is the economical option. Black coated chain-link blends into the yard, and privacy slats block the view. See <a href="/chain-link-fence-installation">chain-link fence installation</a>. Need a welded mesh fence, with wires welded into squares instead of woven? Tell us the height and what you want to enclose, and we will confirm the options and price in your estimate.',
            '<h3>Metal pool fence</h3>',
            'A Florida pool barrier has to be at least 4 ft. tall on the outside, with no gaps a child can get through or climb, and gates that self-close, self-latch and open away from the pool. Aluminum picket is the usual choice. Read the <a href="/pool-fence-requirements-florida">pool fence requirements in Florida</a>.',
            '<h3>Metal fence installation, step by step</h3>',
            'We measure on site and quote in writing, file the permit with your city, install with our own crew and schedule the final city inspection. Most homes take 1 to 3 days once the permit is approved. See <a href="/fence-installation-process">the full process</a>.'],
      styles=['Aluminum fence', 'Sheet metal privacy fence', 'Galvanized fence', 'Wire mesh / chain-link', 'Pool fence', 'Custom metal gates'],
      gal=[('aluminum/aluminum-horizontal-durafence-04', 'Horizontal sheet metal privacy fence (Durafence)'), ('aluminum/aluminum-white-durafence-01', 'White metal privacy fence (Durafence)'), ('aluminum/aluminum-4-ft-aluminum-black-13', '4 ft. black aluminum fence'), ('aluminum/aluminum-4-ft-aluminum-lakefront-15', 'Lakefront aluminum fence'), ('aluminum/aluminum-horizontal-slat-gate-11', 'Horizontal slat gate'), ('aluminum/aluminum-custom-metal-double-gate-06', 'Custom metal double gate'), ('chain-link/chain-link-galvanized-chain-link-04', 'Galvanized wire mesh fence (chain-link)'), ('chain-link/chain-link-black-chain-link-02', 'Black wire mesh fence (chain-link)')],
      cost=['Linear feet and height', 'Type of metal fence: aluminum, sheet metal panels or galvanized chain-link', 'Gates and self-closing pool hardware', 'Removal of an old fence, if any'],
      faq=[('What kinds of metal fence do you install?', 'Aluminum picket and slat fences, Durafence sheet metal privacy panels, galvanized and black chain-link, pool fences and custom metal gates.'),
           ('What is a sheet metal privacy fence?', 'A fence made of solid metal panels set between posts, with no gaps to see through. We install it as Durafence.'),
           ('Do you install wire or welded mesh fences?', 'We install chain-link, which is a woven wire mesh. For welded mesh, send us the height and size you need and we will confirm the options in your free estimate.'),
           ('Galvanized fence or aluminum fence near the beach?', 'Galvanized steel is protected by a zinc coating, but salt air wears it down over time. Aluminum does not rust, so it is the safer choice close to the ocean.'),
           ('What does a pool fence need in Florida?', 'At least 4 ft. tall on the outside, no climbable openings, and self-closing, self-latching gates that open away from the pool.'),
           ('Do you install metal gates?', 'Yes. Walk gates, double driveway gates and custom metal gates.')]),
 dict(slug='wood-fence-installation', ag='Wood & Chain Link Fence', hero='wood', tag='Wood',
      title='Wood Fence Company in South Florida | Florida Fence Solution',
      desc='Wood fence company in South Florida: horizontal, shadowbox, board-on-board & ranch pine fences in Broward. Permits handled. Free estimate: (754) 208-9268.',
      kicker='Wood fences &#183; South Florida',
      h1='Wood fence company <em>for South Florida homes.</em>',
      sub='Horizontal, shadowbox, board-on-board and ranch-style pine fences, measured, permitted and built on site by our own crew across Broward County.',
      h2='Wood fences that hold up in Florida',
      body=['Wood is still the most affordable way to get a full privacy fence in South Florida. We build with pressure-treated pine rated for ground contact, set every post in concrete and use galvanized or stainless fasteners so the fence does not bleed rust.',
            'Popular styles in Broward include modern horizontal wood, shadowbox (good-neighbor on both sides), board-on-board for full privacy and ranch style for large lots in Davie and Plantation Acres.',
            '<h3>Which wood fence style to choose</h3>',
            table(['Style', 'Privacy', 'Good for'], [
              ['Horizontal wood', 'Full or near-full', 'Modern homes and pool areas'],
              ['Shadowbox', 'High, looks the same from both sides', 'Shared property lines and many HOA communities'],
              ['Board-on-board', 'Full, no gaps', 'Backyards where privacy matters most'],
              ['Notch picket / stockade', 'High', 'Classic look at the lowest cost per foot'],
              ['Ranch style', 'Open', 'Large lots, horse properties and long runs']]),
            '<h3>How we build a wood fence for sun, rain and hurricanes</h3>',
            'South Florida wood fails in predictable places: posts rot at the ground line, fasteners rust and stain the boards, and gates sag. We set posts in concrete, reinforce gate and corner posts, and use hardware that will not rust out. Broward is part of Florida\'s High-Velocity Hurricane Zone, so every fence we install is permitted and built for strong wind. See <a href="/best-hurricane-fence-south-florida">the best hurricane fence for South Florida</a>.',
            '<h3>Keeping a wood fence looking good</h3>',
            'New pressure-treated pine dries out over the first weeks and then can be sealed or stained. Plan on re-sealing every couple of years to protect it from sun and rain. Our guide on <a href="/how-to-clean-a-fence-in-florida">how to clean a fence in Florida</a> covers mildew and algae.',
            '<h3>Wood, PVC or aluminum?</h3>',
            'Wood costs less up front and looks warm and natural. PVC vinyl costs more but needs almost no maintenance, and aluminum is the best choice near salt water. Compare them in <a href="/wood-vs-vinyl-vs-aluminum-fence-florida">wood vs. vinyl vs. aluminum in Florida</a>, or see <a href="/vinyl-pvc-fence-installation">PVC vinyl fences</a> and <a href="/aluminum-pool-fence-installation">aluminum fences</a>.'],
      styles=['Horizontal wood', 'Shadowbox', 'Board-on-board', 'Notch picket', 'Ranch style', 'Capped &amp; custom'],
      gal=[('wood/wood-horizontal-wood-01', 'Horizontal wood'), ('wood/wood-shadowbox-with-gate-03', 'Shadowbox with gate'), ('wood/wood-board-on-board-04', 'Board-on-board'), ('wood/wood-ranch-style-05', 'Ranch style'), ('wood/wood-custom-capped-wood-06', 'Custom capped wood'), ('wood/wood-board-on-board-with-gate-02', 'Board-on-board with gate')],
      cost=['Linear feet and height', 'Style: horizontal, shadowbox, board-on-board or ranch', 'Gates and hardware', 'Stain or sealer, if wanted'],
      faq=[('How long does a wood fence last in South Florida?', 'Pressure-treated pine lasts 10 to 15 years here with sealing every couple of years. Posts set in concrete last the longest.'),
           ('Is wood cheaper than PVC?', 'Yes, wood usually costs less up front. PVC costs more but needs almost no maintenance.'),
           ('Do you stain or seal wood fences?', 'Yes, we can seal or stain the fence after installation to protect it from sun and rain.'),
           ('Do you build horizontal wood fences?', 'Yes. Horizontal wood is one of our most requested modern styles.'),
           ('Where do you install wood fences in South Florida?', 'Across Broward County, including Hollywood, Fort Lauderdale, Pembroke Pines, Miramar, Davie, Weston, Coral Springs and Plantation, plus Miami Gardens.'),
           ('Do I need a permit for a wood fence?', 'In almost every Broward city, yes. We file the permit and schedule the final inspection. <a href="/fence-permit-broward-county">More on fence permits</a>.')]),
 dict(slug='chain-link-fence-installation', ag='Wood & Chain Link Fence', hero='chain', tag='Chain-link',
      title='Chain Link Fences in Broward County | Florida Fence Solution',
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
            'We repair wood, PVC vinyl, aluminum, Durafence and chain-link fences, reset posts in concrete and rehang or replace gates and hardware. If a repair won\'t last, we tell you and quote a replacement instead.',
            'Near the coast? See our <a href="/fence-repair-fort-lauderdale-fl">fence repair in Fort Lauderdale</a> page for canal-front and salt-air repairs.'],
      styles=['Storm damage', 'Leaning or rotten posts', 'Broken panels &amp; pickets', 'Sagging gates', 'Gate hardware &amp; latches', 'Pool gate repairs'],
      gal=[('wood/wood-shadowbox-with-gate-03', 'Wood gate rebuilt'), ('pvc/pvc-standard-pvc-gate-06', 'PVC gate'), ('aluminum/aluminum-durafence-with-gate-03', 'Durafence with gate'), ('chain-link/chain-link-black-chain-link-02', 'Chain-link')],
      cost=['Number of posts and panels to replace', 'Material: wood, PVC, aluminum or chain-link', 'Gate repair or replacement', 'Matching discontinued styles'],
      faq=[('Do you repair fences you didn\'t install?', 'Yes. We repair any wood, PVC, aluminum or chain-link fence.'),
           ('Can you fix a leaning fence?', 'Yes. We reset or replace the posts in concrete so the fence stands straight again.'),
           ('Do you repair storm damage?', 'Yes. After hurricanes and storms we repair panels, posts and gates and can document the damage for your insurance.'),
           ('Repair or replace: how do I know?', 'If most posts are rotten or the fence is past its life, replacing is cheaper long term. We tell you honestly after seeing it.')]),
]

def spage(s):
    area = s.get('area', 'Broward County')
    wa = "https://wa.me/17542089268?text=" + ("Hi! I'd like a free estimate for " + s['tag'].lower() + " fence work.").replace(' ', '%20')
    gal = ''.join(f'<figure class="slide"><a href="{CAT}{f}.webp" target="_blank" rel="noopener"><img src="{CAT}{f}-sm.webp" alt="{cap} by Florida Fence Solution in {area}" loading="lazy" decoding="async" width="640" height="480"></a><figcaption>{cap}</figcaption></figure>' for f, cap in s['gal'])
    chips = ''.join(f'<li>{x}</li>' for x in s['styles'])
    faqs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in s['faq'] + [
        ('Are you licensed and insured?', 'Yes. Florida Fence Solution is licensed and insured, family-owned and based in Hollywood, FL.')])
    others = ''.join(f'<a href="/{u}">{t}</a>' for u, t in SVC_NAV if u != s['slug'])
    cities = ''.join(f'<a href="/fence-company-{c["slug"]}-fl">{c["name"]}</a>' for c in C)
    body = ''.join(p if p.startswith('<') else f'<p>{p}</p>' for p in s['body'])
    cost = ''.join(f'<li>{x}</li>' for x in s['cost'])
    return f'''<div class="ffs">
{HEAD}
<section class="hero city-hero">{img(s['hero'], eager=True).replace('alt=""', f'alt="{s["tag"]} fence {s.get("alt_verb", "installed")} by Florida Fence Solution in {area}"')}
<div class="wrap"><div class="hero-copy">
<span class="kicker">{s.get('kicker', s['tag'] + ' fences &#183; Broward County, FL')}</span>
<h1>{s['h1']}</h1>
<p class="sub">{s['sub']}</p>
<div class="ctas"><a class="btn btn-accent" href="/#estimate">Get a free estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-glass" href="tel:+17542089268">Call (754) 208-9268</a></div>
<a class="rating" href="/#reviews"><b>5.0</b><span class="stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9733;</span><span>17 Google reviews</span></a>
</div></div></section>
<div id="quote" class="q-anchor"></div>

<section id="fences"><div class="wrap">
<div class="head"><div><span class="kicker">{s.get('label', s['tag'])}</span><h2>{s['h2']}</h2></div>
<div class="prose">{body}</div></div>
<ul class="chips" style="margin:8px 0 28px">{chips}</ul>
<div class="cat-grid">{gal}</div>
</div></section>

<section class="why dark"><div class="wrap">
<div class="why-img">{img('crew','', '(max-width:1024px) 90vw, 45vw').replace('alt=""', 'alt="Florida Fence Solution crew"')}</div>
<div class="prose"><span class="kicker">Pricing</span><h2>What affects the price</h2>
<ul class="price">{cost}</ul>
<p>Every estimate is free and in writing, after we measure on site. No surprises: permit, materials, labor and cleanup are included in the quote.</p>
<ol class="reasons"><li><span class="n" aria-hidden="true">1</span><div><h3>Licensed and insured</h3><p>Family-owned, based in Hollywood, FL.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><h3>Permits and HOA, handled</h3><p>We file with your city and build to Florida code.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><h3>Our own crew</h3><p>No random subs. We clean up before we leave.</p></div></li></ol>
</div></div></section>

<section id="faq" class="dark" style="padding-top:0"><div class="wrap faq-grid">
<div><span class="kicker">FAQ</span><h2>{s.get('label', s['tag'])} fence questions</h2></div>
<div class="faq">{faqs}</div></div></section>

<section class="estimate"><div class="wrap">
<div><span class="kicker">Free estimate</span><h2>Get your {s.get('label', s['tag']).lower()} fence quote</h2><p class="lead">Takes a minute. We answer the same day. Hablamos espa&#241;ol.</p>
<div class="ctas" style="margin-top:24px"><a class="btn btn-accent" href="/#estimate">Request an estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-dark" href="tel:+17542089268">Call (754) 208-9268</a><a class="btn btn-dark" href="{wa}" target="_blank" rel="noopener">WhatsApp</a></div></div>
<div class="near"><span class="kicker">More services</span><h3 style="margin-bottom:12px">We also install</h3>{others}<h3 style="margin:20px 0 12px">Areas we serve</h3>{cities}</div>
</div></section>

{foot(wa)}{s.get('ld', '')}
</div>'''

# Service x city landing pages (same template as S; not listed in SVC_NAV or S so other pages' nav stays the same).
SITE = 'https://www.floridafencesolution.com'
def ld(s, city):
    strip = lambda t: re.sub('<[^>]+>', '', t)
    faq = s['faq'] + [('Are you licensed and insured?', 'Yes. Florida Fence Solution is licensed and insured, family-owned and based in Hollywood, FL.')]
    biz = {'@type': 'HomeAndConstructionBusiness', '@id': SITE + '/#business', 'name': 'Florida Fence Solution LLC', 'url': SITE + '/', 'telephone': '+1-754-208-9268',
           'address': {'@type': 'PostalAddress', 'streetAddress': '1331 N 70th Way', 'addressLocality': 'Hollywood', 'addressRegion': 'FL', 'postalCode': '33024', 'addressCountry': 'US'}}
    svc = {'@context': 'https://schema.org', '@type': 'Service', 'name': strip(s['h1']).split(' after')[0].strip(), 'serviceType': 'Fence repair',
           'url': f'{SITE}/{s["slug"]}', 'provider': biz, 'areaServed': {'@type': 'City', 'name': city + ', FL'}}
    fq = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in faq]}
    return ''.join(f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (svc, fq))

L = [
 dict(slug='fence-repair-fort-lauderdale-fl', ag='Fence Repair', hero='louver', tag='Repair', area='Fort Lauderdale, FL', alt_verb='repaired',
      kicker='Fence repair &#183; Fort Lauderdale, FL',
      title='Fence Repair in Fort Lauderdale, FL | Florida Fence Solution',
      desc='Fence repair in Fort Lauderdale, FL: leaning posts, broken panels, sagging gates and storm damage on wood, PVC, aluminum & chain-link. Call (754) 208-9268.',
      h1='Fence repair in Fort Lauderdale, FL <em>after storms, salt air and wear.</em>',
      sub='Leaning posts, broken panels, gates that won\'t latch and storm damage. We repair wood, PVC vinyl, aluminum, Durafence and chain-link fences across Fort Lauderdale.',
      h2='Fort Lauderdale fence repair, done to last',
      body=['Fort Lauderdale is hard on fences. Canal-front lots, sandy soil, salt air and hurricane season all work against posts, panels and hardware. Most damaged fences we see here don\'t need a full replacement: a few posts have shifted, some panels cracked in the wind or a gate dropped and stopped closing. We repair what is broken, match the material you already have and leave the rest of the fence alone.',
            '<h3>Posts</h3>',
            'A leaning fence almost always starts at the post. Wood posts rot at the ground line, and posts set too shallow in sandy soil move after heavy rain or wind. We dig out the failed post, set a new one in concrete and go deeper where the ground is soft, which is common near the Intracoastal and the canals in Coral Ridge, Rio Vista and Riverland.',
            '<h3>Panels and pickets</h3>',
            'Broken pickets, cracked PVC vinyl panels, bent aluminum sections and torn chain-link mesh can usually be replaced one section at a time. We match white or tan PVC, picket and Durafence aluminum, pressure-treated pine and black or galvanized chain-link so the repair blends in with the existing fence.',
            '<h3>Gates</h3>',
            'Gates take the most abuse. Sagging gates, dragging gates, worn hinges and broken latches are some of our most common repair calls in Victoria Park, Tarpon River and Imperial Point. We rehang or rebuild the gate, reinforce the gate post and replace the hardware. On pool fences, we restore self-closing, self-latching gates so the barrier works the way Florida pool safety rules require.',
            '<h3>Storm damage</h3>',
            'After a hurricane or a strong storm, we repair blown-out panels, snapped or leaning posts and damaged gates, and we can document the damage for your insurance claim. If a section was built with shallow posts or weak panels, we fix the cause, not just the part that fell, so it holds up better next season.',
            '<h3>Repair or replace?</h3>',
            'If most posts are rotten or the fence is past its life, a repair won\'t last and replacing it costs less long term. We tell you honestly after seeing it, and quote both when it makes sense. See our general <a href="/fence-repair">fence repair service</a> for all of Broward County, or our <a href="/fence-company-fort-lauderdale-fl">Fort Lauderdale fence company</a> page if you are planning a new fence.'],
      styles=['Leaning or rotten posts', 'Broken panels &amp; pickets', 'Sagging gates', 'Gate hinges &amp; latches', 'Pool gate repairs', 'Storm damage', 'Wood, PVC, aluminum &amp; chain-link'],
      gal=[('wood/wood-shadowbox-with-gate-03', 'Wood gate rebuilt'), ('pvc/pvc-standard-pvc-gate-06', 'PVC gate'), ('aluminum/aluminum-durafence-with-gate-03', 'Durafence with gate'), ('chain-link/chain-link-black-chain-link-02', 'Chain-link')],
      cost=['Number of posts and panels to replace', 'Material: wood, PVC vinyl, aluminum, Durafence or chain-link', 'Gate repair or full gate replacement', 'Matching an older or discontinued style', 'Soil and access on canal-front lots'],
      faq=[('Do you repair fences in Fort Lauderdale that you didn\'t install?', 'Yes. We repair any wood, PVC vinyl, aluminum, Durafence or chain-link fence in Fort Lauderdale, no matter who built it.'),
           ('Can you fix a leaning fence on a canal-front lot?', 'Yes. We reset or replace the posts in concrete and set them deeper in sandy soil so the fence stands straight again.'),
           ('Do you repair hurricane and storm damage?', 'Yes. We repair panels, posts and gates after storms and can document the damage for your insurance claim.'),
           ('Can you repair my pool fence gate?', 'Yes. We fix or replace pool gates and hardware so they self-close and self-latch again.'),
           ('How much does fence repair cost in Fort Lauderdale?', 'It depends on how many posts, panels or gates need work and the material. The estimate is free and in writing after we see the fence.')]),
]
for x in L:
    x['ld'] = ld(x, 'Fort Lauderdale')

os.makedirs('services', exist_ok=True)
smeta = []
for s in S + L:
    html = (css + '\n' + spage(s)).replace('loading="lazy"', 'loading="lazy" fetchpriority="low"').replace('href="/#estimate"', 'href="#quote"').encode('ascii', 'xmlcharrefreplace').decode()
    assert html.count('<div') == html.count('</div'), s['slug']
    open(f'services/{s["slug"]}.html', 'w').write(html)
    smeta.append(dict(slug=s['slug'], ad_group=s['ag'], title=s['title'], desc=s['desc']))
json.dump(smeta, open('services/meta.json', 'w'), indent=1)
open('services/preview.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+open('services/aluminum-pool-fence-installation.html').read()+'</body></html>')
print([len(open(f'services/{s["slug"]}.html').read()) for s in S + L])
