# Publication Project Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle the SAGO and POET publication pages so they read like polished project pages with stronger hero blocks, teaser visuals, section rhythm, and highlight cards.

**Architecture:** Keep the existing Jekyll publication layout intact and implement the redesign in two layers: scoped reusable CSS classes for `project-*` blocks, then HTML-assisted markdown rewrites inside the two target publication files. Reuse existing local figures so the work stays self-contained and does not affect unrelated publication pages.

**Tech Stack:** Jekyll, Markdown with inline HTML, Sass, existing publication collection layout

---

### Task 1: Add scoped project-page styling primitives

**Files:**
- Modify: `assets/css/main.scss`
- Create: `_sass/layout/_project-publication.scss`

- [ ] **Step 1: Add the new Sass partial import**

Update `assets/css/main.scss` so the new project-page partial is imported after `layout/page` and before `layout/archive`:

```scss
    "layout/page",
    "layout/project-publication",
    "layout/archive",
```

- [ ] **Step 2: Write the scoped project-page styles**

Create `_sass/layout/_project-publication.scss` with classes for hero, metadata, button links, teaser blocks, section cards, figure captions, details blocks, and responsive grids. The file should include:

```scss
.project-page {
  --project-accent: #12344a;
  --project-accent-soft: #eef4f8;
  --project-border: #d4e0e8;
  --project-text-soft: #5b6b78;
}

.project-hero {
  margin: 0 0 2.5rem;
  padding: 2.25rem;
  border: 1px solid var(--project-border);
  border-radius: 1.5rem;
  background: linear-gradient(180deg, #f8fbfd 0%, #eef4f8 100%);
}

.project-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.project-link {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 2.75rem;
  padding: 0.7rem 1.2rem;
  border-radius: 999px;
  background: var(--project-accent);
  color: #fff;
}

.project-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}

@media (max-width: 768px) {
  .project-hero {
    padding: 1.4rem;
  }

  .project-grid {
    grid-template-columns: 1fr;
  }
}
```

Also include styles for `.project-section`, `.project-section--alt`, `.project-card`, `.project-teaser`, `.project-caption`, `.project-details`, `.project-figure-grid`, and `.project-results-table`.

- [ ] **Step 3: Sanity-check the stylesheet wiring**

Run:

```bash
rg -n "project-publication" assets/css/main.scss _sass/layout/_project-publication.scss
```

Expected: one import line in `assets/css/main.scss` and multiple scoped class definitions in the new partial.

### Task 2: Rewrite the SAGO publication page into project-page structure

**Files:**
- Modify: `_publications/2026-04-28-asymmetric-unlearning.md`

- [ ] **Step 1: Restructure the top of the page into a hero block**

Replace the simple author-and-links opening with an HTML-assisted hero section containing:
- title context line such as `ACL 2026`
- author list
- action links for arXiv and code
- a short overview paragraph
- a three-card summary for `Retention`, `Forgetting`, and `Guarantee`

The body should start with:

```html
<div class="project-page">
  <section class="project-hero">
    <p class="project-eyebrow">ACL 2026</p>
    <h1 class="project-title">Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem</h1>
    <p class="project-authors"><strong>Zeguan Xiao</strong>, Siqing Li, Yong Wang, Xuetao Wei, Jian Yang, Yun Chen, Guanhua Chen</p>
    <div class="project-links">
      <a class="project-link" href="https://arxiv.org/abs/2604.14808">arXiv</a>
      <a class="project-link" href="https://github.com/sustech-nlp/SAGO">Code</a>
    </div>
  </section>
```

- [ ] **Step 2: Add a teaser/results block near the top**

Move a visually strong figure block close to the hero, using either the Pareto figure or a paired figure layout with the gradient illustration and loss dynamics figure. Include explicit caption text and wrap it in `project-teaser` / `project-figure-grid` containers.

- [ ] **Step 3: Reframe the narrative into separated sections**

Rewrite the remainder into:
- `Motivation`
- `Asymmetric Two-Task Learning`
- `How SAGO Synthesizes Gradients`
- `What the Results Show`
- `Why the Geometry Matters`
- `Takeaway`
- `Citation`

Use alternating `project-section` and `project-section project-section--alt` wrappers.

- [ ] **Step 4: Add a compact results table**

Keep one compact markdown or HTML table that highlights the WMDP comparison and style it with `project-results-table`.

### Task 3: Rewrite the POET publication page into project-page structure

**Files:**
- Modify: `_publications/2026-06-14-reward-generation-gap.md`

- [ ] **Step 1: Add the shared hero pattern**

Convert the existing top matter body into the same project-page shell, with:
- venue eyebrow
- title and author line
- action links for arXiv and code
- one short overview paragraph
- three summary cards for `Problem`, `Intervention`, and `Benefit`

- [ ] **Step 2: Surface the core visual earlier**

Place the reward-generation-gap figure inside a top teaser block immediately after the hero, with a concise caption that explains the prefix-vs-sequence mismatch.

- [ ] **Step 3: Rewrite the article into showcase sections**

Use these sections:
- `Motivation`
- `Why Prefixes Matter`
- `POET in One Idea`
- `Why Equal-Length Training Helps`
- `Results Across Settings`
- `When POET Helps Most`
- `Takeaway`
- `Citation`

Wrap the content in the same scoped project-page containers used on the SAGO page.

- [ ] **Step 4: Keep one representative comparison table**

Retain the existing compact results table, place it inside the results section, and avoid adding extra dense benchmarks beyond what the current page already shows.

### Task 4: Verify rendering and regression boundaries

**Files:**
- Verify: `_publications/2026-04-28-asymmetric-unlearning.md`
- Verify: `_publications/2026-06-14-reward-generation-gap.md`
- Verify: `_sass/layout/_project-publication.scss`
- Verify: one unrelated publication page under `_publications/`

- [ ] **Step 1: Run a local Jekyll build**

Run:

```bash
bundle exec jekyll build
```

Expected: exit code 0 and the site is generated into `_site/` without Liquid or Sass errors.

- [ ] **Step 2: Check that the new project-page classes appear in built output**

Run:

```bash
rg -n "project-hero|project-section|project-card" _site/publication
```

Expected: matches in the two target publication pages.

- [ ] **Step 3: Confirm no unrelated publication picked up the new structure**

Run:

```bash
rg -n "project-hero" _site/publication | wc -l
```

Expected: only the two target pages contribute matches.
