---
description: Interrogate an existing design and rebuild what fails — not surface patching.
argument-hint: [the design, component, or file to fix]
---

The user wants a design fixed: $ARGUMENTS

This is not a request for decoration or a quick patch. Detect what fails, get approval, then rebuild from the last coherent position.

## Procedure

1. **Detect.** Run the `spatial-audit` skill on the target. It produces severity-ranked findings across its five dimensions — conventional pattern, spatial/physical metaphor, visual utility work, object permanence, content framing — each with a fix proposal that names the pattern being replaced, what the visual form will communicate that text alone can't, and whether the element would exist in a physical version of the space.

2. **Present and wait.** Show the findings and fix proposals. Change nothing yet — the audit's approval gate holds inside this command.

3. **On approval, rebuild — don't patch.** For each approved finding, roll back to the last defensible position and rebuild from there. Adding styling is never the fix. If the audit's own anti-pattern table or red flags would catch the proposed fix, it is still conventional — redesign.

4. **Hand resistant choices to the interrogator.** Where the conventional answer is strong and the better answer isn't obvious, invoke the `interrogator` subagent to apply pressure until the choice earns its place or earns its impermanence.

## Output

Return the reworked design, and for each change name what conventional pattern was rejected and what the new form communicates. Do not present a choice you cannot defend across both form and function.
