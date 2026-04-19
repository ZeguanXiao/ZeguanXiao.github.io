# Academic Homepage Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Populate the Academic Pages Jekyll template with Zeguan Xiao's real personal and academic content and publish to GitHub Pages.

**Architecture:** Edit `_config.yml` + `_data/navigation.yml` for site-wide settings, rewrite `_pages/about.md` for the homepage, delete all template placeholder content in collections, create 8 real publication files in `_publications/`, then push to GitHub.

**Tech Stack:** Jekyll (Academic Pages template), GitHub Pages, Markdown + YAML front matter

---

## Batch 1 — Site Config & Navigation

### Task 1: Add .superpowers/ to .gitignore

**Files:**
- Modify: `.gitignore`

- [ ] Append to `.gitignore`:
```
.superpowers/
```

- [ ] Commit:
```bash
git add .gitignore
git commit -m "chore: ignore .superpowers brainstorm artifacts"
```

---

### Task 2: Update `_config.yml`

**Files:**
- Modify: `_config.yml`

- [ ] Set the following fields (leave everything else unchanged):

```yaml
locale: "en-US"
site_theme: "air"
title: "Zeguan Xiao"
title_separator: "-"
name: &name "Zeguan Xiao"
description: &description "PhD Candidate · LLM Safety, Alignment & Robustness"
url: https://ZeguanXiao.github.io
baseurl: ""
repository: "ZeguanXiao/ZeguanXiao.github.io"

author:
  avatar: "profile.jpg"
  name: "Zeguan Xiao"
  bio: "Final-year PhD candidate @ SUFE. LLM Safety, Alignment & Robustness."
  location: "Shanghai, China"
  employer: "Shanghai University of Finance and Economics"
  email: "hainanxzg@gmail.com"
  googlescholar: "https://scholar.google.com/citations?user=rgQWhpUAAAAJ"
  github: "ZeguanXiao"
```

All other social fields (`twitter`, `linkedin`, `orcid`, etc.) should be left blank.

- [ ] Commit:
```bash
git add _config.yml
git commit -m "config: set theme, author info, and social links"
```

---

### Task 3: Update `_data/navigation.yml`

**Files:**
- Modify: `_data/navigation.yml`

- [ ] Replace entire file content with:

```yaml
main:
  - title: "Publications"
    url: /publications/
```

- [ ] Commit:
```bash
git add _data/navigation.yml
git commit -m "config: simplify nav to Publications only"
```

---

## Batch 2 — Homepage & Profile Photo

### Task 4: Copy profile photo

**Files:**
- Add: `images/profile.jpg`

- [ ] Copy the photo:
```bash
cp ~/Documents/Resume-xzg/picture.jpg images/profile.jpg
```

- [ ] Commit:
```bash
git add images/profile.jpg
git commit -m "assets: add profile photo"
```

---

### Task 5: Rewrite `_pages/about.md`

**Files:**
- Modify: `_pages/about.md`

- [ ] Replace entire file content with:

```markdown
---
permalink: /
title: "About"
author_profile: true
---

I am a **final-year** PhD candidate in Management Science and Engineering at Shanghai University of Finance and Economics (SUFE), advised by [Prof. Yun Chen](https://yunc.me/). I am also a visiting student at the Southern University of Science and Technology (SUSTech), working with [Prof. Guanhua Chen](https://ghchen.me/). My research focuses on **LLM Safety, Alignment, and Robustness**, with particular interests in LLM unlearning, uncertainty estimation, and adversarial robustness.

I am actively looking for positions (both academia and industry). Feel free to reach out at [hainanxzg@gmail.com](mailto:hainanxzg@gmail.com)!

## Research Interests

- **LLM Unlearning** — capability-preserving unlearning, robustness against relearning attacks
- **LLM Alignment** — direct alignment algorithms, bridging the reward-generation gap
- **Robustness & Uncertainty** — stress testing, uncertainty estimation via aggregated internal belief
- **LLM Safety / Jailbreak** — automatic jailbreak attack, sequential character-based attacks

## Education

- **Ph.D.** Management Science and Engineering, Shanghai University of Finance and Economics, 2022–2026  
  Advisor: [Prof. Yun Chen](https://yunc.me/)
- **M.S.** Computer Software and Theory, Jinan University, 2018–2021
- **B.S.** Economic Statistics, Dongbei University of Finance and Economics, 2014–2018
```

- [ ] Commit:
```bash
git add _pages/about.md
git commit -m "content: rewrite about page with real bio"
```

---

## Batch 3 — Clean Template Placeholders

### Task 6: Delete all template placeholder files

- [ ] Delete all at once:
```bash
rm _posts/2012-08-14-blog-post-1.md _posts/2013-08-14-blog-post-2.md \
   _posts/2014-08-14-blog-post-3.md _posts/2015-08-14-blog-post-4.md \
   _posts/2199-01-01-future-post.md \
   _talks/2012-03-01-talk-1.md _talks/2013-03-01-tutorial-1.md \
   _talks/2014-02-01-talk-2.md _talks/2014-03-01-talk-3.md \
   _teaching/2014-spring-teaching-1.md _teaching/2015-spring-teaching-2.md \
   _portfolio/portfolio-1.md _portfolio/portfolio-2.html \
   _publications/2009-10-01-paper-title-number-1.md \
   _publications/2010-10-01-paper-title-number-2.md \
   _publications/2015-10-01-paper-title-number-3.md \
   _publications/2024-02-17-paper-title-number-4.md \
   _publications/2025-06-08-paper-title-number-5.md
```

- [ ] Commit:
```bash
git add -A
git commit -m "chore: remove all template placeholder content"
```

---

## Batch 4 — Publications (8 files)

Publication front matter convention:
- `collection: publications`
- `category: conferences` for conference papers; `manuscripts` for journal/preprint under review
- Author list in body with **Zeguan Xiao** bolded

---

### Task 7: BERT4GCN — EMNLP 2021

**File:** `_publications/2021-11-01-bert4gcn.md`

- [ ] Create the file with content:

```markdown
---
title: "BERT4GCN: Using BERT Intermediate Layers to Augment GCN for Aspect-based Sentiment Classification"
collection: publications
category: conferences
permalink: /publication/2021-11-01-bert4gcn
excerpt: 'We propose BERT4GCN, which integrates grammatical sequential features from intermediate BERT layers with syntactic knowledge from dependency graphs for aspect-based sentiment classification.'
date: 2021-11-01
venue: 'Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP 2021)'
paperurl: 'https://aclanthology.org/2021.emnlp-main.775/'
---

**Zeguan Xiao**, Jiarun Wu, Qingliang Chen, Congjian Deng

*EMNLP 2021* · [Paper](https://aclanthology.org/2021.emnlp-main.775/)

Graph-based Aspect-based Sentiment Classification (ABSC) approaches have yielded state-of-the-art results, especially when equipped with contextual word embedding from pre-trained language models (PLMs). BERT4GCN utilizes outputs from intermediate layers of BERT and positional information between words to augment GCN to better encode dependency graphs for downstream classification.
```

- [ ] Commit:
```bash
git add _publications/2021-11-01-bert4gcn.md
git commit -m "content: add BERT4GCN publication (EMNLP 2021)"
```

---

### Task 8: Pruning AdaptPerFusion — NAACL Findings 2022

**File:** `_publications/2022-07-01-pruning-adaptperfusion.md`

- [ ] Create the file with content:

```markdown
---
title: "Pruning AdaptPerFusion with Lottery Ticket Hypothesis"
collection: publications
category: conferences
permalink: /publication/2022-07-01-pruning-adaptperfusion
excerpt: 'We propose a pruning approach for AdaptPerFusion adapter fusion models based on the Lottery Ticket Hypothesis, significantly reducing model size while maintaining performance on GLUE.'
date: 2022-07-01
venue: 'Findings of the Association for Computational Linguistics: NAACL 2022'
paperurl: 'https://aclanthology.org/2022.findings-naacl.110/'
---

Jiarun Wu, Qingliang Chen, **Zeguan Xiao**, Yuliang Gu, Mengsi Sun

*Findings of NAACL 2022* · [Paper](https://aclanthology.org/2022.findings-naacl.110/)

We propose an approach to identify the influence of each adapter module and a novel way to prune adapters based on the Lottery Ticket Hypothesis. Experiments on GLUE show that the pruned model achieves state-of-the-art results while reducing sizes significantly.
```

- [ ] Commit:
```bash
git add _publications/2022-07-01-pruning-adaptperfusion.md
git commit -m "content: add Pruning AdaptPerFusion publication (NAACL Findings 2022)"
```

---

### Task 9: Distract Jailbreak — EMNLP 2024

**File:** `_publications/2024-11-01-distract-jailbreak.md`

- [ ] Create the file with content:

```markdown
---
title: "Distract Large Language Models for Automatic Jailbreak Attack"
collection: publications
category: conferences
permalink: /publication/2024-11-01-distract-jailbreak
excerpt: 'We propose a novel black-box jailbreak framework using malicious content concealing and memory reframing with an iterative optimization algorithm to automatically jailbreak LLMs.'
date: 2024-11-01
venue: 'Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024)'
paperurl: 'https://aclanthology.org/2024.emnlp-main.1042/'
---

**Zeguan Xiao**, Yan Yang, Guanhua Chen, Yun Chen

*EMNLP 2024* · [Paper](https://aclanthology.org/2024.emnlp-main.1042/)

We propose a novel black-box jailbreak framework for automated red teaming of LLMs. We designed malicious content concealing and memory reframing with an iterative optimization algorithm to jailbreak LLMs, motivated by research on the distractibility and over-confidence phenomenon of LLMs.
```

- [ ] Commit:
```bash
git add _publications/2024-11-01-distract-jailbreak.md
git commit -m "content: add Distract Jailbreak publication (EMNLP 2024)"
```

---

### Task 10: SeqAR — NAACL 2025

**File:** `_publications/2025-04-01-seqar.md`

- [ ] Create the file with content:

```markdown
---
title: "SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters"
collection: publications
category: conferences
permalink: /publication/2025-04-01-seqar
excerpt: 'SeqAR is a jailbreak framework that generates and applies sequential auto-generated characters in a cold-start scenario using open-sourced LLMs without any seed templates.'
date: 2025-04-01
venue: 'Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the ACL (NAACL 2025)'
paperurl: 'https://aclanthology.org/2025.naacl-long.1/'
---

Yan Yang, **Zeguan Xiao**, Xin Lu, Hongru Wang, Xuetao Wei, Hailiang Huang, Guanhua Chen, Yun Chen

*NAACL 2025* · [Paper](https://aclanthology.org/2025.naacl-long.1/)

SeqAR generates and optimizes multiple jailbreak characters, then applies them sequentially in a single query to bypass guardrails of the target LLM. SeqAR achieves attack success rates of 88% and 60% on GPT-3.5-1106 and GPT-4, respectively, without relying on proprietary LLMs or human-crafted seed templates.
```

- [ ] Commit:
```bash
git add _publications/2025-04-01-seqar.md
git commit -m "content: add SeqAR publication (NAACL 2025)"
```

---

### Task 11: EAGLE Uncertainty — AAAI 2026

**File:** `_publications/2026-02-01-eagle-uncertainty.md`

- [ ] Create the file with content:

```markdown
---
title: "Enhancing Uncertainty Estimation in LLMs with Expectation of Aggregated Internal Belief"
collection: publications
category: conferences
permalink: /publication/2026-02-01-eagle-uncertainty
excerpt: 'EAGLE is a self-evaluation-based calibration method that aggregates internal beliefs from multiple intermediate layers to derive more accurate LLM confidence scores.'
date: 2026-02-01
venue: 'Proceedings of the AAAI Conference on Artificial Intelligence (AAAI 2026)'
paperurl: 'https://ojs.aaai.org/index.php/AAAI/article/view/34043'
---

**Zeguan Xiao**, Diyang Dou, Boya Xiong, Yun Chen, Guanhua Chen

*AAAI 2026* · [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/34043)

We propose EAGLE (Expectation of AGgregated internaL bEief), a self-evaluation-based calibration method that leverages the internal hidden states of LLMs. By aggregating layer-wise beliefs and calculating the expectation over the resulting confidence score distribution, EAGLE produces refined confidence scores that more faithfully reflect the model's internal certainty.
```

- [ ] Commit:
```bash
git add _publications/2026-02-01-eagle-uncertainty.md
git commit -m "content: add EAGLE uncertainty estimation publication (AAAI 2026)"
```

---

### Task 12: AR-Checker Robustness — arXiv 2025

**File:** `_publications/2025-06-01-ar-checker.md`

- [ ] Create the file with content:

```markdown
---
title: "Automatic Robustness Stress Testing of LLMs as Mathematical Problem Solvers"
collection: publications
category: manuscripts
permalink: /publication/2025-06-01-ar-checker
excerpt: 'AR-Checker generates mathematical problem variants to stress-test LLM robustness while minimizing data contamination risk.'
date: 2025-06-01
venue: 'arXiv:2506.05038 (Under review at ACL 2026)'
paperurl: 'https://arxiv.org/abs/2506.05038'
---

Yutao Hou, **Zeguan Xiao**, Fei Yu, Yihan Jiang, Xuetao Wei, Hailiang Huang, Yun Chen, Guanhua Chen

*Under review at ACL 2026* · [arXiv](https://arxiv.org/abs/2506.05038)

We propose AR-Checker (Automatic Robustness Checker), a framework that generates mathematical problem variants maintaining semantic meaning but likely to fail LLMs. The framework generates variants dynamically for each LLM via multi-round parallel LLM-based rewriting and verification, minimizing data contamination risk.
```

- [ ] Commit:
```bash
git add _publications/2025-06-01-ar-checker.md
git commit -m "content: add AR-Checker robustness publication (arXiv 2025)"
```

---

### Task 13: POET Alignment — ACL Findings 2026

**File:** `_publications/2026-01-02-poet-alignment.md`

- [ ] Create the file with content:

```markdown
---
title: "Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms"
collection: publications
category: manuscripts
permalink: /publication/2026-01-02-poet-alignment
excerpt: 'POET bridges the reward-generation gap in Direct Alignment Algorithms by truncating responses to equal length, better aligning training objectives with autoregressive decoding dynamics.'
date: 2026-01-02
venue: 'Findings of ACL 2026 (arXiv:2506.09457)'
paperurl: 'https://arxiv.org/abs/2506.09457'
---

**Zeguan Xiao**, Yun Chen, Jian Yang, Guanhua Chen, Ke Tang

*Findings of ACL 2026* · [arXiv](https://arxiv.org/abs/2506.09457)

We identify the "reward-generation gap" in Direct Alignment Algorithms (DAAs) — a discrepancy between training objectives and autoregressive decoding dynamics. We propose POET (Prefix-Oriented Equal-length Training), which truncates both preferred and dispreferred responses to the shorter one's length, achieving up to 11.8 points improvement in AlpacaEval 2.
```

- [ ] Commit:
```bash
git add _publications/2026-01-02-poet-alignment.md
git commit -m "content: add POET alignment publication (ACL Findings 2026)"
```

---

### Task 14: LLM Unlearning Asymmetric — ACL 2026

**File:** `_publications/2026-01-01-llm-unlearning-asymmetric.md`

- [ ] Create the file with content:

```markdown
---
title: "Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem"
collection: publications
category: manuscripts
permalink: /publication/2026-01-01-llm-unlearning-asymmetric
excerpt: 'We recast LLM unlearning as an asymmetric two-task problem and propose SAGO, a retention-prioritized gradient synthesis method that consistently pushes the Pareto frontier on unlearning benchmarks.'
date: 2026-01-01
venue: 'ACL 2026 (arXiv:2604.14808)'
paperurl: 'https://arxiv.org/abs/2604.14808'
---

**Zeguan Xiao**, Siqing Li, Yong Wang, Xuetao Wei, Jian Yang, Yun Chen, Guanhua Chen

*ACL 2026* · [arXiv](https://arxiv.org/abs/2604.14808)

We recast LLM unlearning as an asymmetric two-task problem where retention is the primary objective and forgetting is auxiliary. We propose SAGO, a retention-prioritized gradient synthesis method that achieves strictly tighter alignment with the retain gradient. On WMDP Bio (SimNPO+GD), MMLU recovery progresses from 44.6% (naive) to 96.0% (+SAGO) while maintaining comparable forgetting strength.
```

- [ ] Commit:
```bash
git add _publications/2026-01-01-llm-unlearning-asymmetric.md
git commit -m "content: add LLM Unlearning Asymmetric publication (ACL 2026)"
```

---

## Batch 5 — Final Push

### Task 15: Push to GitHub

- [ ] Push all commits:
```bash
git push origin master
```

- [ ] Verify: visit `https://ZeguanXiao.github.io` after ~2 minutes for GitHub Pages to build.
