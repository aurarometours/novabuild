# NovaSignal — content pages. Edit the text here, then run: python3 tools/build.py
# Rule for every claim: it must already be true and stated on the home (prices, preview, 50% / balance,
# 30 days of changes, ownership) or confirmed by the studio. No invented clients, numbers or reviews.
import html, json

SITE = 'https://novasignal.it'
E = lambda s: html.escape(s, quote=True)
WA = 'https://wa.me/393206891014?text='

SECTORS = [('/settori/siti-web-gioiellerie', 'Gioiellerie e orafi'), ('/settori/siti-web-ottici', 'Ottici'), ('/settori/siti-web-antiquariato-design', 'Antiquariato e design')]

SERVICES = [  # (url, short name, one line) — used for related links and the footer
    ('/servizi/realizzazione-siti-web-roma', 'Siti web su misura', 'Siti vetrina, e-commerce e prenotazioni, progettati da zero.'),
    ('/servizi/sviluppo-software-su-misura', 'Software e gestionali', 'Gestionali, pannelli admin e portali clienti su misura.'),
    ('/servizi/sviluppo-web-app', 'Web app e SaaS', 'Piattaforme web con utenti, abbonamenti e pagamenti.'),
    ('/servizi/automazioni-aziendali-ai', 'Automazioni e AI', 'Sito, CRM, email, WhatsApp e calendario che lavorano insieme.'),
    ('/servizi/sviluppo-app-mobile', 'App mobile', 'App iOS e Android, dal prototipo alla pubblicazione sugli store.'),
]

PRICES = {
    'signal': ('Signal', '€1.900', '', 'Il sito su misura che presenta il tuo business come merita: fino a 6 pagine, testi e SEO locale, dominio e hosting il primo anno.'),
    'nova': ('Nova', '€4.900', '', 'Per chi vende online, prenota clienti o parla a più mercati: e-commerce o prenotazioni, multilingua, pagamenti, CRM e calendario.'),
    'supernova': ('Supernova', '€14.000', 'da', 'Software, web app e app mobile costruiti intorno al tuo processo, con pannello admin, database e roadmap evolutiva.'),
    'orbit': ('Orbit', '€490', '/mese', 'SEO continuativa: contenuti, ottimizzazione tecnica e report mensile.'),
    'pulse': ('Pulse', '€590', '/mese', 'Gestione campagne Google e Meta Ads, con report sui risultati.'),
    'care': ('Care', '€79', '/mese', 'Hosting, backup, aggiornamenti e piccole modifiche.'),
}

# hero film per page (by 'img'): the home's world films where they fit, niche films in assets/pages/v-*.mp4
# (src, mobile src or None, legacy 720p src or None, poster)
V = '/assets/video/'; PV = '/assets/pages/'
HERO_VIDEO = {
    'sites':    (V + 'planet-loop.mp4', V + 'planet-m-loop.mp4', None, V + 'planet.jpg'),
    'software': (V + 'corridor.mp4', V + 'corridor-m.mp4', V + 'corridor-l.mp4', V + 'corridor.jpg'),
    'app':      (V + 'grid.mp4', V + 'grid-m.mp4', None, V + 'grid.jpg'),
    'auto':     (V + 'nebula.mp4', V + 'nebula-m.mp4', V + 'nebula-l.mp4', V + 'nebula.jpg'),
}
import os as _os
for _k in ('jewel', 'optic', 'antique', 'webapp', 'cost', 'aura'):
    if _os.path.exists(_os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), 'assets/pages/v-%s.mp4' % _k)):
        HERO_VIDEO[_k] = (PV + 'v-%s.mp4' % _k, None, PV + 'v-%s.mp4' % _k, PV + 'v-%s.jpg' % _k)

def hero_video(pg):
    v = HERO_VIDEO.get(pg['img'])
    if not v or pg.get('legal'): return ''
    src, m, l, poster = v
    return ('<div class="hv%s" aria-hidden="true">' % (' right' if pg['img'] in ('jewel',) else '') + '<video muted playsinline loop preload="none" poster="%s" data-src="%s"%s%s></video></div>'
            % (poster, src, ' data-src-m="%s"' % m if m else '', ' data-src-l="%s"' % l if l else ''))

AURA = {'url': '/lavori/aura-rome-tours', 'img': '/assets/work/aura.jpg', 'name': 'Aura Rome Tours',
        'line': 'Tour privati in golf cart elettrico a Roma: sito, prenotazioni e pagamenti online per un servizio premium.'}

PAGES = [
# ------------------------------------------------------------------------------------------------ siti web
{
 'file': 'servizi/realizzazione-siti-web-roma.html', 'url': '/servizi/realizzazione-siti-web-roma', 'c': 'var(--ember)', 'img': 'sites',
 'title': 'Realizzazione siti web su misura a Roma | NovaSignal',
 'desc': 'Siti vetrina, e-commerce e siti con prenotazioni progettati da zero a Roma. Design su misura, testi e SEO, anteprima gratuita prima di pagare. Da €1.900.',
 'crumb': 'Siti web su misura', 'tag': 'Siti web, e-commerce e brand',
 'h1': 'Realizzazione siti web su misura, a Roma.',
 'lead': 'Progettiamo siti vetrina, e-commerce e siti con prenotazioni partendo da zero: niente template, una struttura pensata per far capire in pochi secondi chi sei e portare il visitatore a scriverti.',
 'service': 'Realizzazione siti web',
 'blocks': [
  ('prose', 'Per chi è', 'Un sito che lavora anche quando lo studio è chiuso.', [
    'Lavoriamo soprattutto con attività che vendono qualità: negozi storici, studi professionali, artigiani, hotel e strutture ricettive, aziende che hanno un prodotto forte ma una presenza online che non lo racconta. Spesso il sito c’è ma è lento, uguale a quello dei concorrenti o fermo da anni; a volte non c’è proprio e tutto passa da Instagram e dal passaparola.',
    'Il nostro lavoro è trasformare quello che rende unica la tua attività in pagine chiare, veloci sul telefono e costruite intorno a un obiettivo preciso: una chiamata, un messaggio WhatsApp, una prenotazione, un acquisto.']),
  ('cards', 'Cosa costruiamo', 'Tre formati, un solo standard.', 'Ogni progetto parte da una prima direzione visiva che vedi prima di pagare.', [
    ('var(--ember)', 'Sito vetrina su misura', 'Fino a 6 pagine disegnate per il tuo brand, con testi scritti per convertire e SEO locale di base.', []),
    ('var(--gold)', 'E-commerce e prenotazioni', 'Catalogo, carrello e pagamenti online, oppure un calendario di prenotazione collegato ai tuoi orari.', []),
    ('var(--aqua)', 'Identità visiva', 'Logo, colori e tipografia quando il brand va costruito o rinnovato insieme al sito.', []),
  ]),
  ('chips', 'Incluso nel lavoro', 'Quello che trovi in ogni sito.', None, ['Design su misura, desktop e mobile', 'Animazioni allo scroll', 'Testi scritti da noi', 'SEO tecnica e locale', 'Tracciamento delle conversioni', 'Dominio e hosting il primo anno', '30 giorni di modifiche dopo il lancio', 'Dominio e sito intestati a te']),
  ('steps', 'Come lavoriamo', 'Dall’idea al lancio in tre settimane.', 'Per un sito Signal servono in media 2–3 settimane dall’anteprima al lancio.', [
    ('Giorni 1–3', 'Anteprima gratuita', 'Ascoltiamo il progetto e ti mostriamo una prima direzione visiva. Paghi solo se ti convince.'),
    ('Giorni 4–10', 'Strategia e contenuti', 'Struttura, testi, obiettivi di conversione. Se non hai materiale, lo prepariamo noi.'),
    ('Giorni 11–18', 'Design su misura', 'Ogni schermata disegnata per il tuo brand, desktop e mobile, con le animazioni già pensate.'),
    ('In parallelo', 'Sviluppo e velocità', 'Codice pulito, caricamento rapido, SEO tecnica e tracciamento delle conversioni.'),
    ('Lancio', 'Online, e non sei solo', 'Dominio, Google Business e 30 giorni di modifiche incluse dopo la pubblicazione.'),
  ]),
  ('price', 'Investimento', 'Prezzi chiari, prima di iniziare.', ['signal', 'nova', 'care']),
  ('case',),
  ('faq', [
    ('Non ho testi né foto. È un problema?', 'No. Scriviamo noi i testi e ti guidiamo su foto e video, oppure usiamo materiale professionale adatto al tuo brand.'),
    ('Come funziona l’anteprima gratuita?', 'Ti mostriamo una prima direzione visiva del progetto prima di qualsiasi pagamento. Se ti convince, versi il 50% e partiamo; il saldo arriva alla consegna.'),
    ('Dominio e sito di chi sono?', 'Tuoi. Dominio, contenuti e sito sono intestati a te, senza vincoli.'),
    ('Lavorate solo a Roma?', 'Lo studio è a Roma, dove incontriamo volentieri i clienti di persona. Lavoriamo anche da remoto, in italiano e in inglese.'),
    ('Perché non un template economico?', 'Perché un template sembra quello che è. Un sito su misura è più veloce, si distingue dai concorrenti ed è costruito per farti contattare.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, vorrei un sito web su misura per la mia attività.',
},
# ------------------------------------------------------------------------------------------------ software
{
 'file': 'servizi/sviluppo-software-su-misura.html', 'url': '/servizi/sviluppo-software-su-misura', 'c': 'var(--gold)', 'img': 'software',
 'title': 'Sviluppo software e gestionali su misura | NovaSignal',
 'desc': 'Gestionali, pannelli admin, portali clienti e database costruiti intorno a come lavori davvero. Studio a Roma, progetti su misura da €14.000.',
 'crumb': 'Software e gestionali', 'tag': 'Software su misura',
 'h1': 'Software e gestionali su misura.',
 'lead': 'Quando il tuo modo di lavorare non entra in un gestionale preconfezionato, il software va costruito intorno a te: clienti, ordini, prenotazioni, pagamenti e report in un unico posto, con le regole della tua azienda.',
 'service': 'Sviluppo software su misura',
 'blocks': [
  ('prose', 'Il problema', 'Fogli Excel, chat e cinque abbonamenti che non si parlano.', [
    'Succede quasi sempre allo stesso modo: l’attività cresce, i dati finiscono sparsi tra fogli di calcolo, email, WhatsApp e strumenti diversi, e ogni giorno qualcuno ricopia a mano le stesse informazioni. Gli errori aumentano, il quadro d’insieme si perde e le decisioni si prendono a intuito.',
    'Un software su misura rimette tutto in fila: <strong>un solo database</strong>, ruoli e permessi per chi ci lavora, i passaggi del tuo processo trasformati in schermate semplici, e i numeri che ti servono sempre aggiornati.']),
  ('cards', 'Cosa costruiamo', 'Strumenti di lavoro, non vetrine.', 'Ogni componente nasce da come lavori oggi, non da un modello standard.', [
    ('var(--gold)', 'Gestionali', 'Clienti, commesse, magazzino, appuntamenti: le tue procedure in un unico sistema.', []),
    ('var(--ember)', 'Pannelli admin', 'Il retro del tuo sito o della tua app, per gestire contenuti, ordini e utenti senza chiamare un tecnico.', []),
    ('var(--aqua)', 'Portali clienti', 'Un’area riservata dove i tuoi clienti vedono documenti, stato dei lavori e pagamenti.', []),
    ('var(--cyan)', 'Database e API', 'Dati strutturati e collegati ai servizi che usi già, invece di copie sparse.', []),
    ('var(--gold)', 'Pagamenti', 'Acconti, saldi e abbonamenti con Stripe, registrati automaticamente nel gestionale.', []),
    ('var(--ember)', 'Dashboard e report', 'I numeri che contano, aggiornati da soli.', []),
  ]),
  ('prose', 'Lo usiamo anche noi', 'Costruito con gli stessi strumenti che usiamo ogni giorno.', [
    'Il pannello con cui NovaSignal gestisce clienti, progetti e pagamenti è un software su misura che abbiamo sviluppato noi: database PostgreSQL, accesso protetto, pagamenti Stripe con conferme automatiche e notifiche via email. È lo stesso approccio che portiamo nei progetti dei clienti.']),
  ('steps', 'Come lavoriamo', 'Prima il processo, poi il codice.', 'Software e app hanno una roadmap dedicata che definiamo insieme.', [
    ('Ascolto', 'Mappa del processo', 'Partiamo da come lavori oggi: chi fa cosa, dove si perde tempo, quali dati servono e a chi.'),
    ('Anteprima', 'Prima direzione', 'Ti mostriamo le schermate principali prima di qualsiasi pagamento. Se ti convince, si parte con il 50%.'),
    ('Roadmap', 'Priorità e fasi', 'Dividiamo il progetto in fasi: prima la parte che ti fa risparmiare più tempo, poi il resto.'),
    ('Sviluppo', 'Rilasci progressivi', 'Lavori su versioni reali man mano che crescono, non su un documento che vedrai tra sei mesi.'),
    ('Dopo', 'Evoluzione', 'Il software cresce con l’azienda: nuove funzioni quando servono, con il piano Care per hosting e aggiornamenti.'),
  ]),
  ('price', 'Investimento', 'Un progetto, un preventivo chiaro.', ['supernova', 'care']),
  ('faq', [
    ('Quanto costa un gestionale su misura?', 'I progetti software partono da €14.000 e il preventivo dipende da quante funzioni, ruoli e integrazioni servono. Lo definiamo dopo l’anteprima, per fasi, così sai sempre cosa stai pagando.'),
    ('Il software di chi è?', 'Tuo. Dati e contenuti restano della tua azienda.'),
    ('Si può collegare a quello che uso già?', 'Sì, quando lo strumento lo permette: pagamenti, email, calendario, fatturazione e altri servizi si collegano tramite le loro API.'),
    ('Quanto tempo serve?', 'Dipende dal perimetro. Definiamo insieme una roadmap a fasi, con una prima versione utilizzabile il prima possibile.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, vorrei parlare di un software su misura per la mia azienda.',
},
# ------------------------------------------------------------------------------------------------ web app
{
 'file': 'servizi/sviluppo-web-app.html', 'url': '/servizi/sviluppo-web-app', 'c': 'var(--aqua)', 'img': 'webapp',
 'title': 'Sviluppo web app e piattaforme SaaS su misura | NovaSignal',
 'desc': 'Web app e piattaforme SaaS con account utente, abbonamenti, pagamenti e pannello admin. Dal prototipo al lancio, con anteprima prima di pagare.',
 'crumb': 'Web app e SaaS', 'tag': 'Web app e SaaS',
 'h1': 'Web app e piattaforme SaaS su misura.',
 'lead': 'Hai un servizio da vendere online in abbonamento, una piattaforma per i tuoi clienti o un’idea da portare sul mercato: la progettiamo e la sviluppiamo dall’interfaccia al database, con pagamenti e pannello di gestione inclusi.',
 'service': 'Sviluppo web app e SaaS',
 'blocks': [
  ('prose', 'Quando serve una web app', 'Più di un sito, senza passare dagli store.', [
    'Una web app si usa dal browser, su computer e telefono, senza installazioni. È la scelta giusta quando i tuoi utenti devono <strong>fare qualcosa</strong>, non solo leggere: registrarsi, prenotare, caricare documenti, gestire un abbonamento, collaborare.',
    'Se il progetto ha bisogno anche di un’app da installare, la affianchiamo con app iOS e Android che usano lo stesso backend.']),
  ('cards', 'Cosa costruiamo', 'Le parti che fanno funzionare una piattaforma.', None, [
    ('var(--aqua)', 'Account e profili', 'Registrazione, accesso, ruoli diversi per clienti, staff e amministratori.', []),
    ('var(--cyan)', 'Abbonamenti e pagamenti', 'Piani mensili o annuali, rinnovi e pagamenti con Stripe.', []),
    ('var(--gold)', 'Pannello admin', 'Utenti, contenuti, ordini e statistiche gestiti da te.', []),
    ('var(--ember)', 'Database e API', 'Un backend solido e documentato, pronto per collegarsi ad altri servizi.', []),
    ('var(--aqua)', 'Interfaccia su misura', 'Progettata come un prodotto: chiara, veloce, coerente con il tuo brand.', []),
    ('var(--cyan)', 'Area clienti', 'Uno spazio riservato per documenti, stato dei lavori e comunicazioni.', []),
  ]),
  ('steps', 'Come lavoriamo', 'Dal prototipo al lancio, a fasi.', None, [
    ('Anteprima', 'Prima direzione', 'Le schermate chiave del prodotto, prima di qualsiasi pagamento.'),
    ('Fase 1', 'Versione essenziale', 'Le funzioni indispensabili per andare online e raccogliere i primi utenti.'),
    ('Fase 2', 'Crescita', 'Nuove funzioni scelte in base a come la piattaforma viene usata davvero.'),
    ('Sempre', 'Hosting e aggiornamenti', 'Infrastruttura, backup e aggiornamenti con il piano Care.'),
  ]),
  ('price', 'Investimento', 'Prezzi chiari, prima di iniziare.', ['supernova', 'care']),
  ('faq', [
    ('Web app o app mobile?', 'Se gli utenti devono soprattutto lavorare da computer o non vuoi passare dagli store, una web app è più rapida da lanciare e aggiornare. Se servono notifiche push, uso offline o presenza sugli store, si affianca un’app iOS e Android.'),
    ('Potete partire da un’idea non ancora definita?', 'Sì. L’anteprima serve proprio a dare forma all’idea prima di investire: vedi le schermate principali e decidi se andare avanti.'),
    ('Come si gestiscono i pagamenti?', 'Con Stripe: pagamenti singoli, abbonamenti, rinnovi e ricevute, collegati al pannello admin.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, vorrei parlare di una web app / piattaforma SaaS.',
},
# ------------------------------------------------------------------------------------------------ automazioni
{
 'file': 'servizi/automazioni-aziendali-ai.html', 'url': '/servizi/automazioni-aziendali-ai', 'c': 'var(--cyan)', 'img': 'auto',
 'title': 'Automazioni aziendali e assistenti AI | NovaSignal',
 'desc': 'Colleghiamo sito, CRM, email, WhatsApp e calendario: lead qualificati, preventivi e report automatici, assistenti AI. Studio a Roma.',
 'crumb': 'Automazioni e AI', 'tag': 'Automazioni e AI',
 'h1': 'Automazioni aziendali e assistenti AI.',
 'lead': 'Meno lavoro ripetitivo, più tempo per vendere. Colleghiamo sito, CRM, email, WhatsApp e calendario perché le richieste arrivino già qualificate, i preventivi partano da soli e i report non vadano più compilati a mano.',
 'service': 'Automazioni aziendali e AI',
 'blocks': [
  ('prose', 'Dove si perde tempo', 'Le stesse operazioni, ogni giorno.', [
    'Rispondere alle stesse domande, copiare i dati di un contatto dal sito al gestionale, ricordarsi di richiamare, preparare a mano preventivi e riepiloghi: sono attività necessarie, ma non richiedono una persona.',
    'Un’automazione ben fatta le prende in carico in silenzio e lascia al tuo team le decisioni e le relazioni. Gli assistenti AI aiutano dove serve linguaggio: rispondere alle richieste frequenti, riassumere, smistare.']),
  ('cards', 'Cosa automatizziamo', 'Esempi concreti.', None, [
    ('var(--cyan)', 'Lead e CRM', 'Le richieste dal sito entrano nel CRM con i dati giusti e chi deve seguirle riceve un avviso.', []),
    ('var(--aqua)', 'WhatsApp ed email', 'Messaggi di conferma, promemoria e follow-up che partono al momento giusto.', []),
    ('var(--gold)', 'Preventivi e documenti', 'Bozze di preventivo e riepiloghi generati dai dati che hai già.', []),
    ('var(--ember)', 'Calendario', 'Appuntamenti e prenotazioni sincronizzati, senza doppie prenotazioni.', []),
    ('var(--cyan)', 'Assistenti AI', 'Risposte alle domande frequenti e smistamento delle richieste, con il tuo tono.', []),
    ('var(--aqua)', 'Report', 'I numeri della settimana raccolti e inviati da soli.', []),
  ]),
  ('steps', 'Come lavoriamo', 'Si parte da un flusso, non da tutto.', None, [
    ('Analisi', 'Il flusso che costa di più', 'Individuiamo l’attività ripetitiva che oggi ti fa perdere più tempo.'),
    ('Anteprima', 'Come funzionerà', 'Ti mostriamo il flusso automatizzato prima di qualsiasi pagamento.'),
    ('Messa in opera', 'Collegamenti e test', 'Colleghiamo gli strumenti, testiamo con casi reali e ti lasciamo il controllo.'),
    ('Poi', 'Il flusso successivo', 'Quando il primo funziona, passiamo al successivo.'),
  ]),
  ('price', 'Investimento', 'Progetto o piano mensile.', ['supernova', 'orbit', 'pulse']),
  ('faq', [
    ('Serve cambiare gli strumenti che uso?', 'Di solito no: colleghiamo quelli che hai già, quando offrono un modo per farlo. Se uno strumento non lo permette, te lo diciamo prima.'),
    ('L’AI risponde al posto mio ai clienti?', 'Solo dove lo decidi tu e con regole chiare. Per le richieste importanti l’assistente raccoglie le informazioni e le passa a una persona.'),
    ('Quanto costa?', 'Dipende da quanti strumenti vanno collegati. I progetti su misura rientrano in Supernova; per SEO e campagne ci sono i piani mensili Orbit e Pulse.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, vorrei automatizzare alcune attività della mia azienda.',
},
# ------------------------------------------------------------------------------------------------ case study
{
 'file': 'lavori/aura-rome-tours.html', 'url': '/lavori/aura-rome-tours', 'c': 'var(--ember)', 'img': 'aura', 'case': True,
 'title': 'Caso studio Aura Rome Tours: sito e prenotazioni | NovaSignal',
 'desc': 'Come abbiamo costruito il sito di Aura Rome Tours, tour privati in golf cart elettrico a Roma: frontend e backend, prenotazioni, pagamenti Stripe, multilingua.',
 'crumb': 'Aura Rome Tours', 'tag': 'Caso studio',
 'h1': 'Aura Rome Tours: un servizio premium che si prenota online.',
 'lead': 'Tour privati in golf cart elettrico a Roma. Il sito doveva trasmettere l’esperienza prima ancora di raccontarla e portare il visitatore, in qualsiasi lingua, fino alla prenotazione e al pagamento.',
 'service': None,
 'blocks': [
  ('shot',),
  ('prose', 'La sfida', 'Vendere un’esperienza, non un giro turistico.', [
    'Aura propone tour privati per piccoli gruppi, con un posizionamento premium in un mercato pieno di offerte simili. Le richieste arrivano da viaggiatori di tutto il mondo, spesso dal telefono e poco prima della partenza: il sito deve convincere in fretta, in più lingue, e chiudere la prenotazione senza passaggi inutili.']),
  ('cards', 'Cosa abbiamo costruito', 'Frontend, backend e gestione.', None, [
    ('var(--ember)', 'Sito e brand', 'Atmosfera cinematografica e un percorso chiaro fino alla richiesta.', []),
    ('var(--gold)', 'Prenotazioni', 'Sistema di prenotazione collegato al database.', []),
    ('var(--aqua)', 'Pagamenti Stripe', 'Pagamento online in fase di prenotazione.', []),
    ('var(--cyan)', 'Multilingua', 'Contenuti per i visitatori internazionali.', []),
    ('var(--ember)', 'Gestione operativa', 'Strumenti interni per organizzare i tour e i driver.', []),
    ('var(--gold)', 'Acquisizione diretta', 'Prenotazioni che arrivano dal sito, senza intermediari.', []),
  ]),
  ('prose', 'Come funziona', 'Un unico sistema, dal primo clic al tour.', [
    'Il cliente sceglie il tour, prenota e paga online; lo staff ritrova prenotazioni e pagamenti nello stesso sistema, senza passare da intermediari. È anche il modello del nostro pacchetto Nova: sito su misura, prenotazioni, pagamenti e più lingue in un solo progetto.']),
  ('visit',),
 ],
 'wa': 'Ciao NovaSignal, ho visto il caso Aura Rome Tours e vorrei qualcosa di simile.',
},

# ------------------------------------------------------------------------------------------------ app mobile
{
 'file': 'servizi/sviluppo-app-mobile.html', 'url': '/servizi/sviluppo-app-mobile', 'c': 'var(--aqua)', 'img': 'app',
 'title': 'Sviluppo app mobile iOS e Android su misura | NovaSignal',
 'desc': 'App iOS e Android dal concept alla pubblicazione sugli store: prenotazioni, fidelizzazione, strumenti interni per il team. Anteprima prima di pagare.',
 'crumb': 'App mobile', 'tag': 'App mobile',
 'h1': 'Sviluppo app mobile iOS e Android.',
 'lead': 'App da installare per i tuoi clienti o per il tuo team: prenotazioni, fidelizzazione, notifiche, strumenti di lavoro. Le progettiamo, le sviluppiamo e le pubblichiamo sugli store.',
 'service': 'Sviluppo app mobile',
 'blocks': [
  ('prose', 'Quando serve un’app', 'Quando il cliente deve tornare, non solo trovarti.', [
    'Un sito si cerca; un’app resta sul telefono. Ha senso quando i tuoi clienti fanno qualcosa <strong>spesso</strong>: prenotano, accumulano punti, ricevono avvisi, ricomprano. Oppure quando il tuo team lavora in movimento e ha bisogno di uno strumento sempre in tasca.',
    'Se l’obiettivo è farsi trovare e ricevere richieste, spesso basta un buon sito o una web app: te lo diciamo prima, non dopo.']),
  ('cards', 'Cosa costruiamo', 'Dall’idea allo store.', None, [
    ('var(--aqua)', 'iOS e Android', 'Un’unica app per entrambe le piattaforme, con lo stesso backend del tuo sito o gestionale.', []),
    ('var(--cyan)', 'UX e prototipo', 'Le schermate principali disegnate e provate prima di scrivere il codice.', []),
    ('var(--gold)', 'Notifiche push', 'Promemoria, offerte e aggiornamenti che arrivano al momento giusto.', []),
    ('var(--ember)', 'Login e profili', 'Account cliente, storico, preferenze e pagamenti.', []),
    ('var(--aqua)', 'Pubblicazione store', 'Preparazione e invio su App Store e Google Play.', []),
    ('var(--cyan)', 'Manutenzione', 'Aggiornamenti per le nuove versioni di iOS e Android.', []),
  ]),
  ('steps', 'Come lavoriamo', 'Prima il prototipo, poi il codice.', None, [
    ('Anteprima', 'Prima direzione', 'Le schermate chiave dell’app, prima di qualsiasi pagamento.'),
    ('Prototipo', 'Si prova sul telefono', 'Un prototipo navigabile per verificare il percorso prima dello sviluppo.'),
    ('Sviluppo', 'Versioni di prova', 'Lavori su build reali installate sul telefono, non su immagini.'),
    ('Store', 'Pubblicazione', 'Gestiamo la preparazione e l’invio agli store.'),
  ]),
  ('price', 'Investimento', 'Prezzi chiari, prima di iniziare.', ['supernova', 'care']),
  ('faq', [
    ('Meglio un’app o una web app?', 'Se servono notifiche push, uso frequente o presenza sugli store, un’app. Se gli utenti lavorano soprattutto da computer o vuoi lanciare in fretta, una web app. Spesso si parte dalla web app e si aggiunge l’app dopo.'),
    ('L’app è mia?', 'Sì. L’app viene pubblicata a nome della tua azienda e i dati restano tuoi.'),
    ('Quanto costa?', 'I progetti app rientrano in Supernova, da €14.000. Il preventivo dipende da funzioni e integrazioni e lo definiamo dopo l’anteprima, a fasi.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, vorrei parlare di un’app mobile.',
},
# ------------------------------------------------------------------------------------------------ settore: gioiellerie
{
 'file': 'settori/siti-web-gioiellerie.html', 'url': '/settori/siti-web-gioiellerie', 'c': 'var(--gold)', 'img': 'jewel',
 'parent': ('Siti web', '/servizi/realizzazione-siti-web-roma'),
 'title': 'Siti web per gioiellerie e orafi a Roma | NovaSignal',
 'desc': 'Siti per gioiellerie, orafi e laboratori: collezioni sempre aggiornate, richieste su WhatsApp, appuntamenti in negozio, inglese per i turisti. Da €1.900.',
 'crumb': 'Gioiellerie e orafi', 'tag': 'Per gioiellerie e orafi',
 'h1': 'Siti web per gioiellerie e orafi.',
 'lead': 'Un gioiello si sceglie con calma e si compra di persona. Il sito deve fare una cosa sola, bene: far innamorare delle tue creazioni e portare il cliente in negozio, o a scriverti.',
 'service': 'Siti web per gioiellerie',
 'blocks': [
  ('prose', 'Cosa vediamo nei negozi', 'Clienti fedeli, creazioni bellissime, sito fermo.', [
    'Visitiamo spesso gioiellerie e laboratori orafi, soprattutto a Roma. La storia si ripete: il lavoro è eccellente, Instagram è curato, ma il sito è vecchio, lento, a volte proprio offline, e chi cerca su Google un regalo importante finisce da qualcun altro.',
    'Vendere oro e preziosi online con carrello e spedizioni è complicato e spesso non serve. Serve invece una <strong>vetrina all’altezza del banco</strong>: le collezioni fotografate bene, la storia del laboratorio, e un modo immediato per chiedere informazioni o fissare un appuntamento.']),
  ('cards', 'Cosa mettiamo nel sito', 'Pensato per come si compra un gioiello.', None, [
    ('var(--gold)', 'Collezioni e creazioni', 'Schede per i pezzi e le linee, facili da aggiornare quando arrivano novità.', []),
    ('var(--ember)', 'Richieste su WhatsApp', 'Ogni pezzo ha il suo pulsante: il cliente ti scrive già sapendo cosa vuole.', []),
    ('var(--aqua)', 'Appuntamento in negozio', 'Per anelli di fidanzamento, su misura e riparazioni, la richiesta arriva con data e motivo.', []),
    ('var(--cyan)', 'Storia e laboratorio', 'Generazioni, mani, materiali: quello che giustifica il prezzo e non si copia.', []),
    ('var(--gold)', 'Inglese incluso', 'Per i turisti che passano davanti alla vetrina e cercano dal telefono.', []),
    ('var(--ember)', 'Google e mappe', 'SEO locale e scheda Google curate, per chi cerca “gioielleria” nella tua zona.', []),
  ]),
  ('price', 'Investimento', 'Una vetrina, non un abbonamento.', ['signal', 'nova', 'care']),
  ('faq', [
    ('Serve un e-commerce?', 'Di solito no: per i gioielli funziona meglio una vetrina curata con richieste dirette e appuntamenti. Se vuoi vendere online alcune linee, il pacchetto Nova include l’e-commerce.'),
    ('Chi aggiorna le nuove creazioni?', 'Puoi farlo tu, oppure ce ne occupiamo noi: ci mandi le foto e le pubblichiamo.'),
    ('Ho poche foto professionali.', 'Ti guidiamo su cosa fotografare e come; dove serve usiamo materiale adatto al tuo brand.'),
    ('Lavorate solo a Roma?', 'Siamo a Roma e passiamo volentieri in negozio. Lavoriamo anche da remoto in tutta Italia.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, ho una gioielleria e vorrei un sito nuovo.',
},
# ------------------------------------------------------------------------------------------------ settore: ottici
{
 'file': 'settori/siti-web-ottici.html', 'url': '/settori/siti-web-ottici', 'c': 'var(--cyan)', 'img': 'optic',
 'parent': ('Siti web', '/servizi/realizzazione-siti-web-roma'),
 'title': 'Siti web per ottici e negozi di occhiali | NovaSignal',
 'desc': 'Siti per ottici: il tuo modo di consigliare la montatura, le marche, gli esami della vista e un modo immediato per prenotare in negozio. Da €1.900.',
 'crumb': 'Ottici', 'tag': 'Per ottici',
 'h1': 'Siti web per ottici.',
 'lead': 'Gli occhiali si vendono con la consulenza: si prova, si confronta, ci si fida di chi ti consiglia. Il sito deve raccontare proprio questo e portare il cliente a sedersi al tuo tavolo.',
 'service': 'Siti web per ottici',
 'blocks': [
  ('prose', 'Il punto', 'Non competere con i siti che vendono montature online.', [
    'Le grandi catene e i portali vendono montature a catalogo. Un ottico indipendente vince su un altro terreno: <strong>esperienza, consiglio, assistenza</strong>, spesso una storia di famiglia. Un sito generico, con una galleria di marche, butta via questo vantaggio.',
    'Il nostro primo cliente NovaSignal è proprio un’ottica storica di Roma: una landing che racconta il metodo del titolare e porta i clienti in negozio, invece di un catalogo che nessuno sfoglia.']),
  ('cards', 'Cosa mettiamo nel sito', 'Quello che serve davvero a un ottico.', None, [
    ('var(--cyan)', 'Il tuo metodo', 'Come scegli con il cliente la montatura giusta: è il motivo per cui viene da te.', []),
    ('var(--aqua)', 'Prenotazione in negozio', 'Richiesta di appuntamento per consulenza, esame della vista o ritiro.', []),
    ('var(--gold)', 'Marche e selezione', 'Le linee che tratti, presentate con gusto, senza trasformare il sito in un catalogo.', []),
    ('var(--ember)', 'Storia del negozio', 'Generazioni, esperienza, il quartiere: la fiducia si costruisce qui.', []),
    ('var(--cyan)', 'WhatsApp e telefono', 'Un tocco per chiamarti o scriverti dal telefono.', []),
    ('var(--aqua)', 'Google e mappe', 'SEO locale e scheda Google per chi cerca “ottico” vicino a sé.', []),
  ]),
  ('price', 'Investimento', 'Prezzi chiari, prima di iniziare.', ['signal', 'care']),
  ('faq', [
    ('Posso vendere occhiali da sole online?', 'Sì, con il pacchetto Nova che include l’e-commerce. Per molti ottici però conviene partire da una vetrina che porta clienti in negozio.'),
    ('Quanto tempo serve?', 'Per un sito Signal servono in media 2–3 settimane dall’anteprima al lancio.'),
    ('Dominio e sito di chi sono?', 'Tuoi. Dominio, contenuti e sito sono intestati a te, senza vincoli.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, ho un negozio di ottica e vorrei un sito.',
},
# ------------------------------------------------------------------------------------------------ settore: antiquariato
{
 'file': 'settori/siti-web-antiquariato-design.html', 'url': '/settori/siti-web-antiquariato-design', 'c': 'var(--ember)', 'img': 'antique',
 'parent': ('Siti web', '/servizi/realizzazione-siti-web-roma'),
 'title': 'Siti web per antiquari e gallerie di design | NovaSignal',
 'desc': 'Siti con catalogo per antiquari, gallerie e negozi di design del Novecento: pezzi sempre aggiornati, inglese per i compratori esteri, richieste dirette.',
 'crumb': 'Antiquariato e design', 'tag': 'Per antiquari e gallerie',
 'h1': 'Siti web per antiquari e gallerie di design.',
 'lead': 'Ogni pezzo è unico, il compratore può essere a Milano come a Londra o New York. Il sito diventa il tuo catalogo nel mondo: pezzi raccontati bene, in inglese, con una richiesta diretta a te.',
 'service': 'Siti web per antiquari',
 'blocks': [
  ('prose', 'Il problema', 'I pezzi migliori finiscono sui marketplace, a nome di altri.', [
    'Molti antiquari e negozi di design vendono attraverso marketplace internazionali: funzionano, ma il cliente resta del portale, le commissioni pesano e il tuo nome passa in secondo piano.',
    'Un sito con <strong>catalogo proprio</strong> costruisce il tuo marchio: i collezionisti ti trovano su Google, vedono tutto quello che hai, e ti scrivono direttamente. I marketplace restano un canale in più, non l’unico.']),
  ('cards', 'Cosa mettiamo nel sito', 'Un catalogo, non una vetrina statica.', None, [
    ('var(--ember)', 'Catalogo dei pezzi', 'Schede con foto, epoca, designer, materiali e misure, facili da aggiornare.', []),
    ('var(--gold)', 'Inglese per l’estero', 'Testi pensati per i compratori internazionali, non tradotti parola per parola.', []),
    ('var(--aqua)', 'Richiesta per pezzo', 'Il cliente chiede prezzo, spedizione o disponibilità del singolo oggetto.', []),
    ('var(--cyan)', 'Vendi e fai valutare', 'Una pagina per chi vuole proporti un pezzo o chiedere una valutazione.', []),
    ('var(--ember)', 'SEO per nicchie', 'Pagine pensate per le ricerche di designer, epoche e categorie che tratti.', []),
    ('var(--gold)', 'Identità', 'Logotipo e immagine coordinata, quando il marchio va rinnovato.', []),
  ]),
  ('price', 'Investimento', 'Prezzi chiari, prima di iniziare.', ['nova', 'signal', 'care']),
  ('faq', [
    ('Chi carica i nuovi arrivi?', 'Puoi farlo tu, oppure ce ne occupiamo noi con un pacchetto di caricamenti annuale.'),
    ('Si può vendere online?', 'Sì, con e-commerce e pagamenti nel pacchetto Nova. Per i pezzi importanti molti preferiscono la richiesta diretta.'),
    ('Posso tenere i marketplace?', 'Certo. Il sito non li sostituisce: ti dà un canale tuo, con il tuo nome.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, ho un negozio di antiquariato/design e vorrei un sito con catalogo.',
},
# ------------------------------------------------------------------------------------------------ risorsa: costi
{
 'file': 'risorse/quanto-costa-un-sito-web.html', 'url': '/risorse/quanto-costa-un-sito-web', 'c': 'var(--gold)', 'img': 'cost',
 'parent': ('Prezzi', '/#prezzi'),
 'title': 'Quanto costa un sito web su misura nel 2026? | NovaSignal',
 'desc': 'Cosa determina il prezzo di un sito web su misura, cosa deve essere incluso e quanto costano i nostri pacchetti, con esempi concreti. Prezzi chiari.',
 'crumb': 'Quanto costa un sito web', 'tag': 'Guida ai prezzi',
 'h1': 'Quanto costa un sito web su misura?',
 'lead': 'Risposta breve: dipende da cosa deve fare il sito. Risposta utile: ecco cosa sposta il prezzo, cosa deve essere sempre incluso e quanto costa da noi, senza asterischi nascosti.',
 'service': None,
 'blocks': [
  ('prose', 'Cosa sposta il prezzo', 'Non il numero di pagine: quello che il sito deve fare.', [
    'Il costo di un sito su misura dipende soprattutto da <strong>tre cose</strong>: quante funzioni deve avere (una vetrina che porta contatti è diversa da un sito che vende, prenota o gestisce clienti), quanti contenuti vanno creati (testi, foto, traduzioni) e quanto deve essere curato il design (un modello adattato contro schermate disegnate apposta, con animazioni).',
    'Il numero di pagine conta meno di quanto si pensi. Sei pagine scritte e disegnate bene valgono più di trenta pagine vuote.']),
  ('table', 'Esempi', 'Cosa serve, e quanto costa da noi.', 'Prezzi IVA esclusa, dal nostro listino.', ['Se ti serve…', 'Pacchetto', 'Prezzo'], [
    ('Presentare l’attività e ricevere contatti', 'Signal', '€1.900'),
    ('Vendere online, prenotare clienti o parlare a più mercati', 'Nova', '€4.900'),
    ('Software, web app o app mobile intorno al tuo processo', 'Supernova', 'da €14.000'),
    ('Hosting, backup, aggiornamenti e piccole modifiche', 'Care', '€79/mese'),
    ('SEO continuativa con report mensile', 'Orbit', '€490/mese'),
  ], 'Tutti i dettagli di ogni pacchetto sono nella <a href="/#prezzi">sezione prezzi</a>.'),
  ('chips', 'Sempre incluso', 'Quello che un sito professionale deve avere, a qualsiasi prezzo.', 'Se un preventivo non lo dice, chiedilo.', ['Dominio intestato a te', 'Versione mobile curata', 'Velocità di caricamento', 'SEO tecnica di base', 'Testi scritti per convertire', 'Modo chiaro per contattarti', 'Modifiche dopo il lancio', 'Nessun vincolo per cambiare fornitore']),
  ('prose', 'Da sapere', 'Le domande da fare prima di firmare.', [
    '<strong>Di chi è il dominio?</strong> Deve essere intestato a te. Se è intestato all’agenzia, cambiare fornitore diventa difficile.',
    '<strong>Cosa costa ogni anno?</strong> Dominio e hosting hanno un costo annuale: fatti dire quale, e cosa include.',
    '<strong>Chi scrive i testi?</strong> Un sito senza testi pensati per i tuoi clienti è una vetrina vuota. Da noi sono inclusi.',
    '<strong>Posso vederlo prima di pagare?</strong> Da noi sì: l’anteprima gratuita ti mostra la direzione visiva prima di qualsiasi pagamento.']),
  ('faq', [
    ('Perché non un sito da poche centinaia di euro?', 'Un template economico può bastare per esserci. Un sito su misura è costruito per farti contattare: testi, struttura e velocità pensati per il tuo cliente.'),
    ('Come si paga?', 'Anteprima gratuita, poi 50% per partire e saldo alla consegna.'),
    ('Quanto tempo serve?', 'Per un sito Signal servono in media 2–3 settimane dall’anteprima al lancio.'),
  ]),
 ],
 'wa': 'Ciao NovaSignal, vorrei un preventivo per un sito.',
},

# ------------------------------------------------------------------------------------------------ privacy
{
 'file': 'privacy.html', 'url': '/privacy', 'c': 'var(--cyan)', 'img': 'optic', 'legal': True,
 'parent': ('Studio', '/'),
 'title': 'Privacy e cookie | NovaSignal',
 'desc': 'Come NovaSignal tratta i dati personali di chi visita novasignal.it, ci contatta o acquista un servizio, e quali cookie e tecnologie usa il sito.',
 'crumb': 'Privacy e cookie', 'tag': 'Informativa ai sensi degli artt. 13–14 del Regolamento UE 2016/679',
 'h1': 'Privacy e cookie.',
 'lead': 'Ultimo aggiornamento: 25 novembre 2026.',
 'service': None,
 'blocks': [
  ('legal', [
   ('Titolare del trattamento', ['NovaSignal di Riccardo El Ghendy, P.IVA 17596721005, Roma (Italia). Per qualsiasi richiesta sui tuoi dati: <a href="mailto:studio@novasignal.it">studio@novasignal.it</a>.']),
   ('Quali dati trattiamo e perché', [
     '<strong>Navigazione.</strong> Quando visiti il sito, il servizio di hosting registra dati tecnici come indirizzo IP, browser, pagina richiesta e orario. Servono a far funzionare il sito e a proteggerlo da abusi (legittimo interesse, art. 6.1.f GDPR).',
     '<strong>Contatti.</strong> Se ci scrivi tramite WhatsApp, email o il modulo del sito (che apre WhatsApp con il messaggio già pronto), trattiamo i dati che ci mandi — nome, azienda, recapiti e contenuto del messaggio — per risponderti e preparare una proposta (misure precontrattuali, art. 6.1.b).',
     '<strong>Acquisti.</strong> Se acquisti un servizio sul sito, il pagamento avviene tramite Stripe: i dati della carta li tratta Stripe e non arrivano a noi. Noi riceviamo nome, email, telefono, dati di fatturazione ed eventuale partita IVA, e li conserviamo nel nostro gestionale per eseguire il contratto e rispettare gli obblighi fiscali e contabili (art. 6.1.b e 6.1.c).',
     'Non usiamo i tuoi dati per profilazione né li vendiamo a terzi.']),
   ('Chi riceve i dati', [
     'Usiamo fornitori che trattano dati per nostro conto, ciascuno per la parte che gli compete: Vercel (hosting del sito), Stripe (pagamenti), Railway (server e database del gestionale), Resend (invio delle email di servizio), Google (caratteri tipografici del sito, caricati dai server di Google Fonts), Meta/WhatsApp (se scegli di scriverci su WhatsApp).',
     'Alcuni di questi fornitori hanno sede negli Stati Uniti: il trasferimento avviene sulla base dell’EU-US Data Privacy Framework o delle clausole contrattuali standard approvate dalla Commissione europea.']),
   ('Per quanto tempo', [
     'I dati tecnici di navigazione per il tempo previsto dal fornitore di hosting per sicurezza e diagnosi. I messaggi di contatto per il tempo necessario a gestire la richiesta e fino a 24 mesi dall’ultimo contatto. I dati di acquisto e fatturazione per 10 anni, come richiesto dalla legge.']),
   ('Cookie e tecnologie simili', [
     'Il sito <strong>non usa cookie di profilazione né strumenti di analisi o pubblicità</strong>, quindi non ti chiede il consenso con un banner.',
     'Usa solo memorie tecniche nel tuo browser (localStorage) per ricordare la lingua che hai scelto e la velocità della lettura guidata. Quando apri il pagamento, Stripe può impostare cookie tecnici necessari a completare il pagamento in sicurezza e a prevenire frodi. Se apri l’anteprima di un sito di un nostro cliente, quel sito può usare i propri cookie, secondo la sua informativa.']),
   ('I tuoi diritti', [
     'Puoi chiedere in qualsiasi momento accesso, rettifica, cancellazione, limitazione, portabilità dei tuoi dati o opporti al trattamento (artt. 15–22 GDPR), scrivendo a <a href="mailto:studio@novasignal.it">studio@novasignal.it</a>. Hai anche il diritto di presentare reclamo al Garante per la protezione dei dati personali (<a href="https://www.garanteprivacy.it" target="_blank" rel="noopener">garanteprivacy.it</a>).']),
   ('Modifiche', ['Se cambia il modo in cui trattiamo i dati aggiorniamo questa pagina e la data in alto.']),
  ]),
 ],
 'wa': 'Ciao NovaSignal, ho una domanda sulla privacy.',
},
]


# ================================================================================================ render
def parent(pg):
    return pg.get('parent') or (('Lavori', '/#lavori') if pg.get('case') else ('Servizi', '/#servizi'))

def ld(pg):
    url = SITE + pg['url']
    crumbs = {'@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': 1, 'name': 'NovaSignal', 'item': SITE + '/'},
        {'@type': 'ListItem', 'position': 2, 'name': parent(pg)[0], 'item': SITE + parent(pg)[1]},
        {'@type': 'ListItem', 'position': 3, 'name': pg['crumb'], 'item': url}]}
    page = {'@type': 'WebPage', '@id': url + '#page', 'url': url, 'name': pg['title'], 'description': pg['desc'], 'inLanguage': 'it',
            'isPartOf': {'@id': SITE + '/#site'}, 'breadcrumb': crumbs}
    graph = [page]
    if pg.get('service'):
        graph.append({'@type': 'Service', '@id': url + '#service', 'name': pg['service'], 'serviceType': pg['service'], 'description': pg['desc'],
                      'provider': {'@type': 'Organization', '@id': SITE + '/#org', 'name': 'NovaSignal', 'url': SITE + '/'},
                      'areaServed': {'@type': 'Country', 'name': 'Italia'}, 'url': url})
    return '<script type="application/ld+json">' + json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '</script>'

def sec_head(eyebrow, h, p=None, c=None):
    t = '<div class="sec-h reveal"><div><p class="tag"><i%s></i>%s</p><h2>%s</h2></div>' % (' style="--c:%s"' % c if c else '', E(eyebrow), E(h))
    return t + ('<p>%s</p></div>' % E(p) if p else '<span></span></div>')

def block(b, pg):
    k = b[0]
    if k == 'prose':
        _, ey, h, paras = b
        return '<section class="sec"><div class="wrap">%s<div class="prose reveal">%s</div></div></section>' % (sec_head(ey, h, c=pg['c']), ''.join('<p>%s</p>' % p for p in paras))
    if k == 'cards':
        _, ey, h, p, cards = b
        cls = 'grid two' if len(cards) in (2, 4) else 'grid'
        body = ''.join('<div class="card" style="--c:%s"><h3>%s</h3><p>%s</p></div>' % (c, E(t), E(d)) for c, t, d, _ in cards)
        return '<section class="sec"><div class="wrap">%s<div class="%s reveal">%s</div></div></section>' % (sec_head(ey, h, p, pg['c']), cls, body)
    if k == 'chips':
        _, ey, h, p, items = b
        return '<section class="sec"><div class="wrap">%s<ul class="chips reveal">%s</ul></div></section>' % (sec_head(ey, h, p, pg['c']), ''.join('<li>%s</li>' % E(i) for i in items))
    if k == 'steps':
        _, ey, h, p, steps = b
        body = ''.join('<li><b>%s</b><div><h3>%s</h3><p>%s</p></div></li>' % (E(a), E(t), E(d)) for a, t, d in steps)
        return '<section class="sec"><div class="wrap">%s<ol class="steps reveal">%s</ol></div></section>' % (sec_head(ey, h, p, pg['c']), body)
    if k == 'price':
        _, ey, h, keys = b
        cards = []
        for key in keys:
            n, v, unit, d = PRICES[key]
            pre = '<span class="pre">da</span>' if unit == 'da' else ''
            suf = '<small>%s</small>' % E(unit) if unit.startswith('/') else ''
            cards.append('<div class="pc%s"><div class="n">%s</div><div class="v">%s%s%s</div><p>%s</p></div>' % (' hl' if key in ('nova', 'supernova') else '', n, pre, v, suf, E(d)))
        note = 'Prezzi IVA esclusa. Anteprima gratuita, poi 50% per partire e saldo alla consegna. <a href="/#prezzi">Tutti i prezzi e cosa include ogni pacchetto</a>.'
        return '<section class="sec" id="prezzi"><div class="wrap">%s<div class="price reveal">%s</div><p class="note">%s</p></div></section>' % (sec_head(ey, h, None, pg['c']), ''.join(cards), note)
    if k == 'case':
        return ('<section class="sec"><div class="wrap">%s<a class="case reveal" href="%s"><img src="%s" alt="Il sito di Aura Rome Tours" width="800" height="500" loading="lazy" decoding="async">'
                '<div><h3>%s</h3><p class="prose">%s</p><span class="go">Leggi il caso studio</span></div></a></div></section>') % (sec_head('Già in orbita', 'Un progetto reale.', None, pg['c']), AURA['url'], AURA['img'], AURA['name'], E(AURA['line']))
    if k == 'shot':
        return '<section class="sec"><div class="wrap"><img class="reveal" src="%s" alt="La home del sito di Aura Rome Tours" width="800" height="500" style="border-radius:18px;width:100%%;max-width:960px;height:auto;border:1px solid var(--line)"></div></section>' % AURA['img']
    if k == 'visit':
        return '<section class="sec"><div class="wrap"><div class="ctas reveal"><a class="btn btn-ghost" href="https://aurarometours.it" target="_blank" rel="noopener">Visita aurarometours.it</a><a class="btn btn-ghost" href="/servizi/realizzazione-siti-web-roma">Siti web su misura</a></div></div></section>'
    if k == 'legal':
        _, items = b
        body = ''.join('<h2 class="lh">%s</h2>%s' % (E(h), ''.join('<p>%s</p>' % x for x in paras)) for h, paras in items)
        return '<section class="sec"><div class="wrap"><div class="prose legal-text">%s</div></div></section>' % body
    if k == 'table':
        _, ey, h, p, head, rows, note = b
        th = ''.join('<th scope="col">%s</th>' % E(x) for x in head)
        tr = ''.join('<tr>%s</tr>' % ''.join(('<th scope="row">%s</th>' if i == 0 else '<td>%s</td>') % E(c) for i, c in enumerate(r)) for r in rows)
        return '<section class="sec"><div class="wrap">%s<div class="tbl reveal"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>%s</div></section>' % (sec_head(ey, h, p, pg['c']), th, tr, '<p class="note">%s</p>' % note if note else '')
    if k == 'faq':
        _, items = b
        body = ''.join('<details><summary>%s</summary><p>%s</p></details>' % (E(q), E(a)) for q, a in items)
        return '<section class="sec faq"><div class="wrap">%s<div class="reveal">%s</div></div></section>' % (sec_head('Domande', 'Domande frequenti.', None, pg['c']), body)
    raise ValueError(k)

def render(pg):
    from urllib.parse import quote
    url = SITE + pg['url']
    blocks = ''.join(block(b, pg) for b in pg['blocks'])
    rel = [s for s in SERVICES if s[0] != pg['url']][:3]
    related = '<section class="sec"><div class="wrap">%s<div class="related reveal">%s</div></div></section>' % (
        sec_head('Altri servizi', 'Lavoriamo anche su:', None, pg['c']), ''.join('<a href="%s"><b>%s</b><span>%s</span></a>' % (u, E(n), E(d)) for u, n, d in rel))
    sec_label, sec_href = parent(pg)
    return f'''<!doctype html>
<!-- generated by tools/build.py from tools/pages.py: edit the text there -->
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{E(pg['title'])}</title>
<meta name="description" content="{E(pg['desc'])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#000000">
<meta property="og:type" content="website">
<meta property="og:site_name" content="NovaSignal">
<meta property="og:locale" content="it_IT">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{E(pg['title'])}">
<meta property="og:description" content="{E(pg['desc'])}">
<meta property="og:image" content="{SITE}/assets/pages/{pg['img']}.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/brand/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/brand/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/pages.css">
<link rel="preload" as="image" href="/assets/pages/galaxy.jpg" media="(min-aspect-ratio:4/5)">
<link rel="preload" as="image" href="/assets/pages/galaxy-m.jpg" media="(max-aspect-ratio:4/5)">
<script>document.documentElement.className += ' js';</script>
{ld(pg)}

</head>
<body>
<div class="space" aria-hidden="true"><video muted playsinline loop preload="none" data-src="/assets/video/galaxy.mp4" data-src-m="/assets/video/galaxy-m.mp4"></video></div>
<a class="skip" href="#main">Vai al contenuto</a>
<header class="nav">
  <div class="wrap nav-in">
    <a class="brand" href="/"><img src="/assets/brand/mark-64.png" srcset="/assets/brand/mark-64.png 1x, /assets/brand/mark-128.png 2x" alt="" width="26" height="26">NovaSignal</a>
    <nav class="nav-links" aria-label="Principale"><a href="/#servizi">Servizi</a><a href="/#lavori">Lavori</a><a href="/#metodo">Metodo</a><a href="/#prezzi">Prezzi</a><a href="/#faq">FAQ</a></nav>
    <a class="btn btn-primary" href="#contatto"><span class="sq"></span>Parliamone</a>
  </div>
</header>
<main id="main">
<section class="p-hero{' short' if pg.get('legal') else ''}">
  {hero_video(pg)}
  <div class="wrap">
    <ol class="crumbs" aria-label="Percorso"><li><a href="/">NovaSignal</a></li><li><a href="{sec_href}">{sec_label}</a></li><li aria-current="page">{E(pg['crumb'])}</li></ol>
    <p class="tag"><i style="--c:{pg['c']}"></i>{E(pg['tag'])}</p>
    <h1>{E(pg['h1'])}</h1>
    <p class="lead">{E(pg['lead'])}</p>
    {'' if pg.get('legal') else '<div class="ctas"><a class="btn btn-primary" href="#contatto"><span class="sq"></span>Richiedi l’anteprima gratuita</a>' + ('' if pg.get('case') else '<a class="btn btn-ghost" href="#prezzi">Vedi i prezzi</a>') + '</div>'}
  </div>
</section>
{blocks}
{'' if pg.get('case') or pg.get('legal') else related}
<section class="cta-band" id="contatto">
  <div class="wrap">
    <p class="tag"><i style="--c:{pg['c']}"></i>Send a signal</p>
    <h2>Raccontaci il tuo progetto.</h2>
    <p class="lead">Rispondiamo entro 24 ore lavorative con una proposta e la data della tua anteprima gratuita.</p>
    <div class="ctas"><a class="btn btn-primary" href="{WA}{quote(pg['wa'])}" target="_blank" rel="noopener"><span class="sq"></span>Scrivici su WhatsApp</a><a class="btn btn-ghost" href="mailto:studio@novasignal.it">studio@novasignal.it</a></div>
    <p class="alt">Preferisci un modulo? <a href="/#contatti">Compila il brief sul sito</a>.</p>
  </div>
</section>
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div><a class="brand" href="/"><img src="/assets/brand/mark-64.png" srcset="/assets/brand/mark-64.png 1x, /assets/brand/mark-128.png 2x" alt="" width="26" height="26">NovaSignal</a><p>Design &amp; Technology Studio a Roma.</p></div>
      <div><h4>Servizi</h4><ul>{''.join('<li><a href="%s">%s</a></li>' % (u, E(n)) for u, n, _ in SERVICES)}</ul></div>
      <div><h4>Per settore</h4><ul>{''.join('<li><a href="%s">%s</a></li>' % (u, E(n)) for u, n in SECTORS)}</ul></div>
      <div><h4>Studio</h4><ul><li><a href="/#lavori">Lavori</a></li><li><a href="{AURA['url']}">Caso studio: Aura</a></li><li><a href="/risorse/quanto-costa-un-sito-web">Quanto costa un sito</a></li><li><a href="/#prezzi">Prezzi</a></li><li><a href="/#faq">FAQ</a></li></ul></div>
      <div><h4>Contatti</h4><ul><li><a href="https://wa.me/393206891014" target="_blank" rel="noopener">WhatsApp</a></li><li><a href="mailto:studio@novasignal.it">studio@novasignal.it</a></li><li><a href="/en" hreflang="en" lang="en">English</a></li></ul></div>
    </div>
    <div class="legal"><span>© 2026 NovaSignal di Riccardo El Ghendy · P.IVA 17596721005 · Roma · <a href="/privacy">Privacy e cookie</a></span><span>Progettato e sviluppato a Roma</span></div>
  </div>
</footer>
<script>
(function () {{ // films: the niche film in the banner first, then the galaxy of the home (never on save-data or reduced motion)
  var c = navigator.connection || {{}};
  if (c.saveData || /2g/.test(c.effectiveType || '') || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var old = !(window.CSS && CSS.supports && CSS.supports('inset', '0')), tall = matchMedia('(max-aspect-ratio: 4/5)').matches;
  function start(v) {{
    var d = v.dataset, src = old ? d.srcL : (tall && d.srcM) || d.src; if (!src) return;
    v.src = src; v.addEventListener('playing', function () {{ v.classList.add('on'); }}, {{ once: true }});
    var p = v.play(); if (p && p.catch) p.catch(function () {{}});
  }}
  var hv = document.querySelector('.hv video'), sp = document.querySelector('.space video');
  if (hv) start(hv);
  if (sp && !old) addEventListener('load', function () {{ setTimeout(function () {{ start(sp); }}, hv ? 2500 : 900); }});
}})();
(function () {{ // sections fade in once
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {{ for (var i = 0; i < els.length; i++) els[i].classList.add('in'); return; }}
  var io = new IntersectionObserver(function (es) {{ es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('in'); io.unobserve(e.target); }} }}); }}, {{ rootMargin: '0px 0px -8% 0px' }});
  for (var j = 0; j < els.length; j++) io.observe(els[j]);
}})();
</script>
</body>
</html>
'''
