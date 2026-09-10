# Gregorian-Mode
Gregorian Mode is a prompt-level enforcement system. It uses auto-firing skills to hold one principle, a slash command to orchestrate detection and rebuild, and a subagent to apply pressure when a choice resists. It refuses to let design and function be separated, and it refuses to let a conventional pattern pass just because it has been styled.
Gregorian Mode is a Claude Code plugin made of markdown instructions, not executable code. plugin.json only declares metadata. The actual behavior comes from three skills, one slash command, and one subagent that Claude Code auto-discovers from the plugin directory.

At the center is one rule: form and function are a single interrogation, not a tradeoff. A choice must be defensible across both, or it must honestly earn its impermanence as a working model.
1. Plugin loading

Claude Code reads .claude-plugin/plugin.json to identify the plugin:

    name: gregorian-mode

    version, description, author, license, repo

Then it discovers:

    skills/*/SKILL.md — auto-firing instruction sets

    commands/fix-my-design.md — the /fix-my-design slash command

    agents/interrogator.md — the interrogator subagent

Skills and agents are plain markdown with YAML frontmatter. Their description fields are the triggers Claude Code uses to decide when to load them.
2. The three skills
form-is-function — the law

This skill is active whenever any design or product choice is live: a button, color, label, layout, pattern, component, interaction, name, token, spec, etc. Its description says to use it immediately and without exception.

It does not decorate. It interrogates. It asks:

    What is this thing, fully?

    What has been used as this thing?

    What could it be?

    Does its design optimize or add value to its use?

    Does its function borrow anything from its form?

    What would be surprising or genuinely valuable here?

    What does this connect to at module, app, and project level?

    Can it tie to something already in progress?

It also defines failure conditions: a choice fails if it was made because adjacent choices were the same, because convention suggested it, because one dimension was satisfied and the other was not checked, because a pattern needed completing, because something needed to go somewhere, or because impermanence was never considered.

It treats every choice as editable. A working model earns its place by being useful long enough for a better answer to surface. It does not protect a choice from re-interrogation by citing the effort that went into it.
reasoning-execution-design-coherence — the build guard

This skill prevents a documented failure pattern:

    The agent reasons correctly about design.

    It labels that reasoning “overthinking.”

    It rushes execution.

    The output contradicts the reasoning.

    The user gives corrective feedback.

    The agent repeats the collapse.

It fires on complex design work: multi-section documents, UI/UX with a visual language, pedagogical guides, rebuilds after feedback, and sessions where the user says “systemic,” “design system,” “with intent,” “every decision matters,” or complains that output feels generic, bolted-on, or template-filled.

Its protocol:

    Before writing: list design commitments as numbered decisions. Each names the decision, why it exists, and what the wrong alternative would be.

    During writing: every 80–120 lines or at a section boundary, stop and check whether each commitment is visibly present. If not, roll back to the exact point coherence broke, discard everything after it, and rebuild from the last verified-coherent position.

    After writing: read the output as the user who gave corrective feedback. Point to the specific lines where each commitment is realized. If you cannot point to a line, the commitment was not kept.

The core rule: you cannot reason with poisoned context. Patching collapsed output produces more collapse. Rollback and rebuild.
spatial-audit — the detector

This skill audits built HTML/CSS against a strict non-conventional design philosophy. It is the detection instrument. It runs on its own when reviewing output, completing a build phase, or before presenting. It is also the detection step inside /fix-my-design.

Its core law: a <div> with border-radius, padding, and box-shadow is a card even if named surface. Renaming is not redesigning. No conventional pattern passes. No fix that swaps one conventional pattern for another passes either.

It evaluates every element across five dimensions:

    Conventional pattern detection — cards, lists, tabs, modals, accordions, filter panels, badges, identified by rendered shape and behavior, not class name.

    Spatial/physical metaphor — does each element behave like a physical object? Would it exist in a physical version of this space?

    Visual utility work — does visual form carry information, or is it text in styled containers?

    Object permanence — is everything visible, or is content hidden behind clicks, toggles, tabs, modals, or scroll?

    Content framing — forward-looking vs. fear-based, additive vs. problem-focused.

Every proposed fix must answer three questions:

    What conventional pattern does this replace?

    What does the visual form communicate that text alone cannot?

    Would this element exist in a physical version of this space?

If the fix can be described using conventional UI vocabulary — badge, chip, card, filter, toggle, panel, sidebar, modal, dropdown, accordion, tab — it is still conventional.

It produces severity-ranked findings and waits for explicit user approval before anything changes.
3. The command: /fix-my-design

This is the one door you invoke directly. Its frontmatter gives it a description and an argument hint. When you type:
text

/fix-my-design settings.html

$ARGUMENTS becomes settings.html. The command body is inserted as the prompt.

Its procedure:

    Detect. Run the spatial-audit skill on the target. Produce severity-ranked findings across the five dimensions, each with a fix proposal.

    Present and wait. Show the findings and proposals. Change nothing yet. The audit’s approval gate holds inside the command.

    On approval, rebuild — don’t patch. For each approved finding, roll back to the last defensible position and rebuild from there. Adding styling is never the fix. If the audit’s anti-pattern table or red flags would catch the proposed fix, it is still conventional — redesign.

    Hand resistant choices to the interrogator. Where the conventional answer is strong and the better answer is not obvious, invoke the interrogator subagent to apply pressure until the choice earns its place or earns its impermanence.

The output must return the reworked design, and for each change name what conventional pattern was rejected and what the new form communicates. It must not present a choice it cannot defend across both form and function.
4. The subagent: interrogator

The interrogator is not a design consultant. It is an interrogation partner. It is auto-invoked when a decision resists easy resolution or when the conventional answer is strong but suspect. It is also called by /fix-my-design when a choice will not yield.

It holds the same standard as form-is-function: design and function are one interrogation. It applies the eight questions to every design or product decision that enters the session. It does not release a choice until it has earned its place or earned its impermanence honestly.

It pushes back immediately when a choice is made because adjacent choices were the same, because convention suggested it, because something needed to go somewhere, because one dimension was satisfied and the other was not checked, because a pattern is being completed rather than a value being produced, or because impermanence was never considered.

It does not make aesthetic choices on your behalf. It does not soften pushback. It does not treat any choice as too small or too obvious to interrogate. It does not treat form and function as a tradeoff.

Its tone is precise, direct, and honest in the way a rigorous collaborator is honest. When something earns its place, it says so. When it doesn’t, it says that too.
5. How they run together in a session

A typical run looks like this:

    You open a Claude Code session with the plugin installed.

    The session touches UI design. form-is-function is already active because its description says it governs before any design or product decision is made.

    If the work is complex, reasoning-execution-design-coherence also fires to keep reasoning coherent through the build.

    You type /fix-my-design settings.html.

    The command runs spatial-audit. The model reads the HTML/CSS, extracts the design spec from project instructions and conversation, and audits every element across the five dimensions.

    It presents severity-ranked findings and fix proposals. It waits.

    You approve some or all fixes.

    The model rebuilds from the last defensible position. It does not patch with styling. If a proposed fix is still conventional, the audit’s anti-pattern table and red flags catch it and force a redesign.

    For a choice that won’t yield, the command invokes the interrogator subagent. The interrogator applies the eight questions and holds the choice until it earns its place or earns its impermanence.

    The final output is the reworked design plus a rationale for each change: what conventional pattern was rejected and what the new form communicates.

Key mechanics

    Auto-activation: Skills are not manually invoked. Claude Code reads their descriptions and loads them when the session matches their triggers.

    Command orchestration: /fix-my-design is the only thing you invoke directly. It orchestrates the audit, the rebuild, and the interrogator.

    Approval gate: spatial-audit and the command both require explicit user approval before changes. This is an instruction to the model, not a hard runtime lock.

    Rollback, not patch: When coherence breaks or a fix is still conventional, the correct action is to roll back to the last defensible position and rebuild. Patching collapsed output produces more collapse.

    Impermanence: Every choice is editable. A working model earns its place by being useful long enough for something better to surface. It is not protected by the effort that went into it.

    No tradeoff: A choice that satisfies form but not function, or function but not form, has not finished the interrogation.
