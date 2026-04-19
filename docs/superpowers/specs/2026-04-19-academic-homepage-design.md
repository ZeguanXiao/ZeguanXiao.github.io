# Academic Homepage Design — Zeguan Xiao

## Problem Statement

Populate the Academic Pages Jekyll template (already forked as `ZeguanXiao/ZeguanXiao.github.io`) with real personal and academic content so it can be published as a live academic website on GitHub Pages.

## Decisions Made

| Decision | Choice | Rationale |
|---|---|---|
| Theme | `air` | Clean, modern, white top bar with blue accents |
| Navigation | About (home) + Publications | No talks/teaching/portfolio content exists |
| Social links | Email, Google Scholar, GitHub | Only links with actual presence |
| CV section | Omitted | Not requested; PDF resume available if needed later |

---

## Site Configuration (`_config.yml`)

```yaml
title: "Zeguan Xiao"
name: "Zeguan Xiao"
description: "PhD Candidate in Management Science and Engineering"
url: "https://ZeguanXiao.github.io"
repository: "ZeguanXiao/ZeguanXiao.github.io"
site_theme: "air"

author:
  avatar: "profile.jpg"
  name: "Zeguan Xiao"
  bio: "Final-year PhD candidate @ SUFE. Research on LLM Safety, Alignment & Robustness."
  location: "Shanghai, China"
  employer: "Shanghai University of Finance and Economics"
  email: "hainanxzg@gmail.com"
  googlescholar: "https://scholar.google.com/citations?user=rgQWhpUAAAAJ"
  github: "ZeguanXiao"
```

All other social fields remain blank/commented out.

---

## Navigation (`_data/navigation.yml`)

```yaml
main:
  - title: "Publications"
    url: /publications/
```

Only the Publications link appears in the header. The homepage (About) is always accessible at `/`.

---

## Profile Photo

Copy `~/Documents/Resume-xzg/picture.jpg` → `images/profile.jpg`, and update `avatar` in `_config.yml` to `"profile.jpg"`.

---

## Homepage (`_pages/about.md`)

```
---
permalink: /
title: "About"
author_profile: true
---

I am a **final-year** PhD candidate in Management Science and Engineering at Shanghai University of Finance and Economics (SUFE), advised by [Prof. Yun Chen](https://yunc.me/). I am also a visiting student at the Southern University of Science and Technology (SUSTech), working with [Prof. Guanhua Chen](https://ghchen.me/). My research focuses on **LLM Safety, Alignment, and Robustness**, with particular interests in LLM unlearning, uncertainty estimation, and adversarial robustness.

I am actively looking for positions (both academia and industry). Feel free to reach out at [hainanxzg@gmail.com](mailto:hainanxzg@gmail.com)!

## Research Interests

- **LLM Unlearning** — capability-preserving unlearning, robustness against relearning attacks
- **LLM Alignment** — direct alignment algorithms, reward-generation gap
- **Robustness & Uncertainty** — stress testing, uncertainty estimation via aggregated internal belief
- **LLM Safety / Jailbreak** — automatic jailbreak attack, sequential character-based attacks

## Education

- **Ph.D.** in Management Science and Engineering, Shanghai University of Finance and Economics, 2022–2026
  Advisor: [Prof. Yun Chen](https://yunc.me/)
- **M.S.** in Computer Software and Theory, Jinan University, 2018–2021
- **B.S.** in Economic Statistics, Dongbei University of Finance and Economics, 2014–2018
```

---

## Publications (`_publications/`)

8 files total, one per paper, sorted by date descending. Each file uses the standard front matter with `collection: publications` and `category:` set to `manuscripts` (journal/conference) or `conferences`.

| Filename | Title | Venue | Year | Category |
|---|---|---|---|---|
| `2026-01-01-llm-unlearning-asymmetric.md` | Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem | arXiv:2604.14808 (Under review ACL 2026) | 2026 | manuscripts |
| `2026-01-02-uncertainty-aggregated-belief.md` | Enhancing Uncertainty Estimation in LLMs with Expectation of Aggregated Internal Belief | AAAI 2026 | 2026 | conferences |
| `2025-01-01-reward-generation-gap.md` | Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms | arXiv:2506.09457 (Under review ACL 2026) | 2025 | manuscripts |
| `2025-01-02-robustness-stress-testing.md` | Automatic Robustness Stress Testing of LLMs as Mathematical Problem Solvers | arXiv:2506.05038 (Under review ACL 2026) | 2025 | manuscripts |
| `2025-01-03-seqar-jailbreak.md` | SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters | NAACL 2025 | 2025 | conferences |
| `2024-01-01-distract-jailbreak.md` | Distract Large Language Models for Automatic Jailbreak Attack | EMNLP 2024 | 2024 | conferences |
| `2022-01-01-pruning-adaptperfusion.md` | Pruning AdaptPerFusion with Lottery Ticket Hypothesis | NAACL Findings 2022 | 2022 | conferences |
| `2021-01-01-bert4gcn.md` | BERT4GCN: Using BERT Intermediate Layers to Augment GCN for Aspect-based Sentiment Classification | EMNLP 2021 | 2021 | conferences |

Each publication's `excerpt` will be a one-sentence description. `paperurl` will link to arXiv or the ACL Anthology where available. Author lists and citation counts from Google Scholar will be included in the body of each file.

---

## Files to Modify / Create

| File | Action |
|---|---|
| `_config.yml` | Edit — personal info, theme, social links |
| `_data/navigation.yml` | Edit — keep only Publications |
| `_pages/about.md` | Edit — replace template content |
| `images/profile.jpg` | Add — copy from resume folder |
| `_publications/*.md` | Create — 8 new files, delete 5 template files |
| `_posts/*.md` | Delete — 5 template post files |
| `_talks/*.md` | Delete — 4 template talk files |
| `_teaching/*.md` | Delete — 2 template teaching files |
| `_portfolio/*.md` | Delete — 2 template portfolio files |

---

## Deployment

The repository `ZeguanXiao/ZeguanXiao.github.io` is already configured for GitHub Pages. After pushing, the site will be live at `https://ZeguanXiao.github.io` automatically via the `pages-build-deployment` workflow.
