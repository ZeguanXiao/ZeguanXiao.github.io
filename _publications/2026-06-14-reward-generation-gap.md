---
title: "Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms"
collection: publications
category: conferences
permalink: /publication/2026-06-14-reward-generation-gap
date: 2026-06-14
venue: "Findings of ACL 2026"
paperurl: "https://arxiv.org/abs/2506.09457"
---

**Zeguan Xiao**, Yun Chen, Jian Yang, Guanhua Chen, Ke Tang

[[arXiv]](https://arxiv.org/abs/2506.09457) [[Code]](https://github.com/sustech-nlp/POET)

---

We're excited to share our paper **"Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms"**, accepted at **Findings of ACL 2026**. This post gives an accessible overview of the paper's main idea: even when direct alignment algorithms optimize preferences over whole responses, language models still generate text token by token, and that mismatch matters more than it may seem.

Our proposed method, **POET (Prefix-Oriented Equal-length Training)**, is intentionally simple: instead of changing the optimization objective of methods like DPO or SimPO, it changes the training pairs so that the preferred and dispreferred responses are compared at the same length. This small adjustment turns out to consistently improve alignment performance across several settings.

---

## The Problem: Direct Alignment Still Misses Something

Direct Alignment Algorithms (DAAs), such as **DPO** and **SimPO**, are attractive because they are much simpler than the full RLHF pipeline. Rather than training a separate reward model and then running reinforcement learning, they optimize directly from preference pairs: a prompt, a preferred response, and a dispreferred response.

That simplicity is a big reason DAAs have become so widely used. But there is also a hidden limitation: these methods optimize preference at the **whole-sequence level**, while generation happens **left to right**, one token at a time.

This creates what we call the **reward-generation gap**:

- training rewards are defined over complete responses
- decoding quality depends heavily on early token decisions
- sequence-level optimization does not guarantee that the better response also has the better prefix

In other words, a model can become better at ranking full responses under the training objective without necessarily becoming better at generating strong prefixes during inference.

<figure>
<img src="/images/poet/intro_issue.png" alt="Illustration of the reward-generation gap: whole-sequence preference optimization does not guarantee better prefixes during autoregressive generation" style="width:100%">
<figcaption><strong>Figure 1:</strong> DAAs are trained to prefer one full response over another, but during inference the model must commit to prefix tokens first. Better sequence-level rewards do not automatically imply better early-generation behavior.</figcaption>
</figure>

---

## Our Key Insight: Good Generations Depend Disproportionately on Good Prefixes

Why should prefixes matter so much?

Because autoregressive generation is path-dependent. Once a model makes a weak choice early in a response, later tokens are produced under that flawed context. Early mistakes can propagate and become harder to recover from.

The paper argues that this matters especially for DAAs because their implicit reward signals effectively treat tokens too uniformly. But in generation, prefix tokens are often more consequential than later ones:

- they set the direction of the answer
- they influence tone, structure, and intent
- they shape all later predictions

This means that an alignment method can improve the score of a response "on average" while still under-emphasizing the part of the sequence that matters most for generation quality.

The central question then becomes:

**Can we train DAAs in a way that better reflects the importance of early tokens, without redesigning the algorithm from scratch?**

---

## Method: Prefix-Oriented Equal-length Training (POET)

Our answer is **POET**, a very simple data-level intervention.

For each preference pair:

1. Take the preferred response and the dispreferred response.
2. Find the length of the shorter one.
3. Truncate both responses to that same length.
4. Train the underlying DAA on these equal-length response pairs.

That is the whole method.

Why is this useful? Because it forces the comparison to happen over matched-length prefixes instead of letting longer suffixes dominate the learning signal. In effect, POET makes DAAs pay more attention to the part of the response that matters most during left-to-right generation.

This gives POET three practical advantages:

- **Universal compatibility:** it can be plugged into DPO, SimPO, and other DAAs without changing their objectives
- **Hyperparameter-free:** there is no extra truncation ratio to tune in the default version
- **Low implementation overhead:** it is just a preprocessing change to preference pairs

This simplicity was an important design goal for us. We did not want a method that only works if one also adopts a new loss, an extra reward model, or a delicate weighting schedule.

---

## Why Equal-Length Training Makes Sense

The natural concern is whether truncation destroys the original preference label. If the preferred response only becomes clearly better near the end, truncating it could introduce noise.

Our analysis suggests that this is often not the case in standard alignment data. The quality gap between preferred and dispreferred responses tends to emerge **early**, and then grows with diminishing returns as the prefix gets longer.

<figure>
<img src="/images/poet/delta_means.png" alt="Average prefix quality difference grows early and then plateaus as prefix length increases" style="width:100%">
<figcaption><strong>Figure 2:</strong> The quality gap between preferred and dispreferred responses appears early in the prefix and then gradually saturates. This is exactly the regime where equal-length training is most natural.</figcaption>
</figure>

This result supports the intuition behind POET:

- the early part of a response already contains much of the useful preference signal
- later tokens add information, but often with diminishing marginal value
- matching lengths is a reasonable way to reduce sequence-level bias while preserving preference structure

Empirically, the paper also finds high consistency between the original preference ordering and the truncated equal-length version, especially in higher-quality preference datasets.

---

## Results: Better Alignment Across Settings

We evaluate POET on top of both **DPO** and **SimPO**, across base and instruction-tuned models. The overall pattern is very consistent: POET improves instruction-following performance without introducing extra tuning burden.

The most striking headline result is a gain of **+11.8 points** on **AlpacaEval 2 LC** for **Mistral-Base + DPO**.

Here are a few representative examples from the paper:

| Setting | Baseline | + POET | Gain |
|---|---:|---:|---:|
| Mistral-Base (7B) + DPO, AlpacaEval 2 LC | 12.9 | 24.7 | **+11.8** |
| Llama-3-Base (8B) + DPO, AlpacaEval 2 LC | 16.9 | 28.4 | **+11.5** |
| Llama-3-Base (8B) + SimPO, AlpacaEval 2 LC | 28.0 | 33.8 | **+5.8** |
| Mistral-Base (7B) + DPO, safety rate | 45.2 | 82.1 | **+36.9** |

Two aspects are especially encouraging:

- **The gains are broad rather than isolated.** We see improvements across multiple model families and across both reference-based and reference-free DAAs.
- **The method helps where prefixes matter most.** Safety alignment is a good example: safe responses often diverge from unsafe ones very early, so emphasizing prefixes is especially effective there.

The paper also checks downstream tasks and finds that POET does **not** increase the usual alignment tax. In most settings, general capability is preserved, and in some cases it improves slightly as well.

---

## POET Actually Produces Better Prefixes

The most direct validation of the paper's story is not just that benchmark numbers go up, but that the trained models genuinely generate better prefixes.

That is exactly what we observe.

<figure>
<img src="/images/poet/prefix_quality.png" alt="Models trained with POET generate higher-quality prefixes across different prefix lengths" style="width:100%">
<figcaption><strong>Figure 3:</strong> Models trained with POET consistently generate higher-quality prefixes than their standard DAA counterparts across prefix lengths, supporting the paper's core mechanism.</figcaption>
</figure>

This is important because it closes the loop between the paper's diagnosis and its fix:

- the problem is a mismatch between training signals and generation dynamics
- POET changes training to pay more attention to matched prefixes
- the resulting models generate stronger prefixes in practice

That makes POET feel less like a heuristic and more like a targeted intervention on the actual failure mode.

---

## When Does POET Help Most?

POET is not a claim that every preference dataset should always be truncated in this way.

Its effectiveness depends on a practical condition: the preference ordering should mostly survive equal-length truncation. In datasets where the preferred answer only becomes clearly superior very late in the sequence, POET may help less or even hurt.

The paper's experiments suggest that POET works best when:

- preferred and dispreferred responses already differ meaningfully in their early prefixes
- the preference data has a reasonably strong quality gap
- the task cares about getting the beginning of the response right

This also explains why POET is especially compelling for instruction following and safety alignment, while tasks that hinge on a critical final token may be a less natural fit.

---

## Takeaway: Alignment Objectives Should Respect Generation Dynamics

The broader message of this paper is simple:

**If a model generates token by token, alignment methods should pay attention to where generation quality actually comes from.**

Direct alignment algorithms are powerful partly because they are simple. But simplicity at the sequence level can hide a mismatch with how language models actually decode. POET shows that we can reduce this mismatch with an equally simple intervention: compare preferred and dispreferred responses at equal length, so training better reflects prefix importance.

We like this result because it combines three things that do not always appear together:

- a clear diagnosis of a real limitation in current DAAs
- a lightweight method that is easy to adopt
- consistent empirical gains across models and tasks

If you are working with DPO-, SimPO-, or other DAA-style training pipelines, POET is a very low-friction idea worth trying.

---

## Citation

```bibtex
@inproceedings{xiao2026poet,
  title={Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms},
  author={Xiao, Zeguan and Chen, Yun and Yang, Jian and Chen, Guanhua and Tang, Ke},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  year={2026}
}
```
