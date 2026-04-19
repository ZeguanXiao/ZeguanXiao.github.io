---
title: "Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem"
collection: publications
category: conferences
permalink: /publication/2025-04-30-asymmetric-unlearning
date: 2026-04-28
venue: "ACL 2026"
paperurl: "https://arxiv.org/abs/2604.14808"
---

**Zeguan Xiao**, Siqing Li, Yong Wang, Xuetao Wei, Jian Yang, Yun Chen, Guanhua Chen

*Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL), 2026*

[[arXiv]](https://arxiv.org/abs/2604.14808) [[Code]](https://github.com/sustech-nlp/SAGO)

## TL;DR

We recast LLM unlearning as an **asymmetric two-task problem** — retention is the primary objective, forgetting is auxiliary — and propose **SAGO** (Sign-Align Gradient Optimization), a retention-prioritized gradient synthesis method. On WMDP and RWKU benchmarks, SAGO recovers up to 96% of original model performance while maintaining strong forgetting, showing that *reshaping gradient geometry* beats simple loss re-balancing.

## Motivation

Machine unlearning for LLMs aims to remove targeted knowledge (e.g., hazardous biosecurity or cybersecurity information) while preserving the model's general capabilities. Existing methods like Gradient Ascent (GA) on the forget set often cause catastrophic performance degradation. Even improved methods (NPO, SimNPO, GradDiff) that combine forget and retain objectives still suffer from **gradient conflicts** — the forget and retain gradients pulling the model in opposing directions.

A key observation motivates our work: unlearning is *not* a symmetric multi-task learning problem. We don't seek a balanced compromise between forgetting and retaining. Instead, retention is the **primary** objective (the model should still work well), and forgetting is **auxiliary** (applied under a do-no-harm constraint). This asymmetry makes standard multi-task methods, which aim to equalize task progress, suboptimal or even harmful.

## Method: Retention-Prioritized Gradient Synthesis

We propose a framework that decouples task-specific gradient extraction from conflict-aware combination:

1. **Compute task gradients separately**: Extract forget gradient $g_f$ and retain gradient $g_r$ independently.
2. **Synthesize a conflict-free update**: Combine them using a retention-prioritized strategy.

We instantiate this framework with two methods:

### PCGrad (Adapted)

We adapt Project Conflicting Gradients to the unlearning setting with a **module-wise** variant. When the forget gradient conflicts with the retain gradient in a specific module, we project the forget gradient onto the orthogonal complement of the retain gradient — removing only the harmful component while preserving beneficial forgetting directions.

### SAGO (Our Proposed Method)

SAGO performs **element-wise sign-aligned gating**:
- For parameters where forget and retain gradients have **the same sign** (no conflict): allow the forget gradient through.
- For parameters where they have **opposite signs** (conflict): use the retain gradient instead.

$$\tilde{g}_f = g_f \odot \mathbb{I}(g_f \odot g_r \geq 0), \quad \tilde{g}_r = g_r \odot \mathbb{I}(g_f \odot g_r < 0)$$

$$g_{\text{final}} = \alpha \tilde{g}_r + \gamma \tilde{g}_f$$

This guarantees that **no coordinate in the final update ever opposes the retain gradient**, achieving strictly tighter alignment with retention than PCGrad.

## Theoretical Guarantees

Both PCGrad and SAGO ensure non-negative cosine similarity with the retain gradient $g_r$:
- **PCGrad**: $\cos\theta_P = (1 + \|\tilde{g}_f\|^2 / \|g_r\|^2)^{-1/2} \geq 0$
- **SAGO**: Achieves strictly positive cosine similarity through element-wise sign constraints, with no dimension ever opposing retention.

SAGO's advantage comes from two mechanisms: (1) the gated gradients are orthogonal by construction ($\tilde{g}_f^\top \tilde{g}_r = 0$), eliminating direct conflicts; and (2) every coordinate of the final update is sign-aligned with $g_r$.

## Key Results

### WMDP Benchmark (Biosecurity & Cybersecurity)

| Method (Bio) | Forget ↓ | MMLU ↑ | Recovery % |
|---|---|---|---|
| SimNPO+GD (naive) | 26.7 | 26.7 | 44.6% |
| + PCGrad | 27.6 | 56.4 | 94.0% |
| + SAGO | **28.2** | **57.4** | **96.0%** |

SAGO consistently pushes the Pareto frontier outward: at comparable forgetting levels, it achieves substantially higher retention across all base objectives (GA+GD, NPO+GD, SimNPO+GD).

### RWKU Benchmark (Real-World Knowledge Unlearning)

On RWKU with LLaMA3-8B-Instruct, SAGO improves neighbor retention by up to +13.3 ROUGE-L points over PCGrad while maintaining effective forgetting, strictly dominating prior methods on the retention-forgetting frontier.

### Gradient Geometry Analysis

Tracking cosine similarities over 100 training steps reveals:
- SAGO achieves the **highest Comb-Retain similarity** (strongest alignment with retention)
- SAGO reduces the natural Forget-Retain conflict (negative cosine similarity is weakest)
- GradDiff achieves high Comb-Forget but at the cost of degraded retention

## Key Takeaway

> The key to effective LLM unlearning is **reshaping gradient geometry** — how loss gradients are combined and resolved — rather than merely re-balancing losses between forgetting and retention tasks.

Our framework is **plug-and-play**: it integrates seamlessly with diverse unlearning objectives (GA+GD, NPO+GD, SimNPO+GD) and is readily extensible to future methods. The code is available at [https://github.com/sustech-nlp/SAGO](https://github.com/sustech-nlp/SAGO).
