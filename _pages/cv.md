---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* Ph.D. in Management Science and Engineering, Shanghai University of Finance and Economics (SUFE), Sept 2022 – Jul 2026 (expected)
  * School of Computing and Artificial Intelligence (SCAI)
  * Advisor: Prof. Yun Chen
* Visiting Student, Southern University of Science and Technology (SUSTech), Apr 2023 – Apr 2026
  * Advisor: Prof. Guanhua Chen
* M.S. in Computer Software and Theory, Jinan University, Sept 2018 – Jul 2021
* B.S. in Economic Statistics, Dongbei University of Finance and Economics, Sept 2014 – Jul 2018

Research Interests
======
* LLM Safety & Red-teaming: automated adversarial attack generation, jailbreak detection and defense
* LLM Alignment: scalable oversight, reward modeling, preference learning
* LLM Robustness: out-of-distribution generalization, calibration
* LLM Unlearning: capability-preserving unlearning, robust unlearning against relearning attacks

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

