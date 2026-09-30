---
type: llm
weight: 2
---

Fourteen issues are seeded in the fixture:
1. messages/ko.json notifications.commentReply — "{name} 님이 회원님의 댓글에 답글을 작성하였습니다." (습니다체 and 회원님 in a 해요체 feed)
2. messages/ko.json notifications.mention — "{name}가 나를 언급했어요." (particle glued to the placeholder, and no 님 unlike every other notification)
3. messages/ko.json admin.subtitle.reports — "신고 내역을 검토하고 처리합니다." (the only 합니다체 admin subtitle)
4. messages/ko.json emptyState.bookmarks — "현재 북마크된 게시물이 존재하지 않습니다." (translation-ese, drifts from the 해요체 empty states)
5. messages/ko.json errors.upload — "파일을 업로드하는 과정에서 오류가 발생하였습니다. 다시 시도하여 주시기 바랍니다." (stiff, drifts from the 해요체 errors)
6. messages/ko.json dialog.leaveGroup.title — "이 모임에서 정말로 나가시겠습니까?" (the other dialog titles are ~할까요?)
7. messages/ko.json onboarding.step3 — "관심 있는 태그를 선택하여 맞춤 피드를 받아보실 수 있습니다." (the other steps are 해요체)
8. components/SettingsNotifications.tsx — "이메일을 통해 주간 요약을 받아보실 수 있습니다." (~을 통해 and 습니다체 among 해요체 helper texts)
9. app/(marketing)/page.tsx h1 — "질문과 답이 오가는 우리 학교의 작은 광장" (decorative metaphor headline)
10. app/(marketing)/page.tsx h2 — "규모는 작아도, 기록은 모두 진짜입니다" (contrast, comma-split section title; the other section titles are labels)
11. components/Header.tsx aria-label — "알림 목록을 열기 위한 버튼입니다" (verbose, translation-ese; the other aria-labels are short like "메뉴 열기")
12. components/PostComposer.tsx toast — "게시물이 성공적으로 등록되었습니다!" ("성공적으로" calque and 습니다체 among 해요체 toasts)
13. emails/welcome.ts — "귀하의 계정이 성공적으로 생성되었음을 알려드립니다." (stiff notice line inside a 해요체 welcome email)
14. server/notify.ts notifyLike body — "${actor} 님께서 회원님의 게시물에 좋아요를 누르셨습니다." (drifts from its in-app twin and the other push bodies)

PASS if the reply proposes a rewrite for at least 11 of the 14, each rewrite is natural Korean in the register of its surface, keeps the meaning, and keeps every placeholder exactly ({name}, ${actor}).
FAIL if it proposes rewrites for 10 or fewer, or a rewrite changes the meaning or drops or renames a placeholder.
