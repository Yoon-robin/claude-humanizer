export function welcomeEmail(name: string) {
  return {
    subject: `${name} 님, ITCS 커넥트에 오신 걸 환영해요`,
    body: [
      `반가워요, ${name} 님!`,
      "귀하의 계정이 성공적으로 생성되었음을 알려드립니다.",
      "먼저 프로필을 채우고 관심 있는 모임을 찾아보세요.",
      "궁금한 점은 이 메일에 답장해 주시면 돼요.",
    ].join("\n\n"),
  };
}
