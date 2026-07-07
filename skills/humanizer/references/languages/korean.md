# Korean — AI Tells, Fixes & Examples

Language-specific reference for the `humanizer` skill; load it when the target
language is Korean. Each entry names a tell, explains *why* it reads as
machine-made, and gives before → after pairs. Work from these patterns, but
always let the read-aloud test have the final word — context can make any "rule"
the wrong call.

## Contents

1. [번역투 · 직역체 — Translation-ese](#1-번역투--직역체--translation-ese)
2. [과한 정중함 · 상투어 — Over-politeness & clichés](#2-과한-정중함--상투어--over-politeness--clichés)
3. [밋밋한 리듬 — Flat rhythm](#3-밋밋한-리듬--flat-rhythm)
4. [구조적 과잉 — Structural excess](#4-구조적-과잉--structural-excess)
5. [Quick swap table](#5-quick-swap-table)
6. [Worked examples by copy type](#6-worked-examples-by-copy-type)

---

## 1. 번역투 · 직역체 — Translation-ese

These are structures imported from English word order and grammar. Each is
correct Korean, but a native writer wouldn't reach for it.

**`~에 대해` / `~에 관하여` (about X).** English "about" attaches to everything;
Korean usually takes a plain particle.
- ❌ 건강에 대해 생각해 보세요.
- ✅ 건강을 생각해 보세요.
- ❌ 이 제품에 대한 정보를 확인하세요.
- ✅ 이 제품 정보를 확인하세요.

**`~을/를 통해` (through / via) for simple means.** Use `~(으)로`.
- ❌ 앱을 통해 간편하게 주문하세요.
- ✅ 앱으로 간편하게 주문하세요.
- ❌ 이메일을 통해 안내드리겠습니다.
- ✅ 이메일로 안내드리겠습니다.

**`~을 제공합니다` / `~을 가지고 있습니다` (provides / has).** Direct calques of
English verbs. Korean prefers `있다`, `~ㅂ니다`, or a plain verb.
- ❌ 다양한 기능을 제공합니다.
- ✅ 기능이 다양합니다. / 여러 기능을 쓸 수 있어요.
- ❌ 이 노트북은 긴 배터리 수명을 가지고 있습니다.
- ✅ 이 노트북은 배터리가 오래갑니다.

**Overused `~들` (explicit plurals).** Korean marks plurality by context; piling
on `~들` is a translation reflex.
- ❌ 사용자들은 다양한 혜택들을 받을 수 있습니다.
- ✅ 사용자는 다양한 혜택을 받을 수 있어요.

**`당신` (you).** Almost never used to address a reader in real Korean copy —
it sounds like a dubbed film. Drop it, use the service/brand relationship, or
address by role.
- ❌ 당신의 하루를 더 특별하게 만들어 드립니다.
- ✅ 오늘 하루가 조금 특별해집니다. / 당신의 → (그냥 생략) 하루를 바꿔요.

**Chained `~할 수 있습니다` as the default ending.** When every sentence ends in
"can/able to," it flatlines. Vary with direct statements or imperatives.
- ❌ 저장할 수 있습니다. 공유할 수 있습니다. 편집할 수 있습니다.
- ✅ 저장하고, 공유하고, 바로 편집하세요.

**Double passives — `~되어집니다`, `제공되어집니다`.** Grammatically redundant and
a hallmark of machine output.
- ❌ 자동으로 저장되어집니다.
- ✅ 자동으로 저장됩니다.

**`그것은 / 이것은 ~입니다` (it is / this is) as a sentence opener.** English
dummy subjects don't carry into natural Korean.
- ❌ 그것은 우리가 가장 자신 있는 기능입니다.
- ✅ 저희가 가장 자신 있는 기능이에요.

**`다양한` overuse.** AI reaches for 다양한 (various) before every noun. Once is
fine; as a default modifier it's filler — cut it or name the actual things.
- ❌ 다양한 기능과 다양한 혜택을 다양한 방식으로 제공합니다.
- ✅ 필요한 기능은 다 있고, 혜택도 쏠쏠해요.

**`및` / `등` as default connectors.** 및 is stiff 문어체 that rarely belongs in copy;
`등` trailing every list is a report reflex. Use `~와/과`, `-고`, or just a comma.
- ❌ 예약 및 결제, 알림 등의 기능을 지원합니다.
- ✅ 예약하고 결제하고, 알림까지 챙겨 줘요.

**`보다 더 ~` (comparative calque).** `보다` as a bare "more" adverb is translationese.
- ❌ 보다 나은 경험을 제공하기 위해.
- ✅ 더 나은 경험을 위해. / 좀 더 낫게 만들려고.

**Hype verbs — `~을 자랑합니다` / `~로 유명합니다` / `~을 선사합니다`.** Boast calques.
- ❌ 압도적인 성능을 자랑합니다. / 잊지 못할 경험을 선사합니다.
- ✅ 성능은 확실해요. / 한번 쓰면 계속 쓰게 돼요.

---

## 2. 과한 정중함 · 상투어 — Over-politeness & clichés

Padding that signals deference or hype but carries no information. Strip it; what
remains is usually stronger.

**Deference padding.**
- ❌ 많은 관심과 사랑 부탁드립니다.
- ✅ (대개 삭제) — or a concrete ask: 다음 업데이트도 기대해 주세요.
- ❌ 꼭 확인하시기 바랍니다.
- ✅ 꼭 확인해 주세요. / 확인해 보세요.

**`여러분` on repeat.** Occasional is fine; every paragraph is a tell.
- ❌ 여러분, 이번 이벤트에 여러분의 많은 참여 바랍니다.
- ✅ 이번 이벤트, 놓치지 마세요. (or just address the reader once)

**Empty superlatives — `완벽한 / 특별한 / 최고의 / 혁신적인`.** They describe nothing.
Replace with a concrete benefit or cut.
- ❌ 완벽한 경험을 선사하는 특별한 제품입니다.
- ✅ 손에 딱 감기는 그립, 하루 종일 가는 배터리.

**Ad-cliché imperatives.** `지금 바로 ~하세요!` / `놓치지 마세요!` / `서두르세요!` read
as template filler. Keep at most one, and only if it earns its place.
- ❌ 지금 바로 신청하세요! 이 기회를 놓치지 마세요!
- ✅ 신청은 오늘까지예요.

**Forced friendliness.** `함께 ~해요`, `~하는 건 어떨까요?` when nothing warrants the
warmth.
- ❌ 우리 함께 건강한 습관을 만들어 가는 건 어떨까요?
- ✅ 건강한 습관, 오늘부터 시작해요.

---

## 3. 밋밋한 리듬 — Flat rhythm

The single most reliable AI signature. Even when every word is fine, uniform
sentence length and repeated endings feel synthetic. Human copy varies on
purpose.

**Uniform endings.** Every line `~습니다`, or every line `~요`.
- ❌ 저희는 신선한 재료만 씁니다. 매일 아침 직접 굽습니다. 정성을 다합니다.
- ✅ 신선한 재료만 씁니다. 매일 아침, 직접 굽고요. 그게 저희 방식이에요.

Note the ✅ blends 씁니다 / 굽고요 / 방식이에요. Mixing 합니다체 and 해요체 within polite
copy is a *fix*, not a new problem — real writers do it and it reads warm. Keep
the politeness level steady; vary the endings freely.

**Uniform length.** Three medium sentences in a row → break the pattern with a
short one or a fragment.
- ❌ 이 앱은 일정을 관리해 줍니다. 알림도 보내 줍니다. 통계도 제공합니다.
- ✅ 일정을 관리하고, 알림을 보내요. 통계는 덤. (fragment lands the beat)

**No fragments or questions.** Real copy uses both.
- ❌ 당신의 취향에 맞는 음악을 추천해 드립니다.
- ✅ 취향 저격 플레이리스트. 오늘은 뭐 들을래요?

**Technique:** after drafting, deliberately cut one sentence in half and let one
line end on a noun. Rhythm is created by contrast, not by any single line.

**Reach for a wider ending palette.** AI copy defaults to `~습니다` / `~요` and
nothing else. Human Korean writing pulls from a much bigger set — deploy these to
break monotony (register-appropriate):
- **명사형 종결** — 하루가 조용해지는 경험. / 충전 걱정 없는 30시간.
- **`~거든요`** (offering a reason, warm) — 저희가 좀 까다롭거든요.
- **`~더라고요`** (shared discovery) — 써 보니 확실히 다르더라고요.
- **`~잖아요`** (assumed agreement) — 매일 쓰는 거잖아요.
- **`~죠` / `~하죠`** (soft assertion) — 이 정도면 충분하죠.
- **`~고요` / `~고` 연결** to trail warmly — 알림도 새로 들어왔고요.
These aren't slang; they're how real people write. One or two per piece, matched
to the brand voice, does more than any single clever line.

---

## 4. 구조적 과잉 — Structural excess

English-essay scaffolding forced onto copy that should just flow.

**Bullets where prose belongs.** Short marketing/blog copy rarely needs lists.
- ❌
  ```
  이 제품의 장점:
  - 가볍습니다
  - 튼튼합니다
  - 저렴합니다
  ```
- ✅ 가볍고 튼튼한데, 가격까지 착해요.

**Ordinal signposting.** `첫째, 둘째, 셋째` / `먼저 ~ 다음으로 ~ 마지막으로` in a
paragraph that doesn't need enumeration.
- ❌ 첫째, 사용이 간편합니다. 둘째, 디자인이 예쁩니다. 셋째, 가격이 좋습니다.
- ✅ 쓰기 쉽고, 예쁘고, 가격도 좋아요.

**Rigid `~뿐만 아니라 ~도` parallelism.** Fine once; mechanical when it's the only
connective.
- ❌ 성능이 좋을 뿐만 아니라 디자인도 좋습니다.
- ✅ 성능도 디자인도 잡았어요.

**Slick symmetrical 대구 (too-perfect parallelism).** A flawlessly balanced,
antithetical line looks polished but reads as manufactured cleverness — the move
AI and lazy copywriters reach for, not how a person actually talks. One
immaculate parallel is a tell. Break the symmetry, or let one side go plain. Note
the fixes below are *not* just another tidy 대구.
- ❌ 소리는 지우고, 하루는 채우고.
- ✅ 소음을 지우면, 하루가 조용해져요.
- ❌ 일할 땐 완벽하게, 쉴 땐 확실하게.
- ✅ 집중해야 할 땐 확실히 잡아 줘요. 쉴 땐 그냥 편하게.

**Three-part intro-body-conclusion in miniature.** AI loves wrapping even a
two-line message in a tidy arc. Cut to the point.
- ❌ 안녕하세요. 오늘은 새로운 소식을 전해 드리려 합니다. 바로 신제품 출시 소식입니다.
- ✅ 새 제품이 나왔어요.

---

## 5. Quick swap table

| ❌ AI-ish | ✅ Natural | Note |
|---|---|---|
| ~에 대해 생각하다 | ~을 생각하다 | drop the calque |
| ~을 통해 | ~(으)로 | simple means |
| ~을 제공합니다 | ~이 있어요 / ~할 수 있어요 | de-calque "provide" |
| ~을 가지고 있습니다 | ~이 있습니다 | de-calque "have" |
| 사용자들, 혜택들 | 사용자, 혜택 | drop redundant ~들 |
| 당신 | (생략) / 역할·관계로 | readers aren't 당신 |
| ~되어집니다 | ~됩니다 | kill double passive |
| 많은 관심 부탁드립니다 | (삭제) / 구체적 요청 | remove deference padding |
| 완벽한 / 특별한 / 최고의 | 구체적 혜택으로 교체 | superlatives say nothing |
| 지금 바로 ~하세요! | 한 번만, 꼭 필요할 때 | limit ad clichés |
| 첫째, 둘째, 셋째 | 자연스러운 나열 | drop ordinal scaffolding |
| ~뿐만 아니라 ~도 | ~도 ~도 | loosen rigid parallelism |
| 다양한 (반복) | (삭제) / 실제 대상 명시 | filler modifier |
| 및 / ~ 등 | ~와/과, -고, 쉼표 | stiff 문어체 connectors |
| 보다 나은 | 더 나은 | comparative calque |
| ~을 자랑합니다 / 선사합니다 | 구체 서술로 | boast calques |


---

## 6. Worked examples by copy type

Realistic AI-drafted pieces, their humanized rewrites, and the specific tells
fixed. Use these to calibrate what "done" looks like per format — the target
register differs by context, and humanizing never means flattening everything to
one tone.

### Marketing / ad copy

Register: usually 명사형 종결 or 해요체. Punchy, rhythmic, benefit-first.

**Before (AI):**
> 저희 제품은 최고의 품질을 제공하는 완벽한 솔루션입니다. 다양한 기능들을 통해 당신의
> 일상을 더욱 특별하게 만들어 드립니다. 지금 바로 구매하세요!

**After (human):**
> 매일 쓰는 물건일수록, 잘 만든 게 티가 나요.
> 손에 감기는 무게, 오래가는 배터리. 하나면 충분합니다.

Fixed: `최고의/완벽한/특별한` empty superlatives, `~을 제공하는`, `기능들`, `~을 통해`,
`당신의`, `지금 바로 ~하세요!` cliché, and flat rhythm → varied lines with a fragment.

---

### UI microcopy

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

### SNS / blog post

Register: 해요체 or 반말 by brand. Conversational, opinionated, rhythm-heavy.
Fragments and questions welcome.

**Before (AI):**
> 오늘은 여러분께 저희의 새로운 카페를 소개해 드리고자 합니다. 저희 카페는 신선한 원두를
> 사용할 뿐만 아니라 아늑한 분위기도 제공합니다. 많은 관심 부탁드립니다!

**After:**
> 드디어 문 열었어요. 우리 동네에 이런 카페 하나쯤 있었으면 했거든요.
> 원두는 매주 직접 볶고, 자리는 넉넉하게. 조용히 앉아 있기 좋은 곳이에요.
> 놀러 오세요 :)

Fixed: `여러분께`, `~하고자 합니다`, `~뿐만 아니라 ~도`, `~을 제공합니다`, `많은 관심
부탁드립니다` → warm, specific, varied rhythm. (Emoji kept minimal and only where a
casual brand voice supports it — not as proof-of-humanity.)

---

### Email / newsletter

Register: 해요체 or 습니다체 depending on formality. Warmer than a notice, more
structured than SNS. The trap here is the mechanical greeting-body-closing arc.

**Before (AI):**
> 안녕하세요, 고객님. 저희 서비스를 이용해 주셔서 진심으로 감사드립니다. 이번에 저희는
> 새로운 기능을 출시하게 되었음을 알려 드리고자 합니다. 해당 기능을 통해 더욱 편리하게
> 서비스를 이용하실 수 있습니다. 앞으로도 많은 관심 부탁드립니다.

**After:**
> 안녕하세요, OO님.
> 오래 기다리셨죠? 이번 주부터 예약을 앱에서 바로 할 수 있어요.
> 전화도, 대기도 없이 몇 번의 탭이면 끝나요. 한번 써 보시고 어떤지 알려 주세요.

Fixed: generic `고객님`, `~게 되었음을 알려 드리고자 합니다`, `~을 통해`, `~하실 수 있습니다`,
`많은 관심 부탁드립니다`, and the rigid three-beat arc → a direct, personal note with
a real ask. Register stays polite (해요체) — humanized, not casualized.

---

### Register drift (product & codebase copy)

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

---

### Calibration notes

- **The formal cases still read formal.** Look at the email — it never drops into
  slang. Humanizing a 습니다체/해요체 piece means removing translation-ese and
  padding, not lowering the register.
- **Specificity replaces hype.** Almost every fix swaps an empty superlative for a
  concrete detail (매주 직접 볶는 원두, 몇 번의 탭). Concreteness is what makes copy
  sound like a person who actually knows the product.
- **Rhythm is the finish line.** In every "after," sentence lengths vary and at
  least one line lands short. If your rewrite is all medium sentences, it isn't
  done.
- **Mostly-clean is the expected result in tidy copy.** In a codebase or product
  that's already been cleaned once, most strings you scan will have no tell, and
  the real ones are a small minority — often register drift (above), not classic
  translation-ese. Don't manufacture finds to feel productive; that's the
  no-overcorrect rule again. In one large production scan the classic 번역투
  (`~을 통해` / `제공합니다` / `되어집니다` / `하시기 바랍니다`) appeared zero times across the
  whole component tree — the real work was a handful of drift fixes.
