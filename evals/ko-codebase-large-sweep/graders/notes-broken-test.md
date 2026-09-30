---
type: llm
---

PASS if the reply points out that __tests__/PostComposer.test.tsx asserts on the exact toast text "게시물이 성공적으로 등록되었습니다!", so changing that toast means updating the test.
FAIL if it proposes changing that toast without mentioning the test.
