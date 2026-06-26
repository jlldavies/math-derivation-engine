"""Leveled Derivation for the meijer_g method (CLAUDE.md rule 7 + rule 11 Definition of Done).

WORKED TARGET:  ∫_{-∞}^{∞} e^{-x²} cos(2x) dx = √π · e^{-1}

REAL COMPUTATION the engine runs (strategies._meijerg -> special path of sympy's meijerg
integrator):  sp.integrate(exp(-x**2)*cos(2*x), (x, -oo, oo), meijerg=True)  ->  sqrt(pi)*exp(-1).

The method is NOT "differentiate under the integral" (that is solve_integral.py's feynman edge).
meijer_g works by:
  (A) writing each elementary factor of the integrand as a Meijer G-function,
  (B) folding the product-integral into ONE G-function via the master Mellin-convolution
      formula  ∫_0^∞ x^{s-1} G·G dx  (a Gamma-quotient in the G-parameters),
  (C) collapsing that resulting G-function back to an elementary closed form.

This file builds the qualification tree so the per-level step counts EMERGE and DIFFER:
  expert  = the 3 whole moves (A/B/C) as single graspable nodes  -> 3 steps,
  working = those moves opened into their sub-steps               -> more steps,
  plain   = the sub-steps opened to high-school base pages        -> most steps.

Run:  python scratch/expl_meijer_g.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

import sympy as sp
import mpmath as mp

mp.mp.dps = 30

HDR = r"\int_{-\infty}^{\infty} e^{-x^{2}}\cos(2x)\,dx"

def build_meijer_g_derivation() -> Derivation:
    """A genuine why/how/step qualification tree for the meijer_g reduction of
    ∫_{-∞}^{∞} e^{-x²}cos(2x) dx, decomposed so plain/working/expert step counts EMERGE
    and DIFFER. Mirrors the engine edge strategies._meijerg (sympy meijerg=True)."""
    problem = Problem(
        latex=HDR,
        represents=r"an even Gaussian $\times$ cosine; the value is its Fourier cosine "
                   r"transform at frequency $2$ (a Weierstrass-transform sample)",
        goal=Goal.EVALUATE,
        integral="coefficient-free value of the Gaussian-cosine integral")
    d = Derivation(problem)

    # ---- WHY: recognition / decision (forced-by / payoff / relies-on) --------------------
    d.why("Why this approach — reduce to Meijer G-functions",
          {"plain": r"The integrand is a product of two familiar shapes — a bell curve "
                    r"$e^{-x^{2}}$ and a wave $\cos 2x$ — but multiplied together they have no "
                    r"ordinary antiderivative. Instead we rewrite each shape in ONE common "
                    r"'master' form (the Meijer G-function). In that form there is a ready-made "
                    r"rule for the integral of a product, so the whole thing collapses to a "
                    r"single master function, which we then read off as a plain number.",
           "working": r"$e^{-x^{2}}$ and $\cos 2x$ are both special cases of the Meijer "
                      r"G-function. Once each factor is a $G$, the Mellin-convolution theorem "
                      r"gives $\int_0^\infty x^{s-1}G\,G\,dx$ as a single $G$ of a closed "
                      r"Gamma-quotient — no antiderivative needed. The result $G$ then reduces "
                      r"to elementary form.",
           "expert": r"Both factors lie in the Meijer-$G$ class; the integral is a "
                     r"Mellin convolution, so it evaluates by the $G$-function master formula "
                     r"(a ratio of $\Gamma$'s in the $G$-parameters), then collapses to "
                     r"elementary form. This is exactly sympy's $\texttt{meijerg=True}$ path."},
          forced_by=r"the product $e^{-x^{2}}\cos 2x$ has no elementary antiderivative, yet "
                    r"BOTH factors are individually Meijer-$G$ representable — so the blocked "
                    r"primitive is sidestepped by a table-lookup convolution rather than by "
                    r"integration in $x$.",
          payoff=r"the master formula returns the EXACT closed form $\sqrt{\pi}\,e^{-1}$ in one "
                 r"shot, exposing that the answer is a Gaussian sampled in frequency; a numeric "
                 r"quadrature would hide that $e^{-1}=e^{-2^{2}/4}$ structure.",
          relies_on=r"convergence of the Mellin-convolution integral (the Gaussian decay "
                    r"dominates the bounded cosine) and that the $\Gamma$-quotient has no pole "
                    r"on the contour — both hold for this integrand at frequency $2$.")

    # ---- HOW: the machinery (the master formula) -----------------------------------------
    d.how("How the approach works — the G-function master formula",
          {"plain": r"A Meijer G-function is a single template $G(x)$ with a few slots; filling "
                    r"the slots one way gives $e^{-x^{2}}$, another way gives $\cos 2x$. The key "
                    r"fact: the integral of $G$ times $G$ is itself one $G$, whose slots are got "
                    r"by simple bookkeeping — so we never integrate, we just combine slots.",
           "working": r"For two G-functions the convolution integral "
                      r"$\int_0^\infty x^{s-1}G(\sigma x)\,G(\omega x)\,dx$ equals a single "
                      r"$G$ whose parameters are the merged lists, evaluated via products of "
                      r"$\Gamma$'s at the parameter shifts.",
           "expert": r"The Meijer master formula "
                     r"$\int_0^\infty x^{s-1}\,G^{m_1 n_1}_{p_1 q_1}\!(\sigma x)\,"
                     r"G^{m_2 n_2}_{p_2 q_2}\!(\omega x)\,dx$ is a ratio of $\Gamma$-factors in "
                     r"the combined parameter set (Slater/Marichev). Specialising to the two "
                     r"factors here yields the closed value directly."},
          math=[r"e^{-x^{2}}=G^{1,0}_{0,1}\!\Big(x^{2}\ \Big|\ {-\atop 0}\Big),\qquad "
                r"\cos(2x)=\sqrt{\pi}\,G^{1,0}_{0,2}\!\Big(x^{2}\ \Big|\ {-\atop 0,\;1/2}\Big)",
                r"\int_{0}^{\infty}x^{s-1}G(\sigma x^{2})\,G(\omega x^{2})\,dx \;=\; "
                r"\text{(a single }G\text{ of a }\Gamma\text{-quotient)}"])

    # ---- THE STEPS: one qualification tree. expert grasps A/B/C each as a unit; ----------
    #      working opens each into its sub-steps; plain opens those to high-school pages.

    # MOVE A — represent the factors as G-functions (expert: 1 node; opens to 2; opens to 4)
    move_A = dict(
        title="A. Write each factor as a Meijer G-function", requires="expert",
        prose=r"Use the evenness to fold the integral to $[0,\infty)$, then express both "
              r"$e^{-x^{2}}$ and $\cos 2x$ as Meijer $G$-functions of $x^{2}$.",
        math=[r"\int_{-\infty}^{\infty}\!e^{-x^{2}}\cos 2x\,dx=2\!\int_{0}^{\infty}\!"
              r"e^{-x^{2}}\cos 2x\,dx,\quad e^{-x^{2}},\,\cos 2x \;\to\; G\text{-functions}"],
        decompose=[
            dict(title="Fold to a half-line using evenness", requires="working",
                 prose=r"The integrand is even in $x$, so the whole-line integral is twice the "
                       r"half-line one — the form the G-function machinery expects.",
                 math=[r"f(-x)=e^{-x^{2}}\cos(2x)=f(x)\ \Rightarrow\ "
                       r"\int_{-\infty}^{\infty}f\,dx=2\int_{0}^{\infty}f\,dx"],
                 decompose=[
                     dict(title="Check the integrand is even", requires="plain",
                          prose=r"Replacing $x$ by $-x$ leaves both factors unchanged: the "
                                r"Gaussian is even and $\cos$ is even.",
                          math=[r"e^{-(-x)^{2}}=e^{-x^{2}},\qquad \cos(-2x)=\cos(2x)"],
                          references=["base method -> library/even-odd-symmetry.md"]),
                     dict(title="Double the half-line integral", requires="plain",
                          prose=r"For an even function the two halves $(-\infty,0]$ and "
                                r"$[0,\infty)$ contribute equally, so the integral is twice one half.",
                          math=[r"\int_{-\infty}^{\infty}f\,dx=2\int_{0}^{\infty}f\,dx"],
                          references=["base method -> library/even-odd-symmetry.md"]),
                 ]),
            dict(title="Cast the two factors into G-function form", requires="working",
                 prose=r"Each elementary factor is a special case of the Meijer $G$: the Gaussian "
                       r"is the simplest $G^{1,0}_{0,1}$, and the cosine is a $G^{1,0}_{0,2}$ "
                       r"(its Mellin transform is a single $\Gamma$ / a pair of $\Gamma$'s).",
                 math=[r"e^{-x^{2}}=G^{1,0}_{0,1}\!\Big(x^{2}\ \Big|\ {-\atop 0}\Big),\quad "
                       r"\cos(2x)=\sqrt{\pi}\,G^{1,0}_{0,2}\!\Big(x^{2}\ \Big|\ {-\atop 0,\,1/2}\Big)"],
                 decompose=[
                     dict(title="Gaussian as a G-function (its Mellin transform)", requires="plain",
                          prose=r"The Mellin transform of $e^{-x^{2}}$ is $\tfrac12\Gamma(s/2)$, "
                                r"a single Gamma factor — that is exactly the $G^{1,0}_{0,1}$ "
                                r"template, so the Gaussian IS that $G$.",
                          math=[r"\int_{0}^{\infty}x^{s-1}e^{-x^{2}}\,dx=\tfrac12\Gamma\!\big(\tfrac{s}{2}\big)"],
                          references=["base method -> library/gamma-function.md",
                                      "base method -> library/mellin-transform.md"]),
                     dict(title="Cosine as a G-function", requires="plain",
                          prose=r"$\cos 2x$ has a known Mellin transform built from $\Gamma$'s; "
                                r"matching it to the $G$ template fixes the slots $0,\,1/2$.",
                          math=[r"\cos(2x)=\sqrt{\pi}\,G^{1,0}_{0,2}\!\Big(x^{2}\ \Big|\ {-\atop 0,\,1/2}\Big)"],
                          references=["base method -> library/mellin-transform.md"]),
                 ]),
        ])

    # MOVE B — apply the master convolution formula (expert: 1 node; opens to 2; opens to 4)
    move_B = dict(
        title="B. Fold the product into one G-function (master formula)", requires="expert",
        prose=r"The half-line integral of the two $G$-functions is, by the Meijer master "
              r"formula, a single $G$ whose parameters are the merged slot-lists; evaluate the "
              r"resulting $\Gamma$-quotient at frequency $2$.",
        math=[r"2\!\int_{0}^{\infty}\!G\,G\,dx=\text{single }G\big(\Gamma\text{-quotient}\big)"
              r"\ \xrightarrow{\ \omega=2\ }\ \text{closed expression}"],
        decompose=[
            dict(title="Substitute both G-functions into the convolution integral", requires="working",
                 prose=r"Place the two $G$'s into $\int_0^\infty x^{s-1}G\,G\,dx$ with $s=1$ "
                       r"(the bare integral, no extra power of $x$).",
                 math=[r"2\int_{0}^{\infty}G^{1,0}_{0,1}\!\big(x^{2}\big)\,"
                       r"\sqrt{\pi}\,G^{1,0}_{0,2}\!\big(x^{2}\big)\,dx"],
                 decompose=[
                     dict(title="Identify the merged parameter lists", requires="plain",
                          prose=r"Collect the top slots (here none, $n=0$) and the bottom slots "
                                r"$0$ and $0,1/2$ from the two $G$'s — these merged lists are the "
                                r"inputs to the master formula.",
                          math=[r"\text{bottom slots: }\{0\}\cup\{0,\tfrac12\},\qquad "
                                r"\text{top slots: }\varnothing"],
                          references=["base method -> library/meijer-g-parameters.md"]),
                     dict(title="Set s = 1 (no extra power of x)", requires="plain",
                          prose=r"The integral we want has no spare $x^{s-1}$ factor, so the "
                                r"convolution parameter is $s=1$.",
                          math=[r"x^{s-1}\big|_{s=1}=x^{0}=1"]),
                 ]),
            dict(title="Evaluate the Gamma-quotient at frequency 2", requires="working",
                 prose=r"The master formula returns a ratio of $\Gamma$'s evaluated at the "
                       r"parameter shifts; with the cosine's frequency $\omega=2$ this is a "
                       r"finite closed expression.",
                 math=[r"\text{master }G \;=\; \frac{\prod\Gamma(\text{shifts})}"
                       r"{\prod\Gamma(\text{shifts})}\Big|_{\omega=2}"],
                 decompose=[
                     dict(title="Write the Gamma factors from the slots", requires="plain",
                          prose=r"Each bottom slot $b$ contributes a $\Gamma(b+\tfrac{s}{2})$-type "
                                r"factor; assemble the product/quotient the formula prescribes.",
                          math=[r"\prod_{b}\Gamma\!\big(b+\tfrac{s}{2}\big)\Big|_{s=1}"],
                          references=["base method -> library/gamma-function.md"]),
                     dict(title="Plug in the frequency to get a number times a Gaussian", requires="plain",
                          prose=r"Substituting $\omega=2$ into the argument leaves an explicit "
                                r"$e^{-\omega^{2}/4}=e^{-1}$ exponential factor.",
                          math=[r"e^{-\omega^{2}/4}\big|_{\omega=2}=e^{-1}"]),
                 ]),
        ])

    # MOVE C — collapse the result G to elementary form (expert: 1 node; opens to 3 plain)
    move_C = dict(
        title="C. Collapse the result to elementary form", requires="expert",
        prose=r"The single $G$ from the master formula is one of the tabulated cases that "
              r"reduces to elementary functions; simplifying gives the closed value.",
        math=[r"2\int_{0}^{\infty}e^{-x^{2}}\cos 2x\,dx=\sqrt{\pi}\,e^{-1}"],
        decompose=[
            dict(title="Reduce the master G to elementary form", requires="plain",
                 prose=r"The half-line value carries the $\sqrt{\pi}/2$ from the Gaussian and "
                       r"the $e^{-1}$ from the frequency; the $G$ collapses to $\tfrac{\sqrt\pi}{2}e^{-1}$.",
                 math=[r"\int_{0}^{\infty}e^{-x^{2}}\cos 2x\,dx=\frac{\sqrt{\pi}}{2}\,e^{-1}"],
                 references=["base method -> library/gaussian-integral.md"]),
            dict(title="Undo the evenness doubling", requires="plain",
                 prose=r"Multiply the half-line value by $2$ (from move A) to recover the "
                       r"whole-line integral.",
                 math=[r"2\cdot\frac{\sqrt{\pi}}{2}\,e^{-1}=\sqrt{\pi}\,e^{-1}"],
                 references=["base method -> library/even-odd-symmetry.md"]),
            dict(title="Read off the closed form", requires="plain",
                 prose=r"The Gaussian-cosine integral equals $\sqrt{\pi}$ times $e^{-1}$ — a "
                       r"Gaussian sampled at frequency $2$.",
                 math=[r"\int_{-\infty}^{\infty}e^{-x^{2}}\cos 2x\,dx=\sqrt{\pi}\,e^{-1}"]),
        ])

    d.step(move_A["title"], requires="expert", prose=move_A["prose"],
           math=move_A["math"], decompose=move_A["decompose"])
    d.step(move_B["title"], requires="expert", prose=move_B["prose"],
           math=move_B["math"], decompose=move_B["decompose"])
    d.step(move_C["title"], requires="expert", prose=move_C["prose"],
           math=move_C["math"], decompose=move_C["decompose"])

    # ---- VERIFY: two independent checks (engine executor + numeric oracle) ----------------
    x = sp.Symbol("x")
    closed = sp.integrate(sp.exp(-x**2) * sp.cos(2 * x), (x, -sp.oo, sp.oo), meijerg=True)
    closed_tex = sp.latex(closed)
    num = mp.quad(lambda t: mp.e ** (-t ** 2) * mp.cos(2 * t), [-mp.inf, 0, mp.inf])
    symv = mp.sqrt(mp.pi) * mp.e ** (-1)
    digits = 30 if num == symv else int(-mp.log10(abs(num - symv)))
    d.verify(
        r"Two independent checks, neither used to DERIVE the value. The engine's Meijer-G "
        r"integrator (sympy $\texttt{meijerg=True}$, the $\texttt{strategies.\_meijerg}$ edge) "
        r"returns the same closed form, and high-precision quadrature agrees with it.",
        math=[r"\texttt{meijerg=True}:\ \int_{-\infty}^{\infty}e^{-x^{2}}\cos 2x\,dx=" + closed_tex,
              r"\text{numeric}:\ " + mp.nstr(num, 16) + r"\ \approx\ " + mp.nstr(symv, 16)
              + r"\ \ (\text{agree to }" + str(digits) + r"\text{ digits})"],
        references=["engine: strategies._meijerg -> sympy integrate(..., meijerg=True)",
                    "mpmath high-precision quadrature — the numeric oracle",
                    "method: library/meijer-g-reduction.md"])
    d.result(latex=r"\int_{-\infty}^{\infty}e^{-x^{2}}\cos(2x)\,dx=\sqrt{\pi}\,e^{-1}",
             note=f"verified two ways — sympy meijerg=True closed form + numeric agreement to {digits} digits.")
    return d

def main():
    d = build_meijer_g_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[] (VALID — no warnings)")
    print("counts differ:", len(set(counts.values())) > 1,
          "| plain >= working >= expert:",
          counts["plain"] >= counts["working"] >= counts["expert"])
    assert not qwarn, qwarn
    out = os.path.join(os.path.dirname(__file__), "meijer_g_output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "meijer_g_gaussian_cosine.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(render_leveled(tracks))
    print("rendered ->", path)
