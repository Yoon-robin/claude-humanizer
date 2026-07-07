# [Language] — AI Tells & Fixes

Template for adding a new language catalog to the `humanizer` skill. Copy this to
`<language>.md` (lowercase English name, e.g. `japanese.md`, `spanish.md`), fill it
in, and the skill will load it automatically when it detects that language.

The universal five families live in `SKILL.md`; your job here is to make them
**concrete for this language** — the specific words, particles, structures, and
register system a native writer would notice. Keep entries as `❌ before → ✅ after`
pairs; examples do far more than abstract rules.

## What to cover

Adapt these to the language (some won't apply; add ones that are unique to it):

1. **Translation-ese / calques** — the structures imported from English (or from
   whatever language AI tends to "think" in) that a native writer wouldn't use.
   List the most common offenders with plain-native replacements.

2. **Over-formality, deference & cliché padding** — the hype words and empty
   politeness formulas specific to this language's marketing/business register.

3. **Flat rhythm** — how monotony shows up here (uniform endings, uniform length),
   and how native copy varies it. Note any sentence-ending or particle patterns
   that AI overuses.

4. **Structural excess** — signposting words, list reflexes, and formatting habits
   that read as machine-made in this language.

5. **Slick symmetrical parallelism** — the too-perfect balanced construction in
   this language, and how to break it.

6. **Register system (important):** describe how this language encodes
   formality/politeness (speech levels, honorifics, tu/vous, contractions …), so
   the skill knows what to hold constant. This is where languages differ most.

## Structure to follow

- Open with 2–3 sentences on this language's overall AI "fingerprint."
- A `## Contents` list if the file gets long (>150 lines).
- One `##` section per family, each with named entries and ❌/✅ pairs.
- A `## Quick swap table` for the highest-frequency fixes.
- At least one `## Worked example` — a full AI-sounding paragraph and its
  humanized rewrite, with a note on which tells were fixed and which protected
  spans were preserved.

Look at `korean.md` and `english.md` as finished references before writing yours.
