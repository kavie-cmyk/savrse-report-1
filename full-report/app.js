
(function(){
  const $=(s,root=document)=>root.querySelector(s);
  const $$=(s,root=document)=>Array.from(root.querySelectorAll(s));
  const toc=$('.side-toc'), openBtn=$('#toc-open'), closeBtn=$('#toc-close');
  function setToc(open){ if(!toc) return; toc.classList.toggle('open',open); if(openBtn) openBtn.setAttribute('aria-expanded', String(open));}
  openBtn?.addEventListener('click',()=>setToc(true)); closeBtn?.addEventListener('click',()=>setToc(false));
  $$('.side-toc a').forEach(a=>a.addEventListener('click',()=>{if(innerWidth<=820)setToc(false)}));

  function runSearch(value){
    const q=value.trim().toLowerCase(), box=$('#search-results');
    if(!box) return;
    if(!q){box.classList.remove('open');box.innerHTML='';return;}
    const sections=$$('.chapter,.appendix-section,.part-section');
    const matches=[];
    for(const s of sections){
      const txt=s.textContent.toLowerCase();
      if(txt.includes(q)){
        const h=$('h2,h3',s); const id=s.id || h?.id;
        if(id && h) matches.push({id,title:h.textContent.trim(),snippet:txt.includes(q)?'Có nội dung phù hợp trong section này.':''});
      }
      if(matches.length>=30) break;
    }
    box.innerHTML=matches.length?matches.map(m=>`<a href="#${m.id}"><strong>${m.title}</strong><small>${m.snippet}</small></a>`).join(''):`<div style="padding:12px">Không tìm thấy kết quả.</div>`;
    box.classList.add('open');
    $$('#search-results a').forEach(a=>a.addEventListener('click',()=>box.classList.remove('open')));
  }
  const desk=$('#report-search'), mob=$('#report-search-mobile');
  desk?.addEventListener('input',e=>{if(mob)mob.value=e.target.value;runSearch(e.target.value)});
  mob?.addEventListener('input',e=>{if(desk)desk.value=e.target.value;runSearch(e.target.value)});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'){setToc(false);$('#search-results')?.classList.remove('open')}});

  $$('.table-filter').forEach(inp=>{
    inp.addEventListener('input',()=>{
      const table=document.getElementById(inp.dataset.target); if(!table) return;
      const q=inp.value.trim().toLowerCase();
      $$('tr',table).forEach((tr,i)=>{if(i===0 || tr.closest('thead')) return; tr.hidden=q && !tr.textContent.toLowerCase().includes(q);});
    });
  });

  $$('.image-asset img').forEach(img=>{
    const markFailed=()=>{const fig=img.closest('.image-asset'); if(fig) fig.classList.add('failed');};
    img.addEventListener('error',markFailed,{once:true});
    window.setTimeout(()=>{if(!img.complete || img.naturalWidth===0) markFailed();},3000);
  });

  const navMap=new Map($$('[data-nav-target]').map(a=>[a.dataset.navTarget,a]));
  if('IntersectionObserver' in window){
    const obs=new IntersectionObserver(entries=>{
      const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>a.boundingClientRect.top-b.boundingClientRect.top)[0];
      if(!visible) return;
      $$('[data-nav-target].active').forEach(a=>a.classList.remove('active'));
      navMap.get(visible.target.id)?.classList.add('active');
    },{rootMargin:'-15% 0px -70% 0px',threshold:[0,0.01]});
    $$('.part-section,.appendix-section').forEach(s=>obs.observe(s));
  }

  // Native-details print safety handled by CSS; no content is network-fetched or JS-generated.
})();
