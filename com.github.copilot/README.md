# com.github.copilot

GitHub Copilot's client-extension namespace under the [Agent Plugins 1.0.0](https://agent-plugins.org/specification) standard (§8: client extensions). Copilot in VS Code, the Copilot CLI, and the GitHub Copilot app read the portable `skills/` directory and the root `plugin.json` from the repository root, then read Copilot-specific components from this directory — `agents/` (`.agent.md` custom agents), `commands/`, `rules/`, and `hooks/hooks.json`. Other clients ignore this namespace, so the package stays portable.

## What ships here

| Component | File | Role |
|---|---|---|
| Interrogator | [`agents/interrogator.agent.md`](agents/interrogator.agent.md) | Custom agent (`.agent.md`, the format VS Code documents for plugin agents) — the pressure applied to a design choice that resists |
| Fix procedure | [`commands/fix-my-design.command.md`](commands/fix-my-design.command.md) | Thin wrapper: loads and follows the `fix-my-design` skill |

The five portable skills need nothing here — they are discovered from `skills/` by every Agent Plugins client, Copilot included. The two files above exist so Copilot users get the full plugin (the interrogation pressure and the `/fix-my-design` door) rather than the skills alone.

## Porting note

Both files port the components under [`com.anthropic.claude/`](../com.anthropic.claude/) (the Claude Code namespace, issue #2's packaging split) into Copilot's documented formats: the subagent becomes an `.agent.md` custom agent, and the slash command keeps its Claude-style frontmatter. Discovery of the command file follows the namespace layout the VS Code agent-plugins documentation shows; if a given Copilot surface does not surface it, the portable path still works — ask for the fix procedure in words ("Run fix-my-design on `<target>`"), which is the documented universal door in the root [README](../README.md#usage).