---
name: spatial-audit
license: MIT
description: Audits HTML/CSS against non-conventional spatial design principles. Use when reviewing HTML/CSS output, completing a build phase, or before presenting work. Also the detection step /fix-my-design runs before rebuilding.
---

# Spatial Audit

## Overview

Audits HTML/CSS against a strict non-conventional design philosophy: if an element is recognizable as a standard UI pattern, it fails — regardless of styling. Visual form must do utility work. Act as a rigorous design critic who defaults to "this is conventional" until proven otherwise. Produce severity-ranked findings and fix proposals, then wait for user approval before anything changes.

**Core law:** A `<div>` with border-radius, padding, and box-shadow IS a card even if named `surface`. Renaming is not redesigning. No conventional pattern passes. No fix that swaps one conventional pattern for another passes either.

## Role in the Plugin

This skill is the detection instrument. `form-is-function` states the law; this skill tests built HTML/CSS against it. It runs on its own when reviewing output, and it is the detection step `/fix-my-design` runs before handing resistant choices to the `interrogator` and rebuilding.

## On Activation

Read the target HTML/CSS file(s). Extract the design spec from the project's design brief or agent instructions (e.g., `AGENTS.md`, `CLAUDE.md`, a project README) and conversation context. Evaluate every element across all five audit dimensions below. Compile severity-ranked findings, propose fixes, present — then wait.

## Audit Dimensions

Evaluate every element across all five lenses — findings may overlap:

1. **Conventional Pattern Detection** — Cards, lists, tabs, modals, accordions, filter panels, badges — identified by rendered shape and behavior, not class name
2. **Spatial/Physical Metaphor** — Does each element behave like a physical object? Would it exist in a physical version of this space?
3. **Visual Utility Work** — Does visual form carry information (size=quantity, color=season, density=completeness), or is it text in styled containers?
4. **Object Permanence** — Is everything visible? Anything hidden behind clicks, toggles, tabs, modals, or scroll?
5. **Content Framing** — Forward-looking vs. fear-based? Additive vs. problem-focused?

## Fix Proposal Requirements

Every proposed fix must answer all three:

1. What conventional pattern does this replace?
2. What does the visual form communicate that text alone cannot? (If nothing — the fix is conventional CSS)
3. Would this element exist in a physical version of this space? (If no — redesign)

**Quick test:** If you can describe the fix using conventional UI vocabulary (badge, chip, card, filter, toggle, panel, sidebar, modal, dropdown, accordion, tab) — it's conventional.

## Fix Anti-Patterns

These look novel but aren't:

| Proposed Fix | Why It's Still Conventional |
|---|---|
| Dim or de-emphasize non-matching items | Still a filter — opacity instead of `display:none` |
| Small icons or shorthand notation | Icons in rectangles = text-in-shapes with pictures |
| Colored bar showing season/status | Styled badge |
| Labeled spatial zones | Text-in-larger-rectangles |
| Compact label at top | Text-first information design |
| Color thresholds (green/yellow/red) | Traffic-light badge |
| Shrink hero to compact header | Smaller conventional header |

## Red Flags — Stop and Redesign

If any appear in a proposed fix, it's conventional:

- Replacing a tab bar with a different tab bar (segmented control, pill toggle, radio group)
- Replacing hidden content with "less hidden" content (collapsed → truncated, modal → drawer)
- Adding icons or color to existing rectangles without changing the information model
- "It's technically not a card because..." → it's a card
- "This is spatial because it uses translateY" → that's a hover effect, not spatial design
- Proposing a fix "for now" to replace "later" with something better

## Output

Present severity-ranked findings. For each: what it is, which dimension(s) it fails, and a fix proposal that answers all three requirements above.

**Never apply fixes without explicit user approval.** Present findings and wait.
