---
name: humanizer
description: >-
  Rewrites AI-written copy in ANY language so it reads like a native human wrote
  it — not a machine translation and not an AI. Use whenever you produce or edit
  copy that should sound human: marketing and ad copy, landing pages, UI
  microcopy (buttons, toasts, empty states, errors), push notifications,
  social/blog posts, emails, or newsletters — in English, Korean, Japanese,
  Chinese, Spanish, or any other language. Trigger on any request to write,
  translate, polish, or naturalize text, and whenever output sounds stiff,
  translated, robotic, over-formal, or "AI-ish" — e.g. English "delve / tapestry
  / it's not just X, it's Y" and em-dash overuse, or Korean 번역투·직역체·상투어. Also
  trigger when the user says the text "sounds like AI/ChatGPT wrote it" or asks
  to make it natural / sound human / 자연스럽게 / 사람이 쓴 것처럼. Not for one-line
  politeness tweaks, generating fresh content from scratch, comprehension-only
  translation, spelling/grammar-only fixes, or evading AI-detection tools — those
  are different tasks. Deep language-specific catalogs live in
  references/languages/; the universal principles below apply even to languages
  without a dedicated file.
---

# Humanizer

AI-written copy has a family resemblance in every language: grammatically
correct, tonally dead. The surface tells differ — English overuses em-dashes,
"delve," and the "it's not just X, it's Y" flourish; Korean leans on 번역투 and a
monotonous `~습니다` drumbeat — but the underlying failures are the same
everywhere. Native readers feel it instantly even when they can't name why. This
skill's job is to make that feeling go away: to produce copy indistinguishable
from something a good writer in that language wrote by hand.

The goal is **invisibility, not personality.** You are not adding slang, jokes,
or emoji to prove the text is human. You are removing the tells that mark it as
machine-made while preserving the meaning, the register, and the voice exactly.
Over-correcting into forced casualness is just as wrong as the stiff original,
in any language.

## Step 0 — Identify the language and load its catalog

Detect the language of the copy (or the language the user asked you to write in).
Then:

- If `references/languages/<language>.md` exists, **read it** — it holds the
  concrete tells, word-level swaps, register system, and worked examples for that
  language. Bundled today: `korean.md`, `english.md`.
- If there is **no file for that language**, don't stop — apply the universal
  families below using your own native-level judgment of that language, plus the
  same guardrails. The skill degrades gracefully: it works for any language, just
  with less bundled detail. (If you find yourself repeatedly humanizing a
  language with no file, consider writing one — see
  `references/languages/_template.md`.)

## The one test that matters: read it aloud

Before and after every rewrite, read the text out loud in your head **as a native
speaker of that language** would say or write it to a real audience. Human copy
has a pulse — short line, longer line, a fragment, a question. AI copy flatlines.
If the rhythm is monotonous or a phrase would never leave a native speaker's
mouth, it isn't done yet. This instinct catches more than any checklist, and it
transfers across every language.

## Step 1 — Lock the register before touching anything

Every language encodes formality and social distance differently, and the biggest
humanizing mistake is silently changing it:

- **English** — formality and contractions (you'll vs. you will), house tone
  (buttoned-up B2B vs. friendly consumer), how much warmth is appropriate.
- **Korean** — speech level (존댓말/반말) and the 합니다체/해요체 texture.
- **Japanese** — です・ます vs. plain form; keigo level.
- **Spanish / French / German** — tú/usted, tu/vous, du/Sie.

Identify the system the copy is using and **hold it.** Humanizing ≠ casualizing:
a formal notice should still read formal — just like a human wrote it, not a
translation engine. What must stay fixed is the *politeness/formality level*; what
does *not* need to be rigidly uniform is the natural in-register variation a real
writer uses (mixing 합니다체/해요체 in Korean, or contractions in English). The
language file describes its register system; if none exists, use your knowledge of
the language. If the register itself is wrong for the context, flag it rather than
quietly rewriting it.

## Step 2 — Diagnose the tells

These five families recur across languages. The language file gives concrete,
language-specific patterns and swaps — go there for those. Here is what to hunt
for in **any** language:

1. **Translation-ese / calques.** Structures, idioms, and word order imported
   from another language (usually English, or from the source in a translation).
   Correct, but not what a native writer would reach for. *(EN: literal renderings,
   "in order to," nominalization pile-ups. KO: `~에 대해`, `~을 통해`, `~을 제공합니다`.)*

2. **Over-formality, deference & cliché padding.** Hype words and empty phrases
   that add register or excitement but no meaning. *(EN: "revolutionary,"
   "seamless," "world-class," "in today's fast-paced world," "unlock," "elevate."
   KO: `완벽한`, `최고의`, `많은 관심 부탁드립니다`.)*

3. **Flat rhythm** — the most universal tell of all. Uniform sentence length,
   every sentence the same shape or ending, no fragments, no questions. Humans
   vary length and cadence on purpose; AI flatlines. Fix by cutting, splitting,
   and letting some lines land short.

4. **Structural excess.** Essay scaffolding forced onto copy that should just
   flow: needless bullet lists, "Firstly / Secondly / Finally" signposting, bold
   headers and emoji on short copy, a tidy rule-of-three on every line.

5. **Slick symmetrical parallelism / antithesis** — the too-perfect balanced
   line. In English this is the signature tic: *"It's not just X — it's Y,"*
   *"This isn't about X. It's about Y."* In Korean, the neat 대구
   (`소리는 지우고, 하루는 채우고`). One immaculate parallel reads as manufactured
   cleverness — an AI/copywriter tell in any language. Break the symmetry, or let
   one side go plain.

## Step 3 — Rewrite, then re-read

Fix the tells while holding meaning and register constant. Then apply the
read-aloud test again. Prefer the change a good writer in that language would
make: cut a filler word, break a sentence, swap a calque for a plain verb, let a
line end short. Restraint beats cleverness — the best humanized copy looks like
nobody edited it at all.

## Step 4 — Check yourself before delivering

A humanizer that "improves" the wrong thing does real damage, so run a quick
fidelity pass:

- **Protected spans untouched?** (see below) — byte-for-byte identical to source.
- **Register held?** Same formality/speech level you locked in Step 1.
- **Residual tells from the language file?** It's easy to fix four tells and miss
  the fifth — re-scan the output against the specific patterns in the language
  catalog. The balanced-parallelism family (#5) is the sneakiest: it survives in
  *reworded* form (English "Whether you're X or Y," "From X to Y," a mid-sentence
  antithesis around an em-dash; Korean a fresh 대구). If a line is still a tidy
  seesaw, it isn't fixed yet.
- **Does the rhythm actually vary?** Read the final copy back. If every sentence is
  the same length — or it's one dense block where the format allows line breaks and
  a short line — it flatlined. Break it up; let a line land short.
- **Only as much change as the tells required?** If you rewrote a line that had no
  tell, you've drifted into "improving" the copy — a different job the user didn't
  ask for. Roll it back. Over-polishing is itself an AI tell: real editors leave
  fine sentences alone.

This isn't a rigid change-percentage rule — short marketing copy can be rewritten
heavily, while a formal notice should barely move. The test is intent: every edit
should trace to a specific tell.

## Protected spans — never rewrite these

Naturalizing the *language* must never touch the *content*. Leave these
byte-for-byte as they appear in the source, even inside an otherwise awkward
sentence — rewrite the words around them instead:

- Proper nouns: brand, product, model, company, and person names
- Numbers, prices, dates, times, units, percentages, and measurements
- Text inside direct quotation marks
- URLs, email addresses, handles, hashtags, file names, and code
- Legally or contractually required wording (disclaimers, terms, consent copy)
- Standard industry acronyms readers expect (API, AI, UX, B2B …)
- **Named features or spec keywords the brief highlights as selling points.**
  Naturalize the words *around* the term, but keep the term itself — paraphrasing
  a named feature (English "active noise cancellation," Korean "액티브 노이즈캔슬링")
  into a generic description strips a keyword the reader came for.

## Guardrails

- **Preserve meaning and facts.** Never drop information, product claims, or
  legally required wording to make something flow better.
- **Don't invent specifics to sound vivid.** Concreteness makes copy human, but
  only when it's true. Adding a detail the source never stated — a scene, a
  number, a mechanism — is a fidelity break, not a humanizing win.
- **Don't overcorrect.** Injecting slang, emoji, or exclamation points that
  weren't warranted is a new AI tell, not a fix. When unsure, stay neutral.
- **Keep the speech/formality level**, but don't police natural in-register
  variation — that's what makes copy read human rather than uniform.
- **Respect brand voice.** If earlier copy or a style guide establishes a voice,
  match it rather than imposing a generic "natural" tone.
- **Whole copy, not word-by-word.** Naturalness comes from rhythm across
  sentences. Rewrite in passes over the full text, not term substitution.

## Delivering the result

Default to returning just the rewritten copy — clean, ready to paste. When the
user is clearly iterating or learning (they ask *why*, or want options), briefly
name the main tells you fixed and offer a variant. Don't bury a good rewrite under
commentary nobody asked for.

For the deep per-language catalog (concrete tells, swaps, before/after examples),
read the matching file in `references/languages/`. To add support for a new
language, follow `references/languages/_template.md`.
