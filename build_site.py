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

from index_page import INDEX_BODY, INDEX_SCRIPT
from kp_cards import KP_GRID, KP_TAP_JS

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
 pub("Preprint", "Unfollowing partisan accounts reduces out-party animosity and increases social media satisfaction",
     "https://doi.org/10.31234/osf.io/acbwg",
     "Rathje, He, Harjani, Roozenbeek, Pretus, Gray, van der Linden &amp; Van Bavel — preprint under review"),
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
 pub("Preprint", "The Impact of Sycophantic AI on Attitudes and Decisions",
     "https://osf.io/preprints/psyarxiv/vmyek_v1",
     "Rathje, Ye, Globig, Pillai, Oldemburgo de Mello, Chen &amp; Van Bavel — preprint under review"),
 pub("Preprint", "Individual-level interventions against sycophantic AI reduce its appeal but not its persuasiveness",
     "https://arxiv.org/abs/2607.25166",
     "Ye, Kraut &amp; Rathje — preprint"),
 pub("Preprint", "What counts as AI sycophancy? A taxonomy and expert survey of a fragmented construct",
     "https://arxiv.org/abs/2605.21778",
     "Ye, Ibrahim, Bo, Cheng, Mattsson, Vennemeyer, Kraut &amp; Rathje — preprint"),
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
  <h1>Key Publications</h1>
  <p>All publications and preprints on
     <a href="https://scholar.google.com/citations?user=tw5jvawAAAAJ" target="_blank" rel="noopener">Google Scholar</a>.</p>
</div>
<section style="padding-top:36px">
  <div class="wrap">
    <div class="kp-grid" style="margin-bottom:72px">
{KP_GRID}
    </div>
    <div class="filter-pills" role="tablist" aria-label="Filter publications">
      <button data-f="all" class="active">All</button>
      <button data-f="social">Social Media</button>
      <button data-f="ai">AI</button>
    </div>
    <div class="pub-cols" id="pubCols">
    <div class="pub-group" id="group-social">
      <h2>Social Media</h2>
      <p class="group-note">Virality, polarization, misinformation, and interventions to fix our feeds.</p>
      {SOCIAL}
    </div>
    <div class="pub-group" id="group-ai">
      <h2>Artificial Intelligence</h2>
      <p class="group-note">How humans interact with AI — and how AI can advance psychological science.</p>
      {AI}
    </div>
    </div>
    <p class="see-all"><a href="https://scholar.google.com/citations?user=tw5jvawAAAAJ" target="_blank" rel="noopener">All 45+ publications on Google Scholar →</a></p>
  </div>
</section>
"""

# ---------------------------------------------------------------- people
PEOPLE_BODY = """
<div class="wrap page-hero">
  <div class="eyebrow">People</div>
  <h1>Who we are</h1>
</div>
<section style="padding-top:20px">
  <div class="wrap">
    <div class="bio">
      <div class="avatar"><img src="images/steve.jpg" alt="Steve Rathje" onerror="this.parentNode.textContent='SR'"></div>
      <div>
        <h3>Steve Rathje</h3>
        <div class="role">Lab Director · Assistant Professor of Human-Computer Interaction</div>
        <p>Steve Rathje is an Assistant Professor of Human-Computer Interaction in the School of
           Computer Science at Carnegie Mellon University, with a courtesy appointment in the
           Department of Social and Decision Sciences. Previously, he was an NSF postdoctoral fellow
           at NYU. He received his PhD from the University of Cambridge, where he was a Gates
           Cambridge Scholar. Before that, he studied Psychology and Symbolic Systems as an
           undergraduate at Stanford University. He has published more than 40 academic papers on
           the psychology of technology in journals such as Nature, Science, and PNAS, and has
           received more than $3.5 million in grant funding for his work. He was included on the
           2025 Forbes 30 Under 30 list, received the SAGE Emerging Scholar Award from the Society
           for Personality and Social Psychology in 2026, and was named a Rising Star by the
           Association for Psychological Science in 2024. His dissertation received the Psychology
           of Technology Dissertation Award and was a finalist for the SESP Dissertation Award.
           Steve has discussed his work on CBS Mornings, the Discovery Channel, the Freakonomics
           podcast, and more. He has presented his work at the Aspen Ideas Festival, VivaTech, and
           several universities, including Harvard, Stanford, MIT, Brown, Columbia, Carnegie Mellon,
           USC, NYU, and the University of Cambridge. Steve is also interested in science
           communication, and his writing has appeared in the Washington Post, the Guardian, the
           New York Times, the Los Angeles Times, the Boston Globe, and Psychology Today. He also
           makes science communication videos on TikTok under the name
           <a href="https://www.tiktok.com/@stevepsychology" target="_blank" rel="noopener">@stevepsychology</a>
           and has more than 1 million followers.</p>
        <p style="margin-top:12px"><a href="https://stevenrathje.com/media/Steve%20Rathje%20CV%202026.pdf" target="_blank" rel="noopener">Curriculum Vitae →</a></p>
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
           she is a co-author on the lab's sycophantic AI paper.
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
    <div class="section-head"><h2 style="font-size:26px">Selected Media Appearances</h2></div>
    <div class="video-grid">
      <figure class="vid">
        <iframe src="https://www.youtube.com/embed/lLvywTb7tf0" title="CBS Mornings appearance" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
        <figcaption><b>CBS Mornings</b></figcaption>
      </figure>
      <figure class="vid">
        <iframe src="https://www.youtube.com/embed/5VorYAlj3OQ" title="Discovery Channel appearance" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
        <figcaption><b>Discovery Channel</b></figcaption>
      </figure>
      <figure class="vid">
        <iframe src="https://www.youtube.com/embed/qF_ic4m_4h4?start=2296" title="Aspen Ideas Festival appearance" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
        <figcaption><b>Aspen Ideas Festival</b></figcaption>
      </figure>
    </div>
    <div class="section-head"><h2 style="font-size:26px">Science Communication Videos</h2></div>
    <div class="tiktok-grid">
      <figure class="tt">
        <iframe src="https://www.tiktok.com/embed/v2/7168636914830970118" title="TikTok by @stevepsychology" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
      </figure>
      <figure class="tt">
        <iframe src="https://www.tiktok.com/embed/v2/7207531638555741446" title="TikTok by @stevepsychology" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
      </figure>
      <figure class="tt">
        <iframe src="https://www.tiktok.com/embed/v2/7568992502691138839" title="TikTok by @stevepsychology" allowfullscreen loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
      </figure>
    </div>
    <p class="see-all" style="margin-bottom:56px"><a href="https://www.tiktok.com/@stevepsychology" target="_blank" rel="noopener">More on @stevepsychology (1M+ followers) →</a></p>
    <div class="section-head"><h2 style="font-size:26px">Podcasts</h2></div>
    <a class="podcast-banner" href="https://freakonomics.com/podcast/why-is-u-s-media-so-negative/" target="_blank" rel="noopener">
      <span class="podcast-eyebrow">Podcast</span>
      <span class="podcast-title">Freakonomics Radio</span>
      <span class="podcast-sub">"Why Is U.S. Media So Negative?" — listen&nbsp;→</span>
    </a>
    <a class="podcast-banner" href="https://open.spotify.com/episode/7CoKK7v3p1kAYAwRi3tPXU" target="_blank" rel="noopener">
      <span class="podcast-eyebrow">Podcast</span>
      <span class="podcast-title">Stanford Psychology Podcast</span>
      <span class="podcast-sub">listen on Spotify&nbsp;→</span>
    </a>
    <a class="podcast-banner" href="https://www.youtube.com/watch?v=9uNoCf8GiY8&t=3357s" target="_blank" rel="noopener">
      <span class="podcast-eyebrow">Podcast</span>
      <span class="podcast-title">The Downside with Gianmarco Soresi</span>
      <span class="podcast-sub">"The Stanford Podcast Experiment" — watch on YouTube&nbsp;→</span>
    </a>

    
    <div class="section-head"><h2 style="font-size:26px">Op-Eds</h2></div>
    <ul class="media-list" style="padding-left:0;margin-bottom:56px">
      <li><b><a href="https://www.nytimes.com/2024/08/14/opinion/new-york-times-endorsements.html" target="_blank" rel="noopener">Re “Why Schools Are Pushing Laws to Ban Smartphones” (Business, Aug. 14)</a></b> <span>— New York Times letter to the editor (2024)</span></li>
      <li><b><a href="https://www.bostonglobe.com/2023/12/07/opinion/rathje-van-bavel-paradox-of-internet-virality/" target="_blank" rel="noopener">Why we click on stuff we know we won't like</a></b> <span>— Boston Globe op-ed (2023)</span></li>
      <li><b><a href="https://www.washingtonpost.com/politics/2021/07/13/why-facebook-really-really-doesnt-want-discourage-extremism/" target="_blank" rel="noopener">Why Facebook really, really doesn't want to prevent extremism</a></b> <span>— Washington Post op-ed (2021)</span></li>
      <li><b><a href="https://www.latimes.com/opinion/story/2021-05-02/theater-empathy-live-performance-psychology" target="_blank" rel="noopener">Why theater makes us better people. Bring it back.</a></b> <span>— Los Angeles Times op-ed (2021)</span></li>
      <li><b><a href="https://www.theguardian.com/science/head-quarters/2017/jul/20/the-power-of-framing-its-not-what-you-say-its-how-you-say-it" target="_blank" rel="noopener">The power of framing: it’s not what you say, it’s how you say it</a></b> <span>— The Guardian (2017)</span></li>
      <li><b><a href="https://www.psychologytoday.com/us/blog/words-matter/201810/why-people-ignore-facts" target="_blank" rel="noopener">Why People Ignore Facts</a></b> <span>— Psychology Today (2018)</span></li>
    </ul>

    <div class="section-head"><h2 style="font-size:26px">Press coverage</h2></div>
    <p class="press-logos">Our research has been covered by the <strong><a href="https://www.nytimes.com/2022/10/06/opinion/elon-musk-twitter.html" target="_blank" rel="noopener">New York Times</a></strong> ·
      <strong><a href="https://www.washingtonpost.com/politics/2021/07/13/why-facebook-really-really-doesnt-want-discourage-extremism/" target="_blank" rel="noopener">Washington Post</a></strong> · <strong><a href="https://www.bbc.com/news/technology-57558028" target="_blank" rel="noopener">BBC</a></strong> · <strong><a href="https://www.nbcnews.com/tech/tech-news/go-viral-social-media-attack-political-opponent-study-says-rcna1277" target="_blank" rel="noopener">NBC</a></strong> ·
      <strong><a href="https://www.wsj.com/articles/reason-why-you-should-attend-live-theater-11636403394" target="_blank" rel="noopener">Wall Street Journal</a></strong> · <strong><a href="https://www.theatlantic.com/magazine/archive/2022/05/social-media-democracy-trust-babel/629369/" target="_blank" rel="noopener">The Atlantic</a></strong> ·
      <strong><a href="https://www.theguardian.com/education/2021/jun/30/critical-race-theory-rightwing-social-media-viral-video" target="_blank" rel="noopener">The Guardian</a></strong> · <strong><a href="https://www.youtube.com/watch?v=WLfr7sU5W2E" target="_blank" rel="noopener">60 Minutes</a></strong> and more.</p>
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
     INDEX_BODY.replace("__KP_GRID__", KP_GRID), INDEX_SCRIPT + KP_TAP_JS)
PUBS_SCRIPT = """
<script>
const pills=document.querySelectorAll('.filter-pills button');
const cols=document.getElementById('pubCols');
const gS=document.getElementById('group-social'), gA=document.getElementById('group-ai');
pills.forEach(btn=>btn.addEventListener('click',()=>{
  pills.forEach(x=>x.classList.remove('active'));
  btn.classList.add('active');
  const f=btn.dataset.f;
  gS.style.display=(f==='ai')?'none':'';
  gA.style.display=(f==='social')?'none':'';
  cols.style.gridTemplateColumns=(f==='all')?'':'1fr';
}));
</script>"""

page("publications.html", "Publications — Psychology of Technology Lab",
     "Key publications from the Psychology of Technology Lab, organized by social media and AI.",
     PUBS_BODY, PUBS_SCRIPT + KP_TAP_JS)
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
