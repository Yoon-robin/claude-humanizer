import json, re, sys
from collections import defaultdict
from pathlib import Path
J = Path(sys.argv[1])
agg = defaultdict(lambda: defaultdict(list))
probs = defaultdict(list)
for out in sorted(J.glob("*_out.json")):
    tag = out.stem.replace("_out", "")
    key = json.loads((J / f"{tag}_key.json").read_text(encoding="utf-8"))
    raw = out.read_text(encoding="utf-8")
    m = re.search(r"\{[\s\S]*\}", raw)
    data = json.loads(m.group(0))
    n = len(data["ranking"])
    for pos, lab in enumerate(data["ranking"]):
        agg[key[lab].split("_")[1]]["rank"].append(pos + 1)
    for lab, sc in data["scores"].items():
        run = key[lab]; cond = run.split("_")[1]
        for k in ("naturalness", "fidelity", "restraint"):
            agg[cond][k].append(sc[k])
        agg[cond]["register"].append(1 if sc["register_held"] else 0)
        for p in sc.get("fidelity_problems", []):
            probs[run].append(f"[{tag}] {p}")
avg = lambda v: sum(v) / len(v)
print("cond  natural  fidelity  restraint  register  mean-rank(1=best of 8)  n")
for c, name in [("A", "full skill"), ("S", "SKILL.md only"), ("B", "one sentence"), ("C", "nothing")]:
    a = agg[c]
    print(f"{c} {name:14s} {avg(a['naturalness']):.2f}  {avg(a['fidelity']):.2f}  {avg(a['restraint']):.2f}  {avg(a['register']):.2f}  {avg(a['rank']):.2f}  {len(a['rank'])}")
print("\nper piece mean rank:")
for piece in ["L1", "L2", "L3"]:
    row = defaultdict(list)
    for out in J.glob(f"{piece}_*_out.json"):
        tag = out.stem.replace("_out", "")
        key = json.loads((J / f"{tag}_key.json").read_text(encoding="utf-8"))
        data = json.loads(re.search(r"\{[\s\S]*\}", out.read_text(encoding="utf-8")).group(0))
        for pos, lab in enumerate(data["ranking"]):
            row[key[lab].split("_")[1]].append(pos + 1)
    print(" ", piece, {c: round(avg(v), 2) for c, v in sorted(row.items())})
print("\nfidelity problems:")
for run in sorted(probs):
    for p in probs[run]:
        print(" ", run, p[:220])
