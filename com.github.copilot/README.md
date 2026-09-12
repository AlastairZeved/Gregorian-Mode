# com.github.copilot

GitHub Copilot's client-extension namespace. Copilot (in VS Code, the CLI, and the app) reads the portable `skills/` directory and the root [plugin.json](../plugin.json) manifest directly from the repository root, then looks inside this directory for Copilot-specific extensions — custom agents, hooks.

This repository ships no Copilot-specific components, so the portable skills load as-is. A Copilot-specific wrapper belongs here if one is ever warranted, following the same packaging split as [`com.anthropic.claude/`](../com.anthropic.claude/).