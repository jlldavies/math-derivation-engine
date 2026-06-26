"""Leveled Derivation for method hyperbolic_exp_rewrite (lifted from the gap-closing build, rule 7/11)."""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = r"\int \operatorname{sech}^2 x\,dx \;=\; \tanh x + C"

def build_hyperbolic_exp_rewrite_derivation():
    problem = Problem(
        latex=HDR,
        represents=r"a hyperbolic integrand SymPy returns unevaluated; rewrite to $e^x$ form",
        goal=Goal.EVALUATE,
        integral=r"\int \operatorname{sech}^2 x\,dx")
    d = Derivation(problem)

    # ---- WHY (the recognition / decision) --------------------------------------------
    d.why("Why this approach — rewrite the hyperbolic to exponentials",
          {"plain": r"The CAS just hands $\int\operatorname{sech}^2 x\,dx$ straight back, "
                    r"unsolved. But $\operatorname{sech} x$ is only shorthand for "
                    r"$2/(e^x+e^{-x})$. If we write it out in $e^x$, the integrand becomes an "
                    r"ordinary fraction the CAS knows how to integrate.",
           "working": r"$\operatorname{sech}^2 x$ is left unevaluated by the direct integrator, "
                      r"but it is an exact rational function of $e^x$. Substituting the defining "
                      r"exponential identity turns a stuck hyperbolic integral into a rational "
                      r"integral in $u=e^x$ that the CAS resolves.",
           "expert": r"The direct integrator stalls on $\operatorname{sech}^2 x$; rewriting via "
                     r"$\operatorname{sech} x=2/(e^x+e^{-x})$ maps the integrand into "
                     r"$\mathbb{Q}(e^x)$, where elementary integration is decidable (Risch over "
                     r"the rational tower), so the CAS catch-all closes it."},
          forced_by=r"the direct(CAS) edge returns $\int\operatorname{sech}^2 x\,dx$ "
                    r"UNEVALUATED — the integral atom survives, so search must transform the "
                    r"STATE rather than ask the same integrator again.",
          payoff=r"one exact rewrite converts a stuck hyperbolic form into a rational function of "
                 r"$e^x$, which direct(CAS) integrates in a single further step; we trade a "
                 r"special-function wall for ordinary partial-fraction territory.",
          relies_on=r"$\operatorname{sech} x=2/(e^x+e^{-x})$ is an identity (not an approximation), "
                    r"so the rewritten integrand is EQUAL to the original; the resulting "
                    r"antiderivative is therefore correct, though written in $e^x$ and free to "
                    r"differ from $\tanh x$ by a constant.")

    # ---- HOW (the machinery) ---------------------------------------------------------
    d.how("How the approach works — the exponential identity feeds the CAS",
          {"plain": r"Replace each hyperbolic function by its $e^x$ formula, then let the CAS "
                    r"integrate the resulting fraction.",
           "working": r"Apply `.rewrite(exp)` to the integrand (the exact identities), producing a "
                      r"rational function of $e^x$; hand that new integral to direct(CAS).",
           "expert": r"The strategy emits a new search state $\int g(e^x)\,dx$ with "
                     r"$g\in\mathbb{Q}(e^x)$; the existing direct(CAS) edge then finishes it, so "
                     r"this method is a single graph edge feeding the CAS catch-all."},
          math=[r"\operatorname{sech} x=\frac{2}{e^{x}+e^{-x}},\qquad "
                r"\operatorname{sech}^2 x=\frac{4}{(e^{x}+e^{-x})^{2}}"])

    # ---- STEPS (worked execution; tree -> emergent per-level counts) -----------------
    d.step("Rewrite and integrate", requires="expert",
           prose=r"Rewrite $\operatorname{sech}^2 x$ in exponentials, integrate the rational "
                 r"function of $e^x$, and reconcile the $e^x$ antiderivative with $\tanh x$.",
           math=[r"\int\operatorname{sech}^2 x\,dx=\int\frac{4}{(e^{x}+e^{-x})^{2}}\,dx="
                 r"-\frac{2}{e^{2x}+1}=\tanh x-1"],
           decompose=[
               dict(title="Apply the exponential identity", requires="plain",
                    prose=r"Write $\operatorname{sech} x=2/(e^x+e^{-x})$, so its square is "
                          r"$4/(e^x+e^{-x})^2$ — a plain fraction built from $e^x$.",
                    math=[r"\operatorname{sech}^2 x=\left(\frac{2}{e^{x}+e^{-x}}\right)^{2}"
                          r"=\frac{4}{(e^{x}+e^{-x})^{2}}"],
                    references=["base method -> library/hyperbolic-definitions.md"]),
               dict(title="Reduce to a rational function of e^x", requires="working",
                    prose=r"Multiply top and bottom by $e^{2x}$ to clear the $e^{-x}$; the "
                          r"integrand becomes a rational function of $u=e^x$, which the CAS "
                          r"integrates directly.",
                    math=[r"\frac{4}{(e^{x}+e^{-x})^{2}}=\frac{4e^{2x}}{(e^{2x}+1)^{2}}"],
                    decompose=[
                        dict(title="Clear the negative exponent", requires="plain",
                             prose=r"$(e^x+e^{-x})^2=e^{2x}(1+e^{-2x})^2$; multiplying through by "
                                   r"$e^{2x}$ removes every negative power.",
                             math=[r"\frac{4}{(e^{x}+e^{-x})^{2}}\cdot\frac{e^{2x}}{e^{2x}}"
                                   r"=\frac{4e^{2x}}{(e^{2x}+1)^{2}}"]),
                        dict(title="Now it is rational in u = e^x", requires="plain",
                             prose=r"With $u=e^x$ the integrand is $4u^2/(u^2+1)^2$ times $du/u$ "
                                   r"— a rational function direct(CAS) can integrate.",
                             math=[r"\int\frac{4e^{2x}}{(e^{2x}+1)^{2}}\,dx,\quad u=e^{x}"],
                             references=["base method -> library/rational-integration.md"]),
                    ]),
               dict(title="The CAS antiderivative", requires="working",
                    prose=r"direct(CAS) returns $-2/(e^{2x}+1)$. Its derivative is "
                          r"$4e^{2x}/(e^{2x}+1)^2$ — exactly the rewritten integrand — so it is a "
                          r"valid antiderivative.",
                    math=[r"\frac{d}{dx}\!\left(\frac{-2}{e^{2x}+1}\right)"
                          r"=\frac{4e^{2x}}{(e^{2x}+1)^{2}}=\operatorname{sech}^2 x"],
                    references=["engine -> direct(CAS) integrator"],
                    decompose=[
                        dict(title="What the CAS gives back", requires="plain",
                             prose=r"The CAS integrates the fraction and returns the simple "
                                   r"answer $-2/(e^{2x}+1)$.",
                             math=[r"\int\operatorname{sech}^2 x\,dx=\frac{-2}{e^{2x}+1}"],
                             references=["engine -> direct(CAS) integrator"]),
                        dict(title="Check by differentiating back", requires="plain",
                             prose=r"Differentiate the answer; you get the integrand back, so the "
                                   r"answer is right.",
                             math=[r"\frac{d}{dx}\!\left(\frac{-2}{e^{2x}+1}\right)"
                                   r"=\frac{4e^{2x}}{(e^{2x}+1)^{2}}=\operatorname{sech}^2 x"],
                             references=["base method -> library/differentiation-check.md"]),
                    ]),
               dict(title="Reconcile with the published tanh x", requires="working",
                    prose=r"The CAS form differs from the published $\tanh x$ only by a constant: "
                          r"$-2/(e^{2x}+1)=\tanh x-1$. An antiderivative is unique up to $+C$, so "
                          r"both are correct.",
                    math=[r"\tanh x=\frac{e^{2x}-1}{e^{2x}+1}=1-\frac{2}{e^{2x}+1}"
                          r"\;\Rightarrow\;\frac{-2}{e^{2x}+1}=\tanh x-1"],
                    decompose=[
                        dict(title="Why a constant is allowed", requires="plain",
                             prose=r"Two functions with the same derivative differ by a constant, "
                                   r"so a $-1$ between them does not change correctness.",
                             math=[r"\frac{d}{dx}(\tanh x-1)=\operatorname{sech}^2 x"
                                   r"=\frac{d}{dx}\!\left(\frac{-2}{e^{2x}+1}\right)"],
                             references=["base method -> library/constant-of-integration.md"]),
                    ]),
           ])

    d.verify(
        r"Two independent checks, neither used to DERIVE the result. Symbolically, "
        r"$d/dx$ of the engine answer (rewritten to $e^x$) minus the integrand simplifies to $0$; "
        r"and the engine answer equals the published $\tanh x$ up to the additive constant $-1$.",
        math=[r"\frac{d}{dx}\!\left(\frac{-2}{e^{2x}+1}\right)-\operatorname{sech}^2 x=0,\qquad "
              r"\frac{-2}{e^{2x}+1}-\tanh x=-1=\text{const}"],
        references=["symbolic check: sp.diff(result)-integrand rewritten to exp -> 0",
                    "published: en.wikipedia.org/wiki/List_of_integrals_of_hyperbolic_functions",
                    "method: library/hyperbolic-exp-rewrite.md"])

    d.result(latex=r"\int\operatorname{sech}^2 x\,dx=\frac{-2}{e^{2x}+1}=\tanh x+C",
             note="engine-produced via rewrite(exp)+direct(CAS); verified d/dx==integrand and "
                  "==tanh x up to the constant -1.")
    return d
