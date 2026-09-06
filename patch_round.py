#!/usr/bin/env python3
"""Batch: abstracts on key cards, zoom covers, 2-col pubs, sans-serif, mechanical brain."""
import re, json, html, urllib.request

def fetch_abs(doi):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22{doi}%22&resultType=core&format=json&pageSize=1"
    try:
        with urllib.request.urlopen(url, timeout=12) as r:
            res = json.load(r)['resultList']['result'][0]
        a = html.unescape(re.sub(r'<[^>]+>', ' ', res.get('abstractText', '')))
        return ' '.join(a.split())
    except Exception:
        return ''

ABS = {
 'virality': "Why do some ideas spread widely, while others fail to catch on? We review the psychology of information spread, or the psychology of “virality.” Similar types of information tend to spread in many contexts, both online and offline. This is likely because similar psychological processes drive information spread across contexts. We explain how these psychological processes interact with structural features of information environments, including norms, networks, and incentive structures. Surprisingly, widely shared content is often not widely liked—a phenomenon called “the paradox of virality.” We discuss the strengths and limitations of the virality metaphor, and future directions for the field, such as leveraging recent advances in artificial intelligence to better understand how information spreads across cultures and contexts.",
 'sycophancy': "There is widespread concern that AI chatbots are “sycophantic,” or overly agreeable and validating. However, less is known about the causal impact of interacting with sycophantic AI on beliefs and behaviors. Across seven studies (total n = 7,227), we found that people enjoyed interacting with sycophantic AI chatbots more than interacting with neutral chatbots or “disagreeable” chatbots that challenged them. Brief conversations with sycophantic chatbots about political or personal topics increased the strength of people’s attitudes. Sycophantic chatbots also inflated people’s perceptions that they were better than the average person on desirable traits, and led people to bet more money that they scored better than average on tasks purporting to measure desirable traits. Participants consistently rated sycophantic chatbots as more “unbiased” than disagreeable chatbots, suggesting that people may be blind to biases in AI output that aligns with their views.",
 'unfollow': "There is considerable debate over social media’s causal effects. In a correlational study (n₁ = 1,447) and two digital field experiments (n₂ = 496, n₃ = 1,133), we examined the effect of (un)following partisan accounts. Incentivizing Twitter/X users to unfollow partisan accounts significantly improved their feelings toward the opposing party, with effects persisting for at least six months. Unfollowing also led participants to engage with more accurate news accounts, increased satisfaction with their Twitter/X feeds, and reduced the amount of political content they reported seeing a full year later, without reducing engagement. This work demonstrates the benefits of targeted approaches for improving one’s social media experience.",
 'animosity': fetch_abs('10.1073/pnas.2024292118'),
 'accuracy': fetch_abs('10.1038/s41562-023-01540-w'),
 'gpt': fetch_abs('10.1073/pnas.2308950121'),
 'peoplethink': fetch_abs('10.1177/17456916231190392'),
}
for k, v in ABS.items():
    print(k, len(v))

def add_abs(text, author_anchor, key):
    """insert abstract <p> after the authors bold in a .meta div"""
    if not ABS.get(key):
        return text
    old = f'<div class="meta"><b>{author_anchor}</b></div>'
    new = f'<div class="meta"><b>{author_anchor}</b><p class="abs">{ABS[key]}</p></div>'
    assert old in text, author_anchor[:40]
    return text.replace(old, new)

# ---------------- index_page.py ----------------
t = open('index_page.py').read()
t = add_abs(t, 'Rathje &amp; Van Bavel', 'virality')
t = add_abs(t, 'Rathje, Van Bavel &amp; van der Linden', 'animosity')
t = add_abs(t, 'Rathje, Ye, Globig, Pillai, Oldemburgo de Mello, Chen &amp; Van Bavel', 'sycophancy')
# virality cover: fill the frame
t = t.replace('<img src="images/virality-cover.jpg" alt="" onerror="this.remove()">',
              '<img class="fit-cover" src="images/virality-cover.jpg" alt="" onerror="this.remove()">')

# ---- mechanical brain ----
bstart = t.find("// ===== brain:")
bend = t.find("// ===== unified method tiles")
assert bstart > -1 and bend > bstart
mech = '''// ===== brain: circuit-board mind — chips, traces, gears; spark + drag =====
(function(){
  const cv=document.getElementById('brain'); if(!cv) return;
  const W=560,H=460,ctx=hiDPI(cv,W,H);
  const blobs=[
    [0.50,0.42,0.34,0.27],[0.28,0.46,0.17,0.20],[0.66,0.34,0.20,0.18],
    [0.76,0.60,0.13,0.11],[0.42,0.62,0.22,0.12],
  ];
  const inBrain=(x,y)=>blobs.some(([cx,cy,rx,ry])=>{
    const dx=(x-cx)/rx, dy=(y-cy)/ry; return dx*dx+dy*dy<=1;});
  const gears=[
    {x:0.42*W,y:0.40*H,r:30,teeth:10,sp:0.010,a:0},
    {x:0.63*W,y:0.31*H,r:19,teeth:8,sp:-0.0158,a:0.3},
    {x:0.56*W,y:0.60*H,r:23,teeth:9,sp:0.013,a:0.7},
  ];
  const nearGear=(x,y)=>gears.some(g=>Math.hypot(x-g.x,y-g.y)<g.r+14);
  const N=64, nodes=[];
  let guard=0;
  while(nodes.length<N && guard++<30000){
    const x=Math.random(), y=Math.random();
    if(inBrain(x,y) && !nearGear(x*W,y*H))
      nodes.push({x:x*W, y:y*H, r:3.2+Math.random()*1.8, ph:Math.random()*6.28});
  }
  nodes.push({x:0.80*W,y:0.74*H,r:3.5,ph:0},{x:0.84*W,y:0.82*H,r:3.5,ph:1});
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
  const pulses=[];
  setInterval(()=>{ if(pulses.length<6) pulses.push({e:Math.floor(Math.random()*edges.length),t:0}); }, 550);
  function trace(a,b){ // right-angle circuit trace
    const mx=a.x+(b.x-a.x)*0.5;
    ctx.beginPath(); ctx.moveTo(a.x,a.y); ctx.lineTo(mx,a.y); ctx.lineTo(mx,b.y); ctx.lineTo(b.x,b.y); ctx.stroke();
  }
  function jagged(a,b,mag){
    ctx.beginPath(); ctx.moveTo(a.x,a.y);
    for(let s=1;s<6;s++){
      const t=s/6, nx=b.y-a.y, ny=a.x-b.x, len=Math.hypot(nx,ny)||1;
      const off=(Math.random()-0.5)*mag;
      ctx.lineTo(a.x+(b.x-a.x)*t+nx/len*off, a.y+(b.y-a.y)*t+ny/len*off);
    }
    ctx.lineTo(b.x,b.y); ctx.stroke();
  }
  function gear(g,color,alpha){
    ctx.save(); ctx.translate(g.x,g.y); ctx.rotate(g.a);
    ctx.strokeStyle=color; ctx.globalAlpha=alpha; ctx.lineWidth=2; ctx.lineJoin='round';
    ctx.beginPath();
    const T=g.teeth;
    for(let i=0;i<=T*4;i++){
      const seg=Math.floor(i/2)%2, r=seg?g.r*0.8:g.r, ang=(i/(T*4))*Math.PI*2;
      i===0?ctx.moveTo(Math.cos(ang)*r,Math.sin(ang)*r):ctx.lineTo(Math.cos(ang)*r,Math.sin(ang)*r);
    }
    ctx.closePath(); ctx.stroke();
    ctx.beginPath(); ctx.arc(0,0,g.r*0.34,0,6.29); ctx.stroke();
    for(let s=0;s<3;s++){ const a2=s*Math.PI*2/3;
      ctx.beginPath(); ctx.moveTo(Math.cos(a2)*g.r*0.34,Math.sin(a2)*g.r*0.34);
      ctx.lineTo(Math.cos(a2)*g.r*0.72,Math.sin(a2)*g.r*0.72); ctx.stroke(); }
    ctx.restore(); ctx.globalAlpha=1;
  }
  function draw(t){
    ctx.clearRect(0,0,W,H);
    const accent=css('--accent')||'#1E5FD8', mutedC=css('--muted')||'#888', hair=css('--hairline')||'#ddd';
    // faint board silhouette
    ctx.save(); ctx.globalAlpha=0.3;
    blobs.forEach(([cx,cy,rx,ry])=>{ ctx.beginPath();
      ctx.ellipse(cx*W,cy*H,rx*W,ry*H,0,0,6.29); ctx.fillStyle=hair; ctx.fill(); });
    ctx.restore();
    // traces
    ctx.lineJoin='round';
    edges.forEach(([i,j])=>{
      const a=nodes[i],b=nodes[j];
      const d=distToSeg(mouse,a,b);
      if(d<42){
        ctx.lineWidth=1.8; ctx.strokeStyle=accent;
        ctx.shadowColor=accent; ctx.shadowBlur=10;
        jagged(a,b,7); ctx.shadowBlur=0;
      } else {
        ctx.lineWidth=1.2; ctx.strokeStyle=mutedC; ctx.globalAlpha=0.35;
        trace(a,b); ctx.globalAlpha=1;
      }
    });
    // signal pulses along traces (follow the elbow path)
    for(let k=pulses.length-1;k>=0;k--){
      const p=pulses[k]; p.t+=0.02;
      if(p.t>=1){pulses.splice(k,1);continue;}
      const [i,j]=edges[p.e], a=nodes[i], b=nodes[j], mx=a.x+(b.x-a.x)*0.5;
      const L1=Math.abs(mx-a.x), L2=Math.abs(b.y-a.y), L3=Math.abs(b.x-mx), L=L1+L2+L3||1;
      let d=p.t*L, x, y;
      if(d<L1){ x=a.x+Math.sign(mx-a.x)*d; y=a.y; }
      else if(d<L1+L2){ x=mx; y=a.y+Math.sign(b.y-a.y)*(d-L1); }
      else { x=mx+Math.sign(b.x-mx)*(d-L1-L2); y=b.y; }
      ctx.beginPath(); ctx.arc(x,y,2.2,0,6.29);
      ctx.fillStyle=accent; ctx.globalAlpha=0.85; ctx.fill(); ctx.globalAlpha=1;
    }
    // gears
    gears.forEach((g,gi)=>{ if(!reduceMotion) g.a+=g.sp; gear(g, gi===1?accent:mutedC, gi===1?0.75:0.5); });
    // chips
    nodes.forEach(n=>{
      const d=Math.hypot(mouse.x-n.x, mouse.y-n.y);
      const hot=d<46;
      const r=n.r+(hot?2:Math.sin(t/700+n.ph)*0.4);
      ctx.fillStyle=hot?accent:mutedC;
      if(hot){ctx.shadowColor=accent;ctx.shadowBlur=12;}
      ctx.beginPath(); ctx.roundRect(n.x-r,n.y-r,r*2,r*2,1.5); ctx.fill();
      ctx.shadowBlur=0;
    });
    if(!reduceMotion) requestAnimationFrame(draw);
  }
  requestAnimationFrame(draw);
})();

'''
t = t[:bstart] + mech + t[bend:]
t = t.replace('fire neurons with your cursor · drag them to rewire',
              'spark the circuits with your cursor · drag the chips to rewire')
open('index_page.py','w').write(t)

# ---------------- build_site.py (publications page) ----------------
b = open('build_site.py').read()
b = add_abs(b, 'Rathje &amp; Van Bavel', 'virality')
b = add_abs(b, 'Rathje, Van Bavel &amp; van der Linden', 'animosity')
b = add_abs(b, 'Rathje*, Mirea* et al.', 'gpt')
b = add_abs(b, 'Rathje, Ye et al.', 'sycophancy')
b = add_abs(b, 'Rathje, Roozenbeek, Van Bavel &amp; van der Linden', 'accuracy')
b = add_abs(b, 'Rathje, Robertson, Brady &amp; Van Bavel', 'peoplethink')
b = add_abs(b, 'Rathje, He, Harjani, Roozenbeek, Pretus, Gray, van der Linden &amp; Van Bavel', 'unfollow')
b = b.replace('<img src="images/virality-cover.jpg" alt="Trends in Cognitive Sciences cover" onerror="this.remove()">',
              '<img class="fit-cover" src="images/virality-cover.jpg" alt="Trends in Cognitive Sciences cover" onerror="this.remove()">')
# two-column layout: social left, AI right
b = b.replace('    <div class="pub-group">\n      <h2>Social Media</h2>',
              '    <div class="pub-cols">\n    <div class="pub-group">\n      <h2>Social Media</h2>')
b = b.replace('''    <p class="see-all"><a href="https://scholar.google.com/citations?user=tw5jvawAAAAJ" target="_blank" rel="noopener">All 45+ publications on Google Scholar →</a></p>''',
              '''    </div>
    <p class="see-all"><a href="https://scholar.google.com/citations?user=tw5jvawAAAAJ" target="_blank" rel="noopener">All 45+ publications on Google Scholar →</a></p>''')
open('build_site.py','w').write(b)

# ---------------- style.css: sans-serif + zoom + abs + columns ----------------
c = open('style.css').read()
c = c.replace("font-family:'Fraunces',Georgia,serif;line-height:1.12;text-wrap:balance;font-weight:600",
              "font-family:'Archivo',system-ui,sans-serif;line-height:1.12;text-wrap:balance;font-weight:700;letter-spacing:-0.02em")
c = c.replace("'Fraunces',serif", "'Archivo',system-ui,sans-serif")
c = c.replace('.key-pub .cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#fff}',
              '.key-pub .cover img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:#fff;transform:scale(1.18)}')
c += """

/* zoomed cover variants + abstracts + pub columns */
.key-pub .cover img.fit-cover{object-fit:cover;transform:none}
.key-pub .abs{font-size:13px;line-height:1.55;color:var(--muted);margin-top:8px;
  display:-webkit-box;-webkit-line-clamp:8;-webkit-box-orient:vertical;overflow:hidden}
.pub-cols{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}
@media(max-width:880px){.pub-cols{grid-template-columns:1fr}}
"""
open('style.css','w').write(c)

# fonts link: Archivo up to 800, drop Fraunces
h = open('_head.tmpl').read()
h = h.replace("css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Archivo:wght@400;500;600;700&display=swap",
              "css2?family=Archivo:wght@400;500;600;700;800&display=swap")
open('_head.tmpl','w').write(h)
print('ALL PATCHED')
