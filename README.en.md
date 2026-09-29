# claude-humanizer

[한국어](README.md)

A Claude Code plugin that makes AI-written copy read like a native human wrote it
— in **any language**, not a machine translation and not an AI.

AI copy has a family resemblance everywhere: grammatically correct, tonally dead.
The surface tells differ by language — English overuses em-dashes, "delve," and
the "it's not just X, it's Y" flourish; Korean leans on 번역투 and a monotonous
`~습니다` drumbeat — but the underlying failures are the same. The `humanizer`
skill strips those tells while preserving meaning, register, and voice.

## Install

In Claude Code:

```text
/plugin marketplace add Yoon-robin/claude-humanizer
/plugin install humanizer@claude-humanizer
```

Or from your shell:

```bash
claude plugin marketplace add Yoon-robin/claude-humanizer
claude plugin install humanizer@claude-humanizer
```

Start a new session. The skill triggers on its own when you write, translate, or
polish copy, or when you ask to make text sound human / 자연스럽게 / less "AI-ish."
To call it explicitly, run `/humanizer:humanizer`. Get updates with
`claude plugin update humanizer@claude-humanizer`.

> If you installed an earlier version by copying `skills/humanizer` into
> `~/.claude/skills/`, delete that copy so you don't load the skill twice.

**Without the plugin system** (Claude.ai or other surfaces that take a skill
folder), copy or upload `skills/humanizer` as a skill.

## What it does

**Copy, one piece at a time.** Marketing and ad copy, landing pages, UI microcopy,
push notifications, social posts, emails, newsletters. It hunts five tell families
that recur in every language:

1. **Translation-ese / calques** — structures imported from another language
2. **Over-formality, deference & cliché padding** — hype and empty phrases
3. **Flat rhythm** — uniform length and cadence (the most universal tell)
4. **Structural excess** — bullets, signposting, and scaffolding forced onto copy
5. **Slick symmetrical parallelism** — the too-perfect balanced line

**A whole product's UI strings.** Point it at a codebase's locale files, JSX text,
and notification templates. In a mature product, most real problems aren't
one-off AI tells but **register drift**: one legacy 습니다체 notification in a feed
that otherwise speaks 해요체, one stiff button in a friendly row, a push message that
no longer matches its in-app twin. The sweep workflow groups strings by the
surface a user sees, converges each surface on its own dominant voice, keeps
placeholders (`{name}`, `${actor}`, ICU plurals) intact, leaves clean strings
alone, and reports what it changed and what it deliberately didn't.

## How it's built

One skill with a language-agnostic spine and per-language catalogs:

```text
.claude-plugin/
├── plugin.json                    ← plugin manifest
└── marketplace.json               ← lets `/plugin marketplace add` find it
skills/humanizer/
├── SKILL.md                       ← workflow + the 5 cross-lingual tell families
└── references/
    ├── codebase-scan.md           ← sweeping a product's UI strings
    └── languages/
        ├── korean.md              ← Korean tells and swaps (read every time)
        ├── korean-examples.md     ← Korean before/after pieces (longer copy only)
        ├── english.md             ← English tells (delve, em-dash, antithesis…)
        ├── english-examples.md    ← English before/after piece
        └── _template.md           ← how to add a new language
evals/                             ← test suite for `claude plugin eval`
.github/                           ← checks that run on every push and PR
```

The skill detects the target language and loads its catalog. Languages without a
dedicated file still work: it falls back to the universal principles and
native-level judgment.

| Language | Catalog | Depth |
|---|---|---|
| Korean | [`korean.md`](skills/humanizer/references/languages/korean.md) | Full, current focus |
| English | [`english.md`](skills/humanizer/references/languages/english.md) | Full |
| Any other | — | Universal principles (graceful fallback) |

Korean is the current focus. English is maintained as is, and other languages run
on the universal principles.

A short fix reads only the tells file; the before/after pieces in
`<language>-examples.md` load for longer copy, so fixing one button doesn't pay
for every example.

## Design principles

- **Invisibility, not personality.** It doesn't add slang, jokes, or emoji to
  prove text is human. It removes the tells that mark it as machine-made and
  stops there. Over-correcting into forced casualness counts as a new tell.
- **Every edit traces to a tell.** Sentences with nothing wrong are left alone. In
  a tidy codebase, changing a small fraction of what was scanned is the expected
  result.
- **Register is held, not lowered.** Formality, speech level, and honorifics stay
  where they were. Fixing drift means returning a string to the voice its surface
  already chose. That's consistency, not casualizing.
- **Content is protected.** Names, numbers, prices, quotes, legal wording,
  placeholders, and the feature names a brief calls out are never rewritten.

**Not a goal: evading AI detectors.** This is a writing-quality tool for copy you
or your team are responsible for. It isn't built to disguise AI-generated
coursework, applications, or other work where AI use has to be disclosed. The
skill's description scopes those requests out, and `evals/neg-detector-evasion`
checks that it stays out.

## Testing

`evals/` holds a suite for [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals)
(needs a recent Claude Code — run `claude update` first):

| Case | Checks |
|---|---|
| `ko-humanize-newsletter`, `en-humanize-blurb` | Rewrites AI-sounding copy: facts kept, tells gone |
| `ko-landing-copy` | Fresh copy: named features kept, no superlatives or slick 대구 |
| `ko-codebase-drift-review` | Sweep of a small app fixture: obvious drift, subtle drift (particle after a placeholder, mixed button labels, a push message in another file), and restraint |
| `ko-formal-notice-keeps-register`, `ko-banmal-brand-caption` | Register held both ways: a formal notice stays formal (date and time untouched), a 반말 brand caption stays 반말 without forced slang or emoji |
| `neg-*` | Requests the skill must **not** take: spelling-only fixes, comprehension-only translation, AI-detector evasion |

Current models handle a single piece of copy well even without the skill, so the
single-piece cases may show a small gap against the baseline. They guard against
the skill making things worse. The skill's clearest effect shows up in codebase
sweeps: leaving clean strings alone and keeping the original meaning.

```bash
claude plugin eval .                            # full suite, with a no-plugin baseline
claude plugin eval . --runs 1 --ablation none   # cheap smoke run
claude plugin eval . --tag trigger              # triggering cases only
```

Each run is a real model call on your account, so the full suite costs money;
start with the smoke run. Results land in `evals/results/`, which is git-ignored.

## Contributing

- **Add a language:** copy
  [`_template.md`](skills/humanizer/references/languages/_template.md) to
  `<language>.md`, fill it in with ❌/✅ pairs, and add it to the table above.
- **Check before pushing:** run `claude plugin validate . --strict` and
  `python .github/scripts/check_plugin.py --base origin/master`. CI runs the same
  checks on every push and pull request.
- **Keep the skill's `description` under 1,024 characters.** It's the only part
  loaded into every session, and longer descriptions are rejected by surfaces that
  enforce the Agent Skills limit. Put "how" in the body and keep "when" in the
  description.
- **Releasing:** installs are pinned to the `version` in
  `.claude-plugin/plugin.json`, so bump it for every change users should receive.
  CI fails if shipped files change without a bump.

## License

MIT — see [LICENSE](LICENSE).
