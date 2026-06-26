"""M1 proposer on the prior problem (∇×(∇φ)) — the LLM drives recognize().

The keyword retriever narrows the wiki to a shortlist; the LLM judges which
pattern actually applies. Run this to emit the shortlist + the exact prompt that
goes to the LLM. The LLM (Claude API, or the agent driving this) answers it; feed
the answer back via --answer to close the loop.

Run:            python examples/m1_recognize_demo.py
With an answer: python examples/m1_recognize_demo.py --answer "sym-antisym-contraction — ..."
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import Problem, Goal  # noqa: E402
from integral_explainer.library import recognize, load_patterns  # noqa: E402
from integral_explainer.proposer import build_recognition_prompt, propose_with_llm  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

problem = Problem(
    latex=r"\nabla\times(\nabla\phi)",
    represents="the curl of a gradient field",
    goal=Goal.PROVE,
)
pats = load_patterns()

shortlist = recognize(f"{problem.latex} {problem.represents}", pats, k=5)
print("STEP 1 — recognize() shortlist (keyword retrieval, the LLM's candidates):")
for p, s in shortlist:
    print(f"   [{s}] {p.id}  ({p.domain})")
print("\nSTEP 2 — prompt handed to the LLM proposer:\n")
print(build_recognition_prompt(problem, shortlist))

answer = None
if "--answer" in sys.argv:
    answer = sys.argv[sys.argv.index("--answer") + 1]

if answer:
    chosen, ans, _ = propose_with_llm(problem, lambda _p: answer, patterns=pats)
    print("\nSTEP 3 — LLM answer fed back through the proposer:")
    print("   answer :", ans)
    print("   chosen :", chosen.id if chosen else None)
    ok = bool(chosen) and chosen.id == "sym-antisym-contraction"
    print("   correct pattern (sym-antisym-contraction):", ok)
else:
    print("\n(LLM answers the prompt above; re-run with --answer \"<id> — <reason>\".)")
