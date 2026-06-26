"""Leveled Derivation for METHOD: parts (integration by parts), worked on
    ∫ x e^{6x} dx = x e^{6x}/6 - e^{6x}/36.

Mirrors the ACTUAL engine computation (CLAUDE.md rule 10 — we explain what the
engine runs, we do not hand-solve and feed an answer in):

  strategies.solve_integral(x*exp(6*x))  searches the integration strategies; the
  winning route uses strategies._by_parts (M_PARTS), the LIATE-ish edge that picks
  the polynomial/log factor as u:

      _by_parts:  u = x   (the polynomial factor),  dv = e^{6x} dx
                  v = ∫ dv = e^{6x}/6                          (sp.integrate(dv, x))
                  ∫ = u·v − ∫ v du = x e^{6x}/6 − ∫ e^{6x}/6 dx

  then the remaining ∫ e^{6x}/6 dx is closed by the CAS catch-all  direct(CAS)
  ( = strategies._direct → sp.integrate ) to e^{6x}/36, giving
      x e^{6x}/6 − e^{6x}/36.

The qualification tree is cut by `requires`:
  - EXPERT grasps "do one integration by parts" as a single node (1 worked step).
  - WORKING sees its sub-moves: pick u & dv (LIATE), apply the IBP formula, finish
    the leftover ∫v du.
  - PLAIN decomposes those further to high-school nodes (each ∫ done explicitly,
    each base move referencing a library page), so the count expands again.

Run:  python scratch/expl_parts.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

def build_parts_derivation() -> Derivation:
    problem = Problem(
        latex=r"\int x\,e^{6x}\,dx",
        represents="a polynomial times an exponential — the textbook integration-by-parts case",
        goal=Goal.EVALUATE,
        integral="x e^{6x}",
    )
    d = Derivation(problem)

    # 1) WHY THIS APPROACH ------------------------------------------------------------------
    d.why(
        "Why integration by parts",
        {"plain": r"The thing inside the integral is a product, $x$ times $e^{6x}$, and there is no "
                  r"simple antiderivative we can just write down. But one of the factors, $x$, gets "
                  r"*simpler* when you differentiate it (its derivative is just $1$), while the other, "
                  r"$e^{6x}$, is easy to integrate. Integration by parts trades the hard integral for "
                  r"an easier one by moving the derivative off $x$ and onto an antiderivative of $e^{6x}$.",
         "working": r"The integrand is a product of an algebraic factor and an exponential. There is no "
                    r"$u$-substitution (no inner function whose derivative also appears) and no elementary "
                    r"antiderivative by inspection. Integration by parts is the right edge: differentiating "
                    r"$x$ lowers its degree to a constant, terminating the recursion in one step.",
         "expert": r"$\int x e^{6x}dx$ is the canonical (algebraic)$\times$(transcendental) product with a "
                   r"degree-1 polynomial factor — LIATE selects $u=x$; one IBP pass reduces the polynomial "
                   r"to a constant and closes the integral."},
        forced_by=r"the integrand is a genuine product whose two factors call for opposite operations — $x$ "
                  r"wants differentiating (it simplifies to $1$), $e^{6x}$ wants integrating (it is closed under "
                  r"$\int$) — which is exactly the configuration integration by parts exploits; neither a direct "
                  r"antiderivative nor a $u$-substitution is available.",
        payoff=r"differentiating $x$ kills the polynomial factor after a single pass, so one application leaves "
               r"a pure exponential integral $\int e^{6x}dx$ that is elementary; the recursion terminates "
               r"immediately rather than regenerating a product.",
        relies_on=r"the product rule $(uv)'=u'v+uv'$ integrated over the interval — i.e. $\int u\,dv=uv-\int v\,du$ "
                  r"— which is valid here because $u=x$ and $v=e^{6x}/6$ are continuously differentiable everywhere.",
    )

    # 2) HOW THE APPROACH WORKS -------------------------------------------------------------
    d.how(
        "How it works — the parts formula and the LIATE choice",
        {"plain": r"Integration by parts says $\int u\,dv = uv-\int v\,du$. You split the product into a part to "
                  r"differentiate ($u$) and a part to integrate ($dv$). Choose $u=x$ (because differentiating it "
                  r"makes it simpler) and $dv=e^{6x}dx$ (because it is easy to integrate). Then you assemble the "
                  r"formula and the leftover integral is simpler than the one you started with.",
         "working": r"$\int u\,dv=uv-\int v\,du$. By LIATE we take $u$ = the Algebraic factor $x$ and "
                    r"$dv=e^{6x}dx$; then $du=dx$ and $v=\tfrac16 e^{6x}$, and the residual $\int v\,du$ carries "
                    r"a polynomial of one lower degree.",
         "expert": r"Parts: $\int u\,dv=uv-\int v\,du$ with the LIATE pick $u=x,\,dv=e^{6x}dx$ "
                   r"($du=dx,\ v=e^{6x}/6$); the residual is a bare exponential integral."},
        math=[r"\int u\,dv = u\,v-\int v\,du,\qquad u=x,\quad dv=e^{6x}\,dx"],
    )

    # 3) THE STEPS — one qualification tree; counts EMERGE from the `requires` cut ----------
    #    EXPERT: the whole IBP pass is ONE node (requires="expert").
    #    WORKING: it decomposes into pick-u/dv, apply-formula, finish-leftover.
    #    PLAIN: each of those decomposes again into high-school nodes w/ base refs.
    d.step(
        "Evaluate by one integration by parts",
        requires="expert",
        prose=r"Take $u=x,\ dv=e^{6x}dx$, so $du=dx,\ v=\tfrac16 e^{6x}$; then "
              r"$\int x e^{6x}dx = uv-\int v\,du = \tfrac{x}{6}e^{6x}-\tfrac16\int e^{6x}dx "
              r"= \tfrac{x}{6}e^{6x}-\tfrac{1}{36}e^{6x}$.",
        math=[r"\int x\,e^{6x}\,dx=\frac{x}{6}e^{6x}-\frac16\int e^{6x}\,dx=\frac{x}{6}e^{6x}-\frac{1}{36}e^{6x}"],
        references=["sub-method: parts (strategies._by_parts / M_PARTS)"],
        decompose=[
            # ---- WORKING step A: choose the parts (LIATE) -------------------------------
            dict(title="Choose u and dv by LIATE", requires="working",
                 prose=r"Split the product so that the factor that *simplifies under differentiation* is $u$. "
                       r"The polynomial $x$ is $u$; the exponential is $dv$. Then compute $du$ and $v$.",
                 math=[r"u=x,\quad dv=e^{6x}\,dx\ \Rightarrow\ du=dx,\quad v=\int e^{6x}\,dx=\frac{e^{6x}}{6}"],
                 references=["sub-method: LIATE factor-ordering rule"],
                 decompose=[
                     dict(title="Differentiate u", requires="plain",
                          prose=r"The derivative of $x$ is $1$, so $du=dx$.",
                          math=[r"\frac{d}{dx}x=1\ \Rightarrow\ du=dx"],
                          references=["base -> library/power-rule.md"]),
                     dict(title="Integrate dv to get v", requires="plain",
                          prose=r"An exponential $e^{6x}$ integrates to itself divided by the constant $6$ from "
                                r"the chain rule.",
                          math=[r"v=\int e^{6x}\,dx=\frac{e^{6x}}{6}"],
                          references=["base -> library/exponential-integral.md"]),
                 ]),
            # ---- WORKING step B: apply the parts formula -------------------------------
            dict(title="Apply the parts formula", requires="working",
                 prose=r"Substitute $u,v,du$ into $\int u\,dv=uv-\int v\,du$. The boundary product $uv$ is "
                       r"$\tfrac{x}{6}e^{6x}$; the leftover integral has $v\,du=\tfrac16 e^{6x}dx$.",
                 math=[r"\int x\,e^{6x}\,dx=\underbrace{\frac{x}{6}e^{6x}}_{uv}"
                       r"-\int \underbrace{\frac{e^{6x}}{6}}_{v}\underbrace{dx}_{du}"],
                 references=["sub-method: parts formula \\int u\\,dv=uv-\\int v\\,du"],
                 decompose=[
                     dict(title="Form the uv term", requires="plain",
                          prose=r"Multiply $u=x$ by $v=\tfrac16 e^{6x}$.",
                          math=[r"u\,v=x\cdot\frac{e^{6x}}{6}=\frac{x}{6}e^{6x}"]),
                     dict(title="Form the leftover integral", requires="plain",
                          prose=r"The piece subtracted is $\int v\,du=\int \tfrac16 e^{6x}\,dx$.",
                          math=[r"\int v\,du=\int\frac{e^{6x}}{6}\,dx=\frac16\int e^{6x}\,dx"]),
                 ]),
            # ---- WORKING step C: finish the leftover integral (direct/CAS) --------------
            dict(title="Finish the leftover exponential integral", requires="working",
                 prose=r"The remaining $\tfrac16\int e^{6x}dx$ is elementary (this is what the engine closes "
                       r"with its direct/CAS edge): $\int e^{6x}dx=\tfrac16 e^{6x}$, so the term is "
                       r"$\tfrac{1}{36}e^{6x}$.",
                 math=[r"\frac16\int e^{6x}\,dx=\frac16\cdot\frac{e^{6x}}{6}=\frac{1}{36}e^{6x}"],
                 references=["sub-method: direct(CAS) / strategies._direct (sp.integrate)"],
                 decompose=[
                     dict(title="Integrate the exponential", requires="plain",
                          prose=r"Again $\int e^{6x}dx=\tfrac16 e^{6x}$ by the same exponential rule.",
                          math=[r"\int e^{6x}\,dx=\frac{e^{6x}}{6}"],
                          references=["base -> library/exponential-integral.md"]),
                     dict(title="Multiply the constants", requires="plain",
                          prose=r"Combine the $\tfrac16$ in front with the $\tfrac16$ from the integral.",
                          math=[r"\frac16\cdot\frac{e^{6x}}{6}=\frac{1}{36}e^{6x}"]),
                 ]),
        ],
    )

    # VERIFY (independent of the derivation) ------------------------------------------------
    d.verify(
        r"Differentiate the claimed antiderivative and check it returns the integrand (the product rule "
        r"run forwards). This is an independent check, not how the answer was derived.",
        math=[r"\frac{d}{dx}\!\left(\frac{x}{6}e^{6x}-\frac{1}{36}e^{6x}\right)"
              r"=\frac16 e^{6x}+\frac{x}{6}\cdot 6e^{6x}-\frac{1}{36}\cdot 6e^{6x}"
              r"=\frac16 e^{6x}+x e^{6x}-\frac16 e^{6x}=x e^{6x}\ \checkmark"],
        references=["check: differentiate the antiderivative (product rule)",
                    "engine: strategies.solve_integral -> route ['parts','direct(CAS)']"],
    )
    d.result(
        latex=r"\int x\,e^{6x}\,dx=\frac{x}{6}e^{6x}-\frac{1}{36}e^{6x}\ (+C)",
        note="one integration by parts (u=x, dv=e^{6x}dx) + a direct exponential integral; "
             "verified by differentiating back.",
    )
    return d
