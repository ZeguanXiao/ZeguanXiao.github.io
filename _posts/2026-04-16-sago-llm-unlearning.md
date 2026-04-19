---
title: "SAGO: Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem"
date: 2026-04-16
permalink: /posts/2026/04/sago-llm-unlearning/
tags:
  - LLM Unlearning
  - Machine Unlearning
  - Gradient Optimization
  - AI Safety
  - ACL 2026
---

We're excited to share our latest work **"Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem"**, accepted at **ACL 2026**! In this post, we provide an accessible overview of the key ideas, our proposed method **SAGO (Sign-Align Gradient Optimization)**, and the main results.

📄 **Paper**: [arXiv:2604.14808](https://arxiv.org/abs/2604.14808) &nbsp; | &nbsp; 💻 **Code**: [github.com/sustech-nlp/SAGO](https://github.com/sustech-nlp/SAGO)

---

## The Problem: LLM Unlearning is Hard

Large Language Models memorize vast amounts of knowledge from their training data — including private information and potentially hazardous content (e.g., biosecurity, cybersecurity threats). While alignment training can teach models to *refuse* harmful queries, adversaries can easily bypass these safeguards through jailbreak attacks.

**Machine Unlearning** offers a more fundamental solution: directly *removing* dangerous knowledge from the model so that even if jailbroken, the model simply doesn't know the harmful content anymore.

However, unlearning faces a critical challenge: **the forgetting-retention trade-off**. Aggressive unlearning degrades the model's general capabilities, while gentle unlearning fails to fully remove the targeted knowledge.

---

## Our Key Insight: Asymmetric Two-Task Learning

We recast LLM unlearning as an **asymmetric two-task learning** problem:

| | Retention (Primary) | Forgetting (Auxiliary) |
|---|---|---|
| **Priority** | ★★★ High | ★ Low |
| **Goal** | Preserve general capabilities | Remove targeted knowledge |
| **Constraint** | Must not be degraded | Applied under do-no-harm |

Unlike standard multi-task learning which seeks a balanced compromise between tasks, unlearning has a **fundamental asymmetry**: retention is the primary objective, and forgetting should only happen where it doesn't harm retention.

This insight motivates a shift from *loss balancing* to **retention-prioritized gradient synthesis**.

---

## Method: Retention-Prioritized Gradient Synthesis

Our framework (Algorithm 1) operates through a simple yet effective two-stage iterative process:

1. **Extract** task-specific gradients: compute forget gradient $g_f$ and retain gradient $g_r$ separately
2. **Synthesize** a conflict-aware update direction using either PCGrad or our novel SAGO

The key design principle: *inject forgetting only where it does not fight retention*.

### PCGrad Adaptation (Module-wise)

We adapt PCGrad to the unlearning setting by projecting the forget gradient onto the orthogonal complement of the retain gradient — but we do this **per-module** rather than globally:

$$\tilde{g}_f^j = g_f^j - \frac{g_f^j \cdot g_r^j}{\|g_r^j\|^2} g_r^j$$

This localized projection prevents conflicts in one module from triggering unnecessary correction elsewhere.

### SAGO: Sign-Align Gradient Optimization

SAGO takes a finer-grained approach through **element-wise sign alignment**:

- **Conflicting dimensions** (where $g_f$ and $g_r$ have opposite signs): Use only the retain gradient — these dimensions carry general knowledge
- **Aligned dimensions** (where $g_f$ and $g_r$ have the same sign): Allow the forget gradient through — these are task-specific and conflict-free

Formally:

$$\tilde{g}_f = g_f \odot \mathbb{I}(g_f \odot g_r \geq 0)$$

$$\tilde{g}_r = g_r \odot \mathbb{I}(g_f \odot g_r < 0)$$

$$g_{\text{final}} = \alpha \tilde{g}_r + \gamma \tilde{g}_f$$

This guarantees that **no coordinate in the final update ever points against the retain signal**.

<figure>
<img src="/images/sago/fig2_gradient_illustration.png" alt="Illustration of PCGrad vs SAGO gradient synthesis" style="width:100%">
<figcaption><strong>Figure 2:</strong> Illustration of final update gradients (red) in PCGrad (a) and SAGO (b). PCGrad projects the forget gradient orthogonally onto the retain gradient. SAGO selectively uses retain gradients in conflicting dimensions and forget gradients in aligned dimensions, achieving higher alignment with the retain direction.</figcaption>
</figure>

---

## Why SAGO Works Better: Theoretical Guarantees

Both PCGrad and SAGO guarantee **non-negative cosine similarity** with the retain gradient, ensuring the update never moves against retention. But SAGO achieves **strictly tighter alignment**:

- **PCGrad**: The projected forget gradient $\tilde{g}_f$ can still dominate in certain dimensions (when $|\tilde{g}_f^i| > |g_r^i|$), causing the final update to oppose retention locally.
- **SAGO**: Guarantees $g_{\text{final}}^i \cdot g_r^i \geq 0$ for **every** dimension — complete elimination of antagonistic updates.

---

## Results: Pushing the Pareto Frontier

### WMDP Benchmark (Biosecurity & Cybersecurity)

<figure>
<img src="/images/sago/fig3_wmdp_pareto.png" alt="Pareto frontier on WMDP benchmark" style="width:100%">
<figcaption><strong>Figure 3:</strong> Performance trade-offs on WMDP Bio (left) and Cyber (right). Stars (★) represent SAGO variants, which consistently push the Pareto frontier upward — better retention at comparable forgetting strength.</figcaption>
</figure>

Key results on **WMDP Bio** (SimNPO+GD):

| Method | MMLU (↑) | Forget Acc (↓) | % Target Recovery |
|--------|----------|----------------|-------------------|
| Naive | 26.7 | 26.1 | 44.6% |
| + PCGrad | 56.4 | 28.9 | 94.0% |
| + **SAGO** | **57.4** | **28.2** | **96.0%** |

SAGO recovers **96% of the original model's MMLU performance** while maintaining comparable forgetting strength!

### RWKU Benchmark (Real-World Knowledge Unlearning)

<figure>
<img src="/images/sago/fig4_rwku_pareto.png" alt="Pareto frontier on RWKU benchmark" style="width:100%">
<figcaption><strong>Figure 4:</strong> Trade-offs on RWKU. SAGO produces a better Pareto frontier than both baselines and PCGrad, achieving superior retention with effective forgetting.</figcaption>
</figure>

On RWKU, SAGO improves neighbor retention by up to **+13.3 ROUGE-L** over PCGrad (GA+GD setting), demonstrating particularly strong gains in preserving knowledge about related but non-targeted entities.

### Loss Dynamics Visualization

<figure>
<img src="/images/sago/fig1_loss_dynamics.png" alt="Loss dynamics during unlearning" style="width:100%">
<figcaption><strong>Figure 1:</strong> Loss dynamics on WMDP Biosecurity. Panels (a) and (b) show that SAGO maintains low retain loss while achieving high forget loss. Panel (c) illustrates how PCGrad and SAGO dynamically refine gradients compared to naive GradDiff.</figcaption>
</figure>

---

## Gradient Geometry Analysis

To understand *why* SAGO works so well, we analyzed the cosine similarity between different gradient components:

| Method | Forget-Retain | Comb-Retain | Comb-Forget |
|--------|--------------|-------------|-------------|
| GradDiff | −0.22 | 0.55 | 0.82 |
| PCGrad | −0.22 | 0.76 | 0.52 |
| **SAGO** | **−0.15** | **0.87** | 0.48 |

Key takeaways:
- SAGO achieves the **highest alignment with the retain gradient** (Comb-Retain = 0.87)
- SAGO also **reduces the raw conflict** between forget and retain gradients (Forget-Retain = −0.15 vs −0.22)
- The controlled, moderate Comb-Forget value ensures forgetting still happens — just without harming retention

---

## Takeaway: Reshape Gradient Geometry, Don't Just Re-balance Losses

Our results demonstrate a fundamental insight: **re-shaping gradient geometry** is the key to mitigating unlearning-retention trade-offs, rather than simply re-balancing loss weights.

SAGO provides a simple, modular, and theoretically grounded solution that:
- ✅ Plugs into any existing forget+retain objective (GA+GD, NPO+GD, SimNPO+GD)
- ✅ Guarantees retention-aligned updates at every parameter
- ✅ Consistently pushes the Pareto frontier across benchmarks
- ✅ Requires no additional hyperparameter tuning beyond the base method

---

## Citation

```bibtex
@inproceedings{xiao2026sago,
  title={Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem},
  author={Xiao, Zeguan and Li, Siqing and Wang, Yong and Wei, Xuetao and Yang, Jian and Chen, Yun and Chen, Guanhua},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2026}
}
```
