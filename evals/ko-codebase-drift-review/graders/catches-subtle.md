---
type: llm
weight: 2
---

Three issues are subtle and only show up with a surface-level, codebase-aware review:
A. notifications.reply "{name}이 내 댓글에 답글을 달았어요." attaches the particle 이 directly to the {name} placeholder (it breaks for names ending in a vowel) and differs from the "{name} 님이" pattern of every other notification.
B. dialog.deletePost.cancel "취소하기" mixes label endings with its sibling button "삭제" in the same row.
C. server/push.ts notifyNewComment body "${actor} 님이 회원님의 글 「${postTitle}」에 댓글을 남기셨습니다." is the push twin of an in-app notification and drifts from the 해요체 notification voice (회원님, 남기셨습니다).

PASS if the reply flags at least two of A, B, and C and proposes a fix for each one it flags that keeps the placeholders exactly ({name}, ${actor}, ${postTitle}).
FAIL if it flags fewer than two of them, or if a proposed fix drops or renames a placeholder.
