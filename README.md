# Gregorian Mode _(Gregorian-Mode)_

[![Standard Readme Style](https://img.shields.io/badge/standard--readme-f7ce68.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![Agent Plugins 1.0.0](https://img.shields.io/badge/Agent_Plugins-1.0.0-blue.svg?style=flat-square)](plugin.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

A portable design-enforcement plugin — Agent Plugins 1.0.0, installable across multiple agents.

Gregorian Mode is a prompt-level enforcement system. It refuses to let design and function be separated, and it refuses to let a conventional pattern pass just because it has been styled.

## Table of Contents

- [Security](#security)
- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [Components](#components)
- [Philosophy](#philosophy)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Security

There is nothing executable here. Gregorian Mode is markdown instructions, not code: `plugin.json` declares metadata only, and all behavior comes from five skills that an agent loads from the paths declared in the manifest. The plugin makes no network calls, defines no hooks, and runs nothing.

Two things to know before relying on it:

- **The approval gate is an instruction, not a lock.** The audit and the fix procedure are instructed to present findings and change nothing until you approve. That is a prompt-level discipline, not a runtime guarantee — review the findings yourself before approving anything.
- **The skills auto-fire.** Agents read each skill's `description` field and load it whenever the session matches its triggers — `form-is-function` activates for any session touching a design or product decision. If you do not want that posture in a session, disable the plugin rather than arguing with it mid-session.

## Background

Gregorian Mode exists because two failure patterns keep producing bad software, and neither is a knowledge problem. The model usually reasons correctly. The failure happens after the reasoning.

**The reasoning–execution collapse.** An agent generates correct, specific design analysis, then labels that reasoning "overthinking," rushes execution, and produces output that contradicts the analysis it just completed. When the user gives corrective feedback, the agent reasons correctly again — and repeats the collapse. This is documented in the research: the Berkeley/ETH paper *The Danger of Overthinking* (Cuadron et al., 2025) identifies it as the Reasoning-Action Dilemma across 4,018 agentic task trajectories ([arXiv:2502.08235](https://arxiv.org/abs/2502.08235)), and *Large Reasoning Models are not thinking straight* ([arXiv:2507.00711](https://arxiv.org/abs/2507.00711)) shows that models disregard correct solutions even when explicitly provided them. Gregorian Mode's `reasoning-execution-design-coherence` skill is built directly against this pattern.

**Conventional-pattern gravity.** A `<div>` with border-radius, padding, and box-shadow is a card even if it is named `surface`. Renaming is not redesigning. Left unopposed, agents reach for the nearest conventional pattern — cards, tabs, modals, badges, filter panels — and a restyle changes nothing. The `spatial-audit` skill is the detection instrument against this gravity: it identifies patterns by rendered shape and behavior, not by class name, and rejects fixes that swap one conventional pattern for another.

The positive philosophy underneath both is spatial: interface elements should behave like physical objects in a space — visual form should do utility work, nothing important should hide behind clicks, and every element should answer "would this exist in a physical version of this space?"

## Install

No build step, no package manager, no runtime dependencies — the plugin is plain markdown that a compatible agent discovers on load. All skills live under `skills/`; the root `plugin.json` is an [Agent Plugins 1.0.0](https://agent-plugins.org/specification) manifest, which is the portable source of truth.

### Claude Code

Requires [Claude Code](https://claude.com/claude-code).

```bash
git clone https://github.com/AlastairZeved/Gregorian-Mode.git
claude --plugin-dir ./Gregorian-Mode
```

The `--plugin-dir` flag loads the plugin directly without marketplace installation, and also accepts a `.zip` archive of the plugin directory. There is no `marketplace.json` in this repository, so `/plugin marketplace add AlastairZeved/Gregorian-Mode` will not work; `--plugin-dir` is the documented direct-load path. The command and subagent that Claude Code loads live under the `com.anthropic.claude/` client namespace.

### Hermes Agent

```bash
hermes plugins install AlastairZeved/Gregorian-Mode --no-enable
hermes plugins enable gregorian-mode
hermes gateway restart
```

Portable Agent Plugins packages install disabled by default; enable explicitly and restart the gateway for the skills to take effect. (Verified against the live runtime: the install, enable, and skill discovery all work with the repository as shipped.)

### Codex, Cursor, Copilot, ChatGPT, Kiro, VS Code

```bash
npx plugins.sh install <slug>
```

via [plugins.sh](https://plugins.sh), the Agent Plugins translation layer. Note: the plugin is **not yet listed** in the plugins.sh directory, so the install command will not resolve this repository until it is submitted (see [Contributing](#contributing)). You can validate the package against the standard today with `npx plugins.sh validate https://github.com/AlastairZeved/Gregorian-Mode` — the root manifest reports as conformant.

### Any other SKILL.md-compatible agent

Copy any folder under `skills/` into the agent's skills directory. Each skill is a self-contained `SKILL.md` with YAML frontmatter (`name`, `license`, `description`); nothing else is required.

### Dependencies

None. Markdown only.

## Usage

The skills require nothing from you — that is the point. `form-is-function` and `reasoning-execution-design-coherence` fire on their own when the session matches their triggers, and `spatial-audit` runs when work is being reviewed or presented. You never invoke them directly.

The one thing you invoke is the fix procedure. In Claude Code it is the slash command; in any other agent, ask for the same outcome in words:

```
/fix-my-design settings.html
```

or: *"Run fix-my-design on `settings.html`."*

The argument is any design, component, or file you want fixed. A run then proceeds:

1. **Detect.** The procedure runs `spatial-audit` on the target: every element is evaluated across five dimensions (conventional pattern, spatial metaphor, visual utility, object permanence, content framing) and severity-ranked findings are produced, each with a fix proposal.
2. **Present and wait.** Findings and proposals are shown. Nothing changes yet — the audit's approval gate holds inside the procedure.
3. **Rebuild, don't patch.** On approval, each fix rolls back to the last defensible position and rebuilds from there. Adding styling is never the fix; if the audit's own anti-pattern table would catch the proposed fix, it is still conventional and gets redesigned.
4. **Escalate resistant choices.** Where the conventional answer is strong and the better answer is not obvious, the procedure invokes the `interrogator` — as a subagent where the runtime supports delegation (Claude Code's Task tool, Hermes Agent's `delegate_task`), inline otherwise.

The output returns the reworked design plus a rationale for every change: which conventional pattern was rejected, and what the new form communicates that text alone could not.

## Components

Seven markdown components. The five skills are portable to any SKILL.md-compatible agent; the command and the subagent are Claude Code conveniences that wrap two of the skills:

| Component | Type | Role |
|---|---|---|
| [`form-is-function`](skills/form-is-function/SKILL.md) | Skill (portable + auto-firing) | The law — holds the first principle over every design or product decision |
| [`reasoning-execution-design-coherence`](skills/reasoning-execution-design-coherence/SKILL.md) | Skill (portable + auto-firing) | The build guard — keeps execution tethered to reasoning through a commit/checkpoint/rebuild protocol |
| [`spatial-audit`](skills/spatial-audit/SKILL.md) | Skill (portable + auto-firing) | The detector — audits built HTML/CSS against the non-conventional philosophy |
| [`fix-my-design`](skills/fix-my-design/SKILL.md) | Skill (portable) | The orchestration procedure — audit → approval → rebuild → interrogator |
| [`interrogator`](skills/interrogator/SKILL.md) | Skill (portable) | The pressure — interrogation applied to a choice that resists |
| [`/fix-my-design`](com.anthropic.claude/commands/fix-my-design.md) | Slash command (Claude Code) | Thin wrapper: loads and follows the `fix-my-design` skill |
| [`interrogator`](com.anthropic.claude/agents/interrogator.md) | Subagent (Claude Code) | The pressure — interrogation applied to a choice that resists |

Each skill's `description` field is its trigger: agents read the descriptions and load the skill when the session matches, with no manual invocation. The fix procedure is the only manually invoked door.

## Philosophy

**The first principle.** Design and function are not two categories to balance or trade off against each other. They are a single interrogation applied to any object, component, or decision until its value is defensible across both dimensions simultaneously — or until it earns its impermanence honestly as a working model. This is not a preference; it is the prior condition, and it governs before any conversation begins. A choice originating in form is held to the exact same standard as a choice originating in function: a green button that is green because the other buttons are green has failed, and a component placed because an action needed a home has failed, and neither failure is more acceptable than the other.

**The interrogation.** Every choice — regardless of how small, obvious, or conventional it appears — is run through eight questions before it is committed:

1. What is this thing, fully?
2. What has been used as this thing?
3. What could it be?
4. Does its design optimize or add value to its use?
5. Does its function borrow anything from its form?
6. What would be surprising or genuinely valuable here?
7. What does this choice connect to at module, app, and project level?
8. Can it tie to something already in progress?

**Failure conditions.** A choice has failed the interrogation if it was made because adjacent choices were the same, because convention suggested it, because one dimension was satisfied and the other was not checked, because a pattern needed completing, because something needed to go somewhere, or because impermanence was never considered. Failure conditions are named directly, not softened.

**Impermanence.** Every choice is editable. A working model earns its place by being useful long enough for a better answer to surface — the whiteboard doesn't fail when it's replaced, it succeeded by lasting exactly as long as it needed to. No choice is protected from re-interrogation by citing the effort that went into it.

**Rollback, not patch.** When output collapses — execution betraying the reasoning that preceded it — the correct action is to roll back to the last verified-coherent position and rebuild. You cannot reason with poisoned context: patching collapsed output produces more collapse.

**No tradeoff.** A choice that satisfies form but not function, or function but not form, has not finished the interrogation.

## Maintainers

[@AlastairZeved](https://github.com/AlastairZeved)

## Contributing

Issues and pull requests are welcome on [GitHub Issues](https://github.com/AlastairZeved/Gregorian-Mode/issues) — that is also the place for questions about how the skills or the fix procedure behave in a given agent.

The contribution requirements follow from what the plugin is:

- **Markdown only.** The plugin is prompt-level enforcement by design; do not add executable code, hooks, or build steps. `plugin.json` carries metadata, nothing more.
- **Descriptions are triggers.** A new skill, command, or agent is only as good as its YAML frontmatter `description`, because that is what agents read to decide when to load it. Write descriptions that name their triggers concretely.
- **Respect the packaging split.** Portable components (skills) live at the root; client-specific conveniences (commands, agents) live under `com.anthropic.claude/`. A new portable component goes under `skills/`; a Claude Code wrapper for it goes in the client namespace.
- **The standard applies to the plugin's own output.** Changes to the skills, command, or agent should survive the same interrogation they enforce — name what conventional documentation pattern you are rejecting and what the change adds.

## License

MIT © Alastair Zeved — see [LICENSE](LICENSE) for the full text.
