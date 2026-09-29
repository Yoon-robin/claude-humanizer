# Codebase Sweeps — Humanizing UI Copy Across a Product

Load this when the job isn't one piece of copy but many strings spread across a
codebase or product: locale/i18n files, JSX/TSX text, notification and email
templates, error messages. The tells are the same five families from `SKILL.md`,
but the unit of judgment changes. In a mature product, most real problems are
**register drift between neighboring strings**, and most strings are already fine.

## Contents

1. [Inventory — find the user-facing strings](#1-inventory--find-the-user-facing-strings)
2. [Group by surface](#2-group-by-surface)
3. [Set each surface's register](#3-set-each-surfaces-register)
4. [Diagnose — own tells and drift](#4-diagnose--own-tells-and-drift)
5. [Edit minimally](#5-edit-minimally)
6. [Report](#6-report)
7. [Parallel sweeps on large repos](#7-parallel-sweeps-on-large-repos)
8. [Korean i18n notes](#8-korean-i18n-notes)

---

## 1. Inventory — find the user-facing strings

Where copy usually lives:

- **Locale files** — `locales/**`, `messages/*.json`, `i18n/**`, `*.po`,
  `strings.xml`, `Localizable.strings`.
- **Inline UI text** — JSX children and user-facing props (`placeholder`, `title`,
  `aria-label`, `alt`, `label`, `description`), toast/`notify()`/`alert()` calls,
  user-facing error classes.
- **Server-side copy** — notification and email templates, push payload builders,
  SMS text.

For Korean, grepping for Hangul finds nearly everything fast:
`rg -n "[가-힣]" --glob '!**/*.test.*'`. For English, search locale values and
string literals in JSX props.

Leave out anything a user never reads: `console.*` and log messages, developer
errors, analytics event names, enum values and keys, test fixtures, and comments.
Humanizing those only adds noise to the diff.

## 2. Group by surface

A **surface** is the set of strings a user sees together or in one flow: one
notification family, one form, one onboarding sequence, one settings page, a row
of adjacent buttons and labels, one email template.

Group by what the user experiences, not by file. A surface often spans files (a
notification's server template and its client renderer), and one big `ko.json` or
`en.json` usually holds many surfaces.

## 3. Set each surface's register

For each surface, tally the speech level — Korean: 해요체 / 합니다체 / 반말 / 명사형;
English: contractions or not, sentence case vs. Title Case, warmth. The dominant
register is the surface's intended voice, and it's usually also the one the newest
strings use.

- **Converge within a surface, never across surfaces.** Different surfaces can
  legitimately differ: legal and consent copy stays formal even when the rest of
  the app speaks 해요체. Pulling a formal surface toward the app's majority voice is
  casualizing, not consistency.
- **No clear majority?** If a surface is genuinely split, or a style guide says
  something else, don't silently pick a winner. Flag it as a product decision.

## 4. Diagnose — own tells and drift

Ask two questions of every string:

1. **Does it carry a tell on its own?** Check the five families and the language
   catalog.
2. **Does it drift from its surface's register?** A string can be clean in
   isolation and still be the one seam on the screen.

Expect "no" to both for most strings. In a tidy codebase, a sweep that changes a
small fraction of what it scanned is a normal, healthy result. Don't manufacture
finds to look productive — that's over-correction, and the diff becomes harder to
review.

## 5. Edit minimally

- **Change only strings with a tell or drift.** Leave everything else
  byte-identical so the diff can be reviewed string by string.
- **Keep interpolation and markup intact** — `{name}`, `{{count}}`, `%s`, `${var}`,
  ICU `{n, plural, …}`, HTML/JSX tags, i18n keys. Rewrite around them.
- **Respect the slot.** Buttons, tabs, and toasts truncate. Don't lengthen a label
  that sits in a tight space.
- **Stay in the language you were asked about.** Don't "sync" other locales unless
  asked; their translators may own them.
- **No drive-by refactors.** Don't rename keys, reorder files, or reformat JSON
  while you're there.

## 6. Report

Deliver a findings report alongside the edits (or instead of them, if the user
asked for a review only):

| Location | Before | After | Why |
|---|---|---|---|
| `messages/ko.json` → `dialog.logout` | 로그아웃하시겠습니까? | 로그아웃할까요? | drift — every other dialog is 해요체 |
| `LoginForm.tsx` placeholder | 이메일을 입력하여 주십시오 | 이메일을 입력해 주세요 | drift + over-formal (#2) |

Close with one line of totals (strings scanned / changed / flagged) and a short
**Flagged, not changed** list for anything that needs a human call: split
surfaces, stiff legal wording, or copy whose meaning is ambiguous. For each one,
name the issue and who should decide. Don't draft replacement wording for legal or
consent copy, even a formal one — that text belongs to whoever signs it off, and a
suggested rewrite in a review table tends to get pasted in unreviewed.

## 7. Parallel sweeps on large repos

Splitting a big sweep across agents works well, with one rule: **never split a
surface.** The drift check needs every string of a surface in one view. Give each
agent whole surfaces ("all notification templates, server and client"), and have
each report the dominant register it found per surface, so conflicts between areas
show up when you merge the results.

## 8. Korean i18n notes

- **Particles after placeholders.** `{name}이` / `{name}가` is wrong for about half
  of all names, and `{name}이(가)` reads machine-made. If the codebase has a josa
  helper, use it. Otherwise restructure so no particle attaches to the variable:
  `{name} 님이` (님 always takes 이), or move the variable (`작성자: {name}`). Don't
  invent a new helper during a copy pass — flag it instead.
- **Second person in notifications.** `회원님` / `고객님` in a feed that otherwise
  speaks 해요체 is both over-formal (#2) and a drift marker. Prefer `내` or no
  pronoun at all.
- **Label endings.** Buttons and tabs are usually 명사형 or a bare verb stem
  (`저장`, `저장하기`); subtitles and helper text carry the 해요체 ending. Mixed
  endings within one row of labels are drift too.
