#!/usr/bin/env python3
"""Assemble the Psychology of Technology Lab static site from templates + page bodies.
Run: python3 build_site.py   (re-run any time you edit a body below)"""
import pathlib

ROOT = pathlib.Path(__file__).parent
HEAD = (ROOT / "_head.tmpl").read_text()
NAV = (ROOT / "_nav.tmpl").read_text()
FOOT = (ROOT / "_foot.tmpl").read_text()

def page(fname, title, desc, body, extra_script=""):
    nav = NAV if fname == "index.html" else NAV.replace(f'href="{fname}"', f'href="{fname}" class="active keep"')
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
{HEAD}</head>
<body>
{nav}
{body}
{FOOT}{extra_script}
</body>
</html>"""
    (ROOT / fname).write_text(html)
    print("wrote", fname)

# ---------------------------------------------------------------- index
INDEX_BODY = """
<header class="hero wrap" id="top">
  <div class="hero-grid">
    <div>
      <div class="eyebrow">Carnegie Mellon University · Human-Computer Interaction Institute</div>
      <h1>How technology rewires <em>what we believe</em> — and how we feel about each other.</h1>
      <p class="lede">The Psychology of Technology Lab studies the psychological impact of emerging
        technologies like social media and AI: why outrage goes viral, why misinformation sticks,
        how sycophantic chatbots shape our minds — and how all of it can be designed better.</p>
      <p class="director">Directed by <strong>Steve Rathje</strong>, Assistant Professor,
        School of Computer Science (courtesy: Social &amp; Decision Sciences)</p>
      <div class="cta-row">
        <a class="btn primary" href="join.html">Join the lab</a>
        <a class="btn ghost" href="#research">Explore our research</a>
      </div>
    </div>
    <div class="demo" aria-label="Interactive demo of the unfollow experiment">
      <div class="demo-title">
        <span>Live demo · a field experiment</span>
        <span id="demoState">before</span>
      </div>
      <div class="meter">
        <div class="meter-label"><span>Out-party animosity</span><b id="meterVal">high</b></div>
        <div class="meter-bar"><div class="meter-fill" id="meterFill"></div></div>
      </div>
      <div id="feed">
        <div class="post" data-partisan>
          <div class="who">@OutrageDaily <span class="tag partisan">partisan</span></div>
          <p>You won't BELIEVE what the other side just did. They are destroying everything…</p>
          <div class="stats">🔁 <span class="tick" data-base="12400">12,400</span> · ❤️ <span class="tick" data-base="31000">31,000</span></div>
        </div>
        <div class="post" data-partisan>
          <div class="who">@HotTakeCentral <span class="tag partisan">partisan</span></div>
          <p>If you still support *them* after this week, you are beyond saving.</p>
          <div class="stats">🔁 <span class="tick" data-base="8300">8,300</span> · ❤️ <span class="tick" data-base="19500">19,500</span></div>
        </div>
        <div class="post">
          <div class="who">@wonderofscience <span class="tag science">science</span></div>
          <p>The James Webb telescope just captured a star being born, 1,300 light-years away. 🌌</p>
          <div class="stats">🔁 2,100 · ❤️ 9,800</div>
        </div>
      </div>
      <button class="btn primary" id="unfollowBtn">Unfollow partisan accounts</button>
      <p class="demo-caption">In our year-long field experiment (n = 1,133), unfollowing partisan
        accounts improved feelings toward the opposing party for at least six months.
        <a href="https://doi.org/10.31234/osf.io/acbwg" target="_blank" rel="noopener">Read the study →</a></p>
    </div>
  </div>
</header>

<div class="wrap">
  <div class="stats-strip">
    <div class="stat"><b data-count="45">0</b><span>peer-reviewed papers</span></div>
    <div class="stat"><b data-count="7485">0</b><span>citations</span></div>
    <div class="stat"><b data-count="76">0</b><span>countries in our global study</span></div>
    <div class="stat"><b data-count="1000000" data-suffix="+">0</b><span>followers reached on @stevepsychology</span></div>
  </div>
</div>

<section id="research">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Research</div>
      <h2>Four questions we keep asking</h2>
      <p>We combine large-scale field experiments, computational social science, and
         psychological theory to understand technology's causal effects — not just its correlations.</p>
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
        <div class="links"><a href="https://doi.org/10.31234/osf.io/acbwg" target="_blank" rel="noopener">Preprint (revision at Nature Communications)</a></div>
      </div>
      <div class="card">
        <h3>What does AI do to our minds?</h3>
        <p>Sycophantic AI chatbots that agree with everything we say can amplify attitude extremity
           and overconfidence. We also build LLM-based methods — like using GPT for multilingual
           psychological text analysis — to advance the science itself.</p>
        <div class="links"><a href="https://osf.io/preprints/psyarxiv/vmyek_v1" target="_blank" rel="noopener">Preprint (revision at Nature)</a> ·
          <a href="https://doi.org/10.1073/pnas.2308950121" target="_blank" rel="noopener">PNAS 2024</a></div>
      </div>
      <div class="card">
        <h3>Is it the same everywhere?</h3>
        <p>Most social media research studies WEIRD samples. Our registered report at Nature tests
           the causal impact of social media abstention across dozens of countries, with a global
           team of collaborators.</p>
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
        <div class="cover alt1"><span class="journal">PNAS · 2021</span>
          <span class="ctitle">Out-group animosity drives engagement on social media</span></div>
        <div class="meta"><b>Rathje, Van Bavel &amp; van der Linden</b>Attacking the other side is the strongest predictor of going viral.</div>
      </a>
      <a class="key-pub" href="https://osf.io/preprints/psyarxiv/vmyek_v1" target="_blank" rel="noopener">
        <div class="cover alt2"><span class="journal">Revision at Nature</span>
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
let ticking=setInterval(()=>{document.querySelectorAll('.tick').forEach(el=>{
  const v=+el.dataset.base+Math.floor(Math.random()*90);
  el.dataset.base=v;el.textContent=v.toLocaleString();});},900);
document.getElementById('unfollowBtn').addEventListener('click',function(){
  clearInterval(ticking);
  document.querySelectorAll('[data-partisan]').forEach(p=>p.classList.add('gone'));
  document.getElementById('meterFill').style.width='38%';
  document.getElementById('meterVal').textContent='lower';
  document.getElementById('demoState').textContent='6 months later';
  const feed=document.getElementById('feed');
  const el=document.createElement('div');
  el.className='post new';
  el.innerHTML='<div class="who">@NASA <span class="tag science">science</span></div>'+
    "<p>Today's view of Earth from the ISS. It's one planet, seen from far enough away. 🌍</p>"+
    '<div class="stats">🔁 4,700 · ❤️ 22,300</div>';
  feed.appendChild(el);
  this.textContent='✓ Feelings toward the out-party: improved';
  this.disabled=true;this.style.background='var(--good)';});
</script>"""

# ---------------------------------------------------------------- publications
def pub(venue, title, url, authors):
    link = f'<a href="{url}" target="_blank" rel="noopener">{title}</a>' if url else title
    return f'''<div class="pub"><div class="venue">{venue}</div>
      <div><div class="title">{link}</div>
      <div class="authors">{authors}</div></div></div>'''

SOCIAL = "".join([
 pub("Nature · RR", "Testing the causal impact of social media usage around the globe",
     "https://osf.io/preprints/psyarxiv/ujtxa_v1",
     "Rathje*, Asimovic*, Ventura*, Mughal, Karsting, Robertson, Barrie, The Global Social Media Experiment Team, Tucker &amp; Van Bavel — Registered Report, In-Principle Acceptance at Nature"),
 pub("TiCS · 2025", "The psychology of virality", "https://doi.org/10.1016/j.tics.2025.06.014",
     "Rathje &amp; Van Bavel — Trends in Cognitive Sciences"),
 pub("Nat Comms · R&amp;R", "Unfollowing partisan accounts reduces out-party animosity and increases social media satisfaction",
     "https://doi.org/10.31234/osf.io/acbwg",
     "Rathje, He, Harjani, Roozenbeek, Pretus, Gray, van der Linden &amp; Van Bavel — invited revision at Nature Communications"),
 pub("Nature · 2024", "To tackle social-media harms, mandate data access for researchers",
     "https://doi.org/10.1038/d41586-024-02853-0", "Rathje — Nature (World View)"),
 pub("PPS · 2023", "People think that social media platforms do (but should not) amplify divisive content",
     "https://doi.org/10.1177/17456916231190392",
     "Rathje, Robertson, Brady &amp; Van Bavel — Perspectives on Psychological Science"),
 pub("NHB · 2023", "Accuracy and social motivations shape belief in (mis)information",
     "https://doi.org/10.1038/s41562-023-01540-w",
     "Rathje, Roozenbeek, Van Bavel &amp; van der Linden — Nature Human Behaviour"),
 pub("PNAS Nexus · 2022", "Social media behavior is associated with vaccine hesitancy",
     "https://doi.org/10.1093/pnasnexus/pgac207",
     "Rathje, He, Roozenbeek, Van Bavel &amp; van der Linden — PNAS Nexus"),
 pub("Sci Adv · 2022", "Psychological inoculation improves resilience against misinformation on social media",
     "https://doi.org/10.1126/sciadv.abo6254",
     "Roozenbeek, van der Linden, Goldberg, Rathje &amp; Lewandowsky — Science Advances"),
 pub("PNAS · 2021", "Out-group animosity drives engagement on social media",
     "https://doi.org/10.1073/pnas.2024292118",
     "Rathje, Van Bavel &amp; van der Linden — Proceedings of the National Academy of Sciences"),
 pub("TiCS · 2021", "How social media shapes polarization", "https://doi.org/10.1016/j.tics.2021.07.013",
     "Van Bavel, Rathje, Harris, Robertson &amp; Sternisko — Trends in Cognitive Sciences"),
])

AI = "".join([
 pub("Nature · R&amp;R", "The Impact of Sycophantic AI on Attitudes and Decisions",
     "https://osf.io/preprints/psyarxiv/vmyek_v1",
     "Rathje, Ye, Globig, Pillai, Oldemburgo de Mello, Chen &amp; Van Bavel — invited revision at Nature"),
 pub("NHB · 2026", "A reporting checklist for LLMs in behavioural science", "",
     "Feuerriegel, Barrie, Crockett, Globig, McLoughlin, Mirea, Spirling, Yang, … Rathje &amp; Ribeiro — Nature Human Behaviour"),
 pub("Nat Comp Sci · 2025", "Generative language models exhibit social identity biases",
     "https://arxiv.org/abs/2310.15819",
     "Hu, Kyrychenko, Rathje, Collier, van der Linden &amp; Roozenbeek — Nature Computational Science"),
 pub("PNAS · 2024", "GPT is an effective tool for multilingual psychological text analysis",
     "https://doi.org/10.1073/pnas.2308950121",
     "Rathje*, Mirea*, Sucholutsky, Marjieh, Robertson &amp; Van Bavel — Proceedings of the National Academy of Sciences"),
 pub("BJP · 2024", "Artificial intelligence chatbots mimic human collective behaviour",
     "https://doi.org/10.1111/bjop.12764",
     "He, Wallis, Andres &amp; Rathje — British Journal of Psychology"),
 pub("NRP · 2024", "Using natural language processing to analyze text data in behavioral science",
     "https://doi.org/10.1038/s44159-024-00392-z",
     "Feuerriegel, Maarouf, Bär, … Rathje, … Van Bavel — Nature Reviews Psychology"),
])

PUBS_BODY = f"""
<div class="wrap page-hero">
  <div class="eyebrow">Publications</div>
  <h1>What we've found</h1>
  <p>Selected work, organized by topic. For the complete list, see
     <a href="https://scholar.google.com/citations?user=tw5jvawAAAAJ" target="_blank" rel="noopener">Google Scholar</a>.</p>
</div>
<section style="padding-top:36px">
  <div class="wrap">
    <div class="key-pubs" style="margin-bottom:64px">
      <a class="key-pub" href="https://doi.org/10.1016/j.tics.2025.06.014" target="_blank" rel="noopener">
        <div class="cover"><img src="images/virality-cover.jpg" alt="Trends in Cognitive Sciences cover" onerror="this.remove()">
          <span class="journal">Trends in Cognitive Sciences · 2025</span>
          <span class="ctitle">The Psychology of Virality</span></div>
        <div class="meta"><b>Rathje &amp; Van Bavel</b>Why some information spreads, online and offline. Among the journal's most-downloaded papers of 2025.</div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1073/pnas.2024292118" target="_blank" rel="noopener">
        <div class="cover alt1"><span class="journal">PNAS · 2021</span>
          <span class="ctitle">Out-group animosity drives engagement</span></div>
        <div class="meta"><b>Rathje, Van Bavel &amp; van der Linden</b>2.7M posts: attacking the out-group predicts virality.</div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1073/pnas.2308950121" target="_blank" rel="noopener">
        <div class="cover alt2"><span class="journal">PNAS · 2024</span>
          <span class="ctitle">GPT is an effective tool for multilingual psychological text analysis</span></div>
        <div class="meta"><b>Rathje*, Mirea* et al.</b>LLMs as instruments for psychological science.</div>
      </a>
      <a class="key-pub" href="https://osf.io/preprints/psyarxiv/ujtxa_v1" target="_blank" rel="noopener">
        <div class="cover alt1"><span class="journal">Nature · Registered Report</span>
          <span class="ctitle">Testing the causal impact of social media around the globe</span></div>
        <div class="meta"><b>Rathje*, Asimovic*, Ventura* et al.</b>A many-country deactivation experiment.</div>
      </a>
      <a class="key-pub" href="https://osf.io/preprints/psyarxiv/vmyek_v1" target="_blank" rel="noopener">
        <div class="cover"><span class="journal">Nature · invited revision</span>
          <span class="ctitle">The Impact of Sycophantic AI on Attitudes and Decisions</span></div>
        <div class="meta"><b>Rathje, Ye et al.</b>Agreeable chatbots amplify extremity and overconfidence.</div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1038/s41562-023-01540-w" target="_blank" rel="noopener">
        <div class="cover alt2"><span class="journal">Nature Human Behaviour · 2023</span>
          <span class="ctitle">Accuracy and social motivations shape belief in (mis)information</span></div>
        <div class="meta"><b>Rathje, Roozenbeek, Van Bavel &amp; van der Linden</b>Paying people to be accurate reduces partisan bias.</div>
      </a>
    </div>
    <div class="pub-group">
      <h2>Social Media</h2>
      <p class="group-note">Virality, polarization, misinformation, and interventions to fix our feeds.</p>
      {SOCIAL}
    </div>
    <div class="pub-group">
      <h2>Artificial Intelligence</h2>
      <p class="group-note">How humans interact with AI — and how AI can advance psychological science.</p>
      {AI}
    </div>
    <p class="see-all"><a href="https://scholar.google.com/citations?user=tw5jvawAAAAJ" target="_blank" rel="noopener">All 45+ publications on Google Scholar →</a></p>
  </div>
</section>
"""

# ---------------------------------------------------------------- people
PEOPLE_BODY = """
<div class="wrap page-hero">
  <div class="eyebrow">People</div>
  <h1>The lab</h1>
  <p>We're a new lab at Carnegie Mellon's Human-Computer Interaction Institute — and growing.
     <a href="join.html">Come join us.</a></p>
</div>
<section style="padding-top:20px">
  <div class="wrap">
    <div class="bio">
      <div class="avatar">SR</div>
      <div>
        <h3>Steve Rathje</h3>
        <div class="role">Lab Director · Assistant Professor of Human-Computer Interaction</div>
        <p>Steve Rathje is an Assistant Professor in the School of Computer Science at Carnegie
           Mellon University, with a courtesy appointment in Social and Decision Sciences. Before
           CMU, he was an NSF and AXA postdoctoral fellow at New York University. He received his
           PhD from the University of Cambridge as a Gates Cambridge Scholar, and studied Psychology
           and Symbolic Systems at Stanford. His research on virality, misinformation, polarization,
           and human–AI interaction has appeared in Nature, Science, PNAS, and Nature Human
           Behaviour, and has been covered by the New York Times, BBC, and 60 Minutes. He was named
           to the Forbes 30 Under 30 list and received the SPSP SAGE Emerging Scholar Award and the
           APS Rising Star Award. He also runs @stevepsychology, a science-communication channel
           with over one million followers.</p>
        <div class="bio-links">
          <a href="https://stevenrathje.com" target="_blank" rel="noopener">Website</a>
          <a href="https://www.hcii.cmu.edu/people/steve-rathje" target="_blank" rel="noopener">CMU page</a>
          <a href="https://scholar.google.com/citations?user=tw5jvawAAAAJ" target="_blank" rel="noopener">Scholar</a>
          <a href="mailto:srathje@andrew.cmu.edu">Email</a>
        </div>
      </div>
    </div>
    <div class="bio">
      <div class="avatar">MY</div>
      <div>
        <h3>Meryl Ye</h3>
        <div class="role">PhD Student (2025–)</div>
        <p>Meryl is a doctoral student and Carnegie Mellon Samson Graduate Fellow. Her research
           examines human–AI interaction, including the psychological consequences of AI sycophancy —
           she is a co-author on the lab's sycophantic AI paper (invited revision at Nature).
           <!-- EDIT: add Meryl's background, prior degrees, and interests --></p>
      </div>
    </div>
    <div class="bio">
      <div class="avatar">KH</div>
      <div>
        <h3>Kevin Hernandez</h3>
        <div class="role">PhD Student (2026–)</div>
        <p>Kevin is an incoming doctoral student studying the psychology of emerging technologies.
           <!-- EDIT: add Kevin's background and interests --></p>
      </div>
    </div>
    <div class="bio">
      <div class="avatar">HK</div>
      <div>
        <h3>Hannah Karsting</h3>
        <div class="role">Research Assistant (2025–)</div>
        <p>Hannah supports the lab's global social media experiment and is a co-author on the
           registered report at Nature testing the causal impact of social media around the globe.
           <!-- EDIT: add Hannah's background --></p>
      </div>
    </div>
    <div class="section-head" style="margin-top:56px">
      <h2 style="font-size:26px">Alumni &amp; past mentees</h2>
    </div>
    <ul class="media-list" style="padding-left:0">
      <li><b>Sarah Mughal</b> <span>— Research Assistant, NYU (2023–2025)</span></li>
      <li><b>Jingzhu Chen</b> <span>— Research Assistant, NYU (2024–2025)</span></li>
      <li><b>Shaye Ann-Hopkins</b> <span>— Research Assistant, Duke University (2024)</span></li>
      <li><b>James K. He</b> <span>— Research Assistant, University of Cambridge (2022–2024)</span></li>
    </ul>
  </div>
</section>
"""

# ---------------------------------------------------------------- media
MEDIA_BODY = """
<div class="wrap page-hero">
  <div class="eyebrow">Media</div>
  <h1>The lab, in public</h1>
  <p>We believe science communication is part of the job — from TikTok explainers with over a
     million followers to TV, podcasts, and op-eds.</p>
</div>
<section style="padding-top:28px">
  <div class="wrap">
    <div class="section-head"><h2 style="font-size:26px">Watch</h2></div>
    <div class="video-grid">
      <!-- EDIT: paste your YouTube embed URLs below (youtube.com/embed/VIDEO_ID) -->
      <iframe src="https://www.youtube.com/embed/REPLACE_ME_1" title="Lab video 1" allowfullscreen loading="lazy"></iframe>
      <iframe src="https://www.youtube.com/embed/REPLACE_ME_2" title="Lab video 2" allowfullscreen loading="lazy"></iframe>
    </div>
    <p class="see-all" style="margin-bottom:56px"><a href="https://www.tiktok.com/@stevepsychology" target="_blank" rel="noopener">More on @stevepsychology (1M+ followers) →</a></p>

    <div class="section-head"><h2 style="font-size:26px">TV &amp; podcasts</h2></div>
    <ul class="media-list" style="padding-left:0;margin-bottom:56px">
      <li><b>Programmed By AI: Conspiracies and Coverups</b> <span>— Discovery Channel (2026)</span></li>
      <li><b>The Science Behind Why Social Media Makes Us Miserable</b> <span>— Andrew Yang Podcast (2025)</span></li>
      <li><b>Discussion of "influencers" and health information</b> <span>— CBS Mornings (2025)</span></li>
      <li><b>The feedback loop of social media</b> <span>— 60 Minutes (2022)</span></li>
      <li><b>Why is the U.S. Media So Negative?</b> <span>— Freakonomics (2021)</span></li>
      <li><b>Guilty as charged: how we contribute to polarizing content</b> <span>— APS Under the Cortex (2023)</span></li>
    </ul>

    <div class="section-head"><h2 style="font-size:26px">Writing</h2></div>
    <ul class="media-list" style="padding-left:0;margin-bottom:56px">
      <li><b>Why we click on stuff we know we won't like</b> <span>— Boston Globe op-ed (2023)</span></li>
      <li><b>Why Facebook really, really doesn't want to prevent extremism</b> <span>— Washington Post op-ed (2021)</span></li>
      <li><b>Why theater makes us better people. Bring it back.</b> <span>— Los Angeles Times op-ed (2021)</span></li>
      <li><b>Words Matter</b> <span>— ongoing column at Psychology Today (2018–)</span></li>
    </ul>

    <div class="section-head"><h2 style="font-size:26px">Press coverage</h2></div>
    <p class="press-logos">Our research has been covered by the <strong>New York Times</strong> ·
      <strong>Washington Post</strong> · <strong>BBC</strong> · <strong>NBC</strong> ·
      <strong>Wall Street Journal</strong> · <strong>The Atlantic</strong> ·
      <strong>The Guardian</strong> · <strong>60 Minutes</strong> and more.</p>
  </div>
</section>
"""

# ---------------------------------------------------------------- join
JOIN_BODY = """
<div class="wrap page-hero">
  <div class="eyebrow">Work With Us</div>
  <h1>Study the technologies that are studying you.</h1>
  <p>We look for people who care about rigorous causal methods <em>and</em> real-world impact.
     The lab sits at the intersection of psychology, HCI, and computational social science —
     people from any of those homes are welcome.</p>
</div>
<section style="padding-top:28px">
  <div class="wrap">
    <div class="cards">
      <div class="card">
        <h3>Prospective PhD students</h3>
        <p>Apply to the <a href="https://www.hcii.cmu.edu/academics/hcii-phd" target="_blank" rel="noopener">HCII PhD program</a>
           and mention the Psychology of Technology Lab in your statement. We admit students with
           backgrounds in psychology, HCI, computer science, and adjacent fields. Feel free to email
           first — even if you're not sure your idea fits.</p>
      </div>
      <div class="card">
        <h3>CMU undergrad &amp; masters students</h3>
        <p>We regularly take research assistants for course credit or pay, on projects spanning
           social media field experiments, LLM-based text analysis, and human–AI interaction studies.
           Email a CV and a couple of sentences about what interests you.</p>
      </div>
      <div class="card">
        <h3>Postdocs</h3>
        <p>Funded openings are posted here when available. If you have your own funding source in
           mind (NSF SBE, fellowships, international schemes), we're glad to sponsor strong
           applications — reach out early.</p>
      </div>
      <div class="card">
        <h3>Collaborators, journalists &amp; everyone else</h3>
        <p>We collaborate widely with scientists, platforms, and policymakers, and we talk to the
           press about social media and AI. If our work is relevant to yours, get in touch.</p>
      </div>
    </div>
    <div class="cta-row" style="margin-top:36px">
      <a class="btn primary" href="mailto:srathje@andrew.cmu.edu">Email the lab</a>
      <a class="btn ghost" href="people.html">Meet the team</a>
    </div>
  </div>
</section>
"""

page("index.html", "Psychology of Technology Lab — Carnegie Mellon University",
     "The Psychology of Technology Lab at Carnegie Mellon University, led by Steve Rathje, studies how social media and AI shape belief, emotion, and division.",
     INDEX_BODY, INDEX_SCRIPT)
page("publications.html", "Publications — Psychology of Technology Lab",
     "Key publications from the Psychology of Technology Lab, organized by social media and AI.",
     PUBS_BODY)
page("people.html", "People — Psychology of Technology Lab",
     "Meet the members of the Psychology of Technology Lab at Carnegie Mellon University.",
     PEOPLE_BODY)
page("media.html", "Media — Psychology of Technology Lab",
     "TV appearances, podcasts, videos, and press coverage from the Psychology of Technology Lab.",
     MEDIA_BODY)
page("join.html", "Work With Us — Psychology of Technology Lab",
     "Join the Psychology of Technology Lab: PhD, research assistant, and collaboration opportunities.",
     JOIN_BODY)
print("done")
