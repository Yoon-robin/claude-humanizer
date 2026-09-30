---
name: humanizer
description: >-
  Makes AI-written copy read like a native human wrote it, in any language
  (detailed catalogs for Korean and English; others use the universal rules).
  Use whenever you write or edit copy people will read: marketing and ad copy,
  landing pages, UI microcopy (buttons, toasts, empty states, errors), push
  notifications, social posts, emails, newsletters, presentation slide titles,
  report headings — and when sweeping a codebase's UI strings (locale/i18n
  files, JSX text, notification templates) for stiff or inconsistent copy. Trigger on
  requests to write, translate, polish, or naturalize text, and whenever output
  sounds stiff, translated, over-formal, or AI-ish (English "delve," "it's not
  just X, it's Y," em-dash overuse; Korean 번역투·직역체·상투어), or the user says it
  "sounds like AI/ChatGPT" or asks to make it natural / 자연스럽게 / 사람이 쓴 것처럼.
  Not for spelling-only fixes, comprehension-only translation, one-line
  politeness tweaks, researching long-form articles, or evading AI detectors.
---

# Humanizer

AI-written copy has a family resemblance in every language: grammatically
correct, tonally dead. The surface tells differ (English leans on em-dashes,
"delve," and "it's not just X, it's Y"; Korean on 번역투 and a monotonous
`~습니다`), but the failures underneath are the same, and native readers feel them
even when they can't name them. Your job is copy a good native writer could have
written by hand.

The goal is **invisibility, not personality.** Don't add slang, jokes, or emoji to
prove the text is human. Remove the tells that mark it as machine-made, and keep
the meaning, register, and voice exactly. Forced casualness is as wrong as the
stiff original.

## Step 0 — Load what the job needs

- Detect the language of the copy (or the one you're asked to write in).
- **Short fix** (a button, a toast, a few lines): this file is enough. Open the
  language file only if you hit a tell it doesn't cover. **Titles and headlines
  are the exception:** also read the language file's titles section.
- **Longer copy** (a paragraph or more): read `references/languages/<language>.md`
  for its tells, swaps, and register notes (bundled: `korean.md`, `english.md`),
  and `<language>-examples.md` for full before/after pieces when you're unsure how
  far to go.
- No file for the language? Apply the families below with native-level judgment
  and the same guardrails. If a language keeps coming up, write a file from
  `references/languages/_template.md`.
- **Sweep over many strings** (locale files, JSX text, notification templates):
  read `references/codebase-scan.md` (inventory, group by surface, set each
  surface's register, edit minimally, report). Skip the language files unless a
  string needs them.

## Read it aloud

Before and after every rewrite, hear the text as a native speaker would say it to
a real audience. Human copy has a pulse: a short line, a longer one, a fragment, a
question. AI copy flatlines. If the rhythm drones or a phrase would never leave a
native speaker's mouth, it isn't done. This catches more than any checklist.

## Step 1 — Lock the register

Each language encodes formality its own way: English contractions and house tone;
Korean 존댓말/반말 and the 합니다체/해요체 texture; Japanese です・ます vs. plain form and
keigo; tu/usted, tu/vous, du/Sie. Identify what the copy uses and **hold it.**
Humanizing isn't casualizing, so a formal notice still reads formal. The
politeness level stays fixed; natural in-register variation (mixing 합니다체 and
해요체, contractions in English) is welcome. If the register itself is wrong for
the context, flag it instead of quietly changing it.

**Zoom out to the surface.** A string with no tell of its own can still be wrong
because it drifts from the copy around it. In product and codebase copy this is
often the main problem: **legacy drift**, where old strings keep an old voice (one
습니다체 notification in a 해요체 feed, two `~관리합니다` labels among `~관리해요`).
Converge on the surface's established register. That's **consistency recovery,
not casualizing**: you restore the voice the surface already chose. For every
string, ask both "is this a tell on its own?" and "what voice do its neighbors on
this screen, flow, or label row use?"

## Step 2 — Diagnose the tells

Five families recur in every language; the language file has the concrete
patterns.

1. **Translation-ese / calques** — structures imported from another language.
   (EN "in order to," noun pile-ups; KO `~에 대해`, `~을 통해`, `~을 제공합니다`)
2. **Over-formality, cliché & decoration** — hype, empty phrases, and metaphors or
   poetic verbs where a plain word works. (EN "seamless," "unlock," "in today's
   fast-paced world"; KO `완벽한`, `많은 관심 부탁드립니다`, `입구가 모입니다`, `머무는 곳`)
3. **Flat rhythm** — the most universal tell: uniform length and endings, no
   fragments or questions. Cut, split, let a line land short.
4. **Structural excess** — essay scaffolding on copy: needless bullets, "Firstly /
   Finally," bold headers and emoji on short copy, a rule-of-three on every line.
5. **Slick parallelism / antithesis** — the too-perfect balanced line: EN "It's
   not just X, it's Y"; KO 대구 like `소리는 지우고, 하루는 채우고`. Break the symmetry
   or let one side go plain.

**Titles and headlines** (slides, report sections, diagrams) have tells of their
own: a contrast twist (`~지만`), a comma-split or left/right mirror, a metaphor.
Structure and data slides take a label naming what the slide is (`사용 흐름`,
`시스템 아키텍처`); keep a message title for a slide that lands one claim, and keep
it plain. Match the form the rest of the deck uses, and keep numbers, names, and
the qualifiers that change how a number reads, such as a small sample or a period
(`Next.js · Supabase 구성`, not `기술 스택`).

## Step 3 — Rewrite, then re-read

Fix the tells while meaning and register stay put, then read it aloud again. Make
the edit a good native writer would: cut filler, split a sentence, swap a calque
for a plain verb. Restraint beats cleverness; the best result looks unedited.

## Step 4 — Check before delivering

- **Protected spans** (below) are byte-for-byte identical to the source.
- **Register** matches what you locked in Step 1.
- **No residual tells.** Re-scan against the language file; it's easy to fix four
  and miss the fifth. Parallelism survives rewording (EN "Whether you're X or Y,"
  "From X to Y," an antithesis around an em-dash; KO a fresh 대구). If a line
  still seesaws, it isn't fixed.
- **Rhythm varies.** Not every sentence the same length, and not one dense block
  where the format allows line breaks.
- **Every edit traces to a tell.** Rewriting a fine line is "improving," a job
  nobody asked for, and over-polishing is itself a tell, so roll it back. This
  isn't a change-percentage rule: short marketing copy may change a lot, a formal
  notice barely.

## Protected spans — never rewrite

Naturalize the language, never the content. Keep these byte-for-byte, even inside
an awkward sentence, and rewrite around them:

- Proper nouns: brand, product, model, company, and person names
- Numbers, prices, dates, times, units, percentages, measurements
- Text in direct quotation marks
- URLs, emails, handles, hashtags, file names, code
- Placeholders and markup: `{name}`, `{{count}}`, `%s`, `${user}`, ICU
  `{n, plural, …}`, HTML/JSX tags, i18n keys. A renamed or dropped placeholder is
  a shipped bug.
- Legal and contractual wording (disclaimers, terms, consent copy)
- Standard acronyms (API, AI, UX, B2B …)
- **Feature names and spec keywords the brief sells on** (EN "active noise
  cancellation," KO "액티브 노이즈캔슬링"): keep the term, rewrite around it.

## Guardrails

- **Preserve meaning and facts.** Don't drop information, claims, or required
  wording for the sake of flow.
- **Don't invent specifics.** Concreteness only helps when it's true. A scene,
  number, or mechanism the source never stated is a fidelity break.
- **Keep each term's scope.** "Saved items" isn't "saved posts," and 항목 isn't 글.
  If you suspect the narrower word is what the product means, flag it.
- **Keep the product's punctuation and quoting style** around names and
  placeholders (`「${title}」`, `"…"`). It's house style, not a tell.
- **Don't overcorrect.** Unwarranted slang, emoji, or exclamation points are a new
  tell. When unsure, stay neutral.
- **Respect brand voice.** Match an established voice or style guide rather than a
  generic "natural" tone.
- **Work on the whole copy.** Naturalness lives in rhythm across sentences, not in
  term-by-term substitution.

## Delivering the result

Return just the rewritten copy, ready to paste. If the user is iterating or asks
*why*, name the main tells you fixed and offer a variant; don't bury the rewrite
in commentary. For a sweep, deliver a findings report (location, before, after,
why) plus what you flagged but left alone, as `references/codebase-scan.md`
describes.
