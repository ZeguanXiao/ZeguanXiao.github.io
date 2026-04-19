# Homepage Corrections Design

Date: 2026-04-19

## Problem

The academic homepage at `https://ZeguanXiao.github.io` contains multiple factual errors across three areas: personal biography, CV page, and publication entries. Several publications point to wrong papers (incorrect titles, wrong authors, or arXiv IDs belonging to other researchers). The CV page still contains 100% template placeholder content.

## Scope

Fix all factual errors. No structural changes to layouts, navigation, or styling. English-only for now (the `/zh/` bilingual layer is a separate initiative).

---

## Area 1: `_pages/about.md`

Three fixes:

1. **Chinese name typo** — current: `肖泽冠`; correct: `肖泽管`
2. **School name wrong** — current: `School of Information Management and Engineering`; correct: `School of Computing and Artificial Intelligence (SCAI)`
3. **Missing research interest** — add `LLM Unlearning` to the bullet list

---

## Area 2: `_pages/cv.md`

Full rewrite. Replace all GitHub University placeholder content with real information.

### Education

| Degree | Institution | Period |
|---|---|---|
| PhD, Management Science and Engineering | Shanghai University of Finance and Economics, SCAI | Sept 2022 – Jul 2026 |
| MS, Computer Software and Theory | Jinan University | Sept 2018 – Jul 2021 |
| BS, Economic Statistics | Dongbei University of Finance and Economics | Sept 2014 – Jul 2018 |

### Research Experience

- **Visiting Student**, Southern University of Science and Technology (SUSTech), Apr 2023 – Apr 2026, advised by Prof. Guanhua Chen

### Publications

Auto-rendered from `site.publications` collection (existing template loop, already in cv.md).

---

## Area 3: `_publications/`

### Files to delete

| File | Reason |
|---|---|
| `2024-11-12-spt.md` | arXiv:2406.05946 belongs to Xiangyu Qi (not Zeguan Xiao); paper is not in resume |
| `2025-06-07-jailbreak-bench.md` | Title fabricated; arXiv:2506.05038 is a preprint led by co-author Yutao Hou, not accepted |

### Files to fix

| File | Changes |
|---|---|
| `2021-11-07-bert4gcn.md` | Fix authors (Zeguan Xiao, Jiarun Wu, Qingliang Chen, Congjian Deng); fix URL to `2021.emnlp-main.724` |
| `2022-07-10-pruning-adaptperfusion.md` | Full rewrite: correct title "Pruning Adatperfusion with Lottery Ticket Hypothesis", correct authors (Jiarun Wu, Qingliang Chen, Zeguan Xiao, Yuliang Gu, Mengsi Sun), correct URL `2022.findings-naacl.123` |
| `2024-11-12-distract-jailbreak.md` | Fix URL from `2024.emnlp-main.1042` to `2024.emnlp-main.908` |
| `2025-04-29-seqar.md` | Fix title to "SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters"; fix authors (Yan Yang, Zeguan Xiao, Xin Lu, Hongru Wang, Xuetao Wei, Hailiang Huang, Guanhua Chen, Yun Chen); fix URL to `2025.naacl-long.42` |
| `2025-04-30-ar-checker.md` | Rewrite as "Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem" (ACL 2026, arXiv:2604.14808); authors: Zeguan Xiao, Shuai Li, Yiran Wang, Xuetao Wei, Jie Yang, Yun Chen, Guanhua Chen |
| `2025-06-14-scalable-oversight.md` | Fix title to "Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms" (ACL Findings 2026, arXiv:2506.09457); authors: Zeguan Xiao, Yun Chen, Guanhua Chen, Kai Tang |

### Files to add

| New filename | Paper | Venue | URL |
|---|---|---|---|
| `2026-03-14-uncertainty-estimation.md` | Enhancing Uncertainty Estimation in LLMs with Expectation of Aggregated Internal Belief | AAAI 2026 | arXiv:2509.01564, AAAI OJS: 40698 |
| `2026-04-19-representation-guided-unlearning.md` | Representation-Guided Parameter-Efficient LLM Unlearning | ACL Findings 2026 | GitHub: reglu-open |

### Final publication list (8 papers)

| # | Title | Venue | Year |
|---|---|---|---|
| 1 | BERT4GCN | EMNLP | 2021 |
| 2 | Pruning Adatperfusion with Lottery Ticket Hypothesis | NAACL Findings | 2022 |
| 3 | Distract Large Language Models for Automatic Jailbreak Attack | EMNLP | 2024 |
| 4 | SeqAR: Jailbreak LLMs with Sequential Auto-Generated Characters | NAACL | 2025 |
| 5 | Enhancing Uncertainty Estimation in LLMs with Expectation of Aggregated Internal Belief | AAAI | 2026 |
| 6 | Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem | ACL | 2026 |
| 7 | Representation-Guided Parameter-Efficient LLM Unlearning | ACL Findings | 2026 |
| 8 | Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms | ACL Findings | 2026 |

---

## Non-Goals

- No navigation or layout changes
- No bilingual (`/zh/`) content changes
- No new pages or sections
- No style or theme changes

## Verification Criteria

- `about.md` renders with `肖泽管`, `School of Computing and Artificial Intelligence (SCAI)`, and includes LLM Unlearning
- `cv.md` renders with SUFE PhD, Jinan University MS, DUFE BS
- Publications page shows exactly 8 papers, all with correct titles and authors
- No dead links to wrong arXiv IDs or wrong ACL Anthology entries
