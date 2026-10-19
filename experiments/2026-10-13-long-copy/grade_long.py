"""Grade the long-copy A/S/B/C runs: facts kept, planted tells left, register, edit size."""
import difflib, re, sys
from collections import defaultdict
from pathlib import Path

D = Path(sys.argv[1])
FACTS = {
    "L1": {"11월 22일": r"11월\s?22일", "토요일": r"\(토\)|토요일", "오후 3시": r"오후\s?3시", "2층 다목적실": r"2층\s?다목적실",
           "밤의 정원사": r"밤의 정원사", "한서윤": r"한서윤", "계기": r"계기", "집필": r"집필", "홈페이지": r"홈페이지",
           "선착순": r"선착순", "40명": r"40명", "1만 원": r"1만\s?원|10,000원", "음료": r"음료", "사흘 전": r"사흘\s?전|3일\s?전",
           "문자": r"문자", "사인": r"사인", "10%": r"10\s?%", "당일": r"당일"},
    "L2": {"3.2": r"3\.2", "카드 문자": r"카드\s?문자", "자동 입력": r"자동\s?입력", "12곳": r"12\s?곳|12개", "일부": r"일부",
           "다음 달": r"다음\s?달", "예정": r"예정", "수정": r"수정|고칠|고치", "예산": r"예산", "알림": r"알림", "설정": r"설정",
           "다크 모드": r"다크\s?모드", "앱스토어": r"앱스토어|App Store", "구글 플레이": r"구글\s?플레이|Google Play",
           "iOS 16 이상": r"iOS\s?16\s?이상", "안드로이드 10 이상": r"안드로이드\s?10\s?이상"},
    "L3": {"12월 6일": r"12월\s?6일", "토": r"\(토\)|토요일", "오전 1시": r"오전\s?1시", "오전 7시": r"오전\s?7시|1시부터\s?7시|1시\s?~\s?7시", "메일": r"메일",
           "전자결재": r"전자\s?결재", "사내 메신저": r"메신저", "목록 단서": r"메신저\s?등|등의 서비스|같은 서비스|메신저 같은|등 사내",
           "최대 2시간": r"최대\s?2시간", "늦어질 수": r"늦어질 수|연장될 수|늦어질 가능|미뤄질 수|늘어날 수",
           "12월 8일": r"12월\s?8일", "월": r"\(월\)|월요일", "90일": r"90일", "12자 이상": r"12자\s?이상", "대문자": r"대문자",
           "숫자": r"숫자", "특수문자": r"특수\s?문자", "1개 이상": r"1개\s?이상|하나\s?이상|1자\s?이상", "사내 포털": r"사내\s?포털",
           "4120": r"4120", "정보보안팀": r"정보보안팀"},
}
TELLS = {
    "L1": {"되어지": r"되어지|되어집", "통해": r"[을를] 통해", "에 대해": r"에 대해|에 대한|에 관하여|에 관한", "그것은": r"그것은",
           "첫째": r"첫째|둘째|셋째", "지금 바로": r"지금 바로", "마음에 머무": r"마음에 머무", "뜨거운 관심": r"뜨거운 관심",
           "특별한": r"특별한", "및": r" 및 ", "인트로": r"전해 드립니다|이야기하려 합니다"},
    "L2": {"통해": r"[을를] 통해", "당신": r"당신", "다양한": r"다양한", "기능들": r"기능들", "보다": r"보다 ", "제공": r"제공해요|제공합니다",
           "먼저/다음/마지막": r"먼저,|다음으로,|마지막으로,", "대구": r"지출은 가볍게|저축은 똑똑하게", "과장": r"더 이상 어렵지",
           "어떨까요": r"어떨까요", "이모지": r"😊", "한층 더": r"한층 더"},
    "L3": {"되어지": r"되어지", "보다 안전": r"보다 안전", "제공하기 위하여": r"제공하기 위하여|제공하기 위해", "임직원들": r"임직원들",
           "소중한": r"소중한", "통해": r"[을를] 통해", "이는": r"(?:^|\s)이는 "},
}
FORMAL_BREAK = r"[가-힣]요(?:[.!?~]|$)|(?<!니)다(?:[.!?]|$)|[가-힣](?:어|아|야|지|해|네|자|게)(?:[.!?~]|$)"

src = {k: (D.parent / "in" / f"{k}.md").read_text(encoding="utf-8") for k in FACTS}
tok = {}
tf = D.parent / "tokens.txt"
if tf.exists():
    for line in tf.read_text().split("\n"):
        if line.strip():
            k, v = line.split(); tok[k] = int(v)

agg = defaultdict(lambda: defaultdict(list))
print(f"{'run':9s} facts   tells  sim   len   tok   missing / tells left")
for f in sorted(D.glob("L*_*_*.md")):
    piece, cond, run = f.stem.split("_")
    t = f.read_text(encoding="utf-8")
    miss = [k for k, p in FACTS[piece].items() if not re.search(p, t)]
    left = [k for k, p in TELLS[piece].items() if re.search(p, t, re.M)]
    sim = difflib.SequenceMatcher(None, src[piece], t).ratio()
    ln = len(t) / len(src[piece])
    reg = ""
    if piece == "L3" and re.search(FORMAL_BREAK, t, re.M):
        reg = " REGISTER-BREAK:" + str(re.findall(r"[^\n]{0,12}(?:" + FORMAL_BREAK + ")", t, re.M)[:3])
    nf, nt = len(FACTS[piece]), len(TELLS[piece])
    print(f"{f.stem:9s} {nf-len(miss):>2}/{nf:<3} {len(left):>2}/{nt:<3} {sim:.2f}  {ln:.2f}  {tok.get(f.stem, 0)//1000:>3}k  {miss or '-'} / {left or '-'}{reg}")
    a = agg[cond]
    a["facts"].append((nf - len(miss), nf)); a["tells"].append((len(left), nt)); a["sim"].append(sim); a["len"].append(ln)
    if f.stem in tok: a["tok"].append(tok[f.stem])

print("\nby condition:")
for cond, name in [("A", "full skill"), ("S", "SKILL.md only"), ("B", "one sentence"), ("C", "nothing")]:
    a = agg.get(cond)
    if not a: continue
    fk = sum(x for x, _ in a["facts"]); ft = sum(y for _, y in a["facts"])
    tl = sum(x for x, _ in a["tells"]); tt = sum(y for _, y in a["tells"])
    avg = lambda v: sum(v) / len(v) if v else 0
    print(f"  {cond} {name:14s} facts {fk}/{ft}  tells left {tl}/{tt}  sim {avg(a['sim']):.2f}  len {avg(a['len']):.2f}  tok {avg(a['tok'])/1000:.1f}k  runs {len(a['facts'])}")
