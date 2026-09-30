"""Repo checks for the humanizer plugin. Runs in CI and works locally before a push.

1. The plugin and marketplace manifests parse, and the marketplace entry's name
   matches the plugin manifest's name. A mismatch breaks installs.
2. Every SKILL.md description is at most 1,024 characters, the Agent Skills
   limit. Surfaces that enforce it reject the skill.
3. With --base <ref>: if anything users receive changed since <ref>, the version
   in .claude-plugin/plugin.json must differ from <ref>'s. Installs are pinned to
   that version, so an unbumped change never reaches them.
4. CHANGELOG.md has an entry for the current version, so every release records
   what changed and how it was checked.
5. Warns (without failing) when a sentence from an eval input also appears
   verbatim in the skill's files. Overlap lets a model pass by recalling an
   example instead of applying a rule, so keep eval inputs held out.

Usage:
    python .github/scripts/check_plugin.py [--base <git ref>]
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PLUGIN_JSON = ".claude-plugin/plugin.json"
MARKETPLACE_JSON = ".claude-plugin/marketplace.json"
CHANGELOG = "CHANGELOG.md"
MIN_OVERLAP = 12  # characters; shorter shared phrases are usually just the cliché being named
DESCRIPTION_LIMIT = 1024
# Changes under these paths reach people who install the plugin.
SHIPPED_PREFIXES = ("skills/", PLUGIN_JSON)


def read_description(skill_md: Path) -> str:
    """Return the frontmatter description, folded the way YAML folds `>` blocks."""
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, re.S)
    if not match:
        raise ValueError("no frontmatter")
    lines = match.group(1).splitlines()
    for i, line in enumerate(lines):
        if not line.startswith("description:"):
            continue
        value = line[len("description:"):].strip()
        if value not in (">", ">-", "|", "|-"):
            return value.strip("\"'")
        block = []
        for follow in lines[i + 1:]:
            if follow and not follow.startswith((" ", "\t")):
                break
            block.append(follow.strip())
        joiner = "\n" if value.startswith("|") else " "
        return joiner.join(part for part in block if part)
    raise ValueError("no description field")


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True, encoding="utf-8"
    ).stdout


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base", help="git ref to compare against for the version-bump check")
    args = parser.parse_args()
    errors = []

    # 1. Manifests
    plugin = json.loads((ROOT / PLUGIN_JSON).read_text(encoding="utf-8"))
    marketplace = json.loads((ROOT / MARKETPLACE_JSON).read_text(encoding="utf-8"))
    entry_names = [entry.get("name") for entry in marketplace.get("plugins", [])]
    if plugin.get("name") not in entry_names:
        errors.append(
            f"plugin.json name {plugin.get('name')!r} has no matching entry in marketplace.json {entry_names}"
        )
    print(f"manifests: plugin {plugin.get('name')} {plugin.get('version')}")

    # 2. Description length
    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        rel = skill_md.relative_to(ROOT).as_posix()
        try:
            length = len(read_description(skill_md))
        except ValueError as exc:
            errors.append(f"{rel}: {exc}")
            continue
        status = "ok" if length <= DESCRIPTION_LIMIT else "TOO LONG"
        print(f"description: {rel} {length}/{DESCRIPTION_LIMIT} chars {status}")
        if length > DESCRIPTION_LIMIT:
            errors.append(f"{rel}: description is {length} chars, over the {DESCRIPTION_LIMIT} limit")

    # 3. Version bump
    if args.base:
        changed = [p for p in git("diff", "--name-only", args.base).splitlines() if p]
        shipped = [p for p in changed if p.startswith(SHIPPED_PREFIXES)]
        if shipped:
            try:
                base_version = json.loads(git("show", f"{args.base}:{PLUGIN_JSON}")).get("version")
            except subprocess.CalledProcessError:
                base_version = None  # the base predates the plugin manifest
            if base_version is not None and base_version == plugin.get("version"):
                errors.append(
                    f"shipped files changed since {args.base} ({', '.join(shipped)}) but the version is "
                    f"still {base_version}; bump it in {PLUGIN_JSON}"
                )
            else:
                print(f"version: {base_version} -> {plugin.get('version')} ok")
        else:
            print(f"version: no shipped files changed since {args.base}")

    # 4. Changelog entry for the current version
    version = plugin.get("version")
    changelog = ROOT / CHANGELOG
    if not changelog.exists():
        errors.append(f"{CHANGELOG} is missing")
    elif not re.search(rf"^## \[?{re.escape(str(version))}\]?(\s|$)", changelog.read_text(encoding="utf-8"), re.M):
        errors.append(f"{CHANGELOG} has no '## {version}' entry; record what changed and how it was checked")
    else:
        print(f"changelog: entry for {version} ok")

    # 5. Eval inputs that overlap the skill's own text (warning only)
    skill_text = "".join(p.read_text(encoding="utf-8") for p in (ROOT / "skills").rglob("*.md"))
    overlaps = []
    for case in sorted(p for p in (ROOT / "evals").glob("*") if p.is_dir() and p.name != "results"):
        inputs = [p for p in [case / "prompt.md"] if p.exists()] + sorted(
            p for p in (case / "resources").rglob("*") if p.is_file()
        )
        for path in inputs:
            text = path.read_text(encoding="utf-8")
            if path.name == "prompt.md":
                text = text.split("---", 2)[-1]  # body only, not frontmatter
            # sentences and quoted strings with Hangul, long enough to be distinctive
            for piece in re.split(r'[\n"`<>]|(?<=[.?!])\s', text):
                piece = piece.strip(" -•*:0123456789.[]")
                if len(piece) >= MIN_OVERLAP and re.search("[가-힣]", piece) and piece in skill_text:
                    overlaps.append(f"{path.relative_to(ROOT).as_posix()}: {piece}")
    for item in sorted(set(overlaps)):
        print(f"WARNING: eval input also appears in skill files — {item}")
    print(f"eval overlap: {len(set(overlaps))} sentence(s)")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
