# Homepage body + scripts for the Psychology of Technology Lab site.
# Imported by build_site.py.

INDEX_BODY = """
<header class="hero wrap" id="top">
  <div class="hero-grid hero-v2">
    <div>
      <div class="eyebrow">Carnegie Mellon University · Human-Computer Interaction Institute</div>
      <h1 class="lab-title">The Psychology of Technology&nbsp;Lab.</h1>
      <p class="lede">We investigate the psychological effect of emerging technologies,
        such as <strong>social media</strong> and <strong>AI</strong>.</p>
      <p class="director">Principal Investigator: <strong>Steve Rathje</strong>, Assistant Professor,
        Human-Computer Interaction Institute, School of Computer Science, Carnegie Mellon University</p>
      <div class="cta-row">
        <a class="btn primary" href="join.html">Join the lab</a>
        <a class="btn ghost" href="#methods">How we work</a>
      </div>
    </div>
    <div class="brain-wrap" aria-hidden="true">
      <canvas id="brain" width="560" height="460"></canvas>
      <div class="brain-hint">fire neurons with your cursor · drag them to rewire</div>
    </div>
  </div>
</header>



<section id="methods">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Methods</div>
      <h2>We study these questions using the following methods:</h2>
    </div>
    <div class="methods">
      <div class="method">
        <canvas class="micon" id="mData" width="180" height="140"></canvas>
        <h3>Big Data Analysis</h3>
        <div class="links"><span class="links-label">Example publications:</span>
          <a href="https://doi.org/10.1073/pnas.2024292118" target="_blank" rel="noopener">Out-group animosity drives engagement on social media (PNAS)</a>
          <a href="https://doi.org/10.1073/pnas.2308950121" target="_blank" rel="noopener">GPT is an effective tool for multilingual psychological text analysis (PNAS)</a>
        </div>
      </div>
      <div class="method">
        <canvas class="micon" id="mRct" width="180" height="140"></canvas>
        <h3>Lab &amp; Field Experiments</h3>
        <div class="links"><span class="links-label">Example publications:</span>
          <a href="https://osf.io/preprints/psyarxiv/vmyek_v1" target="_blank" rel="noopener">The impact of sycophantic AI on attitudes and decisions (Under Review)</a>
          <a href="https://doi.org/10.31234/osf.io/acbwg" target="_blank" rel="noopener">Unfollowing partisan accounts reduces out-party animosity and increases social media satisfaction (Under Review)</a>
          <a href="https://doi.org/10.1038/s41562-023-01540-w" target="_blank" rel="noopener">Accuracy and social motivations shape belief in (mis)information (Nature Human Behaviour)</a>
        </div>
      </div>
      <div class="method">
        <img class="micon micon-map" src="images/pub-global.jpg" alt="Map of countries in the global social media study">
        <h3>Global Studies</h3>
        <div class="links"><span class="links-label">Example publications:</span>
          <a href="https://osf.io/preprints/psyarxiv/ujtxa_v1" target="_blank" rel="noopener">Testing the causal impact of social media usage around the globe (In Principle Acceptance of Registered Report, Nature)</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="research">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Research</div>
      <h2>Four questions we keep asking</h2>
    </div>
    <div class="cards">
      <div class="card">
        <h3>Why does outrage go viral?</h3>
        <p>Out-group animosity and moral emotion drive engagement online — even though most people
           say they don't want divisive content. We call this the paradox of virality, and we study
           the incentives that create it.</p>
        <div class="links"><a href="https://doi.org/10.1073/pnas.2024292118" target="_blank" rel="noopener">PNAS 2021</a> ·
          <a href="https://doi.org/10.1016/j.tics.2025.06.014" target="_blank" rel="noopener">Trends in Cognitive Sciences 2025</a></div>
      </div>
      <div class="card">
        <h3>Can we redesign our feeds?</h3>
        <p>In field experiments on Twitter/X, incentivizing people to unfollow partisan accounts
           durably reduced out-party animosity and increased satisfaction with their feeds —
           a scalpel, not a sledgehammer.</p>
        <div class="links"><a href="https://doi.org/10.31234/osf.io/acbwg" target="_blank" rel="noopener">Preprint</a></div>
      </div>
      <div class="card">
        <h3>What does AI do to our minds?</h3>
        <p>Sycophantic AI chatbots that agree with everything we say can amplify attitude extremity
           and overconfidence. We also build LLM-based methods to advance the science itself.</p>
        <div class="links"><a href="https://osf.io/preprints/psyarxiv/vmyek_v1" target="_blank" rel="noopener">Preprint</a> ·
          <a href="https://doi.org/10.1073/pnas.2308950121" target="_blank" rel="noopener">PNAS 2024</a></div>
      </div>
      <div class="card">
        <h3>Is it the same everywhere?</h3>
        <p>Most social media research studies WEIRD samples. Our registered report at Nature tests
           the causal impact of social media abstention across dozens of countries.</p>
        <div class="links"><a href="https://osf.io/preprints/psyarxiv/ujtxa_v1" target="_blank" rel="noopener">Registered Report (IPA at Nature)</a></div>
      </div>
    </div>
  </div>
</section>

<section id="key-pubs">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Key Publications</div>
      <h2>Start here</h2>
    </div>
    <div class="key-pubs">
      <a class="key-pub" href="https://doi.org/10.1016/j.tics.2025.06.014" target="_blank" rel="noopener">
        <div class="cover"><img src="images/virality-cover.jpg" alt="" onerror="this.remove()">
          <span class="journal">Trends in Cognitive Sciences · 2025</span>
          <span class="ctitle">The Psychology of Virality</span></div>
        <div class="meta"><b>Rathje &amp; Van Bavel</b>Why some information spreads — online and off.</div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1073/pnas.2024292118" target="_blank" rel="noopener">
        <div class="cover alt1"><img src="images/pub-animosity.jpg" alt="" onerror="this.remove()"><span class="journal">PNAS · 2021</span>
          <span class="ctitle">Out-group animosity drives engagement on social media</span></div>
        <div class="meta"><b>Rathje, Van Bavel &amp; van der Linden</b>Attacking the other side is the strongest predictor of going viral.</div>
      </a>
      <a class="key-pub" href="https://osf.io/preprints/psyarxiv/vmyek_v1" target="_blank" rel="noopener">
        <div class="cover alt2"><img src="images/pub-sycophancy.jpg" alt="" onerror="this.remove()"><span class="journal">Preprint · 2025</span>
          <span class="ctitle">The Impact of Sycophantic AI on Attitudes and Decisions</span></div>
        <div class="meta"><b>Rathje, Ye, Globig, Pillai, Oldemburgo de Mello, Chen &amp; Van Bavel</b>Agreeable chatbots, more extreme humans.</div>
      </a>
    </div>
    <p class="see-all"><a href="publications.html">All publications, by topic →</a></p>
  </div>
</section>
"""

INDEX_SCRIPT = """
<script>
// ===== stat counters =====
const fmt=n=>n>=1e6?(n/1e6)+'M':n.toLocaleString();
const animate=el=>{const target=+el.dataset.count,suffix=el.dataset.suffix||'';
  const t0=performance.now(),dur=1400;
  const step=t=>{const p=Math.min(1,(t-t0)/dur),eased=1-Math.pow(1-p,3);
    el.textContent=fmt(Math.round(target*eased))+(p===1?suffix:'');
    if(p<1)requestAnimationFrame(step);};
  requestAnimationFrame(step);};
const io=new IntersectionObserver(es=>es.forEach(e=>{
  if(e.isIntersecting){animate(e.target);io.unobserve(e.target);}}),{threshold:.6});
document.querySelectorAll('[data-count]').forEach(el=>io.observe(el));

const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
const css=v=>getComputedStyle(document.documentElement).getPropertyValue(v).trim();

// ===== brain: neurons + wires that spark near the cursor =====
(function(){
  const cv=document.getElementById('brain'); if(!cv) return;
  const ctx=cv.getContext('2d'), W=cv.width, H=cv.height;
  // brain silhouette = union of blobs (side profile, facing left)
  const blobs=[
    [0.50,0.42,0.34,0.27],  // main hemisphere
    [0.28,0.46,0.17,0.20],  // frontal lobe
    [0.66,0.34,0.20,0.18],  // parietal
    [0.76,0.60,0.13,0.11],  // cerebellum
    [0.42,0.62,0.22,0.12],  // temporal
  ];
  const inBrain=(x,y)=>blobs.some(([cx,cy,rx,ry])=>{
    const dx=(x-cx)/rx, dy=(y-cy)/ry; return dx*dx+dy*dy<=1;});
  // sample neurons
  const N=80, nodes=[];
  let guard=0;
  while(nodes.length<N && guard++<20000){
    const x=Math.random(), y=Math.random();
    if(inBrain(x,y)) nodes.push({x:x*W, y:y*H, r:2+Math.random()*2, ph:Math.random()*6.28});
  }
  // brain stem tail
  nodes.push({x:0.80*W,y:0.74*H,r:2.5,ph:0},{x:0.84*W,y:0.82*H,r:2.5,ph:1});
  // edges: k nearest
  const edges=[];
  nodes.forEach((a,i)=>{
    const near=nodes.map((b,j)=>({j,d:Math.hypot(a.x-b.x,a.y-b.y)}))
      .filter(o=>o.j!==i).sort((p,q)=>p.d-q.d).slice(0,3);
    near.forEach(o=>{ if(i<o.j) edges.push([i,o.j]); });
  });
  let mouse={x:-999,y:-999}, dragging=null;
  const pos=e=>{const r=cv.getBoundingClientRect();
    return {x:(e.clientX-r.left)*(W/r.width), y:(e.clientY-r.top)*(H/r.height)};};
  cv.addEventListener('pointerdown',e=>{
    const p=pos(e);
    let best=null,bd=20;
    nodes.forEach(n=>{const d=Math.hypot(p.x-n.x,p.y-n.y); if(d<bd){bd=d;best=n;}});
    if(best){dragging=best; cv.setPointerCapture(e.pointerId); cv.style.cursor='grabbing';}
  });
  cv.addEventListener('pointermove',e=>{
    mouse=pos(e);
    if(dragging){
      dragging.x=Math.max(6,Math.min(W-6,mouse.x));
      dragging.y=Math.max(6,Math.min(H-6,mouse.y));
    } else {
      let near=false;
      nodes.forEach(n=>{if(Math.hypot(mouse.x-n.x,mouse.y-n.y)<20)near=true;});
      cv.style.cursor=near?'grab':'crosshair';
    }
  });
  const release=e=>{dragging=null; cv.style.cursor='crosshair';};
  cv.addEventListener('pointerup',release);
  cv.addEventListener('pointercancel',release);
  cv.addEventListener('pointerleave',e=>{if(!dragging)mouse={x:-999,y:-999};});
  const distToSeg=(p,a,b)=>{
    const l2=(a.x-b.x)**2+(a.y-b.y)**2; if(!l2) return Math.hypot(p.x-a.x,p.y-a.y);
    let t=((p.x-a.x)*(b.x-a.x)+(p.y-a.y)*(b.y-a.y))/l2; t=Math.max(0,Math.min(1,t));
    return Math.hypot(p.x-(a.x+t*(b.x-a.x)), p.y-(a.y+t*(b.y-a.y)));};
  // idle traveling pulses
  const pulses=[];
  const spawnPulse=()=>{ if(pulses.length<5) pulses.push({e:Math.floor(Math.random()*edges.length),t:0}); };
  setInterval(spawnPulse, 700);
  function jaggedLine(a,b,mag){
    ctx.beginPath(); ctx.moveTo(a.x,a.y);
    const segs=6;
    for(let s=1;s<segs;s++){
      const t=s/segs, nx=b.y-a.y, ny=a.x-b.x, len=Math.hypot(nx,ny)||1;
      const off=(Math.random()-0.5)*mag;
      ctx.lineTo(a.x+(b.x-a.x)*t+nx/len*off, a.y+(b.y-a.y)*t+ny/len*off);
    }
    ctx.lineTo(b.x,b.y); ctx.stroke();
  }
  function draw(t){
    ctx.clearRect(0,0,W,H);
    const accent=css('--accent')||'#E0402F', mutedC=css('--muted')||'#888', hair=css('--hairline')||'#ddd';
    // soft silhouette
    ctx.save(); ctx.globalAlpha=0.35;
    blobs.forEach(([cx,cy,rx,ry])=>{ ctx.beginPath();
      ctx.ellipse(cx*W,cy*H,rx*W,ry*H,0,0,6.29); ctx.fillStyle=hair; ctx.fill(); });
    ctx.restore();
    // wires
    edges.forEach(([i,j],k)=>{
      const a=nodes[i],b=nodes[j];
      const d=distToSeg(mouse,a,b);
      if(d<42){ // ⚡ electrified
        ctx.lineWidth=1.8; ctx.strokeStyle=accent;
        ctx.shadowColor=accent; ctx.shadowBlur=10;
        jaggedLine(a,b,7); ctx.shadowBlur=0;
      } else {
        ctx.lineWidth=1; ctx.strokeStyle=mutedC; ctx.globalAlpha=0.4;
        ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(b.x,b.y); ctx.stroke();
        ctx.globalAlpha=1;
      }
    });
    // idle pulses
    for(let k=pulses.length-1;k>=0;k--){
      const p=pulses[k]; p.t+=0.02;
      if(p.t>=1){pulses.splice(k,1);continue;}
      const [i,j]=edges[p.e], a=nodes[i], b=nodes[j];
      ctx.beginPath();
      ctx.arc(a.x+(b.x-a.x)*p.t, a.y+(b.y-a.y)*p.t, 2.2, 0, 6.29);
      ctx.fillStyle=accent; ctx.globalAlpha=0.8; ctx.fill(); ctx.globalAlpha=1;
    }
    // neurons
    nodes.forEach(n=>{
      const d=Math.hypot(mouse.x-n.x, mouse.y-n.y);
      const hot=d<46;
      const r=n.r+(hot?2.5:Math.sin(t/700+n.ph)*0.6);
      ctx.beginPath(); ctx.arc(n.x,n.y,Math.max(1,r),0,6.29);
      ctx.fillStyle=hot?accent:mutedC;
      if(hot){ctx.shadowColor=accent;ctx.shadowBlur=12;}
      ctx.fill(); ctx.shadowBlur=0;
    });
    if(!reduceMotion) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();

// ===== method icon: fractal data zoom-out =====
(function(){
  const cv=document.getElementById('mData'); if(!cv) return;
  const ctx=cv.getContext('2d'), W=cv.width, H=cv.height, cx=W/2, cy=H/2;
  // one self-similar cluster layout, reused at every scale
  const pts=Array.from({length:26},()=>({
    a:Math.random()*6.283, r:Math.pow(Math.random(),0.6), d:Math.random()<0.5?'0':'1'}));
  let layers=[3.4, 1.9, 1.05, 0.58, 0.32];
  function draw(){
    ctx.clearRect(0,0,W,H);
    const accent=css('--accent'), mutedC=css('--muted');
    layers=layers.map(s=>s*0.9965);
    if(Math.max(...layers)<2.4) layers.push(4.2);
    layers=layers.filter(s=>s>0.10);
    layers.forEach(s=>{
      const alpha=Math.max(0,Math.min(1,(s-0.10)*1.6))*Math.max(0,Math.min(1,(4.4-s)));
      ctx.globalAlpha=alpha*0.9;
      pts.forEach((p,i)=>{
        const R=p.r*62*s, x=cx+Math.cos(p.a)*R, y=cy+Math.sin(p.a)*R*0.78;
        if(x<-8||x>W+8||y<-8||y>H+8) return;
        if(i%4===0){ ctx.fillStyle=accent; ctx.font=(9*Math.min(s,1.4))+'px ui-monospace,monospace';
          ctx.fillText(p.d,x,y); }
        else { ctx.beginPath(); ctx.arc(x,y,Math.max(0.6,2.2*Math.min(s,1.2)),0,6.29);
          ctx.fillStyle=mutedC; ctx.fill(); }
      });
      // faint self-similar ring
      ctx.beginPath(); ctx.arc(cx,cy,62*s,0,6.29);
      ctx.strokeStyle=mutedC; ctx.globalAlpha=alpha*0.18; ctx.lineWidth=1; ctx.stroke();
    });
    ctx.globalAlpha=1;
    if(!reduceMotion) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();

// ===== method icon: randomization =====
(function(){
  const cv=document.getElementById('mRct'); if(!cv) return;
  const ctx=cv.getContext('2d'), W=cv.width, H=cv.height;
  const parts=[];
  const spawn=()=>{ if(parts.length<14) parts.push({x:W/2,y:8,side:Math.random()<0.5?-1:1,t:0}); };
  setInterval(spawn, 420);
  function draw(){
    ctx.clearRect(0,0,W,H);
    const accent=css('--accent'), mutedC=css('--muted'), hair=css('--hairline');
    // two bins
    ctx.strokeStyle=hair; ctx.lineWidth=2;
    ctx.strokeRect(12,H-38,W/2-26,30); ctx.strokeRect(W/2+14,H-38,W/2-26,30);
    // coin
    ctx.beginPath(); ctx.arc(W/2,26,9,0,6.29); ctx.strokeStyle=mutedC; ctx.lineWidth=1.5; ctx.stroke();
    ctx.fillStyle=mutedC; ctx.font='11px Archivo'; ctx.fillText('R', W/2-3.5, 30);
    for(let k=parts.length-1;k>=0;k--){
      const p=parts[k]; p.t+=0.016;
      if(p.t>=1){parts.splice(k,1);continue;}
      const drop=Math.min(p.t*2,1), veer=Math.max(0,p.t*2-1);
      const x=W/2+p.side*veer*(W/4+2), y=8+drop*(H/2-20)+veer*(H/2-24);
      ctx.beginPath(); ctx.arc(x,y,4,0,6.29);
      ctx.fillStyle=p.side<0?accent:mutedC; ctx.fill();
    }
    if(!reduceMotion) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();


</script>"""
