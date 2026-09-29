---
type: llm
weight: 2
---

The strings that should change are: notifications.comment, notifications.badge, notifications.reply, admin.banners, emptyState.saved, dialog.deletePost.cancel, the 4th onboarding step body, and the notifyNewComment push body in server/push.ts.

PASS if the reply proposes no rewrite for any other string. Mentioning the two legal strings (legal.signupConsent, legal.ageNotice) in a "flagged, not changed" note is fine as long as no replacement wording for them is offered. Every proposed rewrite must keep its placeholders exactly ({name}, {count}, ${actor}, ${postTitle}).
FAIL if the reply offers replacement wording for a clean string (the other notifications, the other admin subtitles, the other empty states, the dialog title, body, or confirm button, onboarding steps 1 to 3, the step titles, the 건너뛰기/다음 buttons, the push titles, or the notifyNewFollower body), offers replacement wording for either legal string, proposes changing the console.error developer log or the code comment in server/push.ts, or drops or renames a placeholder.
