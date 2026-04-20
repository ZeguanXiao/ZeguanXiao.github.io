---
title: "Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem"
collection: publications
category: conferences
permalink: /publication/2026-04-28-asymmetric-unlearning
date: 2026-04-28
venue: "ACL 2026"
paperurl: "https://arxiv.org/abs/2604.14808"
excerpt: "**Zeguan Xiao**, Siqing Li, Yong Wang, Xuetao Wei, Jian Yang, Yun Chen, Guanhua Chen"
project_page: true
---

<div class="project-page">
  <section class="project-hero">
    <p class="project-eyebrow">ACL 2026</p>
    <h1 class="project-title">Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem</h1>
    <p class="project-authors"><strong>Zeguan Xiao</strong>, Siqing Li, Yong Wang, Xuetao Wei, Jian Yang, Yun Chen, Guanhua Chen</p>
    <p class="project-meta">A project page for our ACL 2026 paper on making LLM unlearning more faithful to the real objective: preserve general capability first, and only forget where doing so does not damage retention.</p>
    <div class="project-links">
      <a class="project-link" href="https://arxiv.org/abs/2604.14808">arXiv</a>
      <a class="project-link" href="https://github.com/sustech-nlp/SAGO">Code</a>
    </div>
    <div class="project-grid">
      <article class="project-card">
        <h3>Retention</h3>
        <p>Treat general capability as the primary objective instead of a side constraint that can be traded away too aggressively.</p>
      </article>
      <article class="project-card">
        <h3>Forgetting</h3>
        <p>Inject forgetting only in directions that do not actively conflict with the retain signal.</p>
      </article>
      <article class="project-card">
        <h3>Guarantee</h3>
        <p>SAGO builds updates that stay aligned with retention coordinate by coordinate, not just on average.</p>
      </article>
    </div>
  </section>

  <section class="project-teaser">
    <div class="project-figure-grid">
      <figure>
        <img src="/images/sago/fig2_gradient_illustration.png" alt="Comparison of PCGrad and SAGO gradient synthesis" />
      </figure>
      <figure>
        <img src="/images/sago/fig3_wmdp_pareto.png" alt="Pareto frontier improvements on WMDP with SAGO" />
      </figure>
    </div>
    <p class="project-caption"><strong>Figure overview.</strong> The page starts with the central story of the paper: SAGO changes how forget and retain gradients are combined, and that change pushes the forgetting-retention Pareto frontier upward on WMDP.</p>
  </section>

  <section class="project-section">
    <h2>Motivation</h2>
    <p>LLM unlearning is attractive because it aims to remove dangerous or private knowledge from a model itself, rather than only teaching the model to refuse when asked. In principle that is a stronger defense: if a model genuinely no longer retains a harmful capability, jailbreaks should become much less effective.</p>
    <p>The hard part is that unlearning is never just a forgetting problem. It is also a retention problem. Push too hard and the model loses useful knowledge and general performance. Push too softly and the target knowledge remains recoverable. This is why many unlearning methods end up living on an uncomfortable frontier between forgetting strength and capability preservation.</p>
    <p>Our paper argues that the usual framing is slightly off. The problem is not simply “balance two losses better.” The real question is how to combine updates so that forgetting is allowed only where it does not sabotage retention.</p>
  </section>

  <section class="project-section project-section--alt">
    <h2>Asymmetric Two-Task Learning</h2>
    <p>We recast LLM unlearning as an <strong>asymmetric two-task learning</strong> problem. There are two tasks in play, but they do not have equal status:</p>
    <div class="project-grid">
      <article class="project-card">
        <h3>Primary task</h3>
        <p><strong>Retention</strong> should be preserved whenever possible because it represents the model's general capability and non-target knowledge.</p>
      </article>
      <article class="project-card">
        <h3>Auxiliary task</h3>
        <p><strong>Forgetting</strong> is still necessary, but it should operate under a do-no-harm principle relative to retention.</p>
      </article>
      <article class="project-card">
        <h3>Design shift</h3>
        <p>This changes the engineering target from loss balancing to <strong>retention-prioritized gradient synthesis</strong>.</p>
      </article>
    </div>
    <p>That asymmetric framing is important because it matches how practitioners already evaluate unlearning methods. A method is not considered successful if it forgets well but destroys the model. We should therefore encode that hierarchy directly into the update rule.</p>
  </section>

  <section class="project-section">
    <h2>How SAGO Synthesizes Gradients</h2>
    <p>At each update step, we compute two signals: a forget gradient and a retain gradient. The question is how to merge them. A naive difference-style update can work against retention in exactly the coordinates where general capability is stored. PCGrad improves on this by removing part of the conflict, but it still reasons at a coarser level.</p>
    <p><strong>SAGO</strong>, short for <strong>Sign-Align Gradient Optimization</strong>, goes finer-grained. It examines the relationship between forget and retain gradients element by element:</p>
    <ul>
      <li>If a coordinate is <strong>conflicting</strong>, SAGO keeps the retain direction and blocks the forget direction there.</li>
      <li>If a coordinate is <strong>aligned</strong>, SAGO allows the forget update through because it does not fight retention.</li>
      <li>The final update therefore never points against the retain signal in any coordinate.</li>
    </ul>
    <p>The result is a simple rule with a strong intuition: keep the parts of forgetting that are safe, and suppress the parts that would damage what we want to preserve.</p>
  </section>

  <section class="project-section project-section--alt">
    <h2>What the Results Show</h2>
    <p>Across WMDP and RWKU, SAGO consistently improves the trade-off curve instead of merely moving to a different operating point. That is the main empirical message of the paper.</p>
    <div class="project-results-table">
      <table>
        <thead>
          <tr>
            <th>Method</th>
            <th>MMLU (↑)</th>
            <th>Forget Acc (↓)</th>
            <th>Target Recovery</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Naive</td>
            <td>26.7</td>
            <td>26.1</td>
            <td>44.6%</td>
          </tr>
          <tr>
            <td>+ PCGrad</td>
            <td>56.4</td>
            <td>28.9</td>
            <td>94.0%</td>
          </tr>
          <tr>
            <td><strong>+ SAGO</strong></td>
            <td><strong>57.4</strong></td>
            <td><strong>28.2</strong></td>
            <td><strong>96.0%</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="project-note">Representative result on WMDP Bio with SimNPO+GD. SAGO recovers more of the original model's general performance while maintaining comparable forgetting strength.</p>
    <p>The broader pattern is just as encouraging. On RWKU, SAGO preserves neighboring knowledge much better than stronger but less selective baselines. That matters because practical unlearning is rarely about erasing one isolated fact. It is about removing a target while keeping the surrounding knowledge graph intact.</p>
    <figure>
      <img src="/images/sago/fig4_rwku_pareto.png" alt="RWKU Pareto frontier showing better retention with SAGO" />
      <p class="project-caption"><strong>RWKU trade-offs.</strong> SAGO also improves the frontier on real-world knowledge unlearning, not only on the safety-oriented WMDP setting.</p>
    </figure>
  </section>

  <details class="project-details">
    <summary>More evidence: optimization dynamics and geometry</summary>
    <div class="project-figure-grid" style="margin-top: 1rem;">
      <figure>
        <img src="/images/sago/fig1_loss_dynamics.png" alt="Loss dynamics during unlearning on WMDP Biosecurity" />
        <p class="project-caption"><strong>Loss dynamics.</strong> SAGO keeps retain loss under tighter control while still driving the forget objective effectively.</p>
      </figure>
      <figure>
        <div class="project-results-table">
          <table>
            <thead>
              <tr>
                <th>Method</th>
                <th>Forget-Retain</th>
                <th>Comb-Retain</th>
                <th>Comb-Forget</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>GradDiff</td>
                <td>-0.22</td>
                <td>0.55</td>
                <td>0.82</td>
              </tr>
              <tr>
                <td>PCGrad</td>
                <td>-0.22</td>
                <td>0.76</td>
                <td>0.52</td>
              </tr>
              <tr>
                <td><strong>SAGO</strong></td>
                <td><strong>-0.15</strong></td>
                <td><strong>0.87</strong></td>
                <td>0.48</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="project-caption"><strong>Geometry analysis.</strong> SAGO yields the strongest alignment with the retain direction while keeping enough forgetting pressure to remain effective.</p>
      </figure>
    </div>
  </details>

  <section class="project-section">
    <h2>Why the Geometry Matters</h2>
    <p>One reason we like SAGO is that it is not just an empirical trick. Its behavior lines up with the core failure mode of unlearning. When forget and retain gradients disagree, the model is being asked to modify parameters that likely support general capability. Those are exactly the places where a careless update causes collateral damage.</p>
    <p>SAGO addresses this directly. Instead of averaging away the conflict, it respects the hierarchy between tasks. That gives it a more faithful objective: forgetting should happen, but only where it is compatible with retention. In that sense, the method is both practical and conceptually clean.</p>
  </section>

  <section class="project-section project-section--alt">
    <h2>Takeaway</h2>
    <p>The paper's main message is simple: <strong>LLM unlearning should be treated as an asymmetric optimization problem</strong>. Once we encode that asymmetry into gradient synthesis, the forgetting-retention trade-off becomes much easier to navigate.</p>
    <p>SAGO is appealing because it stays lightweight. It can be plugged into existing forget-plus-retain pipelines, introduces a clear safety-first inductive bias, and consistently pushes the Pareto frontier in the right direction. For practitioners, that means better retention at comparable forgetting strength. For researchers, it suggests that update geometry is at least as important as loss design in unlearning.</p>
  </section>

  <section class="project-section project-citation">
    <h2>Citation</h2>
    <pre><code class="language-bibtex">@inproceedings{xiao2026sago,
  title={Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem},
  author={Xiao, Zeguan and Li, Siqing and Wang, Yong and Wei, Xuetao and Yang, Jian and Chen, Yun and Chen, Guanhua},
  booktitle={Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2026}
}</code></pre>
  </section>
</div>
