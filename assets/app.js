(function(){
"use strict";
var D = JSON.parse(document.getElementById('academyData').textContent);
var $ = function(s, r){ return (r||document).querySelector(s); };
var $$ = function(s, r){ return [].slice.call((r||document).querySelectorAll(s)); };
function headText(h){ var n = h.querySelector('.num'); if (!n) return h.textContent.trim(); return n.textContent + '  ' + h.textContent.slice(n.textContent.length).trim(); }

/* ---------- storage (per browser; always optional) */
var store = {
  get: function(k, d){ try{ var v = localStorage.getItem('aca-'+k); return v===null ? d : JSON.parse(v); }catch(e){ return d; } },
  set: function(k, v){ try{ localStorage.setItem('aca-'+k, JSON.stringify(v)); }catch(e){} }
};
var state = { bm: store.get('bm', {}) };
function save(k){ store.set(k, state[k]); }

/* ---------- light / dark
   Follows the computer's setting until the round button is clicked, then remembers the choice. */
$('#themeBtn').addEventListener('click', function(){
  var root = document.documentElement;
  var isDark = root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  root.dataset.theme = isDark ? 'light' : 'dark';
  try { localStorage.setItem('ai-claude-mastery:theme', root.dataset.theme); } catch (e) { /* storage blocked */ }
});

/* ---------- table of contents */
var chById = {}; D.chapters.forEach(function(c){ chById[c.id] = c; });
var toc = $('#toc'), navLinks = {}, partBtns = {}, partLists = {}, subLists = {};
var openParts = store.get('openParts', {});
D.parts.forEach(function(p){
  var chs = D.chapters.filter(function(c){ return c.part === p.id; });
  var nW = chs.filter(function(c){ return c.written; }).length;
  var btn = document.createElement('button');
  btn.type = 'button'; btn.className = 'nav-part';
  btn.innerHTML = '<span class="pn">' + p.num + '</span><span class="pt"></span>';
  btn.querySelector('.pt').textContent = p.title;
  var list = document.createElement('div'); list.className = 'nav-chs';
  chs.forEach(function(c){
    var el;
    if (c.written){
      el = document.createElement('a'); el.className = 'nav-ch'; el.href = '#' + c.id;
      var art = document.getElementById(c.id);
      var subs = document.createElement('div'); subs.className = 'nav-subs';
      if (art) $$('h3[id]', art).forEach(function(h){
        var s = document.createElement('a'); s.className = 'nav-sub'; s.href = '#' + h.id; s.textContent = headText(h); subs.appendChild(s);
      });
      subLists[c.id] = subs;
      el.innerHTML = '<span class="n">' + c.num + '</span><span class="t"></span><span class="flag"></span>';
      el.querySelector('.t').textContent = c.title;
      list.appendChild(el); list.appendChild(subs);
      navLinks[c.id] = el;
    } else {
      el = document.createElement('div'); el.className = 'nav-ch planned'; el.title = 'Being written';
      el.innerHTML = '<span class="n">' + c.num + '</span><span class="t"></span>';
      el.querySelector('.t').textContent = c.title;
      list.appendChild(el);
    }
  });
  var open = openParts[p.id] !== undefined ? openParts[p.id] : nW > 0;
  btn.setAttribute('aria-expanded', open ? 'true' : 'false'); list.hidden = !open;
  btn.addEventListener('click', function(){
    var o = btn.getAttribute('aria-expanded') !== 'true';
    btn.setAttribute('aria-expanded', o ? 'true' : 'false'); list.hidden = !o;
    openParts[p.id] = o; store.set('openParts', openParts);
  });
  partBtns[p.id] = btn; partLists[p.id] = list;
  toc.appendChild(btn); toc.appendChild(list);
});
function refreshNavFlags(){
  Object.keys(navLinks).forEach(function(id){
    navLinks[id].querySelector('.flag').textContent = state.bm[id] ? '★' : '';
  });
}

/* ---------- chapter controls: bookmark and quizzes (quiz answers are not saved) */
$$('article.chapter').forEach(function(a){
  var id = a.id;
  var meta = $('.ch-meta', a);
  var bm = document.createElement('button'); bm.type = 'button'; bm.className = 'bm';
  function syncBm(){ var on = !!state.bm[id]; bm.classList.toggle('on', on); bm.textContent = on ? '★ Bookmarked' : '☆ Bookmark'; bm.setAttribute('aria-pressed', on); }
  bm.addEventListener('click', function(){ if (state.bm[id]) delete state.bm[id]; else state.bm[id] = Date.now(); save('bm'); syncBm(); refreshNavFlags(); });
  meta.appendChild(bm); syncBm();

  $$('.quiz', a).forEach(function(qzBox){
    var qs = $$('.qz', qzBox);
    var head = $('.quiz-h', qzBox);
    var score = document.createElement('span'); score.className = 'score'; head.appendChild(score);
    var retry = document.createElement('button'); retry.type = 'button'; retry.className = 'retry'; retry.textContent = 'Try this quiz again'; retry.hidden = true;
    qzBox.appendChild(retry);
    var answers = {};
    function update(){
      var n = Object.keys(answers).length, right = 0;
      Object.keys(answers).forEach(function(k){ if (answers[k]) right++; });
      score.textContent = n ? (right + ' of ' + qs.length + ' correct' + (n < qs.length ? ' so far' : '')) : qs.length + ' questions';
      retry.hidden = n === 0;
    }
    qs.forEach(function(q, i){
      var btns = $$('.opts button', q), why = $('.why', q);
      var whyHTML = why ? why.innerHTML : '';
      btns.forEach(function(b){ b.type = 'button'; b.addEventListener('click', function(){
        if (answers[i] !== undefined) return;
        var ok = b.hasAttribute('data-ok');
        btns.forEach(function(x){ x.disabled = true; if (x.hasAttribute('data-ok')) x.classList.add('right'); });
        if (!ok) b.classList.add('wrong');
        if (why){ why.innerHTML = '<b>' + (ok ? 'Correct.' : 'Not quite.') + '</b> ' + whyHTML; why.hidden = false; }
        answers[i] = ok; update();
      }); });
      q._reset = function(){ btns.forEach(function(x){ x.disabled = false; x.classList.remove('right','wrong'); }); if (why){ why.hidden = true; why.innerHTML = whyHTML; } };
    });
    retry.addEventListener('click', function(){ answers = {}; qs.forEach(function(q){ q._reset(); }); update(); });
    update();
  });
});
refreshNavFlags();
function escapeHTML(s){ return s.replace(/[&<>"]/g, function(ch){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[ch]; }); }

/* ---------- scroll spy and reading progress
   Positions are measured once (and again on resize or when sections open) instead of on every
   scroll frame, and the contents rail only changes when the current section changes. */
var spyTargets = [];
$$('#cover, .page, .part-head, article.chapter, article.chapter h3[id]').forEach(function(el){
  var art = el.closest('article.chapter');
  spyTargets.push({ el: el, top: 0, chap: art ? art.id : null, sub: el.tagName === 'H3' ? el.id : null,
    label: art ? (chById[art.id].num + ' · ' + chById[art.id].title) : (el.querySelector('h2') ? el.querySelector('h2').textContent : (el.id === 'cover' ? 'About' : el.textContent.trim().slice(0,60))),
    page: (el.classList.contains('page') || el.id === 'cover') ? el.id : null });
});
var where = $('#where'), rail = $('#railScroll'), bar = $('#progress');
var current = null, openChap = null, activeEls = [];
function measure(){
  var sy = window.scrollY;
  spyTargets.forEach(function(t){ t.top = t.el.getBoundingClientRect().top + sy; });
  // A chapter that is far off screen is not laid out yet, so the headings inside it have no real
  // position. Place those at their chapter's start so the list stays in order for findCurrent.
  var chapTop = 0, nextTop = Infinity;
  for (var i = spyTargets.length - 1; i >= 0; i--){
    var t = spyTargets[i];
    if (!t.sub){ nextTop = t.top; continue; }
    t._next = nextTop;
  }
  spyTargets.forEach(function(t){
    if (!t.sub){ chapTop = t.top; return; }
    if (!(t.top >= chapTop && t.top <= t._next)) t.top = chapTop;
  });
}
function findCurrent(){
  var y = window.scrollY + 130, lo = 0, hi = spyTargets.length - 1, ans = -1;
  while (lo <= hi){ var mid = (lo + hi) >> 1; if (spyTargets[mid].top <= y){ ans = mid; lo = mid + 1; } else hi = mid - 1; }
  return ans < 0 ? null : spyTargets[ans];
}
// Saved positions go stale when far-away chapters are laid out (see style.css). Check the answer
// against the live page: the current item must start above the line and the next chapter-level
// item below it. If not, measure again. This costs two position reads per frame.
function stillRight(cur){
  var line = 130, i = cur ? spyTargets.indexOf(cur) : -1;
  if (cur && cur.el.getBoundingClientRect().top > line + 1) return false;
  for (var j = i + 1; j < spyTargets.length; j++){
    if (spyTargets[j].sub) continue;
    return spyTargets[j].el.getBoundingClientRect().top > line - 1;
  }
  return true;
}
function keepInRail(el){
  var r = el.getBoundingClientRect(), rr = rail.getBoundingClientRect();
  if (r.top < rr.top + 40 || r.bottom > rr.bottom - 40) rail.scrollTop += r.top - rr.top - rr.height / 3;
}
function setActive(cur){
  activeEls.forEach(function(x){ x.classList.remove('active'); });
  activeEls = [];
  if (!cur){ where.textContent = 'About'; return; }
  where.textContent = cur.label;
  if (cur.page){ var fl = $('.rail-front a[href="#' + cur.page + '"]'); if (fl){ fl.classList.add('active'); activeEls.push(fl); } }
  if (!(cur.chap && navLinks[cur.chap])) return;
  var link = navLinks[cur.chap];
  if (openChap !== cur.chap){
    // Open this chapter's sections without making the rail jump: remember where the link was, then restore it.
    var before = link.getBoundingClientRect().top;
    if (openChap && subLists[openChap]) subLists[openChap].classList.remove('open');
    var pid = chById[cur.chap].part;
    if (partLists[pid].hidden){ partLists[pid].hidden = false; partBtns[pid].setAttribute('aria-expanded','true'); }
    subLists[cur.chap].classList.add('open');
    rail.scrollTop += link.getBoundingClientRect().top - before;
    openChap = cur.chap;
    keepInRail(link);
  }
  link.classList.add('active'); activeEls.push(link);
  if (cur.sub){ var s = $('.nav-sub[href="#' + cur.sub + '"]'); if (s){ s.classList.add('active'); activeEls.push(s); } }
}
function spy(){
  var cur = findCurrent();
  if (!stillRight(cur)){ measure(); cur = findCurrent(); }
  if (cur !== current){ current = cur; setActive(cur); }
  var h = document.documentElement.scrollHeight - window.innerHeight;
  bar.style.width = (h > 0 ? Math.min(100, window.scrollY / h * 100) : 0) + '%';
}
var ticking = false;
window.addEventListener('scroll', function(){ if (!ticking){ ticking = true; requestAnimationFrame(function(){ spy(); ticking = false; }); } }, { passive: true });
// A jump to a link may not send a scroll event in every browser, so update straight after it too.
window.addEventListener('hashchange', function(){ spy(); });
document.addEventListener('click', function(e){ if (e.target.closest('a[href^="#"]')) setTimeout(spy, 0); });
var resizeTimer;
window.addEventListener('resize', function(){ clearTimeout(resizeTimer); resizeTimer = setTimeout(function(){ measure(); spy(); }, 150); });
// Content above can change height (opening an "Under the hood" section, fonts loading), so re-measure then.
document.addEventListener('toggle', function(){ measure(); }, true);
// Chapters are laid out only when they come near the screen (see style.css), so their heights change
// as the reader scrolls. Measure again whenever a chapter's size changes.
// After a jump to a link, the chapters around the target are laid out and change height, which would
// push the target off screen; keep it pinned in place until things settle or the reader scrolls.
var pin = null, pinUntil = 0;
function pinTo(id){ pin = id && document.getElementById(id); pinUntil = Date.now() + 3000; }
function unpin(){ pin = null; }
['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function(ev){ window.addEventListener(ev, unpin, { passive: true }); });
window.addEventListener('hashchange', function(){ pinTo(decodeURIComponent(location.hash.slice(1))); });
if (location.hash) pinTo(decodeURIComponent(location.hash.slice(1)));
if (window.ResizeObserver){
  var remeasure;
  var ro = new ResizeObserver(function(){
    if (pin && Date.now() < pinUntil) pin.scrollIntoView();
    clearTimeout(remeasure);
    remeasure = setTimeout(function(){
      if (pin && Date.now() < pinUntil) pin.scrollIntoView();
      measure(); spy();
    }, 100);
  });
  $$('article.chapter, #glossary').forEach(function(el){ ro.observe(el); });
}
window.addEventListener('load', function(){ measure(); spy(); });
if (document.fonts && document.fonts.ready) document.fonts.ready.then(function(){ measure(); spy(); });
measure(); spy();

/* ---------- mobile drawer */
function closeNav(){ document.body.classList.remove('navopen'); }
$('#menuBtn').addEventListener('click', function(){ document.body.classList.toggle('navopen'); });
$('#scrim').addEventListener('click', closeNav);
rail.addEventListener('click', function(e){ if (e.target.closest('a')) closeNav(); });

/* ---------- copy buttons */
$$('.code').forEach(function(c){
  var b = document.createElement('button'); b.type = 'button'; b.className = 'copy'; b.textContent = 'Copy';
  b.addEventListener('click', function(){
    var t = $('pre', c).innerText;
    var ok = function(){ b.textContent = 'Copied'; setTimeout(function(){ b.textContent = 'Copy'; }, 1400); };
    try { navigator.clipboard.writeText(t).then(ok, function(){ selectPre(c); }); } catch(e){ selectPre(c); }
  });
  c.appendChild(b);
});
function selectPre(c){ var r = document.createRange(); r.selectNodeContents($('pre', c)); var s = getSelection(); s.removeAllRanges(); s.addRange(r); }

/* ---------- glossary popovers and filter */
var pop = $('#pop'), popFor = null;
function showPop(el){
  var key = (el.getAttribute('href') || '').replace('#g-', ''), g = D.glossary[key];
  if (!g) return;
  pop.innerHTML = '<b></b><span></span><br><a href="#g-' + key + '">Open in glossary</a>';
  $('b', pop).textContent = g.t; $('span', pop).textContent = g.d;
  pop.hidden = false;
  var r = el.getBoundingClientRect(), pw = pop.offsetWidth, ph = pop.offsetHeight;
  var left = Math.max(16, Math.min(r.left, window.innerWidth - pw - 16));
  var top = r.bottom + 8; if (top + ph > window.innerHeight - 16) top = r.top - ph - 8;
  pop.style.left = left + 'px'; pop.style.top = Math.max(16, top) + 'px'; popFor = el;
}
function hidePop(){ pop.hidden = true; popFor = null; }
document.addEventListener('click', function(e){
  var g = e.target.closest('a.gl');
  if (g){ e.preventDefault(); if (popFor === g) hidePop(); else showPop(g); return; }
  if (!e.target.closest('#pop')) hidePop();
});
document.addEventListener('mouseover', function(e){ var g = e.target.closest('a.gl'); if (g && matchMedia('(hover: hover)').matches) showPop(g); });
document.addEventListener('mouseout', function(e){ var g = e.target.closest('a.gl'); if (g && matchMedia('(hover: hover)').matches && !(e.relatedTarget && e.relatedTarget.closest && e.relatedTarget.closest('#pop'))) hidePop(); });
pop.addEventListener('mouseleave', hidePop);
window.addEventListener('scroll', hidePop, { passive: true });
pop.addEventListener('click', function(e){ if (e.target.closest('a')) hidePop(); });
window.addEventListener('hashchange', function(){
  var h = location.hash.slice(1), dt = h && h.indexOf('g-') === 0 ? document.getElementById(h) : null;
  if (dt){ dt.classList.add('flash'); setTimeout(function(){ dt.classList.remove('flash'); }, 1600); }
});
var gf = $('#glossFilter');
if (gf) gf.addEventListener('input', function(){
  var q = gf.value.trim().toLowerCase(), any = false;
  $$('#glossList dt').forEach(function(dt){
    var dd = dt.nextElementSibling, show = !q || (dt.textContent + ' ' + dd.textContent).toLowerCase().indexOf(q) > -1;
    dt.hidden = !show; dd.hidden = !show; if (show) any = true;
  });
  $('#glossEmpty').hidden = any;
});

/* ---------- generic table filters: <input data-filter="#tableId"> */
$$('input[data-filter]').forEach(function(inp){
  var tbl = $(inp.getAttribute('data-filter')); if (!tbl) return;
  var empty = inp.getAttribute('data-empty') ? $(inp.getAttribute('data-empty')) : null;
  inp.addEventListener('input', function(){
    var q = inp.value.trim().toLowerCase(), any = false, group = null, has = false;
    $$('tr', tbl).slice(1).forEach(function(r){
      if (r.classList.contains('group')){ if (group) group.hidden = !has && !!q; group = r; has = false; return; }
      var show = !q || r.textContent.toLowerCase().indexOf(q) > -1; r.hidden = !show; if (show){ any = true; has = true; }
    });
    if (group) group.hidden = !has && !!q;
    if (empty) empty.hidden = any;
  });
});

/* ---------- search */
var index = [];
$$('article.chapter').forEach(function(a){
  var c = chById[a.id], parts = [], curH = { id: a.id, title: c.title, text: '' };
  var walker = $$('h3[id], p, li, td, dd, dt, summary', a);
  walker.forEach(function(el){
    if (el.tagName === 'H3'){ parts.push(curH); curH = { id: el.id, title: headText(el), text: '' }; }
    else curH.text += ' ' + el.textContent;
  });
  parts.push(curH);
  parts.forEach(function(p){ index.push({ id: p.id, title: p.title, chap: c, text: p.text.replace(/\s+/g,' ') }); });
});
Object.keys(D.glossary).forEach(function(k){ index.push({ id: 'g-' + k, title: D.glossary[k].t, chap: null, text: D.glossary[k].d, gloss: true }); });
var sBox = $('#search'), sIn = $('#searchInput'), sRes = $('#results'), sel = 0, hits = [];
function openSearch(){ sBox.hidden = false; sIn.value = ''; runSearch(); setTimeout(function(){ sIn.focus(); }, 10); }
function closeSearch(){ sBox.hidden = true; }
function runSearch(){
  var q = sIn.value.trim().toLowerCase();
  if (q.length < 2){ sRes.innerHTML = '<div class="empty">Type at least two letters. Try "attention", "tokens", "/compact" or "MCP".</div>'; hits = []; return; }
  var words = q.split(/\s+/);
  hits = index.map(function(it){
    var t = it.title.toLowerCase(), x = it.text.toLowerCase(), s = 0;
    for (var i = 0; i < words.length; i++){
      var w = words[i], inT = t.indexOf(w) > -1, inX = x.indexOf(w) > -1;
      if (!inT && !inX) return null;
      s += (inT ? 10 : 0) + (inX ? 1 : 0) + (it.gloss && inT ? 6 : 0);
    }
    if (t === q) s += 50; else if (t.indexOf(q) === 0) s += 8;
    return { it: it, s: s };
  }).filter(Boolean).sort(function(a,b){ return b.s - a.s; }).slice(0, 30);
  sel = 0;
  if (!hits.length){ sRes.innerHTML = '<div class="empty">Nothing matches "' + escapeHTML(q) + '". Try a shorter or different word.</div>'; return; }
  sRes.innerHTML = hits.map(function(h, i){
    var it = h.it, x = it.text, pos = x.toLowerCase().indexOf(words[0]);
    var snip = pos > -1 ? (pos > 50 ? '…' : '') + x.slice(Math.max(0, pos - 50), pos + 110) + '…' : x.slice(0, 140);
    var where = it.gloss ? 'Glossary' : ('Chapter ' + it.chap.num + (it.id === it.chap.id ? '' : ' · ' + escapeHTML(it.chap.title)));
    return '<a href="#' + it.id + '"' + (i === 0 ? ' class="sel"' : '') + '><span class="rp">' + where + '</span><span class="rt">' + mark(escapeHTML(it.title), words) + '</span><span class="rs">' + mark(escapeHTML(snip), words) + '</span></a>';
  }).join('');
}
function mark(s, words){ words.forEach(function(w){ if (w.length < 2) return; s = s.replace(new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>'); }); return s; }
sIn.addEventListener('input', runSearch);
sIn.addEventListener('keydown', function(e){
  var as = $$('a', sRes);
  if (e.key === 'ArrowDown' || e.key === 'ArrowUp'){
    e.preventDefault(); if (!as.length) return;
    as[sel].classList.remove('sel'); sel = (sel + (e.key === 'ArrowDown' ? 1 : as.length - 1)) % as.length;
    as[sel].classList.add('sel'); as[sel].scrollIntoView({ block: 'nearest' });
  } else if (e.key === 'Enter' && as[sel]){ e.preventDefault(); as[sel].click(); }
});
sRes.addEventListener('click', function(e){ if (e.target.closest('a')){ closeSearch(); closeNav(); } });
sBox.addEventListener('click', function(e){ if (e.target === sBox) closeSearch(); });
$('#searchBtn').addEventListener('click', openSearch);
document.addEventListener('keydown', function(e){
  var typing = /INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName);
  if (e.key === 'Escape'){ if (!sBox.hidden) closeSearch(); hidePop(); closeNav(); }
  else if (!typing && (e.key === '/' || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k'))){ e.preventDefault(); openSearch(); }
});

/* ---------- cover terminal */
var script = [
  ['p','$ '],['t','claude\n'],['d','  Claude Code · ~/projects/shop-app\n\n'],
  ['p','> '],['t','How does a transformer read my prompt? Explain it like I\'m new to AI.\n'],
  ['o','  Think of your prompt as a sentence cut into small pieces called tokens.\n  Each piece looks at every other piece to work out what it means here…\n\n'],
  ['p','> '],['t','/model\n'],['d','  Choose a model for this session…\n\n'],['p','> ']
];
var typer = $('#typer');
var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
function span(cls, txt){ var s = document.createElement('span'); if (cls !== 't') s.className = cls; s.textContent = txt; typer.appendChild(s); return s; }
function caret(){ var c = document.createElement('span'); c.className = 'caret'; typer.appendChild(c); }
if (reduce){ script.forEach(function(s){ span(s[0], s[1]); }); caret(); }
else {
  var i = 0;
  (function next(){
    if (i >= script.length){ caret(); return; }
    var s = script[i++], el = span(s[0], '');
    if (s[0] === 't'){ var k = 0; (function ty(){ el.textContent = s[1].slice(0, ++k); if (k < s[1].length) setTimeout(ty, 22 + Math.random()*35); else setTimeout(next, 350); })(); }
    else { el.textContent = s[1]; setTimeout(next, s[0] === 'p' ? 250 : 600); }
  })();
}
})();
