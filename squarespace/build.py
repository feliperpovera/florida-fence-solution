# Builds Squarespace-ready pieces from index.html: head.html (page header injection) + block.html (code block)
import re
B='https://feliperpovera.github.io/florida-fence-solution/'
s=open('index.html').read()
head=s[s.index('<head>')+6:s.index('</head>')]
css=head[head.index('<style>')+7:head.index('</style>')]
ld=''.join(re.findall(r'<script type="application/ld\+json">.*?</script>',head,re.S))
fonts='\n'.join(l for l in head.splitlines() if 'fonts.g' in l)

def scope(css):
    out=[];i=0
    def sel(x):
        parts=[]
        for p in x.split(','):
            p=p.strip()
            if p in(':root','html','body'): parts.append('#ffs')
            elif p.startswith(('html.','.lenis')): continue
            elif p.startswith(':root'): parts.append('#ffs'+p[5:])
            else: parts.append('#ffs '+p)
        return ','.join(parts)
    while i<len(css):
        j=css.find('{',i)
        if j<0: break
        pre=css[i:j].strip()
        if pre.startswith('@media') or pre.startswith('@supports'):
            depth=1;k=j+1
            while depth: depth+= {'{':1,'}':-1}.get(css[k],0);k+=1
            out.append(pre+'{'+scope(css[j+1:k-1])+'}');i=k;continue
        if pre.startswith('@keyframes'):
            depth=1;k=j+1
            while depth: depth+= {'{':1,'}':-1}.get(css[k],0);k+=1
            out.append(css[i:k].strip());i=k;continue
        k=css.index('}',j)
        s2=sel(re.sub(r'/\*.*?\*/','',pre,flags=re.S).strip())
        if s2: out.append(s2+'{'+css[j+1:k]+'}')
        i=k+1
    return '\n'.join(out)

css=scope(css)
css=css.replace('url(img/',f'url({B}img/')
# hide Squarespace chrome on this page, remove its padding
css+='\n#header,.header,#footer-sections,.sqs-announcement-bar-dropzone{display:none!important}\n.page-section .content-wrapper{padding:0!important;max-width:none!important}\n.sqs-block-code{padding:0!important}\n#ffs{position:relative}'
body=s[s.index('<body>')+6:s.index('</body>')]
# drop proposal + its scripts
body=re.sub(r'<!-- =+ PROPOSAL.*?<!-- =+ WEBSITE =+ -->','',body,flags=re.S)
body=re.sub(r'<button id="show-proposal">.*?</button>','',body)
body=re.sub(r'<script src="https://cdn.jsdelivr.net/npm/lenis[^>]*></script>','',body)
js=body[body.index('<script>')+8:body.rindex('</script>')]
body=body[:body.index('<script>')]
js=re.sub(r"const proposal.*?if \(location.search.includes\('site'\)\) show\(false\);",'',js,flags=re.S)
js=re.sub(r"// Lenis.*?\n}\n?",'',js,flags=re.S)
js=js.replace('document.createTreeWalker(document.body','document.createTreeWalker(document.getElementById(\'ffs\')')
body=re.sub(r'(src|href)="img/',rf'\1="{B}img/',body)
js='(function(){'+js+'})();'
open('squarespace/head.html','w').write(f'{fonts}\n{ld}\n<style>\n{css}\n</style>\n')
open('squarespace/block.html','w').write(f'<div id="ffs">\n{body}\n</div>\n<script>{js}</script>\n')
open('squarespace/preview.html','w').write('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+open('squarespace/head.html').read()+'</head><body style="margin:0">'+open('squarespace/block.html').read()+'</body></html>')
