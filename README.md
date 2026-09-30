# claude-humanizer

[English](README.en.md)

AI 티가 나는 카피를 사람이 쓴 글처럼 다듬어 주는 Claude Code 플러그인이에요.
한국어와 영어는 물론, 어떤 언어에서든 쓸 수 있어요.

AI가 쓴 글은 언어가 달라도 닮은 데가 있어요. 문법은 맞는데 읽으면 생기가 없죠.
겉으로 드러나는 티는 언어마다 달라요. 영어는 em-dash와 "delve", "it's not just X,
it's Y" 같은 표현을 남발하고, 한국어는 번역투와 끝없이 이어지는 `~습니다`에 기대요.
그래도 밑바닥에 있는 문제는 같아요. `humanizer` 스킬은 이런 티를 걷어 내면서 원래
뜻과 말투, 브랜드 목소리는 그대로 지켜요.

## 설치

Claude Code 안에서:

```text
/plugin marketplace add Yoon-robin/claude-humanizer
/plugin install humanizer@claude-humanizer
```

터미널에서 설치해도 돼요:

```bash
claude plugin marketplace add Yoon-robin/claude-humanizer
claude plugin install humanizer@claude-humanizer
```

새 세션을 열면 바로 쓸 수 있어요. 카피를 쓰거나 번역하거나 다듬을 때, 또는
"자연스럽게 고쳐줘", "AI 티 안 나게 해줘"라고 하면 알아서 발동해요. 직접 부르고
싶으면 `/humanizer:humanizer`를 입력하세요. 업데이트는 아래 두 줄로 받고, 받은
뒤에는 새 세션을 열어 주세요.

```bash
claude plugin marketplace update claude-humanizer
claude plugin update humanizer@claude-humanizer
```

> 예전에 `skills/humanizer`를 `~/.claude/skills/`에 직접 복사해서 설치했다면 그
> 폴더는 지워 주세요. 그대로 두면 스킬이 두 번 로드돼요.

**플러그인 시스템이 없는 곳**(Claude.ai처럼 스킬 폴더를 올리는 환경)에서는
`skills/humanizer` 폴더를 스킬로 복사하거나 업로드하면 돼요.

## 하는 일

**카피를 한 편씩 다듬어요.** 마케팅·광고 카피, 랜딩 페이지, UI 마이크로카피, 푸시
알림, SNS 글, 이메일, 뉴스레터, 발표 슬라이드와 보고서 제목을 다뤄요. 어느 언어에서나
반복되는 다섯 가지 티를 찾아요.

1. **번역투·직역체** — 다른 언어에서 구조째 옮겨 온 문장
2. **과한 격식·상투어·꾸밈** — 뜻은 없고 분위기만 띄우는 말, 쉬운 말로 충분한데 굳이 쓴 비유
3. **밋밋한 리듬** — 문장 길이와 끝맺음이 전부 비슷함. 언어를 가리지 않는 가장 흔한 티예요.
4. **구조 과잉** — 카피에 억지로 붙인 불릿, `첫째·둘째` 같은 순서 표시, 목차식 뼈대
5. **매끈한 대구** — 지나치게 딱 떨어지는 균형 문장

**제품 전체의 UI 문구도 훑어요.** 코드베이스의 locale 파일, JSX 텍스트, 알림
템플릿을 한 번에 볼 수 있어요. 이미 한 번 다듬은 제품에서 실제로 문제가 되는 건 AI
티 하나하나보다 **말투 표류(register drift)**인 경우가 많아요. 해요체로 된 알림
목록에 옛날 습니다체 알림 하나가 남아 있거나, 친근한 버튼들 사이에 딱딱한 버튼이 하나
끼어 있거나, 앱 안 알림과 푸시 알림의 문장이 서로 달라진 경우죠.

스윕 워크플로는 사용자가 한 화면에서 함께 보는 문구끼리 묶고, 각 묶음을 원래 쓰던
말투로 맞춰요. `{name}`, `${actor}`, ICU 복수형 같은 플레이스홀더는 건드리지 않고,
멀쩡한 문장도 그대로 둬요. 무엇을 고쳤는지, 무엇을 일부러 안 고쳤는지는 리포트로
정리해 줘요.

## 구조

언어와 상관없는 공통 뼈대 하나에 언어별 카탈로그를 붙인 구조예요.

```text
.claude-plugin/
├── plugin.json                    ← 플러그인 매니페스트
└── marketplace.json               ← `/plugin marketplace add`가 이 리포를 찾게 해 줌
skills/humanizer/
├── SKILL.md                       ← 워크플로 + 언어 공통 다섯 가지 티
└── references/
    ├── codebase-scan.md           ← 제품 UI 문구를 훑는 방법
    └── languages/
        ├── korean.md              ← 한국어 티와 바꿔 쓰기 (매번 읽음)
        ├── korean-examples.md     ← 한국어 전후 예시 (긴 글일 때만 읽음)
        ├── english.md             ← 영어 티 (delve, em-dash, 대구…)
        ├── english-examples.md    ← 영어 전후 예시
        └── _template.md           ← 새 언어를 추가하는 방법
evals/                             ← `claude plugin eval` 테스트 스위트
.github/                           ← 푸시와 PR마다 도는 검증
CHANGELOG.md                       ← 버전별 변경 사항과 측정 결과
```

스킬은 대상 언어를 알아낸 뒤 그 언어의 카탈로그를 불러와요. 전용 파일이 없는 언어도
공통 원칙과 원어민 수준의 판단으로 처리해요.

| 언어 | 카탈로그 | 깊이 |
|---|---|---|
| 한국어 | [`korean.md`](skills/humanizer/references/languages/korean.md) | 전체, 중점적으로 다듬는 중 |
| 영어 | [`english.md`](skills/humanizer/references/languages/english.md) | 전체 |
| 그 밖의 언어 | — | 공통 원칙으로 처리 |

지금은 한국어를 중심으로 다듬고 있어요. 영어는 현재 수준을 유지하고, 다른 언어는
공통 원칙으로 처리해요.

짧은 문구를 고칠 때는 규칙 파일(`korean.md`)만 읽고, 전후 예시(`korean-examples.md`)는
긴 글을 다듬을 때만 읽어요. 버튼 하나를 고치는 데 예시 전체를 불러오지 않도록 나눠
둔 거예요.

## 설계 원칙

- **흔적만 지워요.** 사람이 쓴 척하려고 유행어나 농담, 이모지를 넣지 않아요. 기계가
  쓴 흔적을 지우고 거기서 멈춰요. 억지로 캐주얼하게 만드는 것도 또 다른 티로 봐요.
- **고치는 곳마다 이유가 있어요.** 문제가 없는 문장은 건드리지 않아요. 이미 정리된
  코드베이스라면 훑어본 문구 중 일부만 바뀌는 게 정상이에요.
- **말투의 격은 그대로 둬요.** 격식, 높임 수준, 존댓말·반말은 원래 자리에 둬요. 말투
  표류를 고친다는 건 그 문구를 화면이 원래 쓰던 목소리로 돌려놓는다는 뜻이에요. 격을
  낮추는 일과는 달라요.
- **내용은 보호해요.** 이름, 숫자, 가격, 인용문, 법적 문구, 플레이스홀더, 브리프에서
  강조한 기능 이름은 고쳐 쓰지 않아요.

**목표가 아닌 것: AI 탐지 회피.** 이 플러그인은 직접 책임지는 카피의 품질을 높이는
도구예요. AI 사용을 밝혀야 하는 과제나 자기소개서 같은 결과물을 사람이 쓴 것처럼
꾸미는 용도로는 만들지 않았어요. 스킬 description에서 이런 요청은 범위 밖으로 빼
두었고, `evals/neg-detector-evasion`이 계속 그렇게 동작하는지 확인해요.

## 테스트

`evals/`에는 [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals)용
테스트 스위트가 들어 있어요. 최신 Claude Code가 필요하니 먼저 `claude update`를
실행하세요.

| 케이스 | 확인하는 것 |
|---|---|
| `ko-humanize-newsletter`, `en-humanize-blurb` | AI 티 나는 카피를 다듬을 때 사실을 지키면서 티를 지웠는지 |
| `ko-landing-copy` | 새 카피를 쓸 때 기능 이름을 살렸는지, 최상급 표현이나 매끈한 대구는 없는지 |
| `ko-codebase-drift-review` | 작은 앱 픽스처를 훑을 때 뻔한 표류와 미묘한 표류(플레이스홀더 뒤 조사, 버튼 라벨 불일치, 다른 파일에 있는 푸시 문구)를 찾고, 멀쩡한 문구는 그대로 두는지 |
| `ko-formal-notice-keeps-register`, `ko-banmal-brand-caption` | 말투를 양쪽으로 지키는지: 격식 공지는 격식체로(날짜·시간은 그대로), 반말 브랜드 캡션은 반말로(억지 유행어나 이모지 없이) |
| `ko-slide-titles` | 발표 슬라이드 제목에서 비유·대비·쉼표로 나눈 제목을 이름표형으로 바꾸면서, 고유명사와 숫자는 남기고 괜찮은 제목은 그대로 두는지 |
| `neg-*` | 스킬이 **발동하면 안 되는** 요청: 맞춤법만 고치기, 뜻만 알면 되는 번역, AI 탐지 회피 |

격식 공지나 반말 캡션 같은 한 편짜리 카피는 요즘 모델이 스킬 없이도 잘 처리해서
baseline과 점수 차이가 작아요. 이런 케이스는 스킬이 결과를 오히려 나쁘게 만들지 않는지
지키는 용도예요. 스킬의 차이가 크게 드러난 건 두 곳이에요. 코드베이스 스윕에서 멀쩡한
문구를 건드리지 않고 뜻을 지키는 것, 그리고 슬라이드 제목을 줄이면서 고유명사와 숫자를
남기는 것이에요. 버전별 측정 결과는 [CHANGELOG.md](CHANGELOG.md)에 있어요.

```bash
claude plugin eval .                            # 전체 스위트 + 스킬 없는 baseline과 비교
claude plugin eval . --runs 1 --ablation none   # 가볍게 한 번만
claude plugin eval . --tag trigger              # 발동 여부 케이스만
```

실행할 때마다 계정으로 실제 모델을 호출하니 전체 스위트는 비용이 들어요. 가벼운 실행부터
해 보세요. 결과는 git에서 제외된 `evals/results/`에 저장돼요.

## 기여하기

- **언어 추가:** [`_template.md`](skills/humanizer/references/languages/_template.md)를
  `<언어>.md`로 복사해 ❌/✅ 예시를 채우고, 위 표에도 추가해 주세요.
- **푸시 전 확인:** `claude plugin validate . --strict`와
  `python .github/scripts/check_plugin.py --base origin/master`를 실행하세요. 같은
  검사를 CI가 푸시와 PR마다 돌려요.
- **스킬 `description`은 1,024자 이하로.** 모든 세션에 늘 올라가는 부분이고, Agent
  Skills 한도를 적용하는 곳에서는 더 길면 스킬을 받아 주지 않아요. "어떻게"는 본문에,
  "언제"는 description에 두세요.
- **릴리스:** 설치본은 `.claude-plugin/plugin.json`의 `version`에 고정돼요. 사용자에게
  전달돼야 하는 변경이면 버전을 올리고, [CHANGELOG.md](CHANGELOG.md)에 무엇을 바꿨고
  어떻게 확인했는지 적어 주세요. 둘 중 하나라도 빠지면 CI가 실패해요.

## 라이선스

MIT — [LICENSE](LICENSE)를 참고하세요.
