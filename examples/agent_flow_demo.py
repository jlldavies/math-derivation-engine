"""The working model: an AI tool drives the engine; the engine does the lifting.

No LLM/API lives inside the engine. The agent (Claude) calls the engine's tools
and supplies only the recognition judgement:

  1. agent calls  recognize(problem)        -> engine retrieves a shortlist   [lifting]
  2. agent PICKS the pattern that applies     (the LLM's job — see m1_recognize_demo)
  3. agent calls  trace_from_pattern(...)    -> engine assembles the explanation [lifting]
  4. agent calls  trace.render_html()/md     -> engine renders it               [lifting]

Run:  python examples/agent_flow_demo.py
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import Problem, Goal, trace_from_pattern  # noqa: E402
from integral_explainer.library import recognize, load_patterns  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

problem = Problem(
    latex=r"\nabla\times(\nabla\phi)",
    represents="the curl of a gradient field",
    goal=Goal.PROVE,
)
pats = load_patterns()

# 1. ENGINE: retrieve a shortlist
shortlist = recognize(f"{problem.latex} {problem.represents}", pats, k=5)
print("1. engine recognize() ->", [p.id for p, _ in shortlist])

# 2. AGENT (the LLM) picks — keyword top-1 was 'div-of-curl' (wrong); the agent
#    judges structurally that this is curl-of-grad = ε∂∂φ -> sym-antisym (see
#    examples/m1_recognize_demo.py). That judgement is the ONLY thing the AI supplies.
picked_id = "sym-antisym-contraction"
pattern = next(p for p in pats if p.id == picked_id)
print("2. agent picks         ->", picked_id, f"({pattern.name})")

# 3-4. ENGINE: assemble the explanation from the page, and render it
trace = trace_from_pattern(problem, pattern)
out = os.path.join(os.path.dirname(__file__), "agent_output")
os.makedirs(out, exist_ok=True)
for name, content in (("trace.md", trace.render_markdown()),
                      ("trace.html", trace.render_html())):
    with open(os.path.join(out, name), "w", encoding="utf-8") as f:
        f.write(content)
print("3-4. engine assembled + rendered the explanation from the wiki page:")
print()
print(trace.render_markdown())
print(f"(html written to {out})")
