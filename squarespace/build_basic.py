# Basic plan: no JS. One code block = <style> + HTML.
import re
head=open('squarespace/head.html').read(); block=open('squarespace/block.html').read()
css=head[head.index('<style>')+7:head.index('</style>')]
ld=''.join(re.findall(r'<script type="application/ld\+json">.*?</script>',head,re.S))
html=block[:block.index('<script>')]
html=html.replace(' reveal','').replace('class="reveal"','')
html=re.sub(r'<span class="lang".*?</span>\s*','',html,flags=re.S)
wa="https://wa.me/17542089268?text=Hi!%20I'd%20like%20a%20free%20fence%20estimate."
card=f'''<div class="quote" id="quote">
        <h2>Free Estimate</h2>
        <p>Tell us about your project. We reply the same day — hablamos español.</p>
        <a class="btn btn-gold qbtn" href="{wa}" target="_blank" rel="noopener">WhatsApp Us →</a>
        <a class="btn btn-dark qbtn" href="tel:+17542089268">Call (754) 208-9268</a>
        <a class="btn qbtn qline" href="mailto:floresfloridafencing@gmail.com?subject=Free%20fence%20estimate">Email Us</a>
        <small>No spam. No obligation. Mon–Sat 8AM–6PM.</small>
      </div>'''
html=re.sub(r'<form class="quote".*?</form>',card,html,flags=re.S)
css=re.sub(r'#ffs \.reveal\{[^}]*\}|#ffs \.reveal\.in\{[^}]*\}','',css)
css+='\n#ffs .qbtn{width:100%;justify-content:center;margin-top:12px}#ffs .qline{border-color:var(--line);color:var(--ink)}'
fonts="@import url('https://fonts.googleapis.com/css2?family=League+Spartan:wght@600;700;800&family=DM+Sans:wght@400;500;700&display=swap');\n"
out=f'<style>\n{fonts}{css}\n</style>\n{ld}\n{html}'
out=re.sub(r'\n\s*\n+','\n',out)
open('squarespace/codeblock-basic.html','w').write(out)
open('squarespace/preview-basic.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+out+'</body></html>')
print(len(out))
# Live site: no unverified review content / ratings
g='https://www.google.com/search?q=Florida+Fence+Solution+Hollywood+FL+reviews'
out=re.sub(r'<!-- DEMO REVIEWS.*?<p class="demo-note">.*?</p>',
  f'<p class="lead" style="margin-bottom:26px">Real reviews from real neighbors across Broward County. See what our customers say on Google.</p><a class="btn btn-gold" href="{g}" target="_blank" rel="noopener">Read our Google reviews →</a>',out,flags=re.S)
out=re.sub(r'<div class="g-score">.*?</div></div>','',out,flags=re.S)
out=out.replace('<span class="stars">★★★★★</span> 5.0 on Google · Family-owned','Family-owned · Hablamos Español')
out=out.replace('<div><b>1–3</b>Day installs</div>','<div><b>Free</b>Estimates</div>')
out=out.replace('Our crew installs in 1–3 days and cleans up after.','Our own crew installs your fence and cleans up after.')
out=out.replace('Most residential fences are installed in 1–3 days once the permit is approved.','Most residential fences take just a few days to install once the permit is approved.')
out=out.replace('"text":"Most residential fences are installed in 1–3 days once the permit is approved."','"text":"Most residential fences take just a few days to install once the permit is approved."')
open('squarespace/codeblock-basic.html','w').write(out)
open('squarespace/preview-basic.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0">'+out+'</body></html>')
print('rev', out.count('class="rev"'), out.count('5.0'), out.count('1–3 d'))
