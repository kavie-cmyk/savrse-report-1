
const FULL_REPORT_URL = 'https://docs.google.com/document/d/1p0o3vAIZel3aFqAYfS5BZdOTP2hzeMN45Aecgnb3ax8/edit';
const FULL_ARCHIVE_URL = './full-report/index.html';

document.querySelectorAll('[data-full-report]').forEach(a=>{a.href=FULL_REPORT_URL;a.target='_blank';a.rel='noopener';});
const navToggle=document.querySelector('.nav-toggle'), nav=document.querySelector('#main-nav');
if(navToggle){navToggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');navToggle.setAttribute('aria-expanded',String(open));});}
document.querySelectorAll('#main-nav a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));

function setTabs(buttonSelector,panelAttr,keyAttr){
  document.querySelectorAll(buttonSelector).forEach(btn=>btn.addEventListener('click',()=>{
    document.querySelectorAll(buttonSelector).forEach(b=>{b.classList.remove('active');b.setAttribute('aria-selected','false')});
    btn.classList.add('active');btn.setAttribute('aria-selected','true');
    const key=btn.dataset[keyAttr];
    document.querySelectorAll(`[${panelAttr}]`).forEach(p=>p.classList.toggle('active',p.getAttribute(panelAttr)===key));
  }));
}
setTabs('.track-toggle','data-panel','track');
setTabs('.finalist-tab','data-finalist-panel','finalist');
setTabs('.roadmap-tab','data-roadmap-panel','roadmap');

const methodDialog=document.querySelector('#method-dialog'), evidenceDialog=document.querySelector('#evidence-dialog');
document.querySelectorAll('[data-open-method]').forEach(b=>b.addEventListener('click',()=>methodDialog.showModal()));
document.querySelectorAll('[data-open-evidence]').forEach(b=>b.addEventListener('click',()=>evidenceDialog.showModal()));
document.querySelectorAll('dialog .dialog-close').forEach(b=>b.addEventListener('click',()=>b.closest('dialog').close()));
document.querySelectorAll('dialog').forEach(d=>d.addEventListener('click',e=>{if(e.target===d)d.close()}));

let sw1=true,sw2=true;
function updateDemo(){
 const a=document.querySelector('.route-a'),b=document.querySelector('.route-b'),c=document.querySelector('.route-c');
 a.classList.toggle('active',sw1); b.classList.toggle('active',!sw1); c.classList.toggle('active',sw2);
 const dest=sw1?'A':'B'; document.querySelector('#flow-state').textContent=`Route ${dest} active · S2 ${sw2?'open':'diverted'}`;
}
document.querySelector('[data-switch="1"]')?.addEventListener('click',()=>{sw1=!sw1;updateDemo()});
document.querySelector('[data-switch="2"]')?.addEventListener('click',()=>{sw2=!sw2;updateDemo()});
document.querySelector('#reset-demo')?.addEventListener('click',()=>{sw1=true;sw2=true;updateDemo()});

const sections=[...document.querySelectorAll('main section[id]')];
const navLinks=[...document.querySelectorAll('#main-nav a')];
const io=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){const id=e.target.id;navLinks.forEach(a=>a.classList.toggle('active',a.getAttribute('href')===`#${id}`));}})},{rootMargin:'-20% 0px -70% 0px',threshold:0});
sections.forEach(s=>io.observe(s));

window.P24_11 = {FULL_REPORT_URL,FULL_ARCHIVE_URL,phase:'P24-11',version:'v1.0'};

// Approved benchmark imagery may be blocked by restrictive corporate/browser networks.
// Preserve the source card and disclosure instead of showing a broken image.
// Fallback is applied ONLY on a real load error — not on a timer, so lazy-loaded
// images that simply haven't scrolled into view are never hidden prematurely.
document.querySelectorAll('.benchmark-media img').forEach(img=>{
  const fallback=()=>{
    if(img.naturalWidth>0) return;
    const media=img.closest('.benchmark-media');
    media?.classList.add('image-fallback');
    img.style.display='none';
  };
  img.addEventListener('error', fallback, {once:true});
});
