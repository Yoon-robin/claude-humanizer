"""Regression tests for the regex graders in evals/. Runs in CI, costs nothing.

Each case feeds a known-good or known-bad answer to a grader's pattern and checks
the verdict. The bad answers are real failure modes (swapped numbers, "이상" for
"넘었다", 반말 slipping into a formal notice); the good ones are shaped like real
passing outputs. When a grader changes, these cases show what it now lets through.

Usage:
    python .github/scripts/check_graders.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(rel: str):
    text = (ROOT / "evals" / rel).read_text(encoding="utf-8")
    pattern = re.search(r"^pattern: '(.*)'$", text, re.M).group(1)
    flags = re.M if re.search(r"^flags: .*m", text, re.M) else 0
    not_contains = bool(re.search(r"^match: not_contains$", text, re.M))
    return re.compile(pattern, flags), not_contains


def passes(rel: str, answer: str) -> bool:
    pattern, not_contains = load(rel)
    found = bool(pattern.search(answer))
    return not found if not_contains else found


FORMAL = "ko-formal-notice-keeps-register/graders/stays-formal.md"
BANMAL = "ko-banmal-brand-caption/graders/stays-banmal.md"
SLIDE = "ko-slide-titles/graders/keeps-names-numbers.md"
REPORT = "ko-report-titles/graders/keeps-facts-and-fine-titles.md"
PROPOSAL = "ko-proposal-titles/graders/keeps-facts-and-fine-titles.md"

FORMAL_OK = """[안내] 시스템 정기 점검

안녕하십니까. 운영팀입니다.
11월 2일(토) 오전 2시부터 6시까지 시스템 점검이 있습니다.
점검 중에는 서비스를 이용하실 수 없습니다. 이용에 참고해 주시기 바랍니다.
감사합니다."""
BANMAL_OK = """가을 신메뉴 나왔다.
고소한 밤에 부드러운 크림, 이 조합 장난 아니다.
10월 31일까지만 판매해."""
SLIDE_OK = """1. 스터디메이트
2. 공부할 친구를 찾는 일은 생각보다 어렵습니다
3. 시스템 구성 (게이트웨이 1대)
4. 기술 스택: React Native · Firebase
5. 매칭 수: 한 달 만에 540건 돌파
6. 평균 만족도 4.6점 (표본 적음)
7. 사용자 흐름: 과목 선택 → 친구 매칭
8. 팀 소개 (4명)
9. 다음 학기 계획"""
REPORT_OK = """1. 2026년 3분기 운영 보고
2. 매출과 비용이 함께 늘었습니다
3. 매출 4.2억 원 (전 분기 대비 약 18% 증가)
4. 세 지점 현황
5. 재방문 의향 82% (응답 37건)
6. 4분기 일정
7. 운영팀 · 마케팅팀 · 개발팀 조직도
8. 원두 가격이 최대 12% 오를 수 있습니다"""
PROPOSAL_OK = """1. 사내 도서 대여 서비스 개선안
2. 목차
3. 보유 도서 1,800권 · 지난달 대여 46건
4. 사용 흐름: 검색부터 반납까지 슬랙에서
5. 현재 화면과 바뀔 화면
6. 시범 운영 결과: 2주 만에 대여 약 3배
7. 설문 결과: 책을 빌리지 않은 이유
8. 추가 비용은 월 최대 5만 원입니다
9. 다음 단계"""


def paren_numbers(text: str) -> str:
    return re.sub(r"^(\d)\.", r"\1)", text, flags=re.M)


# (grader, answer, should pass, what it checks)
CASES = [
    (FORMAL, FORMAL_OK, True, "formal notice in 합니다체"),
    (FORMAL, FORMAL_OK + "\n점검 시간에는 접속하지 마.", False, "반말 imperative"),
    (FORMAL, FORMAL_OK + "\n점검 중에는 이용할 수 없어요  ", False, "해요체 with trailing spaces"),
    (FORMAL, FORMAL_OK + "\n점검한다.", False, "plain 한다체"),
    (BANMAL, BANMAL_OK, True, "반말 caption, including 아니다"),
    (BANMAL, BANMAL_OK + "\n밤과 크림 메뉴를 판매합니다.", False, "합니다체 line"),
    (BANMAL, BANMAL_OK + "\n10월 31일까지 팔아요", False, "해요체 without punctuation"),
    (BANMAL, "가을 신메뉴예요 — 고소한 밤과 부드러운 크림.", False, "해요체 before a dash"),
    (SLIDE, SLIDE_OK, True, "correct slide titles"),
    (SLIDE, paren_numbers(SLIDE_OK), True, "1) numbering"),
    (SLIDE, SLIDE_OK.replace("540건", "5400건"), False, "540 inflated to 5400"),
    (SLIDE, SLIDE_OK.replace("540건 돌파", "540건 이상"), False, "이상 (>=) for 넘었다 (>)"),
    (SLIDE, SLIDE_OK.replace("표본 적음", "표본 충분"), False, "small-sample caveat reversed"),
    (SLIDE, SLIDE_OK.replace("팀 소개 (4명)", "팀 소개"), False, "team size dropped"),
    (SLIDE, SLIDE_OK.replace("React Native · Firebase", "앱 · 서버") + "\n참고: React Native, Firebase", False, "names only outside slide 4"),
    (REPORT, REPORT_OK, True, "correct report titles"),
    (REPORT, REPORT_OK.replace("4.2억", "42억"), False, "4.2억 changed to 42억"),
    (REPORT, REPORT_OK.replace("최대 12% 오를 수 있습니다", "12% 오릅니다"), False, "possibility hardened"),
    (PROPOSAL, PROPOSAL_OK, True, "correct proposal titles"),
    (PROPOSAL, paren_numbers(PROPOSAL_OK), True, "1) numbering"),
    (PROPOSAL, PROPOSAL_OK.replace("보유 도서 1,800권 · 지난달 대여 46건", "지난달 도서 46권 · 대여 1,800건"), False, "numbers swapped between nouns"),
    (PROPOSAL, PROPOSAL_OK.replace("보유 도서 1,800권 · 지난달 대여 46건", "보유 도서와 대여 현황"), False, "numbers dropped for a label"),
]


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8")
    failed = 0
    for grader, answer, should_pass, what in CASES:
        ok = passes(grader, answer) == should_pass
        failed += not ok
        verdict = "pass" if should_pass else "fail"
        print(f"{'ok  ' if ok else 'FAIL'} {grader.split('/')[0]}: should {verdict} — {what}")
    print(f"grader cases: {len(CASES) - failed}/{len(CASES)} ok")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
