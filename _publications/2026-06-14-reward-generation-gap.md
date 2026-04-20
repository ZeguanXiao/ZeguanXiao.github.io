---
title: "Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms"
collection: publications
category: conferences
permalink: /publication/2026-06-14-reward-generation-gap
date: 2026-06-14
venue: "Findings of ACL 2026"
paperurl: "https://arxiv.org/abs/2506.09457"
excerpt: "**Zeguan Xiao**, Yun Chen, Jian Yang, Guanhua Chen, Ke Tang"
project_page: true
---

<div class="project-page">
  <section class="project-hero">
    <p class="project-eyebrow">Findings of ACL 2026</p>
    <h1 class="project-title">Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms</h1>
    <p class="project-authors"><strong>Zeguan Xiao</strong>, Yun Chen, Jian Yang, Guanhua Chen, Ke Tang</p>
    <p class="project-meta">This page gives an intuition-first overview of POET, our lightweight method for making direct alignment algorithms better reflect the token-by-token dynamics of language generation.</p>
    <div class="project-links">
      <a class="project-link" href="https://arxiv.org/abs/2506.09457">arXiv</a>
      <a class="project-link" href="https://github.com/sustech-nlp/POET">Code</a>
    </div>
    <div class="project-grid">
      <article class="project-card">
        <h3>Problem</h3>
        <p>Direct alignment methods score full responses, but language models actually commit to prefixes first during decoding.</p>
      </article>
      <article class="project-card">
        <h3>Intervention</h3>
        <p>POET compares preferred and dispreferred responses at matched length, shifting attention toward the part of the sequence that drives generation.</p>
      </article>
      <article class="project-card">
        <h3>Benefit</h3>
        <p>The method is simple, hyperparameter-free in its default form, and improves alignment quality across several settings.</p>
      </article>
    </div>
  </section>

  <section class="project-teaser">
    <figure>
      <img src="/images/poet/intro_issue.png" alt="Illustration of the reward-generation gap between sequence-level rewards and prefix quality" />
      <p class="project-caption"><strong>Core mismatch.</strong> Direct alignment algorithms optimize over full responses, but real generation is autoregressive. Better sequence-level preference scores do not automatically imply stronger early prefixes.</p>
    </figure>
  </section>

  <section class="project-section">
    <h2>Motivation</h2>
    <p>Direct alignment algorithms such as DPO and SimPO are popular because they simplify the RLHF pipeline. Instead of learning a separate reward model and then optimizing with reinforcement learning, they train directly from preference pairs. That simplicity is a major reason these methods are so widely used.</p>
    <p>But there is an underappreciated mismatch hiding inside that setup. Training rewards are defined over complete responses, whereas inference unfolds one token at a time from left to right. A model can therefore become better at ranking full sequences under the training objective without becoming equally better at generating the crucial early tokens that steer the rest of the response.</p>
    <p>We call this the <strong>reward-generation gap</strong>. The paper asks a straightforward question: can we reduce that gap without redesigning direct alignment from scratch?</p>
  </section>

  <section class="project-section project-section--alt">
    <h2>Why Prefixes Matter</h2>
    <p>Autoregressive generation is path-dependent. Once a model makes a weak choice near the beginning of a response, later tokens are produced under that weaker context. Early mistakes can compound. In practice, prefix tokens often determine the direction, tone, structure, and safety profile of the whole answer.</p>
    <p>That is why sequence-level optimization can miss something important. It treats the response as a single object, but the model experiences generation as a sequence of irreversible local commitments. If the preference signal is dominated by later suffix differences, learning may underweight the part of the response that matters most during actual decoding.</p>
    <figure>
      <img src="/images/poet/delta_means.png" alt="Prefix quality difference emerging early and saturating with longer prefixes" />
      <p class="project-caption"><strong>Early signal.</strong> The quality gap between preferred and dispreferred responses already emerges early in the prefix and then tends to saturate, which makes prefix-aware comparisons especially natural.</p>
    </figure>
  </section>

  <section class="project-section">
    <h2>POET in One Idea</h2>
    <p><strong>POET</strong>, short for <strong>Prefix-Oriented Equal-length Training</strong>, is intentionally simple. For each preferred and dispreferred pair, we truncate both responses to the length of the shorter one and train the underlying direct alignment algorithm on those matched-length responses.</p>
    <p>The intervention is small, but the intuition is strong. Equal-length comparison prevents later suffixes from dominating the signal and encourages the method to focus on matched prefixes. That makes the learning problem better aligned with how the model will later generate text.</p>
    <div class="project-grid">
      <article class="project-card">
        <h3>Universal</h3>
        <p>POET works on top of DPO, SimPO, and other direct alignment pipelines because it modifies the training pairs rather than the objective itself.</p>
      </article>
      <article class="project-card">
        <h3>Lightweight</h3>
        <p>No extra reward model, no custom decoding trick, and no mandatory new hyperparameter in the default setup.</p>
      </article>
      <article class="project-card">
        <h3>Targeted</h3>
        <p>The method addresses a specific mismatch between training and inference instead of adding general complexity.</p>
      </article>
    </div>
  </section>

  <section class="project-section project-section--alt">
    <h2>Why Equal-Length Training Helps</h2>
    <p>The natural concern is whether truncation might corrupt the preference label. If the preferred response becomes clearly better only near the end, matching lengths could discard the decisive evidence. Our analysis suggests that many preference datasets do not behave that way. The quality gap often appears early and then grows with diminishing returns.</p>
    <p>That means equal-length training can remove an important bias without throwing away most of the useful signal. Later tokens still matter, but they are not always the most informative part of the comparison for learning to generate better answers.</p>
    <p>From that perspective, POET is not a heuristic bolt-on. It is a data-level way to bring the training comparison closer to the structure of generation.</p>
  </section>

  <section class="project-section">
    <h2>Results Across Settings</h2>
    <p>The empirical pattern is consistent: POET improves alignment quality across multiple model families and multiple direct alignment objectives, while keeping the implementation burden extremely low.</p>
    <div class="project-results-table">
      <table>
        <thead>
          <tr>
            <th>Setting</th>
            <th>Baseline</th>
            <th>+ POET</th>
            <th>Gain</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Mistral-Base (7B) + DPO, AlpacaEval 2 LC</td>
            <td>12.9</td>
            <td>24.7</td>
            <td><strong>+11.8</strong></td>
          </tr>
          <tr>
            <td>Llama-3-Base (8B) + DPO, AlpacaEval 2 LC</td>
            <td>16.9</td>
            <td>28.4</td>
            <td><strong>+11.5</strong></td>
          </tr>
          <tr>
            <td>Llama-3-Base (8B) + SimPO, AlpacaEval 2 LC</td>
            <td>28.0</td>
            <td>33.8</td>
            <td><strong>+5.8</strong></td>
          </tr>
          <tr>
            <td>Mistral-Base (7B) + DPO, safety rate</td>
            <td>45.2</td>
            <td>82.1</td>
            <td><strong>+36.9</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="project-note">Representative results reported in the paper. The strongest gains appear in exactly the settings where getting the early trajectory of a response right matters most.</p>
    <figure>
      <img src="/images/poet/prefix_quality.png" alt="Higher-quality generated prefixes after POET training" />
      <p class="project-caption"><strong>Mechanism validation.</strong> Models trained with POET generate stronger prefixes across prefix lengths, which directly supports the paper's core explanation of why the method works.</p>
    </figure>
  </section>

  <details class="project-details">
    <summary>More context: when POET is likely to help</summary>
    <div style="margin-top: 1rem;">
      <p>POET is most compelling when preferred and dispreferred responses already diverge meaningfully in their early prefixes, and when the task depends heavily on getting the beginning of the answer right. That makes the method especially natural for instruction following and safety alignment.</p>
      <p>By contrast, if a dataset's preference labels depend mostly on very late tokens, equal-length truncation may help less. The method is therefore best understood as a targeted correction for a specific training-inference mismatch, not as a claim that every preference dataset should always be truncated.</p>
    </div>
  </details>

  <section class="project-section project-section--alt">
    <h2>Takeaway</h2>
    <p>The broader lesson of this paper is that <strong>alignment objectives should respect generation dynamics</strong>. Direct alignment methods are appealing because they are simple, but sequence-level simplicity can hide a real mismatch with how language models actually decode.</p>
    <p>POET shows that a very small intervention can reduce that mismatch. By forcing preferred and dispreferred responses to be compared at the same length, the training signal becomes more sensitive to prefixes and therefore more faithful to the part of the sequence that dominates real generation. That combination of clarity, simplicity, and broad empirical gain is what makes the result exciting to us.</p>
  </section>

  <section class="project-section project-citation">
    <h2>Citation</h2>
    <pre><code class="language-bibtex">@inproceedings{xiao2026poet,
  title={Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms},
  author={Xiao, Zeguan and Chen, Yun and Yang, Jian and Chen, Guanhua and Tang, Ke},
  booktitle={Findings of the Association for Computational Linguistics: ACL 2026},
  year={2026}
}</code></pre>
  </section>
</div>
