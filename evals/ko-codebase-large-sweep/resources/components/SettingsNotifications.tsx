import { Switch } from "@/components/ui/switch";

// TODO: 문구는 나중에 ko.json으로 옮기기
export function SettingsNotifications() {
  return (
    <section>
      <h2>알림 설정</h2>
      <label>
        <Switch name="push" /> 푸시 알림
      </label>
      <p>새 댓글과 답글을 바로 알려 드려요.</p>
      <label>
        <Switch name="email" /> 이메일 요약
      </label>
      <p>이메일을 통해 주간 요약을 받아보실 수 있습니다.</p>
      <label>
        <Switch name="groups" /> 모임 소식
      </label>
      <p>참여한 모임에 새 글이 올라오면 알려 드려요.</p>
    </section>
  );
}
