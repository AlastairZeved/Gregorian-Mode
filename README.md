# Gregorian Mode _(Gregorian-Mode)_

[![Standard Readme Style](https://img.shields.io/badge/standard--readme-f7ce68.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
[![Version](https://img.shields.io/badge/version-0.1.0-blue.svg?style=flat-square)](.claude-plugin/plugin.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

A Claude Code plugin that holds design and function as one interrogation — three skills, one command, one interrogator.

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

There is nothing executable here. Gregorian Mode is markdown instructions, not code: `plugin.json` declares metadata only, and all behavior comes from three skills, one slash command, and one subagent that Claude Code loads from the paths declared in `.claude-plugin/plugin.json`. The plugin makes no network calls, defines no hooks, and runs nothing.

Two things to know before relying on it:

- **The approval gate is an instruction, not a lock.** The audit and the `/fix-my-design` command are instructed to present findings and change nothing until you approve. That is a prompt-level discipline, not a runtime guarantee — review the findings yourself before approving anything.
- **The skills auto-fire.** Claude Code reads each skill's `description` field and loads it whenever the session matches its triggers — `form-is-function` activates for any session touching a design or product decision. If you do not want that posture in a session, disable the plugin rather than arguing with it mid-session.

## Background

Gregorian Mode exists because two failure patterns keep producing bad software, and neither is a knowledge problem. The model usually reasons correctly. The failure happens after the reasoning.

**The reasoning–execution collapse.** An agent generates correct, specific design analysis, then labels that reasoning "overthinking," rushes execution, and produces output that contradicts the analysis it just completed. When the user gives corrective feedback, the agent reasons correctly again — and repeats the collapse. This is documented in the research: the Berkeley/ETH paper *The Danger of Overthinking* (Cuadron et al., 2025) identifies it as the Reasoning-Action Dilemma across 4,018 agentic task trajectories ([arXiv:2502.08235](https://arxiv.org/abs/2502.08235)), and *Large Reasoning Models are not thinking straight* ([arXiv:2507.00711](https://arxiv.org/abs/2507.00711)) shows that models disregard correct solutions even when explicitly provided them. Gregorian Mode's `reasoning-execution-design-coherence` skill is built directly against this pattern.

**Conventional-pattern gravity.** A `<div>` with border-radius, padding, and box-shadow is a card even if it is named `surface`. Renaming is not redesigning. Left unopposed, agents reach for the nearest conventional pattern — cards, tabs, modals, badges, filter panels — and a restyle changes nothing. The `spatial-audit` skill is the detection instrument against this gravity: it identifies patterns by rendered shape and behavior, not by class name, and rejects fixes that swap one conventional pattern for another.

The positive philosophy underneath both is spatial: interface elements should behave like physical objects in a space — visual form should do utility work, nothing important should hide behind clicks, and every element should answer "would this exist in a physical version of this space?"

## Install

Requires [Claude Code](https://claude.com/claude-code). No build step, no package manager, no dependencies beyond the CLI itself — the plugin is plain markdown that Claude Code discovers on load.

```bash
git clone https://github.com/AlastairZeved/Gregorian-Mode.git
cd Gregorian-Mode
claude --plugin-dir .
```

The `--plugin-dir` flag loads the plugin directly without marketplace installation. It also accepts a `.zip` archive of the plugin directory if you prefer not to keep the clone.

There is no `marketplace.json` in this repository yet, so `/plugin marketplace add AlastairZeved/Gregorian-Mode` will not work. If you want this plugin in a marketplace, see [Contributing](#contributing).

## Agent Plugins standard

This repository is dual-packaged: it is both a Claude Code plugin (`.claude-plugin/`) and an **Agent Plugins 1.0.0** plugin (root `plugin.json`). The same skills under `skills/` serve both packaging standards — the skills are the portable source of truth; `commands/` and `agents/` are Claude Code conveniences on top of them, kept under the `com.anthropic.claude/` client namespace so the portable root stays clean per the Agent Plugins 1.0.0 standard.

Install paths:

- **Claude Code** — existing marketplace/plugin install, unchanged (see [Install](#install)).
- **Hermes Agent** — `hermes plugins install AlastairZeved/Gregorian-Mode --no-enable` then `hermes plugins enable <plugin-name>` (portable package adapter; skills appear namespaced as `agent-plugin-gregorian-mode-*` via skills_list/skill_view).
- **Codex, Cursor, Copilot, ChatGPT, Kiro, VS Code** — `npx plugins add AlastairZeved/Gregorian-Mode` (Agent Plugins translation layer).
- **Any other SKILL.md-compatible agent** — copy any folder under `skills/` into the agent's skills directory.

## Usage

The skills require nothing from you — that is the point. `form-is-function` and `reasoning-execution-design-coherence` fire on their own when the session matches their triggers, and `spatial-audit` runs when work is being reviewed or presented. You never invoke them directly.

The one thing you invoke is the slash command:

```
/fix-my-design settings.html
```

The argument is any design, component, or file you want fixed. A run then proceeds:

1. **Detect.** The command runs `spatial-audit` on the target: every element is evaluated across five dimensions (conventional pattern, spatial metaphor, visual utility, object permanence, content framing) and severity-ranked findings are produced, each with a fix proposal.
2. **Present and wait.** Findings and proposals are shown. Nothing changes yet — the audit's approval gate holds inside the command.
3. **Rebuild, don't patch.** On approval, each fix rolls back to the last defensible position and rebuilds from there. Adding styling is never the fix; if the audit's own anti-pattern table would catch the proposed fix, it is still conventional and gets redesigned.
4. **Escalate resistant choices.** Where the conventional answer is strong and the better answer is not obvious, the command invokes the `interrogator` subagent, which applies pressure until the choice earns its place or earns its impermanence.

The output returns the reworked design plus a rationale for every change: which conventional pattern was rejected, and what the new form communicates that text alone could not.

## Components

Seven markdown components — the skills are portable to any SKILL.md-compatible agent; the command and the subagent are Claude Code conveniences:

| Component | Type | Role |
|---|---|---|
| [`form-is-function`](skills/form-is-function/SKILL.md) | Skill (portable + auto-firing) | The law — holds the first principle over every design or product decision |
| [`reasoning-execution-design-coherence`](skills/reasoning-execution-design-coherence/SKILL.md) | Skill (portable + auto-firing) | The build guard — keeps execution tethered to reasoning through a commit/checkpoint/rebuild protocol |
| [`spatial-audit`](skills/spatial-audit/SKILL.md) | Skill (portable + auto-firing) | The detector — audits built HTML/CSS against the non-conventional philosophy |
| [`fix-my-design`](skills/fix-my-design/SKILL.md) | Skill (portable) | The orchestration procedure — audit → approval → rebuild → interrogator (portable form of the `/fix-my-design` command) |
| [`interrogator`](skills/interrogator/SKILL.md) | Skill (portable) | The pressure — interrogation applied to a choice that resists (portable form of the `interrogator` subagent) |
| [`/fix-my-design`](com.anthropic.claude/commands/fix-my-design.md) | Slash command (Claude Code) | Thin wrapper: loads and follows the `fix-my-design` skill |
| [`interrogator`](com.anthropic.claude/agents/interrogator.md) | Subagent (Claude Code) | The pressure — interrogation applied to a choice that resists |

Each skill's description field is its trigger: Claude Code reads the descriptions and loads the skill when the session matches, with no manual invocation. The command is the only manually invoked door.

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

Issues and pull requests are welcome on [GitHub Issues](https://github.com/AlastairZeved/Gregorian-Mode/issues) — that is also the place for questions about how the skills or the command behave in a given session.

The contribution requirements follow from what the plugin is:

- **Markdown only.** The plugin is prompt-level enforcement by design; do not add executable code, hooks, or build steps. `plugin.json` carries metadata, nothing more.
- **Descriptions are triggers.** A new skill, command, or agent is only as good as its YAML frontmatter `description`, because that is what Claude Code reads to decide when to load it. Write descriptions that name their triggers concretely.
- **The standard applies to the plugin's own output.** Changes to the skills, command, or agent should survive the same interrogation they enforce — name what conventional documentation pattern you are rejecting and what the change adds.

## License

MIT © Alastair Zeved — see [LICENSE](LICENSE) for the full text.
