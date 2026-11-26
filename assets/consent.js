/* NovaSignal — cookie consent + Google Tag Manager.
   Nothing from Google loads until the visitor accepts (Garante privacy, Italy). The choice is kept in
   localStorage for 6 months; any element with [data-consent] reopens the banner. ES5 on purpose (old iPads). */
(function () {
  var GTM = 'GTM-PH33HJKR', KEY = 'ns-consent', MAX = 182 * 864e5;
  var en = (document.documentElement.lang || 'it').indexOf('en') === 0;
  var T = en
    ? { p: 'We use analytics cookies to understand how the site is used, only if you agree.', more: 'Privacy & cookies', ok: 'Accept', no: 'Decline', href: '/privacy' }
    : { p: 'Usiamo cookie di analisi per capire come viene usato il sito, solo se sei d’accordo.', more: 'Privacy e cookie', ok: 'Accetta', no: 'Rifiuta', href: '/privacy' };

  function read() { try { var v = JSON.parse(localStorage.getItem(KEY) || 'null'); return v && Date.now() - v.t < MAX ? v.v : null; } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {} }

  var loaded = false;
  function loadGTM() {
    if (loaded) return; loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
    window.gtag('consent', 'default', { ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', analytics_storage: 'granted' });
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
    box.querySelector('.y').onclick = function () { save('granted'); hide(); loadGTM(); };
    box.querySelector('.n').onclick = function () { var was = read() === 'granted'; save('denied'); hide(); if (was) location.reload(); };
  }
  function hide() { if (!box) return; var b = box; box = null; b.classList.remove('in'); setTimeout(function () { b.remove(); }, 600); }

  var v = read();
  if (v === 'granted') loadGTM();
  function ready() {
    if (v === null) setTimeout(show, 2000);
    document.addEventListener('click', function (e) { var a = e.target.closest && e.target.closest('[data-consent]'); if (a) { e.preventDefault(); show(); } });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready); else ready();
})();
