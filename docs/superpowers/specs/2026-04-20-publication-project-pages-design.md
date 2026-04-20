# Publication Project Pages Design

## Goal

Restyle the two publication pages below so they feel closer to the reference project page at [VideoLLaMB](https://cancms.github.io/VideoLLaMB.github.io/) while staying inside the current Jekyll site structure:

- [Modeling LLM Unlearning as an Asymmetric Two-Task Learning Problem](/Users/xiaozg/Documents/ZeguanXiao.github.io/_publications/2026-04-28-asymmetric-unlearning.md)
- [Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms](/Users/xiaozg/Documents/ZeguanXiao.github.io/_publications/2026-06-14-reward-generation-gap.md)

The outcome should read like polished academic project pages rather than plain long-form blog posts.

## Reference Traits To Borrow

Borrow the following traits from the reference page, but adapt them to the existing site instead of copying Bulma or recreating the entire layout system:

- a strong hero block with title, author line, venue, and rounded action buttons
- a teaser visual near the top so readers see the method or result before reading dense prose
- content grouped into clearly separated sections with alternating visual rhythm
- lightweight highlight cards for the paper's main ideas
- figure-first storytelling, with full-width visuals and explicit captions
- optional folded details for secondary material

## Scope

### In Scope

- Rewrite the two markdown files into a shared "project page" content structure
- Add a small set of reusable CSS classes for these two pages only
- Reuse existing local images under `/images/sago/` and `/images/poet/`
- Improve mobile and desktop presentation of hero blocks, buttons, cards, figures, and tables

### Out of Scope

- Rebuilding the entire publication template
- Changing global site navigation, sidebar logic, or publication archive behavior
- Adding external UI frameworks or JS-heavy interactions
- Restyling other publication pages

## Content Architecture

Both pages should follow the same high-level structure so the site gains a consistent publication-showcase pattern:

1. Hero block
2. Teaser figure or figure pair
3. Motivation / Problem
4. Key insight
5. Method
6. Results
7. Takeaway
8. Citation

### Page-Specific Emphasis

For the SAGO page:

- use a three-card summary for `Retention`, `Forgetting`, and `Guarantee`
- keep the gradient illustration and Pareto plots visually prominent
- present the asymmetric two-task framing very early

For the POET page:

- use a three-card summary for `Problem`, `Intervention`, and `Benefit`
- lead with the reward-generation mismatch and prefix importance
- keep the prefix-quality and early-gap figures in the main narrative

## Styling Plan

Add a narrow set of classes in the site stylesheet, scoped by explicit class names rather than page-wide overrides. Planned building blocks:

- `project-hero`
- `project-meta`
- `project-links`
- `project-link`
- `project-teaser`
- `project-section`
- `project-section--alt`
- `project-grid`
- `project-card`
- `project-caption`
- `project-details`

Visual direction:

- dark rounded buttons similar to the reference page's action links
- soft gray-blue background blocks for alternating sections
- slightly larger title scale and tighter hero spacing
- bordered, rounded cards for highlight summaries
- centered figures and tables with better breathing room than the current prose flow

## Implementation Approach

### Markdown Changes

- Replace the current linear article flow with HTML-assisted markdown sections
- Add top-of-page hero content directly inside each markdown file
- Group supporting content into semantic blocks that map to the new CSS classes
- Use `details/summary` only for secondary or extended comparisons

### CSS Changes

- Append project-page styles to [assets/css/main.scss](/Users/xiaozg/Documents/ZeguanXiao.github.io/assets/css/main.scss) or an imported partial reachable from it
- Avoid selectors that target generic publication pages globally
- Keep layout compatible with the existing `.page__content` container

## Risks And Mitigations

### Risk: Style leakage to unrelated pages

Mitigation: all new styling must hang off explicit `project-*` classes, with no broad overrides for `figure`, `table`, `h2`, or `.page__content`.

### Risk: Markdown/HTML rendering inconsistencies

Mitigation: keep structure simple, favor plain block-level HTML, and avoid nested custom wrappers that depend on brittle markdown parsing behavior.

### Risk: Mobile crowding in the hero and card rows

Mitigation: use single-column fallback on narrow screens and let action buttons wrap naturally.

## Verification

- Build the site locally with Jekyll
- Confirm both target pages render without Liquid or markdown errors
- Verify hero, teaser, cards, alternating sections, and citation blocks appear on both pages
- Check that at least one unrelated publication page still looks unchanged

## Success Criteria

- Both target pages feel noticeably closer to a modern paper/project showcase page
- The pages remain readable and credible as academic content
- The rest of the site behaves as before
- The implementation stays lightweight enough to reuse for future publication pages if desired
