# NovaSignal — report SEO (branch `seo`, 25/11/2026)

Riferimento: handoff "NovaSignal SEO — handoff per Claude Opus" del 25/11/2026. Niente dati Search Console disponibili: nessun numero di traffico, ranking o copertura è riportato qui.

## 1. Audit reale (verificato il 25/11/2026)

Verifiche fatte con un browser reale sul dominio di produzione e sul repository `aurarometours/novabuild`.

| # | Evidenza | URL / file | Severità | Rimedio | Certezza |
|---|---|---|---|---|---|
| 1 | `robots.txt` → 404 | /robots.txt | Alta | Creato, con riga Sitemap | Verificato |
| 2 | `sitemap.xml` → 404 | /sitemap.xml | Alta | Generata da `tools/build.py`, solo URL canoniche 200 | Verificato |
| 3 | Inglese solo via JavaScript sulla stessa URL; `/en` → 404 (`/en/` → 308 → 404) | index.html, setLang() | Alta | `/en` pre-renderizzata in HTML, hreflang reciproci | Verificato |
| 4 | La home passava da sola all'inglese con browser non italiani. Googlebot si presenta in inglese (en-US): rischio che Google indicizzi `/` in inglese | index.html (`navigator.language`) | Alta | La lingua ora dipende solo dall'URL; ai visitatori stranieri compare un invito discreto verso `/en` | Probabile, da confermare con Ispezione URL di Search Console |
| 5 | Nessun canonical, nessun hreflang, nessun dato strutturato | `<head>` | Media | Aggiunti | Verificato |
| 6 | Copia pubblica completa del sito su `aurarometours.github.io/novabuild/` (GitHub Pages dal ramo main): contenuto duplicato, e "aurarometours" nell'URL | GitHub Pages | Media | Canonical verso novasignal.it e reindirizzamento automatico da github.io. **Azione manuale: disattivare Pages** (Settings → Pages) | Verificato |
| 7 | Link "Privacy e cookie" nel footer → /privacy 404 | footer | Media (anche legale) | Pagina da scrivere: servono nome del titolare e P.IVA | Verificato |
| 8 | Title solo di brand; H1 solo creativo ("Costruiamo il segnale del tuo business.") | `<head>`, hero | Media | Title descrittivo; H1 = "Siti web, software, app e automazioni." (titolo della seconda schermata, già visibile); headline creativa invariata | Verificato |
| 9 | Tutto il catalogo servizi stava nella home: nessuna pagina per intenti distinti | — | Alta per l'acquisizione | 4 pagine servizio + 1 caso studio | — |
| 10 | Vecchia versione negli snippet (title "Siti web, App Mobile & SaaS", listino Essenziale/Signature) | cache dei motori; repo `novafront` | Bassa | Si risolve con la nuova scansione; www → apex funziona già | Probabile cache |
| 11 | /favicon.ico → 404 (l'icona c'è via `<link rel=icon>`) | — | Bassa | Facoltativo | Verificato |
| 12 | /signum: 200 con `X-Robots-Tag: noindex, nofollow`, non bloccato da robots.txt | vercel.json | OK | Lasciato così, escluso dalla sitemap | Verificato |
| 13 | LCP mobile in laboratorio ~16 s sulla home (loader + sequenza di fotogrammi). Uguale prima e dopo | index.html | Media (prestazioni) | Da affrontare a parte: il loader copre il primo contenuto | Lab, non dati reali |

## 2. Mappa URL

| URL | Stato | Canonical | hreflang | Sitemap |
|---|---|---|---|---|
| https://novasignal.it/ | 200 | sé stessa | it → /, en → /en, x-default → / | Sì |
| https://novasignal.it/en | 200 (nuova) | sé stessa | come sopra | Sì |
| /servizi/realizzazione-siti-web-roma | 200 (nuova) | sé stessa | — (solo IT) | Sì |
| /servizi/sviluppo-software-su-misura | 200 (nuova) | sé stessa | — | Sì |
| /servizi/sviluppo-web-app | 200 (nuova) | sé stessa | — | Sì |
| /servizi/automazioni-aziendali-ai | 200 (nuova) | sé stessa | — | Sì |
| /lavori/aura-rome-tours | 200 (nuova) | sé stessa | — | Sì |
| /signum, /signum/en | 200 noindex | — | — | No |
| /presentazione | 307 → /signum | — | — | No |
| www.novasignal.it | → novasignal.it | — | — | — |
| /privacy | 404 | — | — | No (finché non c'è la pagina) |
| /en/, /*.html, slash finale | 308 verso la versione senza slash/estensione (Vercel) | — | — | — |

Nota: `?lang=en` sulla home ora porta a `/en`.

## 3. Cosa è cambiato (file)

- `index.html`:
  - head con title, canonical, hreflang, Open Graph completo e JSON-LD (Organization con contatti e catalogo prezzi già visibile in pagina, WebSite, WebPage);
  - H1 descrittivo;
  - pulsante lingua trasformato in link reale (`/en` ↔ `/`), che cambia lingua senza ricaricare e aggiorna indirizzo, title e description;
  - colonna "Servizi" nel footer e link "Leggi il caso studio" su Aura (visibili solo in italiano);
  - fix: l'etichetta "Lettura guidata" andava a capo su telefono.
- `en.html` (nuova, generata): home inglese renderizzata lato server, con canonical, hreflang e JSON-LD propri.
- `servizi/*.html`, `lavori/aura-rome-tours.html` (nuove, generate da `tools/pages.py`): H1, title e description unici, breadcrumb, JSON-LD (WebPage, Service, BreadcrumbList), prezzi coerenti con la home, FAQ, CTA WhatsApp/email, link interni.
- `assets/pages.css`, `assets/pages/*.jpg`: stile delle pagine contenuto (stessi token della home) e immagini da 22–172 KB.
- `robots.txt`, `sitemap.xml`, `tools/build.py`, `.vercelignore`, `README.md`.

Prezzi, claim, CTA, animazioni e design della home sono invariati.

Tutto il testo nuovo usa solo fatti già dichiarati sul sito:
- anteprima gratuita;
- 50% per partire e saldo alla consegna;
- 30 giorni di modifiche;
- dominio e sito intestati al cliente;
- prezzi.

Le altre informazioni nel testo vengono dall'handoff o dallo studio:
- per Aura: booking, Stripe, multilingua, gestione operativa;
- il pannello interno NovaSignal (PostgreSQL + Stripe + notifiche email).

## 4. Test eseguiti

- **Stato HTTP e link:** tutte le nuove URL rispondono 200 su un server locale che imita Vercel (cleanUrls, niente slash finale). I 13 link interni delle pagine nuove funzionano tutti.
- **Contenuto delle pagine:**
  - un solo H1 per pagina;
  - title di 50–60 caratteri;
  - description di 132–159 caratteri;
  - JSON-LD valido (letto senza errori);
  - nessuno scroll orizzontale su 1440 px e su iPhone 14 Pro.
- **Home `/` e `/en`, desktop e mobile:**
  - lingua giusta;
  - un H1 a pagina;
  - cambio lingua in tutte e due le direzioni;
  - ricarica e preferenza ricordata;
  - zero errori JavaScript;
  - nessun testo italiano rimasto visibile in `/en` (controllo automatico).
- **Regressioni sulla home:**
  - lettura guidata fino ai Prezzi, su mobile, desktop e iPad iOS 12 simulato;
  - finestre dei mondi e checkout;
  - transizione verso Lavori;
  - zero errori.
- **Lighthouse** (laboratorio, mobile simulato e desktop):

  | Pagina | Mobile (perf / acc / bp / seo) | Desktop (perf / acc / bp / seo) |
  |---|---|---|
  | Home prima | 67 / 86 / 96 / 100 | — |
  | Home dopo | 66 / 87 / 96 / 100 | 88 / 91 / 96 / 100 |
  | Pagine servizio | 100 / 94 / 96 / 100, LCP 1,4 s | 100 / 94 / 96 / 100, LCP 0,4 s |

  Sono dati di laboratorio, non i Core Web Vitals reali.

## 5. Rollback

- Branch `seo`: per tornare indietro basta non fare il merge, oppure fare il revert del merge commit.
- Le nuove URL possono restare anche in caso di rollback della home: non dipendono da essa.

## 6. Azioni manuali

1. **Search Console** (proprietà Dominio `novasignal.it`):
   - invia `https://novasignal.it/sitemap.xml`;
   - con Ispezione URL richiedi l'indicizzazione di `/`, `/en` e delle 4 pagine servizio;
   - controlla che "URL canonico selezionato da Google" sia quello giusto e che `/` risulti in italiano.
2. **Baseline da salvare oggi**, prima che la sitemap faccia effetto:
   - Rendimento degli ultimi 3 mesi, esportando query, pagine, paesi e dispositivi;
   - Indicizzazione → Pagine;
   - Core Web Vitals.
3. **GitHub:** `aurarometours/novabuild` → Settings → Pages → disattiva.
4. **Privacy:** servono nome e cognome del titolare e P.IVA per scrivere la pagina `/privacy`, oggi linkata e in 404.
5. **Google Business Profile:** solo se l'attività ha i requisiti (sede reale o area servita). Niente indirizzi inventati.
6. **Misurazione:** oggi non c'è nessun analytics sul sito. Per contare i lead organici servono:
   - eventi per i clic su WhatsApp e mailto;
   - eventi per checkout avviato e completato (Stripe, già registrato nel backend);
   - un modo per collegarli alle pagine di ingresso.

   Da decidere quale strumento usare (es. Plausible o GA4 con consenso).

## 7. Prossimi passi (P1/P2, non fatti)

- Versioni inglesi delle pagine servizio (`/en/custom-software-development`, …), con hreflang reciproci.
- Pagina `/servizi/sviluppo-app-mobile`: l'app mobile è in offerta sulla home (mondo "App mobile" e Supernova).
- Pagine settore. Solo quelle per cui ci sono esigenze e progetti reali da raccontare: gioiellerie e oreficerie (molti prospect a Roma), ottici, antiquariato/design. Mai pagine città o settore fotocopia.
- Risorse sui costi (quanto costa un sito, un gestionale), con fasce prese dal listino.
- Caso studio Moruzzi e altri, solo con autorizzazione del cliente.
- Prestazioni home: LCP mobile, cioè il loader che copre il primo contenuto.
- Coerenza dei prezzi: la home mostra ancora "+IVA" e "IVA esclusa". La presentazione usa "+ fee*". Da allineare con una decisione di Riccardo.
- La frase "Clienti in Italia, Europa, Regno Unito, Stati Uniti ed Emirati" va confermata (handoff: verificare i claim).
