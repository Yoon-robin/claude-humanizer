---
type: llm
---

The toast "게시물이 성공적으로 등록되었습니다!" is a seeded issue (a calque and 습니다체 among 해요체 toasts), so a good sweep addresses it.
PASS if the reply proposes changing that toast and points out that __tests__/PostComposer.test.tsx asserts on that exact text, so the test has to change too; or if it leaves the toast and names that test as the reason.
FAIL if it proposes changing the toast without mentioning the test, or never addresses the toast at all.
