import { sendPush } from "./fcm";
import { logger } from "./logger";

// 푸시 문구는 앱 안 알림(messages/ko.json의 notifications)과 맞춰 둘 것
export async function notifyLike(userId: string, actor: string) {
  await sendPush(userId, {
    title: "좋아요",
    body: `${actor} 님께서 회원님의 게시물에 좋아요를 누르셨습니다.`,
  });
}

export async function notifyComment(userId: string, actor: string) {
  await sendPush(userId, {
    title: "새 댓글",
    body: `${actor} 님이 내 글에 댓글을 달았어요.`,
  });
}

export async function notifyGroupInvite(userId: string, actor: string, group: string) {
  try {
    await sendPush(userId, {
      title: "모임 초대",
      body: `${actor} 님이 ${group} 모임에 초대했어요.`,
    });
  } catch (err) {
    logger.warn("모임 초대 푸시 전송 실패", { userId, err });
  }
}
