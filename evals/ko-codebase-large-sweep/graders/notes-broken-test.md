---
type: llm
---

PASS if the reply doesn't propose changing the toast "게시물이 성공적으로 등록되었습니다!", or if it does and points out that __tests__/PostComposer.test.tsx asserts on that exact text, so the test has to change too.
FAIL if it proposes changing that toast without mentioning the test.
