# 실험 자료

CHANGELOG에 적은 측정을 다시 확인할 수 있도록 입력, 출력, 채점 스크립트, 평가 기록을 그대로 둬요.
여기 있는 파일은 플러그인 설치에 포함되지 않아요.

공통 조건
- 생성: Claude Code 서브에이전트(Claude Opus 5.5). 조건마다 2회.
- 스킬 조건: Skill 도구를 금지하고 저장소의 `SKILL.md`를 직접 읽게 했어요. 설치된 다른 버전이 끼어들지 않게 하려는 거예요.
- 한 문장 조건(B): Skill 도구와 파일 읽기 금지. 지침은 "고칠 때 이름, 숫자와 그 단서(기간·범위·조건), 원래 말투는 그대로 지키고, 꼭 필요한 만큼만 고쳐."
- 없음 조건(C): Skill 도구와 파일 읽기 금지. 도구 호출이 1회(출력 쓰기)인지 확인했어요.
- 토큰: 서브에이전트 한 번 실행 전체. 빈 실행만으로 약 52k가 들어요.

## 2026-10-13-titles (v1.6.0, v1.7.0)

슬라이드 제목 덱 세 개. 덱1은 `evals/ko-slide-titles`와 같은 입력이라 개발용이고, 덱2·덱3은 그때 새로 만든 덱이에요.
파일 이름은 `<덱>_<조건>_<회차>.md`예요. A는 v1.6 스킬, K는 v1.7 + `korean.md` 제목 절, N은 v1.7 `SKILL.md`만이에요.

```bash
python experiments/2026-10-13-titles/grade_exp.py experiments/2026-10-13-titles/out
```

채점 기준은 v1.7 시점 그대로예요. 그때는 `540건 이상`도 통과로 셌는데, v1.8부터 "넘었다"는 `이상`이 아니라 `돌파`·`초과`로 봐요.

## 2026-10-13-long-copy (v1.7.0)

긴 글 세 편(`in/`): L1 서점 뉴스레터(합니다체), L2 앱 업데이트 공지(해요체), L3 사내 공지 메일(격식체).
조건: A 스킬 전체, S `SKILL.md`만(참조 파일 열지 않기), B 한 문장, C 없음. 출력은 `out/`.

- `grade_long.py`: 정규식 사실 체크, 심은 티, 원문 유사도, 토큰(`tokens.txt`). "사실 유지"는 지정한 체크 항목 통과일 뿐, 목적이나 강조 같은 전체 의미 보존까지 보진 않아요.
- `build_judge.py`: GPT-6 블라인드 평가 프롬프트를 만들어요. 글마다 8개 출력을 무작위 이름(R1~R8)으로 두 번 섞어요. `*_key.json`이 이름과 조건의 대응표예요.
- `judge/*_out.json`: `codex exec -m gpt-6-astra -c model_reasoning_effort='"high"' -s read-only`의 원본 응답.
- `agg_judge.py`: 대응표로 조건을 되살려 점수와 순위를 모아요.

```bash
python experiments/2026-10-13-long-copy/grade_long.py experiments/2026-10-13-long-copy/out
python experiments/2026-10-13-long-copy/agg_judge.py experiments/2026-10-13-long-copy/judge
```
