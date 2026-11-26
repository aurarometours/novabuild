/* NovaSignal — cookie consent + Google Tag Manager.
   Google Consent Mode v2: no analytics cookies until the visitor accepts; before that, anonymous cookieless pings only. The choice is kept in
   localStorage for 6 months; any element with [data-consent] reopens the banner. ES5 on purpose (old iPads). */
(function () {
  var GTM = 'GTM-PH33HJKR', GA = 'G-1V60CXXQL4', KEY = 'ns-consent', MAX = 182 * 864e5;
  var en = (document.documentElement.lang || 'it').indexOf('en') === 0;
  var T = en
    ? { p: 'We use analytics cookies to improve the site. If you decline, we only measure anonymous visits, without cookies.', more: 'Privacy & cookies', ok: 'Accept', no: 'Decline', href: '/privacy' }
    : { p: 'Usiamo cookie di analisi per migliorare il sito. Se rifiuti, misuriamo solo visite anonime, senza cookie.', more: 'Privacy e cookie', ok: 'Accetta', no: 'Rifiuta', href: '/privacy' };

  function read() { try { var v = JSON.parse(localStorage.getItem(KEY) || 'null'); return v && Date.now() - v.t < MAX ? v.v : null; } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {} }

  /* Consent Mode v2 "advanced": Google always loads. Until the visitor accepts, analytics_storage is denied,
     so GA sets no cookies and sends only anonymous cookieless pings; after Accept it switches to full measurement.
     Both choices are recorded as a consent_choice event. */
  var loaded = false;
  function gtag() { window.dataLayer.push(arguments); }
  function loadGTM(v) {
    if (loaded) return; loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || gtag;
    window.gtag('consent', 'default', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: v === 'granted' ? 'granted' : 'denied' });
    window.gtag('set', 'ads_data_redaction', true);
    window.gtag('js', new Date());
    window.gtag('config', GA);
    var g = document.createElement('script'); g.async = true; g.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA;
    document.head.appendChild(g);
    window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.googletagmanager.com/gtm.js?id=' + GTM;
    document.head.appendChild(s);
  }

  var css = '.ns-ck{position:fixed;left:16px;bottom:16px;z-index:2147483000;width:min(400px,calc(100% - 32px));padding:18px 18px 16px;border-radius:18px;'
    + 'background:rgba(16,16,18,.86);-webkit-backdrop-filter:blur(18px) saturate(1.4);backdrop-filter:blur(18px) saturate(1.4);border:1px solid rgba(245,245,247,.14);'
    + 'color:#f5f5f7;font:400 .9rem/1.45 Inter,-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;letter-spacing:-.01em;'
    + 'box-shadow:0 20px 60px -20px rgba(0,0,0,.8);opacity:0;transform:translateY(12px);transition:opacity .5s cubic-bezier(.2,.7,.1,1),transform .6s cubic-bezier(.2,.7,.1,1)}'
    + '.ns-ck.in{opacity:1;transform:none}.ns-ck p{margin:0 0 14px;color:rgba(245,245,247,.86)}'
    + '.ns-ck a{color:#f5f5f7;text-decoration:none;border-bottom:1px solid rgba(245,245,247,.35)}'
    + '.ns-ck .b{display:flex}.ns-ck button{flex:1;height:40px;border-radius:999px;font:600 .88rem/1 inherit;cursor:pointer;-webkit-tap-highlight-color:transparent}'
    + '.ns-ck .y{background:#f5f5f7;color:#000;border:0;margin-left:8px}.ns-ck .n{background:transparent;color:#f5f5f7;border:1px solid rgba(245,245,247,.32)}'
    + '@media (max-width:600px){.ns-ck{left:12px;bottom:12px;width:calc(100% - 24px)}}';

  var box = null;
  function show() {
    if (box) return;
    if (!document.getElementById('ns-ck-css')) { var st = document.createElement('style'); st.id = 'ns-ck-css'; st.textContent = css; document.head.appendChild(st); }
    box = document.createElement('div'); box.className = 'ns-ck'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-live', 'polite'); box.setAttribute('aria-label', T.more);
    box.innerHTML = '<p>' + T.p + ' <a href="' + T.href + '">' + T.more + '</a></p><div class="b"><button type="button" class="n">' + T.no + '</button><button type="button" class="y">' + T.ok + '</button></div>';
    document.body.appendChild(box);
    requestAnimationFrame(function () { requestAnimationFrame(function () { box.classList.add('in'); }); });
    box.querySelector('.y').onclick = function () { choose('granted'); };
    box.querySelector('.n').onclick = function () { choose('denied'); };
  }
  function hide() { if (!box) return; var b = box; box = null; b.classList.remove('in'); setTimeout(function () { b.remove(); }, 600); }

  function choose(c) {
    save(c); hide(); loadGTM(c);
    window.gtag('consent', 'update', { analytics_storage: c });
    window.gtag('event', 'consent_choice', { choice: c === 'granted' ? 'accept' : 'decline' });
  }

  var v = read();
  loadGTM(v);
  function ready() {
    if (v === null) setTimeout(show, 2000);
    document.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('[data-consent]'); if (a) { e.preventDefault(); show(); } });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready); else ready();
})();
