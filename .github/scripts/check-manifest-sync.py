#!/usr/bin/env python3
"""Fail when tracked plugin.json manifests disagree on name or version.

Every tracked file named plugin.json (any depth) is a manifest contract with
its own reader: the root manifest is the Agent Plugins 1.0.0 standard,
.claude-plugin/ is Claude Code, .codex-plugin/ is the Codex compatibility
fallback, .cursor-plugin/ is Cursor. They have drifted once before (PR #5
existed to reconcile root with .claude-plugin); issue #8 approved this check
so a drift is loud instead of silent.

Rule: all manifests must agree on `name` and `version`. A manifest missing
either field fails — this repo's convention is that every manifest carries
both, even where a client's spec would make version optional.
"""

import json
import subprocess
import sys


def tracked_manifests():
    out = subprocess.run(
        ["git", "ls-files", "*plugin.json"],
        capture_output=True, text=True, check=True,
    ).stdout.splitlines()
    return sorted(p for p in out if p.strip())


def main() -> int:
    paths = tracked_manifests()
    if not paths:
        print("manifest-sync: error — no tracked plugin.json manifests found", file=sys.stderr)
        return 1

    failures = []
    names = {}
    versions = {}

    for path in paths:
        try:
            with open(path, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{path}: not valid JSON ({exc})")
            continue
        if not isinstance(data, dict):
            failures.append(f"{path}: manifest is not a JSON object")
            continue
        name = data.get("name")
        version = data.get("version")
        if not isinstance(name, str) or not name:
            failures.append(f"{path}: missing or empty `name`")
        else:
            names.setdefault(name, path)
        if not isinstance(version, str) or not version:
            failures.append(f"{path}: missing or empty `version`")
        else:
            versions.setdefault(version, path)

    if len(names) > 1:
        detail = ", ".join(f"{path} has {name!r}" for name, path in sorted(names.items()))
        failures.append(f"name disagreement across manifests: {detail}")
    if len(versions) > 1:
        detail = ", ".join(f"{path} has {version!r}" for version, path in sorted(versions.items()))
        failures.append(f"version disagreement across manifests: {detail}")

    if failures:
        for failure in failures:
            print(f"::error::manifest-sync: {failure}")
        print(f"manifest-sync: FAIL — {len(failures)} problem(s) across {len(paths)} manifests")
        return 1

    name = next(iter(names))
    version = next(iter(versions))
    print(f"manifest-sync: OK — {len(paths)} manifests agree (name={name!r}, version={version!r})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())