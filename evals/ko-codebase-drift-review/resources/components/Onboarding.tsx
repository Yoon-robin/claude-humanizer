import { Button } from "@/components/ui/button";
import { saveStep } from "@/lib/onboarding";

const STEPS = [
  { title: "관심사 고르기", body: "좋아하는 주제를 고르면 피드가 알아서 채워져요." },
  { title: "프로필 꾸미기", body: "사진 한 장이면 친구들이 금방 알아봐요." },
  { title: "첫 글 올리기", body: "거창하지 않아도 돼요. 오늘 있었던 일이면 충분해요." },
  { title: "알림 설정하기", body: "원하시는 알림만 선택하여 받으실 수 있습니다." },
];

type Props = { step: number; onNext: () => void; onSkip: () => void };

export function Onboarding({ step, onNext, onSkip }: Props) {
  async function persist() {
    try {
      await saveStep(step);
    } catch (err) {
      console.error("[Onboarding] 단계 저장 실패", err);
    }
  }

  const current = STEPS[step];

  return (
    <section>
      <h2>{current.title}</h2>
      <p>{current.body}</p>
      <Button variant="ghost" onClick={onSkip}>
        건너뛰기
      </Button>
      <Button
        onClick={async () => {
          await persist();
          onNext();
        }}
      >
        다음
      </Button>
    </section>
  );
}
