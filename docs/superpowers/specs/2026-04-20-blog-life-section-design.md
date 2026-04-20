# Blog / Life Section Design

**Date:** 2026-04-20  
**Status:** Approved

## Problem

The site is currently a pure academic homepage. The owner wants to also share personal life content (travel, reading, hobbies, photography, etc.) without mixing it into the academic sections.

## Approach

Use Jekyll's existing `_posts` collection (already configured in `_config.yml`) to power a dedicated **Blog** section. Posts use `categories` front matter to organize content types. A new archive page at `/blog/` lists all posts. A single navigation entry is added.

## Changes Required

### 1. `_data/navigation.yml`
Add a "Blog" link:
```yaml
main:
  - title: "Publications"
    url: /#publications
  - title: "Blog"
    url: /blog/
```

### 2. `_pages/blog.html`
New page using the `archive` layout to list all posts:
```html
---
title: "Blog"
layout: archive
permalink: /blog/
author_profile: true
---

{% capture written_label %}'Others'{% endcapture %}

{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}
```

### 3. Post Front Matter Convention
All life posts go in `_posts/` with filename `YYYY-MM-DD-slug.md`:
```yaml
---
title: "Post Title"
date: YYYY-MM-DD
categories: [life, travel]   # life + topic tag
tags: [optional, extra, tags]
header:
  teaser: /images/optional-thumbnail.jpg
---
```

Suggested top-level categories:
- `life` — always include to distinguish from academic posts
- `travel`, `reading`, `music`, `photography`, `gaming` — topic

## Out of Scope

- Comments on blog posts (can be enabled later via `_config.yml`)
- A separate photo gallery page (not needed for now)
- Pagination (can be enabled later if posts grow numerous)

## Success Criteria

- `/blog/` page exists and lists all posts
- "Blog" appears in the site header navigation
- Writing a new `.md` file in `_posts/` automatically shows up on the blog page
