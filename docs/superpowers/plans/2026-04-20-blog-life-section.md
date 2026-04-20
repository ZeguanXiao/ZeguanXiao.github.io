# Blog / Life Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Blog section to the site where personal life content (travel, reading, hobbies, photography, etc.) can be published, completely separate from the academic sections.

**Architecture:** Use Jekyll's existing `_posts` collection (already configured in `_config.yml`). Add a `/blog/` archive page that lists all posts grouped by year (matching the `year-archive.html` pattern already in the codebase). Add a "Blog" entry to the header navigation.

**Tech Stack:** Jekyll, Liquid templates, YAML front matter

---

### Task 1: Add Blog entry to navigation

**Files:**
- Modify: `_data/navigation.yml`

- [ ] **Step 1: Open `_data/navigation.yml`**

Current content:
```yaml
main:
  - title: "Publications"
    url: /#publications
```

- [ ] **Step 2: Add the Blog entry**

Replace the full file with:
```yaml
main:
  - title: "Publications"
    url: /#publications
  - title: "Blog"
    url: /blog/
```

- [ ] **Step 3: Commit**

```bash
git add _data/navigation.yml
git commit -m "feat: add Blog entry to site navigation"
```

---

### Task 2: Create the Blog archive page

**Files:**
- Create: `_pages/blog.html`

- [ ] **Step 1: Create `_pages/blog.html`**

```html
---
layout: archive
title: "Blog"
permalink: /blog/
author_profile: true
---

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    <h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}
```

Posts are grouped by year (same pattern as `_pages/year-archive.html`). The `archive-single.html` include renders each post with title, date, excerpt, and optional teaser image.

- [ ] **Step 2: Commit**

```bash
git add _pages/blog.html
git commit -m "feat: add Blog archive page at /blog/"
```

---

### Task 3: Add a sample life post to verify

**Files:**
- Create: `_posts/2026-04-20-hello-blog.md`

- [ ] **Step 1: Create the sample post**

```markdown
---
title: "Hello, Blog!"
date: 2026-04-20
categories: [life]
tags: [meta]
excerpt: "Starting a personal blog section on this site."
---

A place to share thoughts on life outside of research — travels, books, music, and whatever else I find interesting.
```

- [ ] **Step 2: Start the Jekyll dev server**

```bash
bundle exec jekyll serve -l -H localhost
```

- [ ] **Step 3: Verify the blog page**

Open http://localhost:4000/blog/ in a browser.

Expected:
- Page title "Blog" appears
- "Blog" link is visible in the site header navigation
- The "Hello, Blog!" post is listed under a "2026" year heading

- [ ] **Step 4: Verify category archive**

Open http://localhost:4000/categories/life/ and confirm the post appears there.

- [ ] **Step 5: Commit sample post**

```bash
git add _posts/2026-04-20-hello-blog.md
git commit -m "feat: add sample life blog post"
```

---

## Writing New Life Posts

All future life posts follow this front matter convention:

```yaml
---
title: "Post Title"
date: YYYY-MM-DD
categories: [life, travel]   # always include "life"; add topic category
tags: [optional, freeform, tags]
excerpt: "One sentence shown in the post list."
header:
  teaser: /images/optional-thumbnail.jpg  # 300x200px recommended
---
```

Suggested topic categories alongside `life`:
- `travel` — trips and places
- `reading` — books and articles
- `music` — concerts, playlists, discoveries
- `photography` — photo essays
- `gaming` — games played

Image files go in `/images/`. Reference in posts with `![alt text](/images/filename.jpg)`.
