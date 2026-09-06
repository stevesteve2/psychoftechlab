#!/usr/bin/env python3
"""Abstract texts for publication rows."""
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

