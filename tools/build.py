#!/usr/bin/env python3
"""NovaSignal — static build helpers. No build step on Vercel: run this, commit the output.

  python3 tools/build.py

- index.html is the source (Italian). Its JSON-LD is written here.
- en.html   = the same page, pre-rendered in English (served at /en), with the Italian text as data for the in-place switch.
- servizi/*.html, lavori/*.html = content pages, from tools/pages.py
- sitemap.xml with today's date only for files whose content changed.
Needs: python3 + bs4, node (to read the EN dictionary from the page script).
"""
import html, json, re, subprocess, sys, os, datetime, hashlib
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://novasignal.it'
os.chdir(ROOT)

# ---------------------------------------------------------------- structured data
def org():
    return {
        '@type': 'Organization', '@id': SITE + '/#org', 'name': 'NovaSignal', 'url': SITE + '/',
        'logo': SITE + '/assets/brand/mark-512.png', 'image': SITE + '/og-image.jpg',
        'email': 'studio@novasignal.it', 'telephone': '+39 320 689 1014',
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Roma', 'addressCountry': 'IT'},
        'contactPoint': {'@type': 'ContactPoint', 'contactType': 'sales', 'email': 'studio@novasignal.it',
                         'telephone': '+39 320 689 1014', 'availableLanguage': ['Italian', 'English']},
    }

def offers(lang):
    it = lang == 'it'
    P = [('Signal', 1900, 'Sito web su misura, fino a 6 pagine' if it else 'Custom website, up to 6 pages', False),
         ('Nova', 4900, 'Sito con e-commerce o prenotazioni, multilingua' if it else 'Website with e-commerce or booking, multilingual', False),
         ('Supernova', 14000, 'Software, web app e app mobile su misura' if it else 'Custom software, web apps and mobile apps', True)]
    items = []
    for name, price, desc, frm in P:
        spec = {'@type': 'PriceSpecification', 'price': price, 'priceCurrency': 'EUR', 'valueAddedTaxIncluded': False}
        if frm: spec = {'@type': 'PriceSpecification', 'minPrice': price, 'priceCurrency': 'EUR', 'valueAddedTaxIncluded': False}
        items.append({'@type': 'Offer', 'name': name, 'description': desc, 'priceSpecification': spec,
                      'itemOffered': {'@type': 'Service', 'name': name, 'provider': {'@id': SITE + '/#org'}}})
    return {'@type': 'OfferCatalog', 'name': 'Pacchetti NovaSignal' if it else 'NovaSignal packages', 'itemListElement': items}

def ld_home(lang):
    url = SITE + ('/' if lang == 'it' else '/en')
    o = org(); o['hasOfferCatalog'] = offers(lang)
    return {'@context': 'https://schema.org', '@graph': [
        o,
        {'@type': 'WebSite', '@id': SITE + '/#site', 'url': SITE + '/', 'name': 'NovaSignal', 'inLanguage': ['it', 'en'], 'publisher': {'@id': SITE + '/#org'}},
        {'@type': 'WebPage', '@id': url + '#page', 'url': url, 'inLanguage': lang, 'isPartOf': {'@id': SITE + '/#site'}, 'about': {'@id': SITE + '/#org'},
         'name': ('Siti web, software e app su misura a Roma | NovaSignal' if lang == 'it' else 'Custom websites, software and apps from Rome | NovaSignal')}]}

def ld_tag(data):
    return '<script type="application/ld+json" id="ld">' + json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>'

def set_ld(doc, data):
    tag = ld_tag(data)
    if '<!--LDJSON-->' in doc: return doc.replace('<!--LDJSON-->', tag)
    return re.sub(r'<script type="application/ld\+json" id="ld">.*?</script>', lambda m: tag, doc, count=1, flags=re.S)

# ---------------------------------------------------------------- source positions (exact, no re-serialisation)
def offsets(src):
    lines = src.split('\n'); acc = [0]
    for l in lines: acc.append(acc[-1] + len(l) + 1)
    return lambda line, pos: acc[line - 1] + pos

VOID = {'input', 'img', 'br', 'meta', 'link', 'source', 'hr'}
def element_span(src, start):
    """(start, start_tag_end, close_start, end) of the element whose start tag begins at `start`."""
    m = re.compile(r'<([a-zA-Z0-9]+)').match(src, start); name = m.group(1).lower()
    gt = src.index('>', start) + 1
    if name in VOID: return start, gt, gt, gt
    depth, i = 1, gt
    pat = re.compile(r'<(/?)%s\b[^>]*>' % name, re.I)
    while depth:
        t = pat.search(src, i)
        depth += -1 if t.group(1) else 1
        i = t.end()
    return start, gt, t.start(), t.end()

def en_dict(src):
    m = re.search(r'\nconst EN = (\{.*?\n\});', src, re.S)
    out = subprocess.run(['node', '-e', 'process.stdout.write(JSON.stringify(' + m.group(1) + '))'], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)

def build_en(src):
    EN = en_dict(src)
    soup = BeautifulSoup(src, 'html.parser'); off = offsets(src)
    edits, IT = [], {}
    for el in soup.select('[data-i18n]'):
        k = el['data-i18n']; s0 = off(el.sourceline, el.sourcepos)
        a, gt, cs, b = element_span(src, s0)
        inner = src[gt:cs]
        if k not in IT:
            IT[k] = inner if (el.has_attr('data-html') or re.search(r'<\w', EN.get(k, ''))) else el.get_text()
        v = EN.get(k)
        if v is None: continue
        new = v if re.search(r'<\w', v) else html.escape(v, quote=False)
        edits.append((gt, cs, new))
    for el in soup.select('[data-ph]'):
        k = el['data-ph']; IT.setdefault(k, el.get('placeholder', ''))
        if k in EN:
            s0 = off(el.sourceline, el.sourcepos); a, gt, _, _ = element_span(src, s0)
            tag = src[a:gt]; new = re.sub(r'placeholder="[^"]*"', 'placeholder="%s"' % html.escape(EN[k]), tag)
            edits.append((a, gt, new))
    for el in soup.select('[data-only="it"]'):
        s0 = off(el.sourceline, el.sourcepos); a, _, _, b = element_span(src, s0); edits.append((a, b, ''))
    IT['f.err'] = 'Inserisci il tuo nome così sappiamo a chi rispondere.'
    edits.sort(key=lambda e: e[0], reverse=True)
    last = None
    for a, b, new in edits:
        assert last is None or b <= last, 'overlapping edits'
        src = src[:a] + new + src[b:]; last = a
    # head and switch
    rep = [('<html lang="it">', '<html lang="en">'),
           ('<title>Siti web, software e app su misura a Roma | NovaSignal</title>', '<title>Custom websites, software and apps from Rome | NovaSignal</title>'),
           ('<meta name="description" content="NovaSignal progetta e sviluppa siti web, software, app e automazioni su misura. Studio a Roma, clienti in tutto il mondo. Anteprima gratuita prima di pagare.">',
            '<meta name="description" content="NovaSignal designs and builds custom websites, software, apps and automation. Studio in Rome, clients worldwide. Free preview before you pay.">'),
           ('<link rel="canonical" href="https://novasignal.it/">', '<link rel="canonical" href="https://novasignal.it/en">'),
           ('<meta property="og:url" content="https://novasignal.it/">', '<meta property="og:url" content="https://novasignal.it/en">'),
           ('<meta property="og:locale" content="it_IT">\n<meta property="og:locale:alternate" content="en_GB">', '<meta property="og:locale" content="en_GB">\n<meta property="og:locale:alternate" content="it_IT">'),
           ('<meta property="og:description" content="Siti web, software, app e automazioni su misura. Anteprima gratuita prima di pagare.">', '<meta property="og:description" content="Custom websites, software, apps and automation. Free preview before you pay.">'),
           ('<a class="lang" id="langBtn" href="/en" hreflang="en" lang="en" aria-label="Switch to English">EN</a>', '<a class="lang" id="langBtn" href="/" hreflang="it" lang="it" aria-label="Passa all’italiano">IT</a>'),
           ('<a class="skip" href="#main" data-i18n="skip">Vai al contenuto</a>', None)]
    for a, b in rep:
        if b is None: continue
        assert src.count(a) == 1, a[:60]; src = src.replace(a, b)
    src = set_ld(src, ld_home('en'))
    data = '<script>window.__IT_DICT = ' + json.dumps(IT, ensure_ascii=False).replace('</', '<\\/') + ';</script>\n'
    src = src.replace('<script src="assets/js/gsap.min.js"></script>', data + '<script src="assets/js/gsap.min.js"></script>', 1)
    src = src.replace('<!doctype html>', '<!doctype html>\n<!-- generated by tools/build.py from index.html: do not edit by hand -->', 1)
    return src

# ---------------------------------------------------------------- main
def write(path, content):
    old = open(path).read() if os.path.exists(path) else None
    if old != content:
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        open(path, 'w').write(content); print('wrote', path)

def main():
    src = open('index.html').read()
    src = set_ld(src, ld_home('it')); write('index.html', src)
    write('en.html', build_en(src))
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    pages = []
    try:
        import pages as P
        for pg in P.PAGES:
            write(pg['file'], P.render(pg)); pages.append(pg)
    except ImportError:
        pass
    sitemap(pages)

def sitemap(pages):
    today = datetime.date.today().isoformat()
    state_f = 'tools/.lastmod.json'
    state = json.load(open(state_f)) if os.path.exists(state_f) else {}
    urls = [('/', 'index.html', [('it', '/'), ('en', '/en'), ('x-default', '/')]), ('/en', 'en.html', [('it', '/'), ('en', '/en'), ('x-default', '/')])]
    urls += [(p['url'], p['file'], None) for p in pages]
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for url, f, alts in urls:
        h = hashlib.sha1(open(f, 'rb').read()).hexdigest()
        if state.get(f, {}).get('h') != h: state[f] = {'h': h, 'd': today}
        out.append('  <url><loc>%s%s</loc><lastmod>%s</lastmod>' % (SITE, url, state[f]['d']))
        for l, u in alts or []: out.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s%s"/>' % (l, SITE, u))
        out.append('  </url>')
    out.append('</urlset>')
    write('sitemap.xml', '\n'.join(out) + '\n')
    json.dump(state, open(state_f, 'w'), indent=1)

if __name__ == '__main__': main()
