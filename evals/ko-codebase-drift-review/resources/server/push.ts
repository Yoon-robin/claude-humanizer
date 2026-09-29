import { sendPush } from "./fcm";

// 푸시 전송이 실패하면 최대 3번까지 다시 보낸다
const MAX_RETRIES = 3;

export async function notifyNewComment(userId: string, actor: string, postTitle: string) {
  await sendPush(
    userId,
    {
      title: "새 댓글",
      body: `${actor} 님이 회원님의 글 「${postTitle}」에 댓글을 남기셨습니다.`,
    },
    { retries: MAX_RETRIES },
  );
}

export async function notifyNewFollower(userId: string, actor: string) {
  await sendPush(
    userId,
    {
      title: "새 팔로워",
      body: `${actor} 님이 나를 팔로우했어요.`,
    },
    { retries: MAX_RETRIES },
  );
}
