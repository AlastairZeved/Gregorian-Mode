<p align="center">
  <img src="docs/assets/banner.png" alt="Gregorian Mode — form and function are inseparable." width="830">
</p>

<h1 align="center">Gregorian Mode</h1>

<p align="center">
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-f7ce68.svg?style=flat-square" alt="Standard Readme Style"></a>
  <a href="plugin.json"><img src="https://img.shields.io/badge/Agent_Plugins-1.0.0-blue.svg?style=flat-square" alt="Agent Plugins 1.0.0"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT"></a>
</p>

<p align="center">
  <a href="#claude-code"><img src="https://img.shields.io/badge/install-Claude_Code-black?style=flat-square" alt="Install on Claude Code"></a>
  <a href="#hermes-agent"><img src="https://img.shields.io/badge/install-Hermes_Agent-black?style=flat-square" alt="Install on Hermes Agent"></a>
  <a href="#codex"><img src="https://img.shields.io/badge/install-Codex-black?style=flat-square" alt="Install on Codex"></a>
  <a href="#cursor"><img src="https://img.shields.io/badge/install-Cursor-black?style=flat-square" alt="Install on Cursor"></a>
  <a href="#github-copilot"><img src="https://img.shields.io/badge/install-GitHub_Copilot-black?style=flat-square" alt="Install on GitHub Copilot"></a>
</p>

<a name="tldr" id="tldr"></a>
## <img src="docs/assets/icons/bolt.svg" width="26" alt="" align="center"> 01 · At a Glance

Gregorian-Mode is an agent plugin built for designing with intention, your intention. It targets two mimetic sources of failure in agentic design: reasoning-execution collapse and conventional-pattern gravity. Five auto-firing skills built to maintain a user's stated intention for an idea throughout the building process as the agent works, translating intention to decisions in design systems, tokens, and UI, by running in the background. For existing work, a design audit can be invoked via /fix-my-design. 

If a decision cannot resolve without defaulting to standard, trendy/popular, or basic patterned choices without justifying its use in both form and function, a subagent is deployed to interrogate it. 

Again, these skills auto-fire and each one opens with a line describing when it applies; an agent reads that line and loads the skill whenever a session matches what it says. For example, `form-is-function` is invoked in any session touching a design or product decision. If you don't want to have that watchfulness interrupting in a session, disable the plugin rather than arguing with it mid-session.

***[Insert video here]***

<p align="center"><img src="docs/assets/divider.svg" alt="" width="600"></p>

<a name="background" id="background"></a>
## <img src="docs/assets/icons/scroll.svg" width="26" alt="" align="center"> 02 · Background

Gregorian Mode exists because two failure patterns keep producing poorly designed apps, websites, and software - and it's not a knowledge problem. The model can reason through design decisions coherently and even weigh different choices against each other with reasoning that balances the users intended needs, then calls its own analysis **"overthinking"**, and proceeds to reach for conventional patterns, defaults, and popular/trendy choices simply because they're widely used: it builds slop.

| The failure pattern | What Gregorian Mode does about it |
|---|---|
| **The reasoning–execution collapse.** An agent generates correct, specific design analysis, then labels that reasoning "overthinking," rushes execution, and produces output that contradicts the analysis it just completed. Correct it mid-session and it will repeat the same loop, collapsing every time. In research, this is documented in: the Berkeley/ETH paper *The Danger of Overthinking* (Cuadron et al., 2025) identifies it as the Reasoning-Action Dilemma across 4,018 recorded agent task runs ([arXiv:2502.08235](https://arxiv.org/abs/2502.08235)), and *Large Reasoning Models are not thinking straight* ([arXiv:2507.00711](https://arxiv.org/abs/2507.00711)) shows that models disregard correct solutions even when someone hands them one. | The `reasoning-execution-design-coherence` skill is built directly against that collapse. |
| **Conventional-pattern gravity.** Renaming is not redesigning. Left unopposed, agents reach for the nearest conventional pattern — the card, the tab strip, the modal window that drops over everything else, the badge pinned to a corner, the panel of filters; no amount of stylization fixes a form that serves no function. | The form-is-function skill strips the artificial binary choice between form and function that comes with weighting them individually and allows reasoning through choices that serve both form and function holistically. |

<p align="center"><img src="docs/assets/divider.svg" alt="" width="600"></p>

<a name="install" id="install"></a>

## <img src="docs/assets/icons/package.svg" width="26" alt="" align="center"> 03 · Install

The plugin is plain markdown that a compatible agent discovers on load. All skills live under `skills/`; the root `plugin.json` is an [Agent Plugins 1.0.0](https://agent-plugins.org/specification) manifest — a plain statement of what the plugin is and where its pieces sit.

**How to Install:**
You can either point your agent at this repo and instruct it to install the plugin (easiest), or use the below CLI commands to manually install:

<a name="claude-code" id="claude-code"></a>

<details>
  
<summary><strong>Claude Code</strong> · <code>claude --plugin-dir ./Gregorian-Mode</code></summary>


```bash
git clone https://github.com/AlastairZeved/Gregorian-Mode.git
claude --plugin-dir ./Gregorian-Mode
```

The first line copies the plugin down onto your machine; the second loads that copy. The `--plugin-dir` flag loads the plugin directly without marketplace installation, and also accepts a `.zip` archive of the plugin directory. 

</details>

<a name="hermes-agent" id="hermes-agent"></a>
<details>
<summary><strong>Hermes Agent</strong> · <code>hermes plugins install … --no-enable</code></summary>

```bash
hermes plugins install AlastairZeved/Gregorian-Mode --no-enable
hermes plugins enable gregorian-mode
hermes gateway restart
```
</details>

<a name="codex" id="codex"></a>
<details>
<summary><strong>Codex</strong> · <code>codex plugin add ./Gregorian-Mode</code></summary>

Requires OpenAI Codex. Two paths, both shipped:

- **Portable (recommended).** The root [`plugin.json`](plugin.json) declares the Agent Plugins schema, and Codex reads its OpenAI-specific presentation data from `extensions["com.openai"]` (display name "Gregorian Mode", category "design").
- **Compatibility fallback.** The [.codex-plugin/plugin.json](.codex-plugin/plugin.json) manifest.

```bash
git clone https://github.com/AlastairZeved/Gregorian-Mode.git
codex plugin add ./Gregorian-Mode
```
</details>

<a name="cursor" id="cursor"></a>
<details>
<summary><strong>Cursor</strong> · Settings → Customize → Plugins</summary>

Requires Cursor. The repository ships a [.cursor-plugin/plugin.json](.cursor-plugin/plugin.json) manifest pointing Cursor at the portable `skills/` directory and at the `commands/` and `agents/` written in Claude's format.

```bash
git clone https://github.com/AlastairZeved/Gregorian-Mode.git
```

Install from the repository: **Cursor Settings → Customize → Plugins** (or the Customize page), using an import from the copy on your machine. The manifest's `agents` and `commands` paths reference the `com.anthropic.claude/` client namespace; Cursor reads them where a Claude-style command or agent is understood.

</details>

<a name="github-copilot" id="github-copilot"></a>
<details>
<summary><strong>GitHub Copilot</strong> · VS Code "Install Plugin From Source"</summary>

Requires Copilot in VS Code, the Copilot CLI, or the app. Copilot supports Agent Plugins 1.0.0: it reads the portable `skills/` directory and the root `plugin.json`, then reads Copilot-specific components from the [`com.github.copilot/`](com.github.copilot) client namespace. This repository ships components in that namespace — the interrogator as an `.agent.md` custom agent and the fix procedure as a command wrapper — so Copilot users get the full plugin, not only the portable skills.

```bash
# VS Code: Chat: Install Plugin From Source (Command Palette), then enter the repo URL
https://github.com/AlastairZeved/Gregorian-Mode
```

</details>

<details>
  
<summary><strong>OpenClaw</strong> · <code>openclaw plugins install git:github.com/…</code></summary>

OpenClaw installs bundles — a plugin's files packaged together — straight from git, the tool that tracks a project's files and copies them between machines. The standard-format detection picks this repository up as an Agent Plugins (or Codex-marker) bundle and maps the portable `skills/` automatically:

```bash
openclaw plugins install git:github.com/AlastairZeved/Gregorian-Mode
openclaw plugins list        # verify: shows Format: bundle
openclaw gateway restart     # mapped skills load in the next session
```
</details>

<p align="center"><img src="docs/assets/divider.svg" alt="" width="600"></p>

<a name="philosophy" id="philosophy"></a>
## <img src="docs/assets/icons/columns.svg" width="26" alt="" align="center"> 04 · Philosophy

| Room | What hangs in it |
|---|---|
| **The first principle** | Design and function are not two categories to balance or trade off against each other. They are one set of questions applied to any object, component, or token until its value holds up on both counts at once (or until it honestly earns the right to be temporary as a working model, something good enough to use now). A choice that came from how something looks is held to the exact same standard as a choice that came from what it does: a green button that is green because the other buttons are green has failed, and a component placed because an action needed a home has also failed. |
| **The interrogation** | Every choice including the small, obvious, or conventional, is vetted through eight questions before committing: 1. What is this thing, fully? 2. What has been used as this thing? 3. What could it be? 4. Does its design optimize or add value to its use? 5. Does its function borrow anything from its form? 6. What would be surprising or genuinely valuable here? 7. What does this choice connect to at every scale — the module it sits in, the app around it, the project beyond that? 8. Can it tie to something already in progress? |
| **Failure conditions** | A choice has failed the interrogation if it was made because the choices beside it were the same, because convention suggested it, because function was satisfied without bothering to check form, because a pattern simply needed to be completed, or because something needed to go somewhere. Failure conditions are named bluntly. |
| **Impermanence** | Every choice remains editable, and being finished is not the same as being permanent. A working design earns its place by being useful long enough for a better answer to emerge. No choice is protected from re-interrogation just because you can cite the effort that went into it. |
| **Rollback, not patch** | When output collapses, the agent will roll back to the last verified-coherent position and rebuild. You cannot reason with poisoned context; once bad output sits in the conversation, it pulls the next answer down with it and continues the collapse loop. |
| **No tradeoff** | A choice that satisfies form but not function, or function but not form, has not finished the interrogation. |

<p align="center"><img src="docs/assets/divider.svg" alt="" width="600"></p>
