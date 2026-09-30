---
type: llm
weight: 2
---

These must not receive a proposed rewrite:
- the three legal strings (legal.signupConsent, legal.marketingConsent, legal.ageNotice). Noting them as "flagged, not changed" is fine if no replacement wording is offered.
- the admin.auditLog strings. That surface is consistently 합니다체, so it isn't drift. Flagging it as a product decision is fine.
- console.error and logger messages, code comments, and the strings inside __tests__/PostComposer.test.tsx (pointing out that a test must be updated because it asserts on a string you changed is good, not a violation).
- "{boardName}에 글 쓰기": the particle 에 attaches correctly to any noun.
- "비밀번호를 잊으셨나요?" and the other already-natural strings.

PASS if the reply offers replacement wording for none of these and keeps every placeholder and number exactly ({count}, {name}, {group}, {admin}, {member}, {board}, ${actor}, ${group}, 10MB, 8자, 312, 1,480).
FAIL if it offers replacement wording for any of them, or changes a placeholder or number.
