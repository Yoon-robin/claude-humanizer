import Link from "next/link";

export default function Landing() {
  return (
    <main>
      <section>
        <h1>질문과 답이 오가는 우리 학교의 작은 광장</h1>
        <p>질문하고 자료를 나누는 우리 학교 커뮤니티예요.</p>
        <Link href="/signup">학교 이메일로 시작하기</Link>
      </section>
      <section>
        <h2>주요 기능</h2>
        <ul>
          <li>게시판별로 질문하고 답해요.</li>
          <li>강의 자료를 올리고 내려받아요.</li>
          <li>관심사가 같은 사람끼리 모임을 만들어요.</li>
        </ul>
      </section>
      <section>
        <h2>규모는 작아도, 기록은 모두 진짜입니다</h2>
        <p>가입자 312명 · 게시글 1,480개</p>
      </section>
      <section>
        <h2>자주 묻는 질문</h2>
      </section>
    </main>
  );
}
