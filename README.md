# NovaSignal — sito

Sito statico, nessuna build: si pubblica così com'è.

## Struttura
- `index.html` — pagina unica (HTML, CSS e JS inclusi)
- `assets/hero/` — 240 fotogrammi della hero (desktop)
- `assets/hero-m/` — 160 fotogrammi della hero (telefono, verticali)
- `assets/video/` — video delle scene; i file `-m` sono le versioni verticali per telefono
- `assets/work/` — screenshot dei lavori
- `assets/js/` — GSAP, ScrollTrigger e Lenis (inclusi, niente CDN)
- `.nojekyll` — fa servire a GitHub Pages i file così come sono

## GitHub Pages
1. Carica il contenuto di questa cartella nella radice del repository (ramo `main`).
2. Settings → Pages → Source: "Deploy from a branch" → `main` / `(root)`.
3. Il sito è su `https://<account>.github.io/<repository>/`.

## Aura Rome Tours nella sezione Lavori
Finché aurarometours.it invia `X-Frame-Options: SAMEORIGIN`, la sua card apre il sito in una nuova scheda.
Per renderla navigabile dentro la card, nel `.htaccess` di aurarometours.it:

    <IfModule mod_headers.c>
      Header always unset X-Frame-Options
      Header always set Content-Security-Policy "frame-ancestors 'self' https://novasignal.it https://www.novasignal.it"
    </IfModule>

poi in `index.html`, nella card di Aura, cambia `data-frame="blocked"` in `data-frame="ok"`.
(Se pubblichi l'anteprima su un dominio github.io, aggiungi anche quell'indirizzo a `frame-ancestors`.)

## Presentazione commerciale
- `signum/index.html` (IT) e `signum/en.html` (EN): un solo link, `/signum`. La lingua segue il telefono di chi apre (italiano → IT, altrimenti EN); il tasto IT/EN la cambia e la ricorda. L'indirizzo resta sempre `/signum`. Il vecchio `/presentazione` rimanda qui.
- `signum/a/`: immagini della presentazione; video e screenshot dei lavori riusano `assets/`
- Header di sicurezza dedicati in `vercel.json` (CSP, niente iframe, noindex)
- `og-image.jpg`: immagine di anteprima quando si condivide il link della home
- La guida per chi presenta è cifrata (AES-GCM): nel codice pubblico c'è solo il testo cifrato

## Compatibilità con Safari vecchi (iOS 12–13)
- `assets/hero-j/` e `assets/hero-m-j/`: fotogrammi JPEG leggeri (uno ogni quattro) usati solo dove WebP non è supportato
- Il CSS ha i fallback per `clamp()`, `inset`, `svh`, `sticky`, `clip-path`, `aspect-ratio`; uno script ricostruisce le spaziature flex dove `gap` non funziona
- Dopo modifiche al CSS, rilancia lo script dei fallback (`css_legacy.py`) e controlla che nel JS non ci siano `?.` o `??`
