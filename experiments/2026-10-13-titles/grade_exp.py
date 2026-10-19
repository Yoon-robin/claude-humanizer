"""Grade the A/B/C title experiment per slide.

Facts: each must appear on its own slide's line.
Untouched: titles that were already fine must come back unchanged.
Tells: the metaphor or hook words that should be gone.
"""
import re
import sys
from pathlib import Path

D = Path(sys.argv[1])

DECKS = {
    "d1": {
        "facts": {
            4: [("React Native", r"React Native"), ("Firebase", r"Firebase")],
            5: [("540", r"540"), ("한 달", r"한\s?달"), ("넘음", r"넘|이상|돌파|초과")],
            6: [("4.6", r"4\.6"), ("표본 단서", r"표본|응답")],
        },
        "untouched": {1: "스터디메이트", 2: "공부할 친구를 찾는 일은 생각보다 어렵습니다", 9: "다음 학기 계획"},
        "tells": {3: r"흘러", 7: r"나타납니다", 8: r"한 방향"},
    },
    "d2": {
        "facts": {
            2: [("매출", r"매출"), ("비용", r"비용")],
            3: [("18%", r"18"), ("4.2억", r"4\.2"), ("약", r"약|가량|안팎|내외"), ("전 분기", r"전\s?분기|직전 분기|QoQ")],
            5: [("82%", r"82"), ("37건", r"37")],
            8: [("최대", r"최대"), ("12%", r"12"), ("가능성", r"수 있|가능|전망|우려|예상|위험")],
        },
        "untouched": {1: "2026년 3분기 운영 보고", 6: "4분기 일정", 8: "원두 가격이 최대 12% 오를 수 있습니다"},
        "tells": {4: r"리듬", 5: r"뿐이지만", 7: r"지붕"},
    },
    "d3": {
        "facts": {
            3: [("1,800", r"1,?800"), ("46", r"46"), ("지난달", r"지난\s?달")],
            4: [("슬랙", r"슬랙|Slack")],
            6: [("2주", r"2\s?주"), ("약", r"약|가량|안팎|내외"), ("3배", r"3\s?배")],
        },
        "untouched": {1: "사내 도서 대여 서비스 개선안", 2: "목차", 8: "추가 비용은 월 최대 5만 원입니다", 9: "다음 단계"},
        "tells": {3: r"지만", 4: r"모든 길|통합니다", 5: r"왼쪽은|오른쪽은", 6: r"말해", 7: r"까요|\?"},
    },
}


def slides(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r"^\D*?(\d+)\.\s*(.+?)\s*$", line)
        if m and 1 <= int(m.group(1)) <= 9 and int(m.group(1)) not in out:
            out[int(m.group(1))] = re.sub(r"\*\*|`", "", m.group(2)).strip()
    return out


rows = []
for f in sorted(D.glob("d*_*_*.md")):
    deck, cond, run = f.stem.split("_")
    spec = DECKS[deck]
    s = slides(f.read_text(encoding="utf-8"))
    facts_total = sum(len(v) for v in spec["facts"].values())
    missing = [f"{n}:{label}" for n, items in spec["facts"].items() for label, pat in items
               if not re.search(pat, s.get(n, ""))]
    changed = [n for n, want in spec["untouched"].items() if s.get(n, "") != want]
    tells = [n for n, pat in spec["tells"].items() if re.search(pat, s.get(n, ""))]
    rows.append((deck, cond, run, facts_total - len(missing), facts_total, missing, changed, tells))

print(f"{'run':10s} {'facts kept':10s} {'fine titles changed':22s} {'tells left':10s} missing")
for deck, cond, run, kept, total, missing, changed, tells in rows:
    print(f"{deck}_{cond}_{run:5s} {kept:>2}/{total:<7} {str(changed or '-'):22s} {str(tells or '-'):10s} {', '.join(missing) or '-'}")

print("\nby condition (both decks, both runs):")
for cond, name in [("A", "skill v1.6"), ("K", "v1.7 + korean.md"), ("N", "v1.7 SKILL only"), ("B", "one sentence"), ("C", "nothing")]:
    sel = [r for r in rows if r[1] == cond]
    if not sel:
        continue
    kept = sum(r[3] for r in sel); total = sum(r[4] for r in sel)
    changed = sum(len(r[6]) for r in sel); tells = sum(len(r[7]) for r in sel)
    print(f"  {cond} {name:13s} facts {kept}/{total} ({kept/total:.0%})  fine titles changed {changed}  tells left {tells}  runs {len(sel)}")
