---
permalink: /
title: "Zeguan Xiao (肖泽管)"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a final-year PhD candidate at the [School of Computing and Artificial Intelligence (SCAI)](https://scai.sufe.edu.cn/), [Shanghai University of Finance and Economics (SUFE)](https://www.sufe.edu.cn/), advised by Prof. [Yun Chen](https://yunc.me/). I am also a visiting student at [Southern University of Science and Technology (SUSTech)](https://www.sustech.edu.cn/), working with Prof. [Guanhua Chen](https://ghchen.me/).

My research focuses on the **safety, alignment, and robustness of large language models (LLMs)**.

**I am actively looking for full-time research positions (industry or academia).** Feel free to reach out via email!

---

<h2 id="publications">Publications</h2>


{% include base_path %}

{% if site.publication_category %}
  {% for category in site.publication_category %}
    {% assign title_shown = false %}
    {% for post in site.publications reversed %}
      {% if post.category != category[0] %}
        {% continue %}
      {% endif %}
      {% unless title_shown %}
        <h3>{{ category[1].title }}</h3><hr />
        {% assign title_shown = true %}
      {% endunless %}
      {% include archive-single.html %}
    {% endfor %}
  {% endfor %}
{% else %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% endif %}
