# claude-humanizer

Claude Agent Skills that make Claude's Korean copy read like a native human
wrote it — not a machine translation and not an AI.

Korean written by AI is usually grammatically perfect and completely lifeless:
every sentence the same length, every clause ending in `~습니다`, every idea
padded with `번역투` and empty superlatives. Native readers feel it instantly.
These skills strip those tells while preserving meaning, register, and brand
voice.

## Skills

| Skill | What it does |
|---|---|
| [`korean-humanizer`](skills/korean-humanizer/) | Rewrites any Korean copy — marketing, UI microcopy, SNS/blog, email — to sound naturally human. |

## What it fixes

- **번역투 · 직역체** — `~에 대해`, `~을 통해`, `~을 제공합니다`, overused `~들`, `당신`
- **과한 정중함 · 상투어** — `많은 관심 부탁드립니다`, `완벽한`/`특별한`/`최고의`, `지금 바로 ~하세요!`
- **밋밋한 리듬** — uniform sentence length, every line ending the same way
- **구조적 과잉** — needless bullet lists, `첫째/둘째/셋째` signposting, forced parallelism

See [`ai-tells.md`](skills/korean-humanizer/references/ai-tells.md) for the full
catalog and [`examples.md`](skills/korean-humanizer/references/examples.md) for
before/after copy in each format.

## Install

**Claude Code** — copy the skill into your skills directory:

```bash
# user-level (available in every project)
cp -r skills/korean-humanizer ~/.claude/skills/

# or project-level
cp -r skills/korean-humanizer .claude/skills/
```

Restart Claude Code (or start a new session) and the skill loads automatically.
It triggers whenever you write, translate, or polish Korean copy — or when you
ask to make Korean text `자연스럽게` / `사람이 쓴 것처럼`.

**Claude.ai / other surfaces** — upload the `korean-humanizer` folder as a skill
wherever Agent Skills are supported.

## Design principle

The goal is **invisibility, not personality.** The skill does not add slang,
jokes, or emoji to prove text is human — it removes the tells that mark it as
machine-made and stops there. Over-correcting into forced casualness is treated
as a new AI tell, not a fix. Register (명사형 / 해요체 / 습니다체 / 반말) is always
preserved.

## License

MIT — see [LICENSE](LICENSE).
