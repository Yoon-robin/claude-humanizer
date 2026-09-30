# Codebase Sweeps — Humanizing a Product's UI Strings

Read this when the job is many strings across a codebase: locale files, JSX text,
notification and email templates, error messages. The tells are the families in
`SKILL.md`; what changes is the unit of judgment. In a mature product most strings
are fine, and most real problems are **register drift between neighbors**.

## Contents

1. [Inventory](#1-inventory)
2. [Group by surface](#2-group-by-surface)
3. [Set each surface's register](#3-set-each-surfaces-register)
4. [Diagnose and edit](#4-diagnose-and-edit)
5. [Report](#5-report)
6. [Large repos](#6-large-repos)
7. [Korean i18n notes](#7-korean-i18n-notes)

## 1. Inventory

- **Where copy lives:** locale files (`locales/**`, `messages/*.json`, `i18n/**`,
  `*.po`, `strings.xml`, `Localizable.strings`); JSX children and user-facing props
  (`placeholder`, `title`, `aria-label`, `alt`, `label`); toasts and alerts; server
  notification, push, email, and SMS templates.
- For Korean, `rg -n "[가-힣]" --glob '!**/*.test.*'` finds nearly everything.
- Skip what users never read: logs, developer errors, analytics names, enum values
  and keys, test fixtures, comments.

## 2. Group by surface

A surface is what a user sees together or in one flow: a notification family, a
form, an onboarding sequence, a row of buttons, an email. Group by experience, not
by file. A notification's server template and its in-app twin are one surface, and
one `ko.json` holds many surfaces.

## 3. Set each surface's register

Tally the speech level per surface (KO 해요체 / 합니다체 / 반말 / 명사형; EN
contractions, sentence vs. Title Case, warmth). The dominant one, usually the
voice of the newest strings, is the target.

- **Converge within a surface, never across.** A consistently formal surface, such
  as legal copy or an audit log, stays formal even when the app speaks 해요체.
- **No clear majority, or a style guide says otherwise?** Flag it as a product
  decision instead of picking a winner.

## 4. Diagnose and edit

- Ask of every string: does it carry a tell on its own, and does it drift from its
  surface? Expect "no" for most. Changing a small fraction of what you scanned is
  a healthy result; don't manufacture finds.
- Change only strings with a tell or drift, and leave the rest byte-identical.
- Keep placeholders, markup, and keys intact (see protected spans in `SKILL.md`).
- Respect the slot: buttons, tabs, and toasts truncate.
- Don't touch other locales unless asked, and don't rename keys or reformat files.
- **Search the repo for every string you change.** Tests, snapshots, and e2e
  scripts often assert on exact copy (`getByText("…")`). List each one that has to
  change with it.

## 5. Report

| Location | Before | After | Why |
|---|---|---|---|
| `messages/ko.json` → `dialog.logout` | 로그아웃하시겠습니까? | 로그아웃할까요? | drift — every other dialog is 해요체 |
| `LoginForm.tsx` placeholder | 이메일을 입력하여 주십시오 | 이메일을 입력해 주세요 | drift + over-formal (#2) |

Close with totals (scanned / changed / flagged) and a short **Flagged, not
changed** list: split surfaces, legal wording, ambiguous copy, each with who should
decide. Don't draft replacement wording for legal or consent copy; a suggestion in
a review table tends to get pasted in unreviewed.

## 6. Large repos

Split the work across agents by whole surfaces, never splitting one, and have each
report the register it found per surface so conflicts show up when you merge.

## 7. Korean i18n notes

- **Particles after placeholders.** `{name}이` / `{name}가` breaks for about half of
  all names, and `{name}이(가)` reads machine-made. Use the codebase's josa helper
  if it has one; otherwise restructure (`{name} 님이`, `작성자: {name}`). Particles
  that don't depend on 받침, such as `에`, `의`, `도`, `와 함께`, are fine. Don't
  invent a helper mid-pass; flag it.
- **`회원님` / `고객님`** in a 해요체 feed is over-formal and a drift marker. Prefer
  `내` or no pronoun.
- **Label endings.** Buttons and tabs are usually 명사형 or a verb stem (`저장`,
  `저장하기`); helper text carries the ending. Mixed forms in one row are drift.
