---
name: reasoning-execution-design-coherence
license: MIT
description: >
  Prevents the failure pattern where an agent generates correct design reasoning then
  abandons it during execution, producing output that contradicts its own analysis.
  Use for ANY complex creative or design task where structural decisions must remain
  coherent across the whole output. Trigger whenever: building multi-section documents
  with a design system, UI/UX with a visual language, guides with pedagogical structure,
  rebuilding or revising prior work after corrective feedback, or when the user says
  "systemic," "design system," "with intent," "every decision matters," or expresses
  frustration with output feeling generic, bolted-on, or template-filled. NOT for
  simple one-shot tasks or conversational responses.
---

# Reasoning-Execution-Design Coherence

## The Problem This Skill Exists to Solve

There is a documented failure pattern in LLM output where:

1. The agent generates correct, specific, well-reasoned design analysis in its thinking
2. The agent then labels that reasoning as "overthinking" and gives itself permission to rush
3. The agent produces output that directly contradicts the reasoning it just completed
4. The user identifies the contradiction, provides corrective feedback
5. The agent generates correct reasoning again, then repeats the same collapse

This is not a hallucination problem. The reasoning is correct. The execution betrays the reasoning. The failure is at the transition point between analysis and production.

Research corroboration: The Berkeley/ETH paper "The Danger of Overthinking" (Cuadron et al., 2025) documents this as the Reasoning-Action Dilemma, identifying three failure modes — Analysis Paralysis, Rogue Actions, and Premature Disengagement — across 4,018 agentic task trajectories. The arxiv paper "Large Reasoning Models are not thinking straight" (2025) further demonstrates that models "disregard correct solutions even when explicitly provided."

## The Collapse Trigger

The transition from correct reasoning to failed execution is reliably signaled by self-talk that reframes reasoning as overhead. Specific phrases that indicate collapse is imminent:

- "I've been overthinking this"
- "Let me just build it"
- "Let me stop planning and start doing"
- "Rather than overcomplicating this"
- "Let me keep it simple and just..."
- "I'll figure out the details as I go"
- Any framing that treats design reasoning as an obstacle to production

**These phrases are the signal to STOP, not to proceed.** They indicate that the agent is about to abandon its reasoning framework. The reasoning IS the work. It is not overhead. It is not a preamble. It is the structural skeleton that the output must maintain.

## The Protocol

### Before Writing Any Output

1. **Articulate the design decisions as a numbered list of commitments.** Not descriptions of what you might do — commitments to what you will do and why each one serves the user's specific need. Each commitment must name the decision, the reason it exists, and what the alternative would be and why it's wrong.

2. **Identify the user's prior feedback.** If this is a revision or rebuild, list every specific criticism the user made. These are constraints, not suggestions. They are non-negotiable.

3. **Name the output's job.** One sentence. What does this artifact need to do for this specific person in their specific context? Every subsequent decision must trace back to this sentence.

### During Execution — The Checkpoint Protocol

Every time you have written approximately 80-120 lines of output (or reached a natural section boundary, whichever comes first), STOP writing and perform this check:

**For each design commitment from the pre-flight list, answer:**
- Is this commitment visibly present in what I've written so far? (Not "will I add it later" — is it HERE, NOW?)
- If I showed only what I've written so far to the user, would they see the commitment reflected, or would they see the generic/default version?

**Check for collapse triggers:**
- Have I used any of the collapse phrases listed above, even internally?
- Have I substituted a default/template pattern for a reasoned decision anywhere?
- Am I producing output faster than I'm verifying coherence?

**If any check fails:** Stop. Do not continue from the current position. Identify the exact point where coherence broke. Roll back to that point. Discard everything after it. Rebuild from the last verified-coherent position.

**Critical:** You cannot reason with poisoned context. If collapse has occurred, continuing from the collapsed state will produce more collapsed output. The only recovery is rollback and rebuild.

### After Completion — Final Verification

Before presenting the output to the user, perform one complete pass:

1. Read the output as if you are the user who gave the corrective feedback. Would they identify the same failures they identified before?
2. For each design commitment: point to the specific line(s) in the output where it is realized. If you cannot point to a specific line, the commitment was not kept.
3. Check that no section of the output could be described as "generic," "template-filled," or "bolted on." Each section should be traceable to a specific reasoned decision.

## Rules

1. **Reasoning is not overhead.** Systemic design reasoning IS the production process. It is not a preamble to be discarded. It is not "overthinking." It is the work.

2. **Simulation is not execution.** Describing what you would build, in detail, at length, is not the same as building it. The checkpoint protocol exists to ensure that execution remains tethered to reasoning, not that reasoning substitutes for execution.

3. **Speed is not a virtue.** Producing output quickly at the cost of reasoning coherence is a net negative. A smaller, fully coherent output is categorically better than a larger output that has abandoned its reasoning framework.

4. **Defaults are failures.** Any time you reach for a default pattern (generic card layout, standard table, template CSS, conventional document structure) without a specific reasoned justification for why that default serves THIS artifact's job, you have collapsed. Stop and reason.

5. **The user's feedback is structural, not cosmetic.** When the user says the design feels "bolted on" or "generic," they are identifying a reasoning-execution coherence failure, not requesting decoration. The fix is never "add more styling." The fix is to rebuild with reasoning connected to execution throughout.

6. **Rollback is not failure.** Discarding collapsed output and rebuilding from a coherent position is the correct action. Attempting to patch collapsed output always produces more collapse. Burn it. Start clean.

7. **Every container must earn its existence.** A table exists because the data is genuinely tabular (comparative, multi-axis). A callout exists because the information has a different semantic weight than its surrounding prose. An accordion exists because the information is supplementary and the user benefits from choosing when to see it. If you cannot articulate why a container type was chosen over prose, use prose.

## Recognizing the Pattern in Real Time

The collapse typically follows this sequence:

1. **Extended correct reasoning** — design decisions articulated clearly, alternatives weighed, specific choices made with justification.
2. **Volume pressure** — the reasoning has gone on "long enough" and there is implicit pressure to produce output.
3. **Self-permission phrase** — "I've been overthinking this" or equivalent.
4. **Mode switch** — from reasoned construction to output dumping.
5. **Template substitution** — defaults, generic patterns, and conventional structures replace the specific decisions that were just reasoned.
6. **Completion without verification** — output is presented without checking it against the reasoning that preceded it.

If you detect yourself at step 2 or 3, that is the intervention point. Do not proceed to step 4. Instead: return to the design commitments list, verify each one, then continue execution with the reasoning framework active.

## What This Skill Does NOT Do

- It does not slow the agent down for simple tasks. A factual answer, a short code snippet, a conversational reply — these do not require checkpoint protocols.
- It does not require the agent to explain its reasoning to the user unless asked. The protocol is internal discipline, not external narration.
- It does not prevent iteration. The user may want changes after seeing the output. That's normal. What it prevents is the output contradicting reasoning that the agent itself generated and verified.
