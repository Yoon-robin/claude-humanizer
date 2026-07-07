---
name: korean-humanizer
description: >-
  Rewrites Korean copy so it reads like a native human wrote it — not a machine
  translation and not an AI. Use this whenever you produce or edit ANY
  Korean-language copy: marketing and ad copy, landing pages, UI microcopy
  (buttons, toasts, empty states, error messages), push notifications, SNS/blog
  posts, emails, or newsletters — even when the user doesn't say the word
  "humanize." Trigger on any request to write, translate, polish, or naturalize
  Korean text, and whenever Korean output sounds stiff, translated, overly
  formal, or "AI-ish" (번역투, 직역체, 어색한 존댓말, 상투어). Also use when the user says
  the Korean "sounds like AI wrote it" or asks to make it 자연스럽게 / 사람이 쓴 것처럼.
---

# Korean Humanizer

Korean written by AI is usually grammatically correct and completely lifeless.
It reads like a careful translation of English: every sentence the same length,
every clause ending in `~습니다`, every idea padded with `~에 대해` and `~을 통해`,
every product "완벽하고 특별한." Native readers feel it instantly even when they
can't name why. This skill's job is to make that feeling go away — to produce
copy indistinguishable from something a good Korean writer wrote by hand.

The goal is **invisibility, not personality.** You are not adding slang, jokes,
or emoji to prove the text is human. You are removing the tells that mark it as
machine-made while preserving the meaning, the register, and the brand voice
exactly. Over-correcting into forced casualness is just as wrong as the stiff
original.

## The one test that matters: read it aloud

Before and after every rewrite, read the Korean out loud in your head as if a
real person were saying or writing it to a real audience. Human copy has a
pulse — short line, longer line, a fragment, a question. AI copy flatlines. If
the rhythm is monotonous or a phrase would never leave a Korean speaker's mouth,
it isn't done yet. This instinct catches more than any checklist.

## Workflow

### 1. Lock the register before touching anything

Korean lives or dies on speech level, and the biggest humanizing mistake is
silently changing it. Identify what the copy is using and **keep it**:

- **명사형 종결** — headline/slogan style, no verb ending ("당신의 아침을 바꾸는 커피")
- **해요체** — warm, conversational, most brand/app voice ("지금 바로 시작해 보세요")
- **하십시오체 / 습니다체** — formal, official, B2B, legal ("서비스를 이용해 주셔서 감사합니다")
- **반말** — young/casual brands, close community ("오늘 뭐 먹지?")

Match the source. A push notification and a legal notice are not the same voice,
and humanizing does not mean "make everything casual." If the register itself is
wrong for the context, flag it to the user rather than quietly rewriting it.

### 2. Diagnose the tells

Read the draft against the four families of AI tells below. Most stiff Korean
has several at once. For the full catalog with many worked before/after pairs,
read `references/ai-tells.md` — go there whenever you want concrete swaps rather
than working from memory.

**번역투 · 직역체 (translation-ese).** Structures imported from English that a
Korean writer wouldn't reach for:
- `~에 대해` / `~에 관하여` where a plain particle works ("건강에 대해 생각하다" → "건강을 생각하다")
- `~을 통해` for simple means ("앱을 통해 주문하세요" → "앱으로 주문하세요")
- `~을 제공합니다`, `~을 가지고 있습니다` (calques of "provides" / "has")
- Overuse of `~들` for plurals Korean marks with context ("사용자들은" → "사용자는")
- `당신` as a stand-in for "you" — Koreans almost never address readers this way
- Chained `~할 수 있습니다` as a default sentence ending
- Awkward passives: `~되어집니다`, `제공되어집니다`

**과한 정중함 · 상투어 (over-politeness & clichés).** Padding that adds
deference or hype but no meaning:
- `~하시기 바랍니다`, `많은 관심 부탁드립니다`, `여러분` sprinkled everywhere
- Empty superlatives: `완벽한`, `특별한`, `최고의`, `혁신적인` with nothing behind them
- Ad-cliché imperatives: `지금 바로 ~하세요!`, `놓치지 마세요!`
- Forced-friendly `함께 ~해요` and `~하는 건 어떨까요?` when it isn't warranted

**밋밋한 리듬 (flat rhythm).** The dead giveaway:
- Every sentence roughly the same length
- Every sentence ending `~습니다` (or every one `~요`)
- No fragments, no one-line punch, no varied endings
- Fix by cutting, splitting, and letting some lines land short. Human copy mixes
  lengths on purpose.

**구조적 과잉 (structural excess).** English-essay scaffolding forced onto copy
that doesn't need it:
- Bullet lists where flowing prose is natural
- `첫째, 둘째, 셋째` / `먼저 ~ 다음으로 ~ 마지막으로` signposting
- Rigid `~뿐만 아니라 ~도` parallelism
- A mechanical intro-body-conclusion shape in three tidy sentences

### 3. Rewrite, then re-read

Fix the tells while holding meaning and register constant. Then apply the
read-aloud test again. Prefer the change that a Korean copywriter would make:
drop a particle, break a sentence, swap a Latinate calque for a plain verb, let
a line end on a noun. Restraint beats cleverness — the best humanized copy looks
like nobody edited it at all.

## Guardrails

- **Preserve meaning and facts.** Never drop information, product claims, or
  legally required wording to make something flow better.
- **Don't overcorrect.** Injecting slang, emoji, aegyo, or exclamation points
  that weren't warranted is a new AI tell, not a fix. When unsure, stay neutral.
- **Keep the register.** Humanizing ≠ casualizing. A formal notice should still
  read formal — just like a human wrote it, not a translation engine.
- **Respect brand voice.** If earlier copy or a style guide establishes a voice,
  match it rather than imposing a generic "natural" tone.
- **Whole copy, not word-by-word.** Naturalness comes from rhythm across
  sentences. Rewrite in passes over the full text, not term substitution.

## Delivering the result

Default to returning just the rewritten Korean — clean, ready to paste. When the
user is clearly iterating or learning (they ask *why*, or want options), briefly
name the main tells you fixed and offer a variant. Don't bury a good rewrite
under commentary nobody asked for.

For end-to-end before/after copy in each format (marketing, UI microcopy,
SNS/blog, email), read `references/examples.md`.
