"""Build blind GPT-6 judge prompts: each piece's 8 outputs shuffled under random labels, two shuffles."""
import json, random, sys
from pathlib import Path

S = Path(sys.argv[1])
KIND = {"L1": "a bookstore newsletter", "L2": "an app update announcement", "L3": "an internal company notice email (formal)"}
for piece in ["L1", "L2", "L3"]:
    src = (S / "in" / f"{piece}.md").read_text(encoding="utf-8")
    outs = sorted((S / "out").glob(f"{piece}_*.md"))
    for shuffle in (1, 2):
        rng = random.Random(f"{piece}-{shuffle}-humanizer")
        order = outs[:]
        rng.shuffle(order)
        labels = [f"R{i+1}" for i in range(len(order))]
        key = {lab: f.stem for lab, f in zip(labels, order)}
        (S / "judge" / f"{piece}_{shuffle}_key.json").write_text(json.dumps(key, indent=1), encoding="utf-8")
        parts = [f"""You are judging Korean copy edits. A user gave an AI-sounding Korean draft of {KIND[piece]} and asked: "AI가 쓴 티가 나. 자연스럽게 다듬어 줘. 다듬은 글만 줘." Below are the source and {len(order)} independent rewrites labeled R1..R{len(order)}. You don't know how any rewrite was produced; judge only the text.

Score each rewrite:
- naturalness (1-5): would a skilled native Korean copywriter have written it? Penalize remaining AI tells (번역투 like ~을 통해/~에 대해/~되어지다/제공합니다, clichés, hype, slick 대구, ordinal signposting, empty superlatives, forced friendliness, emoji), and also penalize new tells or forced casualness.
- fidelity (1-5): every fact, name, number, date, condition, scope, and hedge from the source is kept with the same meaning; nothing invented; no possibility turned into a certainty. 5 = perfect. List each problem concretely.
- restraint (1-5): edits only what needed fixing, keeps the source's register and structure where they were fine; 1 = heavy rewriting, cut content, or register change.
- register_held (true/false): politeness level and speech style suit the source (formal notice stays formal; 해요체 stays polite).

Then give an overall ranking best to worst.

Reply with JSON only, no prose, in this shape:
{{"scores": {{"R1": {{"naturalness": n, "fidelity": n, "restraint": n, "register_held": true, "fidelity_problems": ["..."], "tells_left": ["..."]}}, ...}}, "ranking": ["R?", ...]}}

=== SOURCE ===
{src}
"""]
        for lab, f in zip(labels, order):
            parts.append(f"=== {lab} ===\n{f.read_text(encoding='utf-8').strip()}\n")
        (S / "judge" / f"{piece}_{shuffle}_prompt.md").write_text("\n".join(parts), encoding="utf-8")
print("built")
