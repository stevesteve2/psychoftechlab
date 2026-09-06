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
        <div class="cover"><img class="fit-cover" src="images/virality-cover.jpg" alt="Trends in Cognitive Sciences cover" onerror="this.remove()">
          <span class="journal">Trends in Cognitive Sciences · 2025</span>
          <span class="ctitle">The Psychology of Virality</span></div>
        <div class="meta"><b>Rathje &amp; Van Bavel</b><p class="abs">Why do some ideas spread widely, while others fail to catch on? We review the psychology of information spread, or the psychology of “virality.” Similar types of information tend to spread in many contexts, both online and offline. This is likely because similar psychological processes drive information spread across contexts. We explain how these psychological processes interact with structural features of information environments, including norms, networks, and incentive structures. Surprisingly, widely shared content is often not widely liked—a phenomenon called “the paradox of virality.” We discuss the strengths and limitations of the virality metaphor, and future directions for the field, such as leveraging recent advances in artificial intelligence to better understand how information spreads across cultures and contexts.</p></div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1073/pnas.2024292118" target="_blank" rel="noopener">
        <div class="cover alt1"><img src="images/pub-animosity.jpg" alt="" onerror="this.remove()"><span class="journal">PNAS · 2021</span>
          <span class="ctitle">Out-group animosity drives engagement</span></div>
        <div class="meta"><b>Rathje, Van Bavel &amp; van der Linden</b><p class="abs">There has been growing concern about the role social media plays in political polarization. We investigated whether out-group animosity was particularly successful at generating engagement on two of the largest social media platforms: Facebook and Twitter. Analyzing posts from news media accounts and US congressional members ( n = 2,730,215), we found that posts about the political out-group were shared or retweeted about twice as often as posts about the in-group. Each individual term referring to the political out-group increased the odds of a social media post being shared by 67%. Out-group language consistently emerged as the strongest predictor of shares and retweets: the average effect size of out-group language was about 4.8 times as strong as that of negative affect language and about 6.7 times as strong as that of moral-emotional language-both established predictors of social media engagement. Language about the out-group was a very strong predictor of "angry" reactions (the most popular reactions across all datasets), and language about the in-group was a strong predictor of "love" reactions, reflecting in-group favoritism and out-group derogation. This out-group effect was not moderated by political orientation or social media platform, but stronger effects were found among political leaders than among news media accounts. In sum, out-group language is the strongest predictor of social media engagement across all relevant predictors measured, suggesting that social media may be creating perverse incentives for content expressing out-group animosity.</p></div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1073/pnas.2308950121" target="_blank" rel="noopener">
        <div class="cover alt2"><img src="images/pub-gpt.jpg" alt="" onerror="this.remove()"><span class="journal">PNAS · 2024</span>
          <span class="ctitle">GPT is an effective tool for multilingual psychological text analysis</span></div>
        <div class="meta"><b>Rathje*, Mirea* et al.</b><p class="abs">The social and behavioral sciences have been increasingly using automated text analysis to measure psychological constructs in text. We explore whether GPT, the large-language model (LLM) underlying the AI chatbot ChatGPT, can be used as a tool for automated psychological text analysis in several languages. Across 15 datasets ( n = 47,925 manually annotated tweets and news headlines), we tested whether different versions of GPT (3.5 Turbo, 4, and 4 Turbo) can accurately detect psychological constructs (sentiment, discrete emotions, offensiveness, and moral foundations) across 12 languages. We found that GPT ( r = 0.59 to 0.77) performed much better than English-language dictionary analysis ( r = 0.20 to 0.30) at detecting psychological constructs as judged by manual annotators. GPT performed nearly as well as, and sometimes better than, several top-performing fine-tuned machine learning models. Moreover, GPT's performance improved across successive versions of the model, particularly for lesser-spoken languages, and became less expensive. Overall, GPT may be superior to many existing methods of automated text analysis, since it achieves relatively high accuracy across many languages, requires no training data, and is easy to use with simple prompts (e.g., "is this text negative?") and little coding experience. We provide sample code and a video tutorial for analyzing text with the GPT application programming interface. We argue that GPT and other LLMs help democratize automated text analysis by making advanced natural language processing capabilities more accessible, and may help facilitate more cross-linguistic research with understudied languages.</p></div>
      </a>
      <a class="key-pub" href="https://osf.io/preprints/psyarxiv/ujtxa_v1" target="_blank" rel="noopener">
        <div class="cover alt1"><img src="images/pub-global.jpg" alt="" onerror="this.remove()"><span class="journal">Nature · Registered Report</span>
          <span class="ctitle">Testing the causal impact of social media around the globe</span></div>
        <div class="meta"><b>Rathje*, Asimovic*, Ventura* et al.</b></div>
      </a>
      <a class="key-pub" href="https://osf.io/preprints/psyarxiv/vmyek_v1" target="_blank" rel="noopener">
        <div class="cover"><img src="images/pub-sycophancy.jpg" alt="" onerror="this.remove()"><span class="journal">Preprint · 2025</span>
          <span class="ctitle">The Impact of Sycophantic AI on Attitudes and Decisions</span></div>
        <div class="meta"><b>Rathje, Ye et al.</b><p class="abs">There is widespread concern that AI chatbots are “sycophantic,” or overly agreeable and validating. However, less is known about the causal impact of interacting with sycophantic AI on beliefs and behaviors. Across seven studies (total n = 7,227), we found that people enjoyed interacting with sycophantic AI chatbots more than interacting with neutral chatbots or “disagreeable” chatbots that challenged them. Brief conversations with sycophantic chatbots about political or personal topics increased the strength of people’s attitudes. Sycophantic chatbots also inflated people’s perceptions that they were better than the average person on desirable traits, and led people to bet more money that they scored better than average on tasks purporting to measure desirable traits. Participants consistently rated sycophantic chatbots as more “unbiased” than disagreeable chatbots, suggesting that people may be blind to biases in AI output that aligns with their views.</p></div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1038/s41562-023-01540-w" target="_blank" rel="noopener">
        <div class="cover alt2"><img src="images/pub-accuracy.jpg" alt="" onerror="this.remove()"><span class="journal">Nature Human Behaviour · 2023</span>
          <span class="ctitle">Accuracy and social motivations shape belief in (mis)information</span></div>
        <div class="meta"><b>Rathje, Roozenbeek, Van Bavel &amp; van der Linden</b><p class="abs">The extent to which belief in (mis)information reflects lack of knowledge versus a lack of motivation to be accurate is unclear. Here, across four experiments (n = 3,364), we motivated US participants to be accurate by providing financial incentives for correct responses about the veracity of true and false political news headlines. Financial incentives improved accuracy and reduced partisan bias in judgements of headlines by about 30%, primarily by increasing the perceived accuracy of true news from the opposing party (d = 0.47). Incentivizing people to identify news that would be liked by their political allies, however, decreased accuracy. Replicating prior work, conservatives were less accurate at discerning true from false headlines than liberals, yet incentives closed the gap in accuracy between conservatives and liberals by 52%. A non-financial accuracy motivation intervention was also effective, suggesting that motivation-based interventions are scalable. Altogether, these results suggest that a substantial portion of people's judgements of the accuracy of news reflects motivational factors.</p></div>
      </a>
      <a class="key-pub" href="https://doi.org/10.1177/17456916231190392" target="_blank" rel="noopener">
        <div class="cover alt1"><img src="images/pub-peoplethink.jpg" alt="" onerror="this.remove()"><span class="journal">Perspectives on Psychological Science · 2023</span>
          <span class="ctitle">People think that social media platforms do (but should not) amplify divisive content</span></div>
        <div class="meta"><b>Rathje, Robertson, Brady &amp; Van Bavel</b><p class="abs">Recent studies have documented the type of content that is most likely to spread widely, or go "viral," on social media, yet little is known about people's perceptions of what goes viral or what should go viral. This is critical to understand because there is widespread debate about how to improve or regulate social media algorithms. We recruited a sample of participants that is nationally representative of the U.S. population (according to age, gender, and race/ethnicity) and surveyed them about their perceptions of social media virality ( n = 511). In line with prior research, people believe that divisive content, moral outrage, negative content, high-arousal content, and misinformation are all likely to go viral online. However, they reported that this type of content should not go viral on social media. Instead, people reported that many forms of positive content-such as accurate content, nuanced content, and educational content-are not likely to go viral even though they think this content should go viral. These perceptions were shared among most participants and were only weakly related to political orientation, social media usage, and demographic variables. In sum, there is broad consensus around the type of content people think social media platforms should and should not amplify, which can help inform solutions for improving social media.</p></div>
      </a>
      <a class="key-pub" href="https://doi.org/10.31234/osf.io/acbwg" target="_blank" rel="noopener">
        <div class="cover"><img src="images/pub-unfollow.jpg" alt="" onerror="this.remove()"><span class="journal">Preprint · 2025</span>
          <span class="ctitle">Unfollowing partisan accounts reduces out-party animosity and increases social media satisfaction</span></div>
        <div class="meta"><b>Rathje, He, Harjani, Roozenbeek, Pretus, Gray, van der Linden &amp; Van Bavel</b><p class="abs">There is considerable debate over social media’s causal effects. In a correlational study (n₁ = 1,447) and two digital field experiments (n₂ = 496, n₃ = 1,133), we examined the effect of (un)following partisan accounts. Incentivizing Twitter/X users to unfollow partisan accounts significantly improved their feelings toward the opposing party, with effects persisting for at least six months. Unfollowing also led participants to engage with more accurate news accounts, increased satisfaction with their Twitter/X feeds, and reduced the amount of political content they reported seeing a full year later, without reducing engagement. This work demonstrates the benefits of targeted approaches for improving one’s social media experience.</p></div>
      </a>
    </div>
    <div class="pub-cols">
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
