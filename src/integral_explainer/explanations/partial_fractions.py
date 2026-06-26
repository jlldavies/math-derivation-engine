"""LEVELED Derivation for the `partial_fractions` method (CLAUDE.md rules 7 + 11), built
for the WORKED TARGET

    ∫ (3x+11)/(x^2 - x - 6) dx = 4 ln|x-3| - ln|x+2|.

It MIRRORS the engine's real computation (strategies._partial_fractions): the integrand is a
rational function, so the engine calls `sp.apart(g, x)` and re-integrates the decomposition.
`sp.apart` internally (1) FACTORS the denominator, then (2) solves for the cover-up/residue
coefficients of each simple fraction; the re-integration then (3) maps each 1/(x-a) -> ln|x-a|.
So the tree's three working moves are exactly: factor -> decompose (find A,B) -> integrate
term-by-term. Sub-methods referenced: polynomial factoring, the cover-up (residue) rule for the
coefficients, and the base antiderivative ∫dx/(x-a)=ln|x-a| (a u-substitution).

Run:  python scratch/expl_partial_fractions.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

import sympy as sp

HDR = r"\int \frac{3x+11}{x^{2}-x-6}\,dx"

def build_partial_fractions_derivation() -> Derivation:
    """A genuine why/how/step qualification tree for the worked partial-fractions target.

    The frontier cut by `requires` makes the per-level step counts EMERGE:
      - EXPERT grasps the whole 'split into simple fractions and integrate' as ONE node
        (requires='expert')  -> 1 step;
      - WORKING sees its three sub-moves: factor / find the coefficients / integrate
        (each requires='working')          -> 3 steps;
      - PLAIN decomposes those working moves further into high-school nodes (factor by
        finding the roots; cover-up for A then for B; each ∫dx/(x-a)=ln|x-a|; recombine)
                                            -> 7 steps.
    """
    problem = Problem(
        latex=HDR,
        represents="a proper rational function — degree(numerator) < degree(denominator)",
        goal=Goal.EVALUATE,
        integral="(3x+11)/(x^2-x-6)")
    d = Derivation(problem)

    # ---- WHY this approach (the recognition / decision) -----------------------------------
    d.why("Why this approach — split into partial fractions",
          {"plain": r"The integrand is one fraction of polynomials, and there is no simple "
                    r"antiderivative for it as written. But the bottom factors into two pieces, "
                    r"$(x-3)(x+2)$. We can rewrite the single awkward fraction as a SUM of two easy "
                    r"fractions $\frac{A}{x-3}+\frac{B}{x+2}$ — and each of those we already know how "
                    r"to integrate (it gives a logarithm).",
           "working": r"$\frac{3x+11}{x^{2}-x-6}$ is a proper rational function (numerator degree $1$ "
                      r"< denominator degree $2$) with a denominator that splits into distinct linear "
                      r"factors. Partial fractions turns it into $\frac{A}{x-3}+\frac{B}{x+2}$, a sum "
                      r"whose terms integrate to logarithms.",
           "expert": r"Proper rational integrand with squarefree denominator $\prod_i (x-a_i)$; "
                     r"the partial-fraction decomposition $\sum_i \frac{r_i}{x-a_i}$ (residues "
                     r"$r_i=N(a_i)/D'(a_i)$) reduces $\int$ to $\sum_i r_i\ln|x-a_i|$."},
          forced_by=r"the integrand is a PROPER rational function ($\deg N=1<\deg D=2$) and the "
                    r"denominator $x^{2}-x-6=(x-3)(x+2)$ is squarefree with two distinct real roots — "
                    r"exactly the case the simple-pole decomposition is built for.",
          payoff=r"the decomposition replaces one un-integrable-looking fraction by a sum of "
                 r"$\frac{r_i}{x-a_i}$ terms, each a textbook logarithm; the coefficients $4$ and "
                 r"$-1$ then carry the whole answer, which a single number would hide.",
          relies_on=r"the roots are DISTINCT (no repeated factor $\Rightarrow$ no $\frac{C}{(x-a)^2}$ "
                    r"terms) and the fraction is PROPER (else polynomial long division must precede "
                    r"the split). Both hold here.")

    # ---- HOW the approach works (the machinery) -------------------------------------------
    d.how("How the approach works — the cover-up decomposition",
          {"plain": r"Write the fraction as $\frac{A}{x-3}+\frac{B}{x+2}$. To find $A$, cover up the "
                    r"$(x-3)$ factor and put $x=3$ into what's left; to find $B$, cover up $(x+2)$ and "
                    r"put $x=-2$. Then integrate each simple piece.",
           "working": r"For distinct linear factors, $\frac{N(x)}{(x-3)(x+2)}=\frac{A}{x-3}+\frac{B}{x+2}$ "
                      r"with $A,B$ found by the cover-up rule: $A=\big[N(x)/(x+2)\big]_{x=3}$, "
                      r"$B=\big[N(x)/(x-3)\big]_{x=-2}$. Each term integrates via $\int\frac{dx}{x-a}=\ln|x-a|$.",
           "expert": r"Heaviside cover-up = the residue $r_i=\operatorname*{Res}_{x=a_i}\frac{N}{D}"
                     r"=\frac{N(a_i)}{D'(a_i)}$ at each simple pole; $\int\sum_i\frac{r_i}{x-a_i}\,dx"
                     r"=\sum_i r_i\ln|x-a_i|+C$."},
          math=[r"\frac{3x+11}{(x-3)(x+2)}=\frac{A}{x-3}+\frac{B}{x+2},\qquad "
                r"A=\left.\frac{3x+11}{x+2}\right|_{x=3},\ \ B=\left.\frac{3x+11}{x-3}\right|_{x=-2}"])

    # ---- THE STEPS (one qualification tree; per-level counts EMERGE from the cut) ----------
    #   expert  -> 1 (this whole node, requires='expert')
    #   working -> 3 (its three children, each requires='working')
    #   plain   -> 7 (the children's children, all requires='plain')
    d.step("Decompose into simple fractions and integrate", requires="expert",
           prose=r"Factor $x^{2}-x-6=(x-3)(x+2)$; the cover-up residues give $A=4,\ B=-1$, so "
                 r"$\frac{3x+11}{x^{2}-x-6}=\frac{4}{x-3}-\frac{1}{x+2}$; integrating term-by-term "
                 r"yields $4\ln|x-3|-\ln|x+2|$.",
           math=[r"\int\frac{3x+11}{x^{2}-x-6}\,dx=\int\!\Big(\frac{4}{x-3}-\frac{1}{x+2}\Big)dx"
                 r"=4\ln|x-3|-\ln|x+2|+C"],
           references=["method: library/partial-fractions.md"],
           decompose=[
               # ---- working move 1: factor the denominator ----------------------------------
               dict(title="Factor the denominator", requires="working",
                    prose=r"Factor $x^{2}-x-6$ into linear pieces — the engine's first move inside "
                          r"`sp.apart` — so the simple-pole template applies.",
                    math=[r"x^{2}-x-6=(x-3)(x+2)"],
                    references=["sub-method: factoring -> library/factor-quadratic.md"],
                    decompose=[
                        dict(title="Find the roots of the quadratic", requires="plain",
                             prose=r"Solve $x^{2}-x-6=0$; two numbers multiplying to $-6$ and adding to "
                                   r"$-1$ are $-3$ and $+2$, so the roots are $x=3$ and $x=-2$.",
                             math=[r"x^{2}-x-6=0\ \Rightarrow\ (x-3)(x+2)=0\ \Rightarrow\ x=3,\ x=-2"],
                             references=["base -> library/factor-quadratic.md"]),
                    ]),
               # ---- working move 2: find the coefficients A, B (the apart() solve) ----------
               dict(title="Find the coefficients A and B (cover-up rule)", requires="working",
                    prose=r"Solve $\frac{3x+11}{(x-3)(x+2)}=\frac{A}{x-3}+\frac{B}{x+2}$ for $A,B$ by "
                          r"the cover-up rule — this is the linear solve `sp.apart` performs.",
                    math=[r"A=\left.\frac{3x+11}{x+2}\right|_{x=3}=4,\qquad "
                          r"B=\left.\frac{3x+11}{x-3}\right|_{x=-2}=-1"],
                    references=["sub-method: cover-up/residue -> library/heaviside-cover-up.md"],
                    decompose=[
                        dict(title="Cover up (x-3): solve for A", requires="plain",
                             prose=r"Multiply both sides by $(x-3)$ and set $x=3$; the $B$ term dies and "
                                   r"$A$ is what is left: $\frac{3(3)+11}{3+2}=\frac{20}{5}=4$.",
                             math=[r"A=\frac{3(3)+11}{(3)+2}=\frac{20}{5}=4"],
                             references=["base -> library/heaviside-cover-up.md"]),
                        dict(title="Cover up (x+2): solve for B", requires="plain",
                             prose=r"Multiply both sides by $(x+2)$ and set $x=-2$; the $A$ term dies and "
                                   r"$B$ is what is left: $\frac{3(-2)+11}{-2-3}=\frac{5}{-5}=-1$.",
                             math=[r"B=\frac{3(-2)+11}{(-2)-3}=\frac{5}{-5}=-1"],
                             references=["base -> library/heaviside-cover-up.md"]),
                        dict(title="Write the decomposition", requires="plain",
                             prose=r"Put $A=4$, $B=-1$ back in to get the sum of simple fractions.",
                             math=[r"\frac{3x+11}{x^{2}-x-6}=\frac{4}{x-3}-\frac{1}{x+2}"]),
                    ]),
               # ---- working move 3: integrate term-by-term ----------------------------------
               dict(title="Integrate term by term", requires="working",
                    prose=r"Integrate each simple fraction with $\int\frac{dx}{x-a}=\ln|x-a|$ "
                          r"(the re-integration step after `sp.apart`).",
                    math=[r"\int\frac{4}{x-3}\,dx-\int\frac{1}{x+2}\,dx=4\ln|x-3|-\ln|x+2|+C"],
                    references=["sub-method: log antiderivative -> library/log-antiderivative.md"],
                    decompose=[
                        dict(title="Integrate 4/(x-3)", requires="plain",
                             prose=r"Substitute $u=x-3$ ($du=dx$): $\int\frac{4}{u}\,du=4\ln|u|=4\ln|x-3|$.",
                             math=[r"\int\frac{4}{x-3}\,dx=4\ln|x-3|"],
                             references=["base -> library/log-antiderivative.md"]),
                        dict(title="Integrate -1/(x+2)", requires="plain",
                             prose=r"Substitute $u=x+2$ ($du=dx$): $-\int\frac{1}{u}\,du=-\ln|u|=-\ln|x+2|$.",
                             math=[r"\int\frac{-1}{x+2}\,dx=-\ln|x+2|"],
                             references=["base -> library/log-antiderivative.md"]),
                        dict(title="Combine the two logarithms", requires="plain",
                             prose=r"Add the two pieces (one constant $C$ for both) for the final answer.",
                             math=[r"4\ln|x-3|-\ln|x+2|+C"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) ----------------------------------
    d.verify(
        r"Two independent checks. Differentiating the answer recovers the integrand; and the "
        r"symbolic engine (`sp.apart` + term integration, the `partial_fractions` strategy) "
        r"returns the same closed form.",
        math=[r"\frac{d}{dx}\Big(4\ln|x-3|-\ln|x+2|\Big)=\frac{4}{x-3}-\frac{1}{x+2}"
              r"=\frac{4(x+2)-(x-3)}{(x-3)(x+2)}=\frac{3x+11}{x^{2}-x-6}\ \checkmark",
              r"\text{engine: }\ \mathrm{apart}\!\left(\tfrac{3x+11}{x^{2}-x-6}\right)"
              r"=\tfrac{4}{x-3}-\tfrac{1}{x+2}\ \Rightarrow\ 4\ln|x-3|-\ln|x+2|"],
        references=["strategies._partial_fractions — sp.apart + re-integration (the engine path)",
                    "method: library/partial-fractions.md"])
    d.result(latex=r"\int\frac{3x+11}{x^{2}-x-6}\,dx=4\ln|x-3|-\ln|x+2|+C",
             note="verified two ways — differentiate-back recovers the integrand + engine apart() agrees.")
    return d

def main():
    d = build_partial_fractions_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[]  (VALID — no warnings)")
    assert not qwarn, qwarn
    assert len(set(counts.values())) == len(counts), f"counts must all differ: {counts}"
    print("OK: three per-level counts genuinely differ and every step is within reach.")

    # sanity: the engine really produces this closed form (mirrors strategies._partial_fractions)
    x = sp.Symbol("x")
    g = (3 * x + 11) / (x ** 2 - x - 6)
    print("engine apart:", sp.apart(g, x), "| integral:", sp.integrate(g, x))
