"""Leveled Derivation for the u-substitution method (recognition-only).

WORKED TARGET:  ∫ 2x cos(x^2) dx = sin(x^2).

HONESTY NOTE (CLAUDE.md rules 7, 10, 11):
  u_sub is RECOGNITION-ONLY. It has NO honest dedicated executable transform in the
  engine — a generic "substitute u=g(x)" transform was rejected as merely *covering*
  for the executor (it would have to guess g, which is the whole problem). What
  actually evaluates an instance is direct(CAS): SymPy's integrator returns sin(x^2).
  So this Derivation EXPLAINS what u-substitution *would* do on this instance and why
  it is the right recognition, and it marks the HONEST CEILING: the recognizer offers
  the candidate inner function u=g(x); choosing g is a human/recognition judgement, and
  the closed form is then produced & verified by the CAS, not by a bespoke u-sub engine.

The per-level step COUNTS EMERGE from the `requires`/`decompose` tree, never hand-set:
  expert  -> chunks the whole "reverse the chain rule" move into 1 node
  working -> sees that node's 3 sub-moves (spot pattern / rewrite in u / integrate+back-sub)
  plain   -> decomposes each working sub-move further, to high-school steps
plus the shared why + how + verify bands (1 each at every level).
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

def build_u_sub_derivation() -> Derivation:
    problem = Problem(
        latex=r"\int 2x\,\cos\!\left(x^{2}\right)\,dx",
        represents="a product whose first factor is the derivative of the inner function "
                   "of the second — the fingerprint of a reversed chain rule",
        goal=Goal.EVALUATE,
        integral=r"antiderivative of 2x\cos(x^2)")
    d = Derivation(problem)

    # ── WHY (recognition / decision) ───────────────────────────────────────
    d.why("Why this approach — u-substitution (reverse the chain rule)",
          {"plain": r"There is no simple rule for the antiderivative of $2x\cos(x^{2})$ as a whole. "
                    r"But look closely: the $2x$ out front is exactly what you would get by differentiating "
                    r"the inside, $x^{2}$. That is the tell-tale sign that this integral came from the "
                    r"chain rule — so we can run the chain rule backwards by naming the inside $u=x^{2}$.",
           "working": r"The integrand has the shape $f'(g(x))\,g'(x)$ with $g(x)=x^{2}$, $g'(x)=2x$ and "
                      r"$f'=\cos$. That is precisely the output of a chain-rule differentiation, so the "
                      r"antiderivative is $f(g(x))$. Substituting $u=g(x)$ makes that visible and turns the "
                      r"integral into one in $u$ that we already know.",
           "expert": r"Integrand $=\cos(x^{2})\cdot\tfrac{d}{dx}(x^{2})$, i.e. $(F\circ g)'$ with "
                     r"$F=\sin$, $g=x^{2}$. The substitution $u=g(x)$ is the pullback that trivialises it."},
          forced_by=r"the explicit factor $2x=\tfrac{d}{dx}(x^{2})$ multiplying $\cos(x^{2})$: the "
                    r"derivative of the inner function is present, so a reversed chain rule (not parts, "
                    r"not a table lookup of the product) is what the structure selects.",
          payoff=r"naming $u=x^{2}$ collapses the product to the elementary $\int\cos u\,du=\sin u$; the "
                 r"answer $\sin(x^{2})$ then carries the structure (it is a clean composition), which a "
                 r"numeric value of a definite version would destroy.",
          relies_on=r"recognition only: the engine offers the candidate inner $u=g(x)$, but choosing $g$ "
                    r"is a judgement, and the closed form is produced and verified by the CAS — there is "
                    r"no bespoke u-sub executor (honest ceiling, see the final step).")

    # ── HOW (the machinery) ────────────────────────────────────────────────
    d.how("How the approach works — the substitution rule",
          {"plain": r"If you let $u$ stand for the inside, $u=x^{2}$, then a small change in $x$ produces a "
                    r"change in $u$ of $du=2x\,dx$. Every piece of the integral has a $u$-name: the $2x\,dx$ "
                    r"becomes $du$ and $\cos(x^{2})$ becomes $\cos u$. The integral is now $\int\cos u\,du$.",
           "working": r"The substitution rule $\int f(g(x))g'(x)\,dx=\int f(u)\,du$ (with $u=g(x)$, "
                      r"$du=g'(x)\,dx$) rewrites the integral in $u$; integrate in $u$, then put $g(x)$ back.",
           "expert": r"Change of variables $u=g(x)$: $\int (F\circ g)'\,dx=F\circ g$, executed as "
                     r"$\int\cos u\,du=\sin u$ then $u\mapsto x^{2}$."},
          math=[r"u=x^{2},\qquad du=2x\,dx\ \Longrightarrow\ "
                r"\int 2x\,\cos\!\left(x^{2}\right)dx=\int\cos u\,du"])

    # ── STEP (the worked execution) — ONE expert node; the cut makes the counts ──
    d.step("Reverse the chain rule via u = x^2", requires="expert",
           prose=r"Set $u=x^{2}$ so $du=2x\,dx$; the integral becomes $\int\cos u\,du=\sin u$; "
                 r"back-substitute to get $\sin(x^{2})$.",
           math=[r"\int 2x\,\cos\!\left(x^{2}\right)dx\ \overset{u=x^{2}}{=}\ \int\cos u\,du"
                 r"\ =\ \sin u\ =\ \sin\!\left(x^{2}\right)"],
           relies_on=r"sub-methods: chain-rule recognition + the cos antiderivative.",
           decompose=[
               # ---- working sub-move 1: spot the pattern -------------------
               dict(title="Spot the f'(g)·g' pattern and name u", requires="working",
                    prose=r"Identify the inner function $g(x)=x^{2}$ and check its derivative $g'(x)=2x$ "
                          r"appears as a factor; name $u=x^{2}$.",
                    math=[r"g(x)=x^{2},\quad g'(x)=2x,\quad \text{factor }2x\text{ present}\ \Rightarrow\ u=x^{2}"],
                    references=["sub-method → library/chain-rule.md"],
                    decompose=[
                        dict(title="Differentiate the inside", requires="plain",
                             prose=r"The inside is $x^{2}$; by the power rule its derivative is $2x$.",
                             math=[r"\frac{d}{dx}\,x^{2}=2x"],
                             references=["base → library/power-rule.md"]),
                        dict(title="Match it against the front factor", requires="plain",
                             prose=r"The integrand's front factor is also $2x$ — it matches $g'(x)$ exactly, "
                                   r"so this is a reversed chain rule with $u=x^{2}$.",
                             math=[r"2x\,\cos(x^{2})=\underbrace{2x}_{g'(x)}\;\cos\big(\underbrace{x^{2}}_{g(x)}\big)"]),
                    ]),
               # ---- working sub-move 2: rewrite in u -----------------------
               dict(title="Rewrite the whole integral in u", requires="working",
                    prose=r"Compute $du=2x\,dx$ and replace both the $2x\,dx$ and the $x^{2}$, so nothing in "
                          r"$x$ is left.",
                    math=[r"du=2x\,dx,\qquad \int 2x\,\cos(x^{2})\,dx=\int\cos u\,du"],
                    references=["sub-method → library/u-substitution.md"],
                    decompose=[
                        dict(title="Form du from u", requires="plain",
                             prose=r"Differentiate $u=x^{2}$ to get $du=2x\,dx$ — exactly the front part of "
                                   r"the integral.",
                             math=[r"u=x^{2}\ \Rightarrow\ du=2x\,dx"]),
                        dict(title="Swap each x-piece for its u-name", requires="plain",
                             prose=r"$\cos(x^{2})$ becomes $\cos u$ and the leftover $2x\,dx$ becomes $du$.",
                             math=[r"\cos(x^{2})\to\cos u,\qquad 2x\,dx\to du"]),
                        dict(title="Read off the u-integral", requires="plain",
                             prose=r"Putting the pieces together leaves a clean integral purely in $u$.",
                             math=[r"\int 2x\,\cos(x^{2})\,dx=\int\cos u\,du"]),
                    ]),
               # ---- working sub-move 3: integrate and back-substitute ------
               dict(title="Integrate in u and undo the substitution", requires="working",
                    prose=r"$\int\cos u\,du=\sin u$; replace $u$ by $x^{2}$.",
                    math=[r"\int\cos u\,du=\sin u\ \xrightarrow{\,u=x^{2}\,}\ \sin\!\left(x^{2}\right)"],
                    references=["sub-method → library/standard-integrals.md"],
                    decompose=[
                        dict(title="Antiderivative of cosine", requires="plain",
                             prose=r"Since $\tfrac{d}{du}\sin u=\cos u$, the antiderivative of $\cos u$ is $\sin u$.",
                             math=[r"\int\cos u\,du=\sin u\ (+C)"],
                             references=["base → library/standard-integrals.md"]),
                        dict(title="Put x^2 back for u", requires="plain",
                             prose=r"Undo the naming: wherever $u$ stands, write $x^{2}$ again.",
                             math=[r"\sin u\big|_{u=x^{2}}=\sin\!\left(x^{2}\right)"]),
                    ]),
           ])

    # ── VERIFY (the honest ceiling + the independent check) ────────────────
    d.verify(
        r"This method is RECOGNITION-ONLY: there is no bespoke u-substitution executor — choosing the "
        r"inner $u=g(x)$ is the recognition judgement, and the closed form is produced & checked by the "
        r"CAS (direct integration), not by a dedicated transform. The check needs no u-sub: differentiate "
        r"the proposed answer and confirm it reproduces the integrand (the only thing that can be executed "
        r"honestly here).",
        math=[r"\frac{d}{dx}\sin\!\left(x^{2}\right)=\cos\!\left(x^{2}\right)\cdot 2x=2x\,\cos\!\left(x^{2}\right)\ \checkmark",
              r"\text{CAS: }\ \int 2x\,\cos\!\left(x^{2}\right)dx=\sin\!\left(x^{2}\right)\ (+C)"],
        references=["honest ceiling: no dedicated u-sub transform — direct(CAS) solves the instance",
                    "independent check: differentiate the antiderivative (chain rule) — library/chain-rule.md",
                    "method: library/u-substitution.md (recognition-only; captured gate)"])
    d.result(latex=r"\int 2x\,\cos\!\left(x^{2}\right)dx=\sin\!\left(x^{2}\right)+C",
             note="recognition-only u-sub; antiderivative verified by differentiation (chain rule) and by CAS.")
    return d
