# Copilot Instructions

This is a personal academic website built with the [Academic Pages](https://github.com/academicpages/academicpages.github.io) Jekyll template, hosted on GitHub Pages.

## Local Development

```bash
# Install Ruby dependencies (first time or after Gemfile changes)
bundle install

# Serve the site locally with live reload
bundle exec jekyll serve -l -H localhost
# Site available at http://localhost:4000

# Alternative: Docker
docker compose up
```

> **Important**: `_config.yml` is NOT auto-reloaded by live reload. Changes to it require restarting Jekyll.

### JavaScript

```bash
npm install           # install JS dependencies
npm run build:js      # bundle and minify JS to assets/js/main.min.js
npm run watch:js      # watch JS files and rebuild on change
```

## Architecture

### Site Configuration

- **`_config.yml`** — site-wide settings: author bio, social links, site URL, enabled plugins, collection defaults, and publication categories. This is the main file to edit for personal customization.
- **`_data/navigation.yml`** — controls which links appear in the header nav, and in what order. Remove an entry here to hide a section from navigation (without deleting its content).
- **`_data/cv.json`** — structured CV data used by the JSON-based CV layout (`/cv-json/`). The default CV is Markdown-based (`_pages/cv.md`). Only one should be linked in navigation.

### Content Collections

Each content type is a Jekyll collection of Markdown files with YAML front matter:

| Directory | URL pattern | Collection name |
|---|---|---|
| `_publications/` | `/publication/YYYY-MM-DD-slug` | `publications` |
| `_talks/` | `/talks/YYYY-MM-DD-slug` | `talks` |
| `_teaching/` | `/teaching/YYYY-MM-DD-slug` | `teaching` |
| `_portfolio/` | `/portfolio/slug` | `portfolio` |
| `_posts/` | `/posts/YYYY/MM/slug/` | posts |
| `_pages/` | custom permalink | pages |

### Layouts and Templates

- `_layouts/` — full page layouts (`single`, `archive`, `talk`, `cv-layout`, etc.)
- `_includes/` — reusable HTML partials (author profile, SEO tags, scripts, etc.)
- `_sass/` — SCSS source files
- `assets/js/` — JS source; compiled output is `assets/js/main.min.js`

### Static Files

- `files/` — PDFs, ZIPs, and other downloads served at `/files/filename`
- `images/` — images referenced in content

## Content Conventions

### All collection items require these front matter fields:

**Publications** (`_publications/`):
```yaml
---
title: "Paper Title"
collection: publications
category: manuscripts   # manuscripts | conferences | books
permalink: /publication/YYYY-MM-DD-slug
excerpt: 'Short description'
date: YYYY-MM-DD
venue: 'Journal or Conference Name'
paperurl: 'https://...'
citation: 'Author, A. (YYYY). ...'
---
```

**Talks** (`_talks/`):
```yaml
---
title: "Talk Title"
collection: talks
type: "Talk"   # Talk | Tutorial | Workshop
permalink: /talks/YYYY-MM-DD-slug
venue: "Venue Name"
date: YYYY-MM-DD
location: "City, Country"
---
```

**Teaching** (`_teaching/`):
```yaml
---
title: "Course Title"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/YYYY-MM-DD-slug
venue: "University, Department"
date: YYYY-MM-DD
location: "City, Country"
---
```

**Posts** (`_posts/`): filename must be `YYYY-MM-DD-slug.md`; supports `tags:` in front matter.

### Markdown Generator

Use Python scripts or Jupyter notebooks in `markdown_generator/` to batch-generate collection Markdown files from CSV/TSV data:

```bash
python3 markdown_generator/publications.py markdown_generator/publications.csv
python3 markdown_generator/talks.py markdown_generator/talks.tsv
```

### Supported Rich Content

MathJax (LaTeX math), Mermaid diagrams, and Plotly charts are all supported inline in Markdown content.

### Talk Map

`talkmap.py` or `talkmap.ipynb` reads `_talks/` metadata and generates an interactive map at `/talkmap.html`. Re-run after adding new talks.
