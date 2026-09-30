# Korean — Worked Examples

Companion to `korean.md` for the `humanizer` skill: full before/after pieces by
copy type. Read it for longer copy or when you're unsure how far a rewrite
should go. A short fix or a codebase sweep doesn't need it.

Realistic AI-drafted pieces, their humanized rewrites, and the specific tells
fixed. Use these to calibrate what "done" looks like per format — the target
register differs by context, and humanizing never means flattening everything to
one tone.

## Marketing / ad copy

Register: usually 명사형 종결 or 해요체. Punchy, rhythmic, benefit-first.

**Before (AI):**
> 저희 제품은 최고의 품질을 제공하는 완벽한 솔루션입니다. 가벼운 무게와 오래가는 배터리 등
> 다양한 기능들을 통해 당신의 일상을 더욱 특별하게 만들어 드립니다. 지금 바로 구매하세요!

**After (human):**
> 가벼워요. 배터리도 오래가고요.

Fixed: `최고의/완벽한/특별한` empty superlatives, `~을 제공하는`, `다양한 기능들`, `~을 통해`,
`당신의`, `지금 바로 ~하세요!` cliché, and flat rhythm → a short line and a trailing
`~고요`. The rewrite keeps only the source's two facts (가벼운 무게, 오래가는 배터리);
`최고의 품질` is cut rather than turned into a new claim.

---

## UI microcopy

Register: 해요체, short and functional. No hype, no padding. Clarity first, but
still warm and human — not robotic.

**Empty state — Before (AI):**
> 현재 표시할 수 있는 항목이 존재하지 않습니다. 새로운 항목을 추가하시기 바랍니다.

**After:**
> 아직 아무것도 없어요. 첫 항목을 추가해 보세요.

**Error toast — Before (AI):**
> 요청을 처리하는 과정에서 오류가 발생하였습니다. 잠시 후 다시 시도해 주시기 바랍니다.

**After:**
> 잠깐 문제가 생겼어요. 잠시 후 다시 시도해 주세요.

**Button / confirmation — Before (AI):**
> 정말로 이 항목을 삭제하시는 것이 맞으십니까?

**After:**
> 이 항목을 삭제할까요?

Fixed: `존재하지 않습니다`, `~하시기 바랍니다`, over-formal `~하였습니다`, redundant
`과정에서`, and needless deference → concise 해요체 that still sounds like a person.

---

## SNS / blog post

Register: 해요체 or 반말 by brand. Conversational, opinionated, rhythm-heavy.
Fragments and questions welcome.

**Before (AI):**
> 오늘은 여러분께 저희의 새로운 카페를 소개해 드리고자 합니다. 저희 카페는 매주 직접
> 로스팅한 신선한 원두를 사용할 뿐만 아니라 넉넉한 좌석과 아늑한 분위기도 제공합니다.
> 많은 관심 부탁드립니다!

**After:**
> 새로 문 열었어요. 매주 직접 볶은 원두를 쓰고, 자리도 넉넉해요.
> 조용히 앉아 있기 좋은 곳이에요. 놀러 오세요 :)

Fixed: `여러분께`, `~하고자 합니다`, `~뿐만 아니라 ~도`, `~을 제공합니다`, `많은 관심
부탁드립니다` → warm, specific, varied rhythm. The specifics (매주 직접 볶은 원두, 넉넉한
좌석) are the source's own; the rewrite adds no backstory. Emoji kept minimal and only
where a casual brand voice supports it — not as proof-of-humanity.

---

## Email / newsletter

Register: 해요체 or 습니다체 depending on formality. Warmer than a notice, more
structured than SNS. The trap here is the mechanical greeting-body-closing arc.

**Before (AI):**
> 안녕하세요, 고객님. 항상 저희 서비스를 아껴 주셔서 진심으로 감사의 말씀을 드립니다. 이번에 저희는
> 앱에서 바로 예약할 수 있는 새로운 기능을 출시하게 되었음을 알려 드리고자 합니다.
> 이번 주부터 해당 기능을 통해 전화나 대기 없이 더욱 편리하게 서비스를 이용하실 수
> 있습니다. 앞으로도 많은 관심 부탁드립니다.

**After:**
> 안녕하세요, 고객님. 늘 이용해 주셔서 감사합니다.
> 이번 주부터 앱에서 바로 예약하실 수 있어요. 전화하거나 기다리지 않아도 됩니다.

Fixed: `~게 되었음을 알려 드리고자 합니다`, `~을 통해`, `~하실 수 있습니다`, `많은 관심
부탁드립니다`, and the rigid greeting-body-closing arc → a short, direct note. The
formality holds: it stays a polite customer email, blending 합니다체 and 해요체 the way
a real writer would instead of dropping wholesale into 해요체. `고객님` stays too; swapping
in a name variable would change the template, not the tone.

---

## Presentation slide titles (발표 슬라이드 제목)

Register: labels (명사형·개조식) for structural and data slides; a plain message
title only where a slide lands one claim.

Context: a 21-slide deck presenting a student community site. The AI draft gave
every slide a full-sentence title with a hook. The author kept the labels below.

| Slide | ❌ AI draft | ✅ Kept | Tell fixed |
|---|---|---|---|
| Usage data | 숫자는 작지만 전부 실제 기록입니다 | 실제 사용 기록 | `~지만` contrast |
| User flow | 한 번 가입하면, 매일 홈에서 시작합니다 | 사용 흐름 | comma-split title |
| Tech stack | 왼쪽은 프런트엔드, 오른쪽은 백엔드입니다 | 프런트엔드 · 백엔드 구성 | left/right mirror |
| Architecture | 서버 한 대에 네 가지 입구가 모입니다 | 시스템 아키텍처 | metaphor |
| Why we built it | 우리 학교 사람들이 머무는 곳 하나를 만들기로 했습니다 | 우리 학교 사람들이 모이는 곳을 만들기로 했습니다 | poetic verb (머무는) |

The last row stays a sentence because that slide's job is to state the reason for
the project; only the poetic verb goes. The labels don't invent anything: each
names what the slide already shows.

---

## Register drift (product & codebase copy)

Register: whatever the *surrounding* copy already uses. This is the tell that only
appears in context — a string that's fine on its own but out of step with its
neighbors. It's the dominant tell in mature codebases, where old strings keep an
old voice while newer ones move on.

Context: a notification list where recent items are all 해요체 ("도전을 받아들였어요",
"제출했어요"), but one legacy notification stayed 습니다체 with over-formal 2nd person.

**Before (legacy drift):**
> OO 님이 글의 회원님 댓글에 답글을 남겼습니다.

**After:**
> OO 님이 글에 남긴 내 댓글에 답글을 달았어요.

Fixed: converged to the neighbors' 해요체 (`남겼습니다` → `달았어요`) and dropped the
over-formal `회원님` (#2). This overlaps with #2 (over-politeness) and #3 (flat
rhythm) — but the reason this 습니다체 is a tell isn't the sentence itself; it's that
every notification around it is 해요체. In isolation you'd leave it; in context you
fix it. The move is consistency recovery toward the surface's own register, not
casualizing.
