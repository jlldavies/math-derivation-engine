"""The recognition -> explain thread end to end (the agent-facing flow).

A user asks in plain language. The engine RECOGNIZES which pattern page applies
(`recognize`), then AUTO-BUILDS a levelled explanation from that page
(`leveled_trace_from_pattern`) — the explanation contract (why / how / step bands
at expert / working / plain) — and renders it (`render_leveled`). No second LLM
call: the agent supplies only the recognition; the engine does the lifting.

Run:  python examples/recognize_to_explain.py "your maths question"
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import (load_patterns, recognize_pattern,  # noqa: E402
                                leveled_trace_from_pattern, render_leveled,
                                validate_explanation, Problem, Goal)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def explain(query: str):
    pats = load_patterns()
    hits = recognize_pattern(query, pats, k=3)
    if not hits:
        print(f"no pattern recognized for: {query!r}")
        return None
    top, score = hits[0]
    print(f"query: {query!r}")
    print(f"recognized: {top.id}  (score {score}; runners-up "
          f"{[p.id for p, _ in hits[1:]]})")
    problem = Problem(latex=top.latex_parts().get("rule", top.name),
                      represents=f"recognized pattern: {top.name}",
                      goal=Goal.RECOGNIZE, integral=query)
    tracks = leveled_trace_from_pattern(problem, top)
    for lvl, tr in tracks.items():
        warn = validate_explanation(tr)
        print(f"  contract [{lvl}]:", "OK (why+how+step)" if not warn else warn)
    out = os.path.join(os.path.dirname(__file__), "recognize_output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, f"{top.id}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_leveled(tracks))
    print(f"  -> {path}")
    return path


def main():
    q = " ".join(sys.argv[1:]) or "dimensional regularization loop integral epsilon pole"
    explain(q)


if __name__ == "__main__":
    main()
