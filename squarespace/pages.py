# Header-topic pages + blog (plain Squarespace pages, one code block each). Run via cities.py (uses css, img, HEAD, foot, C, S, SVC_NAV, CAT).
PCSS = '''<style>
.ffs .article{max-width:780px}
.ffs .article h2{font-size:clamp(1.5rem,1.1rem + 1.6vw,2.2rem)!important;margin:40px 0 12px}
.ffs .article h3{margin:24px 0 8px}
.ffs .article p,.ffs .article li{color:var(--muted);margin-bottom:12px;line-height:1.65}
.ffs .article ul,.ffs .article ol{margin:0 0 16px 22px}
.ffs .article a{color:inherit;text-decoration:underline;text-decoration-color:var(--accent);text-underline-offset:3px}
.ffs .cmp-wrap{overflow-x:auto;margin:16px 0 24px}
.ffs .cmp{width:100%;min-width:560px;border-collapse:collapse;font-size:.95rem}
.ffs .cmp th,.ffs .cmp td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line)}
.ffs .cmp th{background:var(--light-2)}
.ffs .rv-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:16px;margin-top:24px}
.ffs .rv{background:var(--light-2);border-radius:var(--r);padding:24px}
.ffs .rv p{margin:10px 0 14px}
.ffs .rv b{display:block}
.ffs .rv .st{color:var(--accent)}
.ffs .posts{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;margin-top:24px}
.ffs .post-card{display:block;background:var(--light-2);border-radius:var(--r);padding:26px;text-decoration:none;transition:transform .25s var(--ease)}
.ffs .post-card:hover{transform:translateY(-4px)}
.ffs .post-card h3{margin:8px 0}
.ffs .post-card p{color:var(--muted)}
.ffs .meta{color:var(--muted);font-size:.9rem}
.ffs .city-list a,.ffs .city-list span{display:inline-block;margin:4px 6px 4px 0;padding:8px 14px;border-radius:999px;background:var(--light-2);font-weight:600;font-size:.92rem;text-decoration:none}
.ffs .city-list a:hover{background:var(--accent)}
.ffs .map-static{display:block;border-radius:24px;overflow:hidden;margin-top:24px}
.ffs .map-static img{width:100%;height:auto;display:block}
</style>'''

WA = "https://wa.me/17542089268?text=Hi!%20I'd%20like%20a%20free%20fence%20estimate."
CITY = {c['name']: f'/fence-company-{c["slug"]}-fl' for c in C}

def svc_list():
    return ''.join(f'<li><a href="/{s["slug"]}">{s["tag"]} fences</a>: {s["sub"]}</li>' for s in S)

def rel(links):
    return ''.join(f'<a href="{u}">{t}</a>' for u, t in links)

REVIEWS = [
 ('A. V.', 'Highly recommend them, family run business. Ethan and his dad were fantastic to deal with. Gave me a great price on a durafence for my backyard. The work took 2 days and was excellent and professional.'),
 ('Alexander O.', 'Ethan was fantastic to work with. He was very friendly, responsive, and able to come out the same day, which I really appreciated. He quickly took care of our fence repair and made the whole process easy and stress-free.'),
 ('Michael B.', 'Ethan and the Team were Amazing! They worked with me, and I got exactly what i was looking for! We love our new fence! Very professional, Highly Recommended!'),
 ('Alan T.', 'This is a family business, which is always a plus for me. I enjoy dealing directly with the owners Ethan and his dad.'),
 ('Anna N.', 'Ethan helped with the entire process and did a great job on my new fence! The work was quick and professional!'),
]

POSTS = [
 dict(slug='how-to-clean-a-fence-in-florida', hero='pvc', tag='Maintenance', date='October 20, 2026',
  title='How to Clean a Fence in South Florida (Vinyl, Wood, Aluminum) | Florida Fence Solution',
  desc='How to clean vinyl, wood, aluminum and chain-link fences in South Florida: mold, mildew and green algae, step by step. Tips from a Broward fence contractor.',
  h1='How to clean a fence in South Florida <em>without damaging it.</em>',
  sub='Humidity, rain and shade turn fences green fast. Here is how to clean each material the right way.',
  body='''<p>In Broward County, mildew and green algae can show up on a fence a few months after it is installed, especially on the shady side. The good news: most of it washes off with mild products and a soft brush. The wrong products, or a pressure washer held too close, can do more damage than the dirt.</p>
<h2>Before you start</h2>
<ul><li>Pick a cloudy morning so the cleaner does not dry on the fence.</li><li>Wet nearby plants with plain water first and rinse them again after.</li><li>Test any cleaner on a small, hidden spot.</li><li>Check for loose posts, cracked panels or rot while you are close to the fence.</li></ul>
<h2>How to clean a vinyl (PVC) fence</h2>
<ol><li>Rinse the fence with a garden hose.</li><li>Mix warm water with a few drops of dish soap. For mildew, add one part white vinegar to three parts water.</li><li>Scrub with a soft brush or sponge, top to bottom.</li><li>Rinse well. If you use a pressure washer, keep it on a low setting with a wide fan tip and at least 2 feet away.</li></ol>
<p>Avoid abrasive pads, solvents and harsh chemicals: they dull the finish and make the panels attract dirt faster.</p>
<h2>How to clean a wood fence</h2>
<ol><li>Sweep off loose debris and cobwebs.</li><li>Use an oxygen bleach (sodium percarbonate) wood cleaner mixed as the label says. It removes mildew without eating the wood like chlorine bleach can.</li><li>Let it sit 10 to 15 minutes, scrub with a stiff nylon brush along the grain, and rinse.</li><li>Let the wood dry for at least 48 hours, then apply a sealer or stain to slow down the next round of mildew.</li></ol>
<p>Pressure washing wood at high pressure raises the grain and leaves marks. If you use one, stay on low pressure and keep moving.</p>
<h2>How to clean an aluminum fence or Durafence</h2>
<p>Powder-coated aluminum only needs mild soap, water and a soft cloth or brush. Rinse well. Never use steel wool, scouring powder or acid cleaners, because they scratch the coating that protects the metal.</p>
<h2>How to clean a chain-link fence</h2>
<p>Hose it down, scrub stubborn spots with soapy water and a brush, and rinse. On black vinyl-coated chain-link, use the same gentle approach as aluminum.</p>
<h2>How often should you clean a fence in Florida?</h2>
<p>Once or twice a year is enough for most homes. Fences in full shade, near sprinklers or close to the beach may need it every few months. A quick rinse after heavy pollen season also helps.</p>
<h2>When cleaning is not enough</h2>
<p>If cleaning uncovers soft or rotten wood, leaning posts, cracked vinyl or gates that no longer latch, the fence needs a repair, not a wash. See our <a href="/fence-repair">fence repair service</a>, or if the fence is past its life, compare <a href="/vinyl-pvc-fence-installation">PVC vinyl</a> and <a href="/aluminum-pool-fence-installation">aluminum</a>, which need the least upkeep in Florida.</p>''',
  faq=[('Can I use bleach on a vinyl fence?', 'A diluted solution can remove tough mildew, but test it first, protect your plants and rinse thoroughly. Vinegar and water or a vinyl fence cleaner are gentler options.'),
       ('Will pressure washing damage my fence?', 'High pressure up close can etch vinyl and splinter wood. Use a low setting, a wide fan tip and keep the nozzle at a distance.')]),
 dict(slug='fence-permit-broward-county', hero='alley', tag='Permits', date='October 20, 2026',
  title='Do You Need a Fence Permit in Broward County? | Florida Fence Solution',
  desc='Do you need a permit to build a fence in Broward County, FL? What cities usually ask for, HOA approval, inspections and how long it takes. Explained by a local fence contractor.',
  h1='Do you need a fence permit <em>in Broward County?</em>',
  sub='Short answer: almost always. Here is what the permit involves and how we handle it for you.',
  body='''<p>In nearly every Broward city, including Hollywood, Fort Lauderdale, Pembroke Pines, Miramar, Davie, Weston, Coral Springs and Plantation, a new fence needs a building permit. Unincorporated areas go through Broward County. Replacing an existing fence usually needs one too.</p>
<h2>What the city usually asks for</h2>
<ul><li>A copy of your property survey with the fence line drawn on it.</li><li>Fence height, material and style, plus gate locations.</li><li>Product information or drawings showing how posts are set.</li><li>HOA approval, if your community has an HOA.</li><li>For pools, proof that the fence and gates meet pool barrier rules.</li></ul>
<h2>Height and location rules</h2>
<p>Each city sets its own limits. Many allow taller privacy fences in back and side yards and lower fences in front yards, and corner lots often have visibility rules near the street. Easements and utility lines can also limit where posts go. We check your city's code before we quote, so the design gets approved the first time.</p>
<h2>Why wind matters in Broward</h2>
<p>Broward County is part of Florida's High-Velocity Hurricane Zone. Permitted fences have to be built for strong wind: post depth, concrete footings, spacing and the panel system all matter. That is one reason a cheap, unpermitted fence often fails in the first big storm.</p>
<h2>HOA approval</h2>
<p>If you live in an HOA community, you usually need written approval before the city will issue the permit. HOAs often specify color, height and style. We give you the drawings and specs to submit.</p>
<h2>Inspections</h2>
<p>After installation, the city inspects the fence. Once it passes, the permit is closed. An open or failed permit can cause problems when you sell or refinance, so it is worth doing right.</p>
<h2>How long does it take?</h2>
<p>It depends on the city and how busy it is. Once the permit is approved, most residential fences take 1 to 3 days to install. See our full <a href="/fence-installation-process">fence installation process</a>.</p>
<h2>We handle it for you</h2>
<p>Florida Fence Solution prepares the paperwork, files the permit, follows up with the city and schedules the final inspection. You pick the fence; we deal with the city.</p>''',
  faq=[('Can I build a fence without a permit in Broward?', 'You risk fines, a stop-work order or having to remove the fence, and it can cause issues when you sell the home. We always pull the permit.'),
       ('Do I need a permit to replace an old fence?', 'In most Broward cities, yes. Replacing an entire fence is treated like new construction.')]),
 dict(slug='best-hurricane-fence-south-florida', hero='alu', tag='Hurricanes', date='October 20, 2026',
  title='Best Fence for Hurricanes in South Florida | Florida Fence Solution',
  desc='Which fence holds up best in South Florida hurricanes? Aluminum, Durafence, PVC vinyl, wood and chain-link compared by a Broward fence contractor.',
  h1='The best fence for hurricanes <em>in South Florida.</em>',
  sub='No fence is storm-proof, but some materials and build methods handle hurricane season far better.',
  body='''<p>Every hurricane season we see the same thing: fences that were built right are still standing, and fences with shallow posts or weak panels are lying in the yard. Material matters, but installation matters just as much.</p>
<h2>1. Aluminum and Durafence</h2>
<p>Aluminum does not rust, does not rot and stays strong for decades. Picket aluminum lets wind pass through, so it puts less load on the posts. Durafence is an aluminum privacy system designed for high wind, which makes it one of the best options when you want privacy and storm resistance. <a href="/aluminum-pool-fence-installation">See aluminum and Durafence</a>.</p>
<h2>2. Chain-link</h2>
<p>Wind passes straight through chain-link, so it rarely blows over. Privacy slats add wind load, so posts need to be set properly. <a href="/chain-link-fence-installation">See chain-link fences</a>.</p>
<h2>3. PVC vinyl</h2>
<p>Solid privacy panels catch a lot of wind. A well-installed PVC fence with reinforced posts set in concrete does well; cheap panels and shallow posts do not. Louvered and shadowbox styles let some air through. <a href="/vinyl-pvc-fence-installation">See PVC vinyl fences</a>.</p>
<h2>4. Wood</h2>
<p>Wood privacy fences are affordable, but they act like a sail in strong wind, and posts weaken over time as they rot at ground level. Good concrete footings and regular maintenance help. <a href="/wood-fence-installation">See wood fences</a>.</p>
<div class="cmp-wrap"><table class="cmp"><tr><th>Material</th><th>Wind resistance</th><th>Rust / rot</th><th>Upkeep</th></tr>
<tr><td>Aluminum / Durafence</td><td>Very good</td><td>No rust, no rot</td><td>Very low</td></tr>
<tr><td>Chain-link</td><td>Very good (without slats)</td><td>Galvanized or coated</td><td>Low</td></tr>
<tr><td>PVC vinyl</td><td>Good if reinforced</td><td>No rot</td><td>Low</td></tr>
<tr><td>Wood</td><td>Fair</td><td>Can rot</td><td>Medium to high</td></tr></table></div>
<h2>What makes any fence stronger</h2>
<ul><li>Posts set deep in concrete, not just tamped soil.</li><li>Reinforced posts at gates and corners.</li><li>Correct post spacing for the panel system.</li><li>Stainless or galvanized hardware that will not rust out.</li><li>A permitted install built for Broward's High-Velocity Hurricane Zone.</li></ul>
<h2>After a storm</h2>
<p>Check posts for leaning, look for cracked panels and test gate latches, especially on pool gates. If something is off, our <a href="/fence-repair">fence repair</a> team can fix it before the next storm.</p>''',
  faq=[('What is the most hurricane-resistant privacy fence?', 'Aluminum privacy systems like Durafence are among the strongest options for privacy in high wind.'),
       ('Should I remove fence panels before a hurricane?', 'Generally no. Secure loose items and gates. A properly installed fence is built to stay in place.')]),
 dict(slug='wood-vs-vinyl-vs-aluminum-fence-florida', hero='wood', tag='Materials', date='October 20, 2026',
  title='Wood vs Vinyl vs Aluminum Fence in Florida | Florida Fence Solution',
  desc='Wood vs vinyl (PVC) vs aluminum fence in South Florida: cost, lifespan, maintenance, privacy and hurricane performance compared.',
  h1='Wood vs vinyl vs aluminum: <em>which fence fits your Florida home?</em>',
  sub='A straight comparison from a Broward fence contractor who installs all three.',
  body='''<p>The right fence depends on what you need most: privacy, budget, low maintenance, pool safety or a modern look. Here is how the three most popular materials compare in South Florida's heat, humidity and storms.</p>
<div class="cmp-wrap"><table class="cmp"><tr><th></th><th>Wood</th><th>PVC vinyl</th><th>Aluminum</th></tr>
<tr><td>Upfront cost</td><td>Lowest</td><td>Medium</td><td>Medium to high</td></tr>
<tr><td>Typical lifespan here</td><td>10 to 15 years</td><td>20+ years</td><td>Decades</td></tr>
<tr><td>Maintenance</td><td>Seal or stain every few years</td><td>Rinse occasionally</td><td>Rinse occasionally</td></tr>
<tr><td>Privacy</td><td>Full</td><td>Full</td><td>Picket: low. Durafence: full</td></tr>
<tr><td>Salt air</td><td>OK with good hardware</td><td>Good</td><td>Excellent</td></tr>
<tr><td>Best for</td><td>Budget privacy, natural look</td><td>HOA communities, privacy</td><td>Pools, waterfront, modern look</td></tr></table></div>
<h2>Wood: warm look, lower price</h2>
<p>Pressure-treated pine is the most affordable way to get a full privacy fence. Styles like horizontal, shadowbox and board-on-board look great. The trade-off is upkeep: in Florida, wood needs sealing to fight sun, rain and mildew. <a href="/wood-fence-installation">Wood fence installation</a>.</p>
<h2>PVC vinyl: privacy without painting</h2>
<p>Vinyl never needs paint and will not rot, which is why most Broward HOAs approve it. White and tan are the common colors. It costs more than wood up front but less over time. <a href="/vinyl-pvc-fence-installation">Vinyl fence installation</a>.</p>
<h2>Aluminum and Durafence: built for the coast</h2>
<p>Aluminum will not rust, so it is the go-to near the beach, canals and pools. Picket aluminum is the standard pool fence; Durafence adds full privacy with an aluminum frame built for high wind. <a href="/aluminum-pool-fence-installation">Aluminum and pool fences</a>.</p>
<h2>Our quick recommendation</h2>
<ul><li>Tight budget, want privacy: wood.</li><li>HOA community, want no maintenance: PVC vinyl.</li><li>Pool, waterfront or modern look: aluminum or Durafence.</li><li>Security on a budget: <a href="/chain-link-fence-installation">chain-link</a>.</li></ul>''',
  faq=[('Which fence lasts longest in Florida?', 'Aluminum, followed by PVC vinyl. Both resist rot and humidity far better than wood.'),
       ('Is vinyl fence worth it over wood?', 'If you plan to stay in the home, usually yes: no painting or sealing and a longer life.')]),
 dict(slug='pool-fence-requirements-florida', hero='pvc', tag='Pool safety', date='October 20, 2026',
  title='Pool Fence Requirements in Florida | Florida Fence Solution',
  desc='Florida pool fence requirements explained: barrier height, gaps, self-closing and self-latching gates. What Broward homeowners need to pass inspection.',
  h1='Pool fence requirements <em>in Florida, explained.</em>',
  sub='What a pool barrier needs to pass inspection in Broward County, in plain English.',
  body='''<p>Florida takes pool safety seriously. The Residential Swimming Pool Safety Act (Chapter 515, Florida Statutes) and the Florida Building Code set the baseline for new residential pools, and your city inspects the barrier before the pool is approved.</p>
<h2>The basics of a compliant pool barrier</h2>
<ul><li>At least 4 feet tall, measured on the outside of the barrier.</li><li>No gaps or openings that a 4-inch sphere can pass through.</li><li>No footholds or handholds that make it easy for a child to climb.</li><li>Placed so it cannot be used to climb into the pool area, and kept clear of permanent objects that could be used to climb over it.</li></ul>
<h2>Gates</h2>
<ul><li>Gates open outward, away from the pool.</li><li>Self-closing and self-latching.</li><li>Latches placed high enough that small children cannot reach them, as the code specifies.</li></ul>
<p>Your city may add its own requirements, and other safety features (like alarms on doors that open to the pool) may also apply. We check the current rules for your city before we design the barrier.</p>
<h2>Best materials for pool fences</h2>
<p>Picket aluminum is the most common pool fence in South Florida: it does not rust from pool chemicals or salt air, it keeps the view open, and the spacing is made to meet code. PVC vinyl and Durafence work when you want privacy too. <a href="/aluminum-pool-fence-installation">See aluminum and pool fences</a>.</p>
<h2>Permits and inspection</h2>
<p>A pool fence needs a permit and an inspection. We prepare the paperwork, build to code and schedule the inspection. Read more about <a href="/fence-permit-broward-county">fence permits in Broward County</a>.</p>''',
  faq=[('How tall does a pool fence need to be in Florida?', 'At least 4 feet, measured on the outside. Many homeowners choose taller for privacy.'),
       ('Can my existing fence count as the pool barrier?', 'Sometimes, if it meets the height, gap and gate rules. We can check it and upgrade gates and hardware if needed.')]),
]

PAGES = [
 dict(slug='residential-fence-solutions', nav='Residential Fence Solutions', hero='louver', kicker='Fences &#183; South Florida',
  title='Residential & Custom Fence Solutions in South Florida | Florida Fence Solution',
  desc='Residential and custom fence solutions in Broward County and South Florida: PVC vinyl, aluminum, Durafence, wood and chain-link. Free estimate: (754) 208-9268.',
  h1='Residential fence solutions <em>for South Florida homes.</em>',
  sub='Privacy, pool safety, security or curb appeal: we design, permit and install the right fence for your home.',
  body=lambda: f'''<p>Florida Fence Solution is a family-owned fence contractor based in Hollywood, FL. We install residential and custom fences across Broward County and South Florida, with our own crew, the permit handled and a clean job site when we leave.</p>
<h2>Fence types we install</h2><ul>{svc_list()}</ul>
<h2>Custom fence solutions</h2>
<p>Not every yard fits a catalog. We build custom gates, mixed-material fences (for example aluminum in front and PVC privacy in back), horizontal designs, ranch-style runs for large lots and pool barriers that match the rest of the fence.</p>
<h2>How to choose</h2>
<p>Want privacy with no maintenance? PVC vinyl. Near the water or around a pool? Aluminum or Durafence. Tight budget? Wood or chain-link. Read our full <a href="/wood-vs-vinyl-vs-aluminum-fence-florida">wood vs vinyl vs aluminum comparison</a> or the guide to the <a href="/best-hurricane-fence-south-florida">best fence for hurricanes</a>.</p>
<div class="cat-grid" style="margin-top:24px">{''.join(f'<figure class="slide"><a href="/{s["slug"]}"><img src="{CAT}{s["gal"][0][0]}-sm.webp" alt="{s["tag"]} fence by Florida Fence Solution" loading="lazy" width="640" height="480"></a><figcaption>{s["tag"]} fences</figcaption></figure>' for s in S)}</div>''',
  faq=[('Do you install fences for businesses too?', 'Yes. Most of our work is residential, but we also install chain-link, aluminum and privacy fences for businesses and lots.'),
       ('Do you offer custom gates?', 'Yes. Walk gates, double driveway gates and custom metal gates.')]),
 dict(slug='fence-company-reviews', nav='Fence Company Reviews', hero='crew', kicker='Reviews &#183; 5.0 on Google',
  title='Florida Fence Solution Reviews | 5-Star Fence Company in Broward',
  desc='Read Google reviews of Florida Fence Solution, a family-owned fence company in Hollywood serving Fort Lauderdale and all of Broward County. 5.0 stars.',
  h1='5.0 stars on Google. <em>Every single review.</em>',
  sub='What homeowners in Hollywood, Fort Lauderdale and across Broward say about working with our family business.',
  body=lambda: f'''<p>Looking for the best fence company in Fort Lauderdale, Hollywood or anywhere in Broward? Don't take our word for it. These are real Google reviews from our customers.</p>
<div class="rv-grid">{''.join(f'<div class="rv"><span class="st" aria-label="5 stars">&#9733;&#9733;&#9733;&#9733;&#9733;</span><p>&#8220;{t}&#8221;</p><b>{n}</b><span class="meta">Google review</span></div>' for n, t in REVIEWS)}</div>
<p style="margin-top:24px"><a href="https://maps.google.com/?cid=273622298774698385" target="_blank" rel="noopener">Read all 17 reviews on Google Maps &#8594;</a></p>
<h2>Why customers recommend us</h2>
<ul><li><b>Family-owned.</b> You deal directly with the owners, Ethan and his dad.</li><li><b>Fast response.</b> Estimates often the same week, sometimes the same day.</li><li><b>Clean, professional work.</b> Most installs take 1 to 3 days.</li><li><b>Permits handled.</b> We file with your city and build to code.</li></ul>
<p>Ready to be our next 5-star review? See the <a href="/fence-installation-process">installation process</a> or <a href="/residential-fence-solutions">the fences we install</a>.</p>''',
  faq=[('Is Florida Fence Solution licensed and insured?', 'Yes. We are licensed and insured, family-owned and based in Hollywood, FL.'),
       ('Where can I leave a review?', 'On our Google Business Profile. We read every one.')]),
 dict(slug='fence-installation-process', nav='Fence Installation Process', hero='alley', kicker='Process &#183; Quote to inspection',
  title='Fence Installation Process in Broward County | Florida Fence Solution',
  desc='How fence installation works with Florida Fence Solution: free estimate, design, permit and HOA, 1-3 day install and final city inspection in Broward County.',
  h1='From free quote <em>to final inspection.</em>',
  sub='Four clear steps. We handle the permit, the HOA paperwork and the city inspection.',
  body=lambda: '''<ol class="reasons" style="margin-top:0">
<li><span class="n" aria-hidden="true">1</span><div><h3>Free estimate</h3><p>We visit your home, measure the fence line, talk through styles and gates, and give you a written quote. No pressure, no obligation.</p></div></li>
<li><span class="n" aria-hidden="true">2</span><div><h3>Design &amp; permit</h3><p>You choose the material and style. We prepare the drawings, get HOA approval paperwork ready and file the permit with your city.</p></div></li>
<li><span class="n" aria-hidden="true">3</span><div><h3>Installation</h3><p>Once the permit is approved, our own crew installs the fence. Most homes take 1 to 3 days. Posts are set in concrete and we clean up when we finish.</p></div></li>
<li><span class="n" aria-hidden="true">4</span><div><h3>Final inspection</h3><p>The city inspects the fence and closes the permit. Then we do a walkthrough with you to make sure everything is right.</p></div></li></ol>
<h2>How long does the whole process take?</h2>
<p>The install itself is usually 1 to 3 days. The longest part is often the permit and HOA approval, which depends on your city and community. We keep you updated at every step.</p>
<h2>What you need to have ready</h2>
<ul><li>Your property survey (we can tell you how to get one if you don't have it).</li><li>HOA guidelines, if you have an HOA.</li><li>An idea of where you want gates.</li></ul>
<p>More detail: <a href="/fence-permit-broward-county">Do you need a fence permit in Broward County?</a></p>''',
  faq=[('Do I need to be home during installation?', 'Not the whole time. We need access to the yard and to talk with you at the start and at the final walkthrough.'),
       ('Do you remove the old fence?', 'Yes. We can remove and haul away your old fence as part of the job.')]),
 dict(slug='service-areas', nav='Service Areas', hero='chain', kicker='Areas &#183; Broward County',
  title='Fence Contractor in South Florida & Broward County | Service Areas',
  desc='Local fence contractor serving South Florida: Hollywood, Fort Lauderdale, Pembroke Pines, Miramar, Davie, Weston, Coral Springs, Plantation, Miami Gardens and all of Broward.',
  h1='Your local fence contractor <em>in South Florida.</em>',
  sub='Based in Hollywood, FL. Serving all of Broward County, plus Miami Gardens.',
  body=lambda: f'''<p>We are a local fence company, not a national lead service. Our shop is at 1331 N 70th Way in Hollywood, and our own crew installs every fence. That keeps estimates fast and quality consistent across South Florida.</p>
<h2>Cities with local pages</h2><div class="city-list">{''.join(f'<a href="{u}">Fence company in {n}</a>' for n, u in CITY.items())}</div>
<h2>We also serve</h2><div class="city-list">{''.join(f'<span>{n}</span>' for n in ['Parkland', 'Sunrise', 'Cooper City', 'Southwest Ranches', 'Lauderhill', 'Pompano Beach', 'Deerfield Beach'])}</div>
<p style="margin-top:16px">Not on the list? If you are in Broward County or nearby, call us at <a href="tel:+17542089268">(754) 208-9268</a>.</p>
<a class="map-static" href="https://maps.google.com/?cid=273622298774698385" target="_blank" rel="noopener" aria-label="Open Florida Fence Solution in Google Maps"><img src="{B}img/map-hollywood.webp" srcset="{B}img/map-hollywood.webp 1280w, {B}img/map-hollywood-2560.webp 2560w" sizes="(max-width:1280px) 100vw, 1280px" width="1280" height="420" loading="lazy" alt="Map: Florida Fence Solution, 1331 N 70th Way, Hollywood, FL 33024"></a>
<p class="meta">Map data &#169; OpenStreetMap contributors</p>''',
  faq=[('Do you charge extra to travel?', 'Not within Broward County. Estimates are free.'),
       ('Do you work in Miami-Dade?', 'We serve Miami Gardens and nearby areas close to our Hollywood shop.')]),
 dict(slug='fence-faq', nav='Fence FAQ', hero='wood', kicker='FAQ &#183; Straight answers',
  title='Fence FAQ: Cost, Permits, Materials & Installation | Florida Fence Solution',
  desc='Answers to common fence questions in Broward County: permits, HOA, installation time, best materials for Florida, pool fences, repairs and estimates.',
  h1='Fence questions, <em>straight answers.</em>',
  sub='Everything Broward homeowners ask us before installing a fence.',
  body=lambda: '<p>Can\'t find your question? Call <a href="tel:+17542089268">(754) 208-9268</a> or send us a WhatsApp. Hablamos espa&#241;ol.</p>',
  faq=[('Do you handle fence permits?', 'Yes. We pull the permit with your city and build to code, HOA rules included. <a href="/fence-permit-broward-county">More on permits</a>.'),
       ('How long does an install take?', 'Most homes take 1 to 3 days once the permit is approved.'),
       ('How much does a fence cost?', 'It depends on material, height, length, gates and whether we remove an old fence. We give you a free written estimate after measuring on site.'),
       ('Which material holds up best in South Florida?', 'Aluminum, PVC vinyl and Durafence handle humidity, salt air and storms with little upkeep. Wood looks warmer and costs less up front. <a href="/wood-vs-vinyl-vs-aluminum-fence-florida">Compare materials</a>.'),
       ('What is the best fence for hurricanes?', 'Aluminum and Durafence, set in concrete. <a href="/best-hurricane-fence-south-florida">Read the guide</a>.'),
       ('Can you help with HOA approval?', 'Yes. We give you the specs and drawings your HOA asks for.'),
       ('Do you install pool fences?', 'Yes, built to Florida pool barrier rules with self-closing, self-latching gates. <a href="/pool-fence-requirements-florida">Pool fence requirements</a>.'),
       ('Do you repair fences?', 'Yes, wood, PVC, aluminum and chain-link. <a href="/fence-repair">Fence repair</a>.'),
       ('How do I clean my fence?', 'Mild soap, water and a soft brush for most materials. <a href="/how-to-clean-a-fence-in-florida">Cleaning guide</a>.'),
       ('Do you remove the old fence?', 'Yes, we remove and haul it away.'),
       ('Which areas do you serve?', 'All of Broward County plus Miami Gardens. <a href="/service-areas">Service areas</a>.'),
       ('Are you licensed and insured?', 'Yes. Licensed and insured, family-owned, based in Hollywood, FL.'),
       ('&#191;Hablan espa&#241;ol?', 'S&#237;. Atendemos en espa&#241;ol y en ingl&#233;s.')]),
]

def gpage(p, extra=''):
    faqs = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in p['faq'])
    body = p['body']() if callable(p['body']) else p['body']
    heroimg = img(p['hero'], eager=True).replace('alt=""', 'alt="Fence installed by Florida Fence Solution in Broward County"')
    return f'''{PCSS}<div class="ffs">
{HEAD}
<section class="hero city-hero">{heroimg}
<div class="wrap"><div class="hero-copy">
<span class="kicker">{p['kicker']}</span>
<h1>{p['h1']}</h1>
<p class="sub">{p['sub']}</p>
<div class="ctas"><a class="btn btn-accent" href="/#estimate">Get a free estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-glass" href="tel:+17542089268">Call (754) 208-9268</a></div>
</div></div></section>
<section><div class="wrap"><div class="article">{extra}{body}</div></div></section>
<section id="faq" class="dark"><div class="wrap faq-grid">
<div><span class="kicker">FAQ</span><h2>Common questions</h2></div>
<div class="faq">{faqs}</div></div></section>
<section class="estimate"><div class="wrap">
<div><span class="kicker">Free estimate</span><h2>Get your fence quote</h2><p class="lead">Takes a minute. We answer the same day. Hablamos espa&#241;ol.</p>
<div class="ctas" style="margin-top:24px"><a class="btn btn-accent" href="/#estimate">Request an estimate <span class="arr" aria-hidden="true">&#8594;</span></a><a class="btn btn-dark" href="tel:+17542089268">Call (754) 208-9268</a><a class="btn btn-dark" href="{WA}" target="_blank" rel="noopener">WhatsApp</a></div></div>
<div class="near"><span class="kicker">Services</span><h3 style="margin-bottom:12px">Fences we install</h3>{SVC_LINKS}<h3 style="margin:20px 0 12px">Guides</h3><a href="/blog">Fence blog</a><a href="/fence-faq">Fence FAQ</a></div>
</div></section>
{foot(WA)}
</div>'''

BLOG = dict(slug='blog', nav='Blog', hero='crew', kicker='Blog &#183; Fence guides',
  title='Fence Blog: Guides for South Florida Homeowners | Florida Fence Solution',
  desc='Fence guides for South Florida homeowners: permits in Broward, pool fence rules, hurricane-ready fences, cleaning and choosing materials.',
  h1='Fence guides <em>for South Florida homeowners.</em>',
  sub='Practical answers from a family-owned Broward fence contractor.',
  body=lambda: '<div class="posts">' + ''.join(f'<a class="post-card" href="/{q["slug"]}"><span class="kicker">{q["tag"]}</span><h3>{re.sub("<[^>]+>", "", q["h1"])}</h3><p>{q["sub"]}</p><span class="meta">{q["date"]}</span></a>' for q in POSTS) + '</div>',
  faq=[('Do you write about my question?', 'Send it to us on WhatsApp. We add new guides based on what homeowners ask.')])

out = PAGES + [BLOG] + [dict(q, nav=re.sub('<[^>]+>', '', q['h1']).rstrip('.'), kicker=f'{q["tag"]} &#183; Fence guide') for q in POSTS]
os.makedirs('pages', exist_ok=True)
pmeta = []
for p in out:
    by = f'<p class="meta">By Florida Fence Solution &#183; {p["date"]}</p>' if 'date' in p else ''
    html = (css + '\n' + gpage(p, by)).encode('ascii', 'xmlcharrefreplace').decode()
    assert html.count('<div') == html.count('</div'), p['slug']
    open(f'pages/{p["slug"]}.html', 'w').write(html)
    pmeta.append(dict(slug=p['slug'], nav=p['nav'], title=p['title'], desc=p['desc']))
json.dump(pmeta, open('pages/meta.json', 'w'), indent=1)
open('pages/preview.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+open('pages/fence-company-reviews.html').read()+'</body></html>')
print({p['slug']: len(open(f'pages/{p["slug"]}.html').read()) for p in out})
