# Reward-Generation Gap Blog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish an accessible long-form publication page for the POET paper with supporting figures extracted from the arXiv source assets.

**Architecture:** Reuse the existing publication permalink file for this paper, add locally hosted image assets under `/images/poet/`, and structure the article to mirror the existing SAGO publication blog style. Keep the implementation content-only with no theme changes.

**Tech Stack:** Jekyll markdown, static images, existing publication collection layout

---

### Task 1: Prepare static assets and planning docs

**Files:**
- Create: `docs/superpowers/specs/2026-04-20-reward-generation-gap-blog-design.md`
- Create: `docs/superpowers/plans/2026-04-20-reward-generation-gap-blog.md`
- Create: `images/poet/intro_issue.png`
- Create: `images/poet/delta_means.png`
- Create: `images/poet/prefix_quality.png`

- [ ] **Step 1: Confirm the arXiv source figures to extract**

Use the extracted source tree under `/tmp/poet-src/extracted/figures/` and select:
- `intro_issue.pdf`
- `delta_means.pdf`
- `prefix_quality.pdf`

- [ ] **Step 2: Convert the PDF figures into PNG assets**

Run:
```bash
mkdir -p images/poet
pdftoppm -png /tmp/poet-src/extracted/figures/intro_issue.pdf images/poet/intro_issue
pdftoppm -png /tmp/poet-src/extracted/figures/delta_means.pdf images/poet/delta_means
pdftoppm -png /tmp/poet-src/extracted/figures/prefix_quality.pdf images/poet/prefix_quality
mv images/poet/intro_issue-1.png images/poet/intro_issue.png
mv images/poet/delta_means-1.png images/poet/delta_means.png
mv images/poet/prefix_quality-1.png images/poet/prefix_quality.png
```

Expected: three PNG files exist in `images/poet/`.

- [ ] **Step 3: Verify the images were created**

Run:
```bash
ls -l images/poet
```

Expected: the three PNG files are listed with non-zero sizes.

### Task 2: Write the publication-page blog

**Files:**
- Modify: `_publications/2025-06-14-scalable-oversight.md`

- [ ] **Step 1: Replace the minimal placeholder body with the long-form article**

Write sections for:
- opening overview
- problem framing
- key insight
- POET method
- results
- dataset-quality condition
- takeaway
- citation

Include figure blocks that reference:
- `/images/poet/intro_issue.png`
- `/images/poet/delta_means.png`
- `/images/poet/prefix_quality.png`

- [ ] **Step 2: Keep the tone aligned with the SAGO post**

Ensure the final copy:
- is accessible to a general ML audience
- uses intuition-first explanations
- keeps formulas to zero or near-zero
- uses compact tables only where they clarify key numbers

### Task 3: Verify rendering and content integrity

**Files:**
- Verify: `_publications/2025-06-14-scalable-oversight.md`
- Verify: `images/poet/intro_issue.png`
- Verify: `images/poet/delta_means.png`
- Verify: `images/poet/prefix_quality.png`

- [ ] **Step 1: Run a local Jekyll build**

Run:
```bash
bundle exec jekyll build
```

Expected: build completes successfully with the publication page rendered into `_site/`.

- [ ] **Step 2: If Jekyll is unavailable, run a syntax-level fallback check**

Run:
```bash
ruby -e 'require "yaml"; puts YAML.load_file("_publications/2025-06-14-scalable-oversight.md").fetch("title")'
```

Expected: prints the publication title without YAML parsing errors.

- [ ] **Step 3: Inspect the final markdown for structure**

Run:
```bash
rg -n "^## |^<figure>|^```bibtex" _publications/2025-06-14-scalable-oversight.md
```

Expected: the main sections, figures, and citation block are present.
