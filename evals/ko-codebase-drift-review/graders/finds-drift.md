---
type: llm
weight: 2
---

Five strings drift from the 해요체 voice of their surface in an obvious way:
1. notifications.comment: "{name} 님이 회원님의 게시글에 댓글을 작성하였습니다."
2. notifications.badge: "새로운 배지를 획득하셨습니다."
3. admin.banners: "메인 배너를 등록하고 관리합니다."
4. emptyState.saved: "현재 저장된 항목이 존재하지 않습니다."
5. the 4th onboarding step body: "원하시는 알림만 선택하여 받으실 수 있습니다."

PASS if the reply proposes a rewrite for at least four of these five, and each proposed rewrite is natural 해요체 that keeps the meaning (for example, emptyState.saved still talks about saved items, not narrowed to "글").
FAIL if it proposes rewrites for three or fewer of them, or if its rewrites change the meaning.
