#!/usr/bin/env python3
"""Revert to organic brain + serif; replace key-pub cards with editorial rows."""
import re
from abstracts import ABS

# ---------- 1. restore organic brain from backup ----------
cur = open('index_page.py').read()
bak = open('index_page_organic_brain_backup.py').read()
b0, b1 = bak.find("// ===== brain:"), bak.find("// ===== unified method tiles")
c0, c1 = cur.find("// ===== brain:"), cur.find("// ===== unified method tiles")
assert min(b0, b1, c0, c1) > -1
cur = cur[:c0] + bak[b0:b1] + cur[c1:]
cur = cur.replace('spark the circuits with your cursor · drag the chips to rewire',
                  'fire neurons with your cursor · drag them to rewire')

# ---------- 2. editorial rows instead of cards ----------
def row(key, img, venue, url, title, authors, cover=False):
    absp = (f'<details class="kp-details"><summary>Abstract</summary>'
            f'<p class="kp-abs">{ABS[key]}</p></details>') if ABS.get(key) else ''
    fig = (f'<div class="kp-fig{" kp-cover" if cover else ""}">'
           f'<img src="images/{img}" alt="" onerror="this.parentNode.remove()"></div>') if img else ''
    return f'''      <div class="kp-row">
        {fig}
        <div>
          <div class="kp-venue">{venue}</div>
          <h3 class="kp-title"><a href="{url}" target="_blank" rel="noopener">{title}</a></h3>
          <div class="kp-authors">{authors}</div>
          {absp}
        </div>
      </div>'''

VIRALITY = row('virality', 'virality-cover.jpg', 'Trends in Cognitive Sciences · 2025',
  'https://doi.org/10.1016/j.tics.2025.06.014', 'The Psychology of Virality',
  'Rathje &amp; Van Bavel', cover=True)
ANIMOSITY = row('animosity', 'pub-animosity.jpg', 'PNAS · 2021',
  'https://doi.org/10.1073/pnas.2024292118', 'Out-group animosity drives engagement on social media',
  'Rathje, Van Bavel &amp; van der Linden')
SYCO = row('sycophancy', 'pub-sycophancy.jpg', 'Preprint · 2025',
  'https://osf.io/preprints/psyarxiv/vmyek_v1', 'The Impact of Sycophantic AI on Attitudes and Decisions',
  'Rathje, Ye, Globig, Pillai, Oldemburgo de Mello, Chen &amp; Van Bavel')
GPT = row('gpt', None, 'PNAS · 2024',
  'https://doi.org/10.1073/pnas.2308950121', 'GPT is an effective tool for multilingual psychological text analysis',
  'Rathje*, Mirea*, Sucholutsky, Marjieh, Robertson &amp; Van Bavel')
GLOBAL = row('global', 'pub-global.jpg', 'Registered Report · In Principle Acceptance at Nature',
  'https://osf.io/preprints/psyarxiv/ujtxa_v1', 'Testing the causal impact of social media usage around the globe',
  'Rathje*, Asimovic*, Ventura*, Mughal, Karsting, Robertson, Barrie, The Global Social Media Experiment Team, Tucker &amp; Van Bavel')
ACCURACY = row('accuracy', 'pub-accuracy.jpg', 'Nature Human Behaviour · 2023',
  'https://doi.org/10.1038/s41562-023-01540-w', 'Accuracy and social motivations shape belief in (mis)information',
  'Rathje, Roozenbeek, Van Bavel &amp; van der Linden')
PEOPLETHINK = row('peoplethink', 'pub-peoplethink.jpg', 'Perspectives on Psychological Science · 2023',
  'https://doi.org/10.1177/17456916231190392', 'People think that social media platforms do (but should not) amplify divisive content',
  'Rathje, Robertson, Brady &amp; Van Bavel')
UNFOLLOW = row('unfollow', 'pub-unfollow.jpg', 'Preprint · 2025',
  'https://doi.org/10.31234/osf.io/acbwg', 'Unfollowing partisan accounts reduces out-party animosity and increases social media satisfaction',
  'Rathje, He, Harjani, Roozenbeek, Pretus, Gray, van der Linden &amp; Van Bavel')

# homepage: 3 rows
s = cur.find('<section id="key-pubs">')
e = cur.find('</section>', s) + len('</section>')
assert s > -1
cur = cur[:s] + f'''<section id="key-pubs">
  <div class="wrap">
    <div class="section-head">
      <div class="eyebrow">Key Publications</div>
      <h2>Start here</h2>
    </div>
    <div>
{VIRALITY}
{ANIMOSITY}
{SYCO}
    </div>
    <p class="see-all"><a href="publications.html">All publications, by topic →</a></p>
  </div>
</section>''' + cur[e:]
open('index_page.py', 'w').write(cur)

# publications page: 8 rows replacing the key grid
b = open('build_site.py').read()
s = b.find('<div class="key-pubs" style="margin-bottom:64px">')
e = b.find('    <div class="pub-cols">')
assert s > -1 and e > s
b = b[:s] + f'''<div style="margin-bottom:72px">
{VIRALITY}
{ANIMOSITY}
{GPT}
{GLOBAL}
{SYCO}
{ACCURACY}
{PEOPLETHINK}
{UNFOLLOW}
    </div>
''' + b[e:]
open('build_site.py', 'w').write(b)

# ---------- 3. serif revert + row CSS ----------
c = open('style.css').read()
c = c.replace("font-family:'Archivo',system-ui,sans-serif;line-height:1.12;text-wrap:balance;font-weight:700;letter-spacing:-0.02em",
              "font-family:'Fraunces',Georgia,serif;line-height:1.12;text-wrap:balance;font-weight:600")
c = c.replace("'Archivo',system-ui,sans-serif", "'Fraunces',serif")
c += """

/* editorial publication rows */
.kp-row{display:grid;grid-template-columns:minmax(220px,320px) 1fr;gap:44px;
  padding:44px 0;border-bottom:1px solid var(--hairline);align-items:start}
.kp-row:last-child{border-bottom:none}
@media(max-width:760px){.kp-row{grid-template-columns:1fr;gap:20px}}
.kp-fig{background:#fff;border:1px solid var(--hairline);border-radius:14px;
  box-shadow:var(--shadow);padding:10px}
.kp-fig img{width:100%;height:auto;border-radius:8px;display:block}
.kp-venue{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;
  color:var(--accent);margin-bottom:8px}
.kp-title{font-size:clamp(21px,2.4vw,28px);line-height:1.2;margin-bottom:10px}
.kp-title a{text-decoration:none}
.kp-title a:hover{color:var(--accent)}
.kp-authors{font-size:14.5px;color:var(--muted);margin-bottom:12px}
.kp-abs{font-size:15px;color:var(--muted);line-height:1.65;max-width:62ch}
"""
open('style.css', 'w').write(c)

h = open('_head.tmpl').read()
h = h.replace("css2?family=Archivo:wght@400;500;600;700;800&display=swap",
              "css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Archivo:wght@400;500;600;700&display=swap")
open('_head.tmpl', 'w').write(h)
print('REVERTED + ROWS DONE')
