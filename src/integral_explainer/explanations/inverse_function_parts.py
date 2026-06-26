"""Leveled Derivation for method inverse_function_parts (lifted from the gap-closing build, rule 7/11)."""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

def build_inverse_function_parts_derivation() -> Derivation:
    """Leveled Derivation for METHOD inverse_function_parts, worked on the cleanest
    representative  int acosh(2x) dx = x acosh(2x) - sqrt(4x^2-1)/2.

    Mirrors the ACTUAL engine route (rule 10): search picks _inverse_function_parts
    (u=acosh(2x), dv=dx -> v=x), giving x acosh(2x) - int x*(2/sqrt(4x^2-1)) dx, whose
    remaining radical integral is closed by direct(CAS). The tree is cut by `requires`:
      EXPERT  grasps "one IBP with u=the inverse function" as a single node;
      WORKING sees pick-u/dv, apply-the-formula, finish-the-radical-integral;
      PLAIN   decomposes each of those to high-school nodes with library refs.
    So the per-level step COUNTS emerge from the cut and differ."""
    problem = Problem(
        latex=r"\int \operatorname{arcosh}(2x)\,dx",
        represents="an inverse hyperbolic function alone — the inverse-function integration-by-parts case",
        goal=Goal.EVALUATE,
        integral=r"\operatorname{arcosh}(2x)",
    )
    d = Derivation(problem)

    # 1) WHY THIS APPROACH ------------------------------------------------------------------
    d.why(
        "Why integration by parts with the inverse function as u",
        {"plain": r"There is no simple antiderivative you can write down for $\operatorname{arcosh}(2x)$ — "
                  r"it is an inverse function, built to *undo* $\cosh$, not to be integrated directly. But it "
                  r"has one very useful feature: when you DIFFERENTIATE it you get a plain algebraic fraction "
                  r"with a square root, $2/\sqrt{4x^2-1}$, which we *do* know how to integrate. Integration by "
                  r"parts lets us trade the inverse function for its (much friendlier) derivative.",
         "working": r"The integrand is a lone inverse-hyperbolic function of a linear argument. A computer "
                    r"algebra system fails on it directly. But $\tfrac{d}{dx}\operatorname{arcosh}(2x)$ is "
                    r"algebraic ($2/\sqrt{4x^2-1}$), so choosing $u=\operatorname{arcosh}(2x)$ and $dv=dx$ in "
                    r"$\int u\,dv=uv-\int v\,du$ converts the transcendental integral into a rational-times-radical "
                    r"one the CAS can finish.",
         "expert": r"$\operatorname{arcosh}(2x)$ has no elementary antiderivative by direct integration, but its "
                   r"derivative is algebraic. With $u=\operatorname{arcosh}(2x),\,dv=dx$, one IBP pass sends the "
                   r"problem to $\int x\cdot 2/\sqrt{4x^2-1}\,dx$, an elementary radical integral; for $x^n$-weighted "
                   r"or squared inverse factors the same edge recurses."},
        forced_by=r"the integrand is a single inverse-hyperbolic function — there is no product to $u$-substitute and "
                  r"no elementary antiderivative by inspection; what IS available is that differentiating the inverse "
                  r"function yields a purely algebraic $1/\sqrt{\,}$ factor, exactly the move integration by parts "
                  r"rewards.",
        payoff=r"one IBP pass replaces the un-integrable $\operatorname{arcosh}$ by an algebraic radical integral that "
               r"$\int$ closes in elementary terms; the closed form $x\operatorname{arcosh}(2x)-\tfrac12\sqrt{4x^2-1}$ "
               r"exposes the $\sqrt{4x^2-1}$ structure a bare number would destroy.",
        relies_on=r"the parts identity $\int u\,dv=uv-\int v\,du$ (the product rule integrated), valid here because "
                  r"$u=\operatorname{arcosh}(2x)$ and $v=x$ are continuously differentiable on the domain $2x>1$.",
    )

    # 2) HOW THE APPROACH WORKS -------------------------------------------------------------
    d.how(
        "How it works — parts with the inverse factor as u, and its algebraic derivative",
        {"plain": r"Integration by parts says $\int u\,dv=uv-\int v\,du$. Here the whole integrand is the part to "
                  r"differentiate: $u=\operatorname{arcosh}(2x)$, and $dv=dx$ (so $v=x$). Differentiating $u$ removes "
                  r"the inverse function and leaves an algebraic square-root fraction, so the leftover integral "
                  r"$\int v\,du$ is something we can actually do.",
         "working": r"$\int u\,dv=uv-\int v\,du$ with $u=\operatorname{arcosh}(2x),\,dv=dx$. Then $v=x$ and "
                    r"$du=\tfrac{2}{\sqrt{4x^2-1}}\,dx$; the residual $\int v\,du=\int \tfrac{2x}{\sqrt{4x^2-1}}\,dx$ "
                    r"is a standard radical integral.",
         "expert": r"Parts with $u=\operatorname{arcosh}(2x),\,dv=dx$ ($v=x$, $du=2/\sqrt{4x^2-1}\,dx$); the residual "
                   r"$\int 2x/\sqrt{4x^2-1}\,dx=\sqrt{4x^2-1}$ closes immediately."},
        math=[r"\int u\,dv=u\,v-\int v\,du,\qquad u=\operatorname{arcosh}(2x),\quad dv=dx,\quad "
              r"du=\frac{2}{\sqrt{4x^2-1}}\,dx,\quad v=x"],
    )

    # 3) THE STEPS — one qualification tree; counts EMERGE from the `requires` cut ----------
    d.step(
        "Evaluate by one integration by parts with u = arcosh(2x)",
        requires="expert",
        prose=r"Take $u=\operatorname{arcosh}(2x),\ dv=dx$, so $v=x,\ du=\tfrac{2}{\sqrt{4x^2-1}}dx$; then "
              r"$\int\operatorname{arcosh}(2x)\,dx = x\operatorname{arcosh}(2x)-\int\tfrac{2x}{\sqrt{4x^2-1}}\,dx "
              r"= x\operatorname{arcosh}(2x)-\tfrac12\sqrt{4x^2-1}$.",
        math=[r"\int\operatorname{arcosh}(2x)\,dx=x\operatorname{arcosh}(2x)-\int\frac{2x}{\sqrt{4x^2-1}}\,dx"
              r"=x\operatorname{arcosh}(2x)-\frac12\sqrt{4x^2-1}"],
        references=["sub-method: inverse_function_parts (this strategy's IBP edge)"],
        decompose=[
            # ---- WORKING step A: choose the parts -------------------------------------
            dict(title="Choose u = the inverse function and dv = dx", requires="working",
                 prose=r"With no product to split, take the inverse function itself as $u$ and $dv=dx$. Then $v=x$, "
                       r"and $du$ is the algebraic derivative of the inverse function.",
                 math=[r"u=\operatorname{arcosh}(2x),\quad dv=dx\ \Rightarrow\ v=x,\quad "
                       r"du=\frac{2}{\sqrt{4x^2-1}}\,dx"],
                 references=["sub-method: LIATE — Inverse function is the highest-priority u"],
                 decompose=[
                     dict(title="Differentiate u (the inverse-function derivative)", requires="plain",
                          prose=r"The derivative of $\operatorname{arcosh}(t)$ is $1/\sqrt{t^2-1}$; with $t=2x$ the "
                                r"chain rule multiplies by $2$, giving $2/\sqrt{4x^2-1}$.",
                          math=[r"\frac{d}{dx}\operatorname{arcosh}(2x)=\frac{2}{\sqrt{(2x)^2-1}}=\frac{2}{\sqrt{4x^2-1}}"],
                          references=["base -> library/inverse-hyperbolic-derivatives.md"]),
                     dict(title="Integrate dv to get v", requires="plain",
                          prose=r"Integrating $dv=dx$ just gives $v=x$.",
                          math=[r"v=\int dx=x"],
                          references=["base -> library/power-rule.md"]),
                 ]),
            # ---- WORKING step B: apply the parts formula ------------------------------
            dict(title="Apply the parts formula", requires="working",
                 prose=r"Substitute into $\int u\,dv=uv-\int v\,du$. The product $uv$ is $x\operatorname{arcosh}(2x)$; "
                       r"the leftover integral has $v\,du=\tfrac{2x}{\sqrt{4x^2-1}}dx$.",
                 math=[r"\int\operatorname{arcosh}(2x)\,dx=\underbrace{x\,\operatorname{arcosh}(2x)}_{uv}"
                       r"-\int\underbrace{x}_{v}\cdot\underbrace{\frac{2}{\sqrt{4x^2-1}}\,dx}_{du}"],
                 references=["sub-method: parts formula \\int u\\,dv=uv-\\int v\\,du"],
                 decompose=[
                     dict(title="Form the uv term", requires="plain",
                          prose=r"Multiply $u=\operatorname{arcosh}(2x)$ by $v=x$.",
                          math=[r"u\,v=x\,\operatorname{arcosh}(2x)"]),
                     dict(title="Form the leftover integral", requires="plain",
                          prose=r"The subtracted piece is $\int v\,du=\int x\cdot\tfrac{2}{\sqrt{4x^2-1}}\,dx$.",
                          math=[r"\int v\,du=\int\frac{2x}{\sqrt{4x^2-1}}\,dx"]),
                 ]),
            # ---- WORKING step C: finish the radical integral (direct/CAS) -------------
            dict(title="Finish the leftover radical integral", requires="working",
                 prose=r"The residual $\int \tfrac{2x}{\sqrt{4x^2-1}}\,dx$ is elementary — this is what the engine "
                       r"closes with its direct/CAS edge. The numerator is the derivative of the radicand up to a "
                       r"constant, so the integral is the square root itself: $\sqrt{4x^2-1}$.",
                 math=[r"\int\frac{2x}{\sqrt{4x^2-1}}\,dx=\sqrt{4x^2-1}"],
                 references=["sub-method: direct(CAS) / strategies._direct (sp.integrate)"],
                 decompose=[
                     dict(title="Recognise a derivative-over-its-root", requires="plain",
                          prose=r"Let $w=4x^2-1$; then $dw=8x\,dx$, so $2x\,dx=\tfrac14 dw$ and the integral is "
                                r"$\int \tfrac14 w^{-1/2}\,dw$.",
                          math=[r"w=4x^2-1,\ dw=8x\,dx\ \Rightarrow\ \int\frac{2x}{\sqrt{4x^2-1}}\,dx"
                                r"=\frac14\int w^{-1/2}\,dw"],
                          references=["base -> library/u-substitution.md"]),
                     dict(title="Integrate the power and back-substitute", requires="plain",
                          prose=r"$\int w^{-1/2}dw=2\sqrt{w}$; the $\tfrac14$ and the $2$ combine to $\tfrac12$, then "
                                r"restore $w=4x^2-1$.",
                          math=[r"\frac14\cdot 2\sqrt{w}=\frac12\sqrt{w}=\frac12\sqrt{4x^2-1}\cdot 2=\sqrt{4x^2-1}"],
                          references=["base -> library/power-rule.md"]),
                 ]),
        ],
    )

    # VERIFY (independent of the derivation) ------------------------------------------------
    d.verify(
        r"Differentiate the claimed antiderivative and check it returns the integrand (the product rule run "
        r"forwards). Independent of how the answer was derived, and it also matches the published Wikipedia "
        r"table row $\int\operatorname{arcosh}(ax)\,dx=x\operatorname{arcosh}(ax)-\sqrt{a^2x^2-1}/a$ at $a=2$.",
        math=[r"\frac{d}{dx}\!\left(x\operatorname{arcosh}(2x)-\tfrac12\sqrt{4x^2-1}\right)"
              r"=\operatorname{arcosh}(2x)+\frac{2x}{\sqrt{4x^2-1}}-\frac{1}{2}\cdot\frac{8x}{2\sqrt{4x^2-1}}"
              r"=\operatorname{arcosh}(2x)\ \checkmark"],
        references=["check: differentiate the antiderivative (and match Wikipedia table)",
                    "engine: search -> route ['inverse_function_parts','direct(CAS)']"],
    )
    d.result(
        latex=r"\int\operatorname{arcosh}(2x)\,dx=x\operatorname{arcosh}(2x)-\frac12\sqrt{4x^2-1}\ (+C)",
        note="one integration by parts (u=arcosh(2x), dv=dx) + a direct radical integral; "
             "verified by differentiating back and matching the Wikipedia table.",
    )
    return d
