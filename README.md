# claude-humanizer

A Claude Agent Skill that makes AI-written copy read like a native human wrote it
— in **any language**, not a machine translation and not an AI.

AI copy has a family resemblance everywhere: grammatically correct, tonally dead.
The surface tells differ by language — English overuses em-dashes, "delve," and
the "it's not just X, it's Y" flourish; Korean leans on 번역투 and a monotonous
`~습니다` drumbeat — but the underlying failures are the same. This skill strips
those tells while preserving meaning, register, and voice.

## How it works

One skill, a language-agnostic spine plus per-language catalogs:

```
skills/humanizer/
├── SKILL.md                     ← universal workflow + the 5 cross-lingual tell families
└── references/languages/
    ├── korean.md                ← Korean tells, swaps, before/after examples
    ├── english.md               ← English tells (delve, em-dash, antithesis, hype…)
    └── _template.md             ← how to add a new language
```

The skill detects the target language and loads its catalog. **Languages without
a dedicated file still work** — it falls back to the universal principles and
native-level judgment (graceful degradation).

## The 5 universal tell families

1. **Translation-ese / calques** — structures imported from another language
2. **Over-formality, deference & cliché padding** — hype and empty phrases
3. **Flat rhythm** — uniform length and cadence (the most universal tell)
4. **Structural excess** — bullets, signposting, and scaffolding forced onto copy
5. **Slick symmetrical parallelism** — the too-perfect balanced line / antithesis

Each language file makes these concrete. See
[`english.md`](skills/humanizer/references/languages/english.md) and
[`korean.md`](skills/humanizer/references/languages/korean.md).

## Supported languages

| Language | Catalog | Depth |
|---|---|---|
| English | [`english.md`](skills/humanizer/references/languages/english.md) | Full |
| Korean | [`korean.md`](skills/humanizer/references/languages/korean.md) | Full |
| Any other | — | Universal principles (graceful fallback) |

Adding a language is a single file — copy
[`_template.md`](skills/humanizer/references/languages/_template.md) to
`<language>.md`, fill it in, and the skill picks it up. PRs welcome.

## Install

**Claude Code** — copy the skill into your skills directory:

```bash
# user-level (available in every project)
cp -r skills/humanizer ~/.claude/skills/

# or project-level
cp -r skills/humanizer .claude/skills/
```

Start a new session and the skill loads automatically. It triggers whenever you
write, translate, or polish copy — or when you ask to make text sound human /
자연스럽게 / less "AI-ish."

**Claude.ai / other surfaces** — upload the `humanizer` folder as a skill wherever
Agent Skills are supported.

## Design principle

The goal is **invisibility, not personality.** The skill does not add slang,
jokes, or emoji to prove text is human — it removes the tells that mark it as
machine-made and stops there. Over-correcting into forced casualness is treated as
a new AI tell, not a fix. Register (formality, speech level, honorifics) is always
preserved.

## License

MIT — see [LICENSE](LICENSE).
