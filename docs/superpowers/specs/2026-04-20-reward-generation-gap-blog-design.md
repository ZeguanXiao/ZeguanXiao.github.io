# Reward-Generation Gap Blog Design

## Goal

Create an English long-form publication page for "Towards Bridging the Reward-Generation Gap in Direct Alignment Algorithms" that matches the tone and readability of the existing SAGO blog post while remaining accessible to a general ML audience.

## Audience

- General ML readers
- Researchers familiar with LLM alignment at a high level
- Readers who want intuition first and details second

## Style Reference

Use the structure and pacing of [_publications/2025-04-30-ar-checker.md](/Users/xiaozg/Documents/ZeguanXiao.github.io/_publications/2025-04-30-ar-checker.md):

- short opening paragraph
- problem framing
- key insight
- method explanation
- result walkthrough with figures
- concise takeaway
- citation block

## Content Structure

1. Opening paragraph introducing the paper and positioning it as an accessible overview
2. `The Problem: Direct Alignment Still Misses Something`
3. `Our Key Insight: Sequence-Level Rewards Do Not Guarantee Good Prefixes`
4. `Method: Prefix-Oriented Equal-length Training (POET)`
5. `Why This Makes Sense`
6. `Results: Better Alignment Across Settings`
7. `When Does POET Help Most?`
8. `Takeaway`
9. Citation block

## Figure Plan

- `intro_issue`: first hero-style figure to explain the reward-generation gap intuitively
- `delta_means`: support the claim that prefix quality differences emerge early
- `prefix_quality`: show that POET improves the quality of generated prefixes
- one compact results summary in text/table rather than overloading the page with dense benchmark visuals

## Constraints

- Keep the post close in length and density to the SAGO blog
- Use fewer formulas than the SAGO page
- Avoid a theory-first presentation
- Keep the markdown compatible with the existing Jekyll publication page setup

