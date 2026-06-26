"""LEVELED Derivation for the `mellin` method (CLAUDE.md rule 7 + rule 11 Definition of Done).

WORKED TARGET:  M[e^{-x}](s) = ∫_0^∞ x^{s-1} e^{-x} dx = Γ(s).

This mirrors the ACTUAL engine computation
    special_methods.mellin_transform_of(sp.exp(-x))  ->  (gamma(s), (0, oo), True)
i.e. sp.mellin_transform applied to e^{-x} returns Γ(s) on the fundamental strip Re(s)>0.

The qualification tree is cut by `requires` so the per-level step counts EMERGE:
  - EXPERT chunks the whole "the Mellin transform of e^{-x} is the Euler integral = Γ(s)"
    into single nodes;
  - WORKING sees the named sub-moves (set up the defining integral, identify it as Euler's
    Gamma integral, name the strip, confirm via the functional equation);
  - PLAIN decomposes those into high-school-checkable pieces, each referencing a base page.

Sub-methods referenced (rule 11 "steps reference the sub-methods they use"):
    mellin transform -> { Mellin-transform DEFINITION (the parametric integral),
                          Gamma-function integral definition (Euler's 2nd integral),
                          convergence test for an improper integral (the strip),
                          integration by parts -> the functional equation Γ(s+1)=sΓ(s) }.

Run:  python scratch/expl_mellin.py
Does NOT modify src/.
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification, validate_references  # noqa: F401

from .. import special_methods as sm
import sympy as sp

HDR = r"M[e^{-x}](s)=\int_{0}^{\infty} x^{\,s-1}\,e^{-x}\,dx"

def build_mellin_derivation() -> Derivation:
    """A genuine why/how/step tree for M[e^{-x}](s)=Γ(s), mirroring sp.mellin_transform.

    The frontier cut (`requires`) makes the level counts emerge and differ:
      expert collapses each move; working splits it; plain decomposes to high-school.
    """
    problem = Problem(
        latex=HDR,
        represents="the Mellin transform of e^{-x}: the parametric integral that DEFINES Γ(s)",
        goal=Goal.EVALUATE,
        integral="M[e^{-x}](s) on the fundamental strip Re(s)>0")
    d = Derivation(problem)

    # --- WHY (the recognition / decision) -------------------------------------------------
    d.why("Why this approach — recognise it as a Mellin transform",
          {"plain": r"The integral has the shape $\int_0^\infty x^{(\text{power})}\,e^{-x}\,dx$. "
                    r"That exact shape is a named object — the *Mellin transform* of $e^{-x}$ — and for "
                    r"this particular function it is a famous integral with a known name, $\Gamma(s)$. So "
                    r"we don't grind out an antiderivative; we recognise the form and read off its name.",
           "working": r"The kernel $x^{s-1}$ against a decaying $e^{-x}$ on $(0,\infty)$ is the Mellin "
                      r"transform $M[f](s)=\int_0^\infty x^{s-1}f(x)\,dx$. For $f=e^{-x}$ this is literally "
                      r"Euler's integral of the second kind, whose value is the Gamma function $\Gamma(s)$.",
           "expert": r"$\int_0^\infty x^{s-1}e^{-x}dx$ is $M[e^{-x}](s)$, the canonical example of a Mellin "
                     r"transform; it coincides with Euler's second integral, so it evaluates to $\Gamma(s)$ "
                     r"on the fundamental strip $\Re(s)>0$ — exactly what $\texttt{sp.mellin\_transform}$ returns."},
          forced_by=r"the integrand is $x^{s-1}$ (a pure power in the parameter $s$) times $e^{-x}$ on "
                    r"$(0,\infty)$ — the defining template of a Mellin transform; no elementary "
                    r"antiderivative in $x$ exists, but the *form* is a named transform.",
          payoff=r"recognising the Mellin form yields the closed form $\Gamma(s)$ as a function of $s$ — a "
                 r"single object carrying the recursion $\Gamma(s+1)=s\,\Gamma(s)$, the poles at $s=0,-1,-2,\dots$, "
                 r"and the value $\Gamma(n)=(n-1)!$; a bare number at one $s$ would hide all of that.",
          relies_on=r"convergence of the improper integral on the strip $\Re(s)>0$: $x^{s-1}$ is integrable at "
                    r"$0$ (needs $\Re(s)>0$) and $e^{-x}$ kills the tail at $\infty$ — so the transform exists "
                    r"and equals $\Gamma(s)$ there.")

    # --- HOW (the machinery) --------------------------------------------------------------
    d.how("How the approach works — the Mellin-transform definition meets Euler's integral",
          {"plain": r"The Mellin transform is just the recipe $M[f](s)=\int_0^\infty x^{s-1}f(x)\,dx$. Put "
                    r"$f(x)=e^{-x}$ into the recipe and you get $\int_0^\infty x^{s-1}e^{-x}\,dx$, which is the "
                    r"standard definition of $\Gamma(s)$.",
           "working": r"Apply the definition $M[f](s)=\int_0^\infty x^{s-1}f(x)\,dx$ with $f=e^{-x}$; the result "
                      r"is Euler's integral $\Gamma(s)=\int_0^\infty x^{s-1}e^{-x}\,dx$, valid for $\Re(s)>0$.",
           "expert": r"$M[\,\cdot\,](s)=\int_0^\infty x^{s-1}(\cdot)\,dx$ on $f=e^{-x}$ is Euler's second "
                     r"integral; it is holomorphic on $\Re(s)>0$ and continues to $\Gamma(s)$ with simple poles "
                     r"at the non-positive integers."},
          math=[r"M[f](s)=\int_{0}^{\infty}x^{\,s-1}f(x)\,dx,\qquad "
                r"M[e^{-x}](s)=\int_{0}^{\infty}x^{\,s-1}e^{-x}\,dx=\Gamma(s)"])

    # --- THE STEPS (one qualification tree; counts EMERGE from the cut) -------------------
    # EXPERT grasps the whole evaluation as ONE node; WORKING sees its 3 sub-moves;
    # PLAIN decomposes those further (the strip + the functional-equation IBP expand most).
    d.step("Evaluate M[e^{-x}](s) = Γ(s)", requires="expert",
           prose=r"Insert $e^{-x}$ into the Mellin definition; the result is Euler's integral, which on the "
                 r"strip $\Re(s)>0$ is $\Gamma(s)$ (the functional equation $\Gamma(s+1)=s\Gamma(s)$ confirms it "
                 r"and continues it past the strip).",
           math=[r"M[e^{-x}](s)=\int_{0}^{\infty}x^{\,s-1}e^{-x}\,dx=\Gamma(s),\qquad \Re(s)>0"],
           references=["sub-method: Mellin transform definition → library/mellin-transform.md",
                       "sub-method: Gamma integral (Euler) → library/gamma-function.md"],
           decompose=[
               # ---- working sub-move 1: write the defining integral --------------------
               dict(title="Write the Mellin transform of e^{-x}", requires="working",
                    prose=r"Substitute $f(x)=e^{-x}$ into the Mellin definition to get the explicit integral.",
                    math=[r"M[e^{-x}](s)=\int_{0}^{\infty}x^{\,s-1}e^{-x}\,dx"],
                    references=["sub-method: Mellin transform definition → library/mellin-transform.md"],
                    decompose=[
                        dict(title="Recall the definition", requires="plain",
                             prose=r"The Mellin transform takes a function and produces a function of $s$ by "
                                   r"integrating it against $x^{s-1}$ from $0$ to $\infty$.",
                             math=[r"M[f](s)=\int_{0}^{\infty}x^{\,s-1}f(x)\,dx"],
                             references=["base → library/mellin-transform.md"]),
                        dict(title="Plug in f(x) = e^{-x}", requires="plain",
                             prose=r"Replace $f(x)$ by $e^{-x}$ inside the integral — nothing else changes.",
                             math=[r"M[e^{-x}](s)=\int_{0}^{\infty}x^{\,s-1}e^{-x}\,dx"],
                             references=["base → library/exponential-function.md"]),
                    ]),
               # ---- working sub-move 2: identify it as Euler's Gamma integral ----------
               dict(title="Identify it as Euler's Gamma integral", requires="working",
                    prose=r"This exact integral is the standard (Euler, second-kind) definition of $\Gamma(s)$.",
                    math=[r"\Gamma(s):=\int_{0}^{\infty}x^{\,s-1}e^{-x}\,dx\ \Rightarrow\ M[e^{-x}](s)=\Gamma(s)"],
                    references=["sub-method: Gamma integral (Euler) → library/gamma-function.md"],
                    decompose=[
                        dict(title="Match the integrand to the Gamma template", requires="plain",
                             prose=r"Our integrand $x^{s-1}e^{-x}$ is term-for-term the integrand in the "
                                   r"definition of $\Gamma(s)$, so the two integrals are the same.",
                             math=[r"\underbrace{x^{\,s-1}e^{-x}}_{\text{ours}}=\underbrace{x^{\,s-1}e^{-x}}_{\Gamma\text{-integrand}}"],
                             references=["base → library/gamma-function.md"]),
                        dict(title="Sanity check at s = 1 (a high-school integral)", requires="plain",
                             prose=r"At $s=1$ the power $x^{s-1}=x^{0}=1$, so the integral is just $\int_0^\infty "
                                   r"e^{-x}dx=1$, and indeed $\Gamma(1)=0!=1$.",
                             math=[r"\Gamma(1)=\int_{0}^{\infty}e^{-x}\,dx=\big[-e^{-x}\big]_{0}^{\infty}=1"],
                             references=["base → library/integration-by-parts.md"]),
                    ]),
               # ---- working sub-move 3: name the strip + confirm by the recursion ------
               dict(title="State the strip and confirm by the functional equation", requires="working",
                    prose=r"The integral converges for $\Re(s)>0$ (the fundamental strip); one integration by "
                          r"parts gives $\Gamma(s+1)=s\,\Gamma(s)$, which both confirms the identification and "
                          r"continues $\Gamma$ to the rest of the plane.",
                    math=[r"\Re(s)>0;\qquad \Gamma(s+1)=s\,\Gamma(s)"],
                    references=["sub-method: convergence of an improper integral → library/improper-integrals.md",
                                "sub-method: integration by parts → library/integration-by-parts.md"],
                    decompose=[
                        dict(title="Why the strip is Re(s) > 0 (the endpoint at 0)", requires="plain",
                             prose=r"Near $x=0$, $e^{-x}\approx 1$, so the integrand behaves like $x^{s-1}$; "
                                   r"$\int_0 x^{s-1}dx$ is finite only when the power $s-1>-1$, i.e. $s>0$.",
                             math=[r"\int_{0}x^{\,s-1}\,dx\ \text{converges}\iff s-1>-1\iff \Re(s)>0"],
                             references=["base → library/improper-integrals.md"]),
                        dict(title="Why the tail at infinity is harmless", requires="plain",
                             prose=r"For large $x$ the factor $e^{-x}$ decays faster than any power $x^{s-1}$ "
                                   r"grows, so the upper end always converges.",
                             math=[r"x^{\,s-1}e^{-x}\xrightarrow[x\to\infty]{}0\ \text{fast}\ \Rightarrow\ "
                                   r"\int^{\infty}\text{converges}"],
                             references=["base → library/improper-integrals.md"]),
                        dict(title="One integration by parts gives the recursion", requires="plain",
                             prose=r"Take $u=x^{s},\ dv=e^{-x}dx$, so $du=s\,x^{s-1}dx,\ v=-e^{-x}$; the boundary "
                                   r"term vanishes and what remains is $s\,\Gamma(s)$.",
                             math=[r"\Gamma(s+1)=\int_{0}^{\infty}x^{s}e^{-x}dx="
                                   r"\big[-x^{s}e^{-x}\big]_{0}^{\infty}+s\!\int_{0}^{\infty}x^{\,s-1}e^{-x}dx=s\,\Gamma(s)"],
                             references=["base → library/integration-by-parts.md"]),
                    ]),
           ])

    # --- VERIFY (independent of the derivation) ------------------------------------------
    F, strip, cond = sm.mellin_transform_of(sp.exp(-sp.Symbol("x", positive=True)))
    d.verify(
        r"Independent check by the engine itself: $\texttt{sp.mellin\_transform}(e^{-x},x,s)$ returns the "
        r"closed form, its fundamental strip, and the convergence condition — matching $\Gamma(s)$ on "
        r"$\Re(s)>0$ without using our hand derivation.",
        math=[r"\texttt{special\_methods.mellin\_transform\_of}(e^{-x}) = \big(" + sp.latex(F)
              + r",\ " + sp.latex(strip) + r",\ " + sp.latex(cond) + r"\big)"],
        references=["engine: special_methods.mellin_transform_of (sp.mellin_transform)",
                    "external gate: en.wikipedia.org/wiki/Mellin_transform → M[e^{-x}](s)=Γ(s)",
                    "method: library/mellin-transform.md"])
    d.result(latex=r"M[e^{-x}](s)=\int_{0}^{\infty}x^{\,s-1}e^{-x}\,dx=\Gamma(s)\quad(\Re(s)>0)",
             note="engine-verified: sp.mellin_transform(e^{-x}) = (Γ(s), strip (0,∞), cond True).")
    return d

def main():
    d = build_mellin_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    rwarn = validate_references(tracks)
    print("level counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[]  -> VALID (no warnings)")
    print("validate_references:", rwarn if rwarn else "[]  -> VALID (every library/ ref resolves)")
    print("counts differ:", len(set(counts.values())) > 1)
    assert not qwarn, qwarn
    assert not rwarn, rwarn
    assert len(set(counts.values())) > 1, counts
