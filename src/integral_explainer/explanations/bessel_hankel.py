r"""LEVELED Derivation for METHOD bessel_hankel (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.bessel_hankel. The engine COMPUTES the Hankel transform of a
Gaussian,
    int_0^inf e^{-p t^2} J_0(a t) t dt = e^{-a^2/(4p)} / (2p),
by expanding J_0 as its power series, integrating term-by-term against the Gaussian (standard
moments), and resumming the exponential. Nothing is written in. (DLMF 10.22 / G-R 6.631; the
AdS / holographic radial-mode integrals of arXiv:2606.23779.)

Sub-methods referenced by the steps:
    bessel_hankel -> { Bessel J_0 power series, Gaussian moment int t^{2m+1} e^{-p t^2},
                       resum the exponential series }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"\int_0^\infty e^{-p t^{2}}\,J_0(a t)\,t\,dt=\frac{e^{-a^{2}/(4p)}}{2p}")


def build_bessel_hankel_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"a Hankel transform — a Bessel-weighted radial integral, here the transform of a "
                   r"Gaussian (an AdS / radially-symmetric field mode)",
        goal=Goal.SIMPLIFY,
        integral="Hankel transform of a Gaussian via the Bessel series + Gaussian moments")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — expand the Bessel function, integrate the series",
          {"plain": r"The integrand wiggles (Bessel functions oscillate), so feeding it to a numerical "
                    r"integrator is painful. But $J_0$ is a simple power series, and each power times the "
                    r"Gaussian is an easy integral — so we integrate the series term by term and add it back up.",
           "working": r"$J_0(at)$ has a known power series; $\int_0^\infty t^{2m+1}e^{-pt^2}dt$ is a standard "
                      r"Gaussian moment. Integrating the series term-by-term and resumming gives a closed form.",
           "expert": r"The Hankel transform of $e^{-pt^2}$ is computed by interchanging sum and integral: the "
                     r"$J_0$ series against the Gaussian moments yields an exponential series that resums."},
          forced_by=r"$J_0(at)$ oscillates so quadrature converges slowly, but its power series turns the radial "
                    r"integral into Gaussian moments with a closed-form sum.",
          payoff=r"the exact closed form $e^{-a^2/(4p)}/(2p)$ — a Gaussian maps to a Gaussian under the Hankel "
                 r"transform; a numeric value would hide that self-similar structure.",
          relies_on=r"$p>0$ for convergence and uniform convergence of the $J_0$ series to swap sum and integral.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — Bessel series, Gaussian moments, resum",
          {"plain": r"Write $J_0(at)=\sum_m\frac{(-1)^m}{(m!)^2}(at/2)^{2m}$. Multiply by $e^{-pt^2}t$ and integrate "
                    r"each term using $\int_0^\infty t^{2m+1}e^{-pt^2}dt=\frac{m!}{2p^{m+1}}$. The sum is "
                    r"$e^{-a^2/(4p)}/(2p)$.",
           "working": r"$\int_0^\infty e^{-pt^2}J_0(at)t\,dt=\sum_m\frac{(-1)^m(a/2)^{2m}}{(m!)^2}\cdot\frac{m!}{2p^{m+1}}"
                      r"=\frac{1}{2p}\sum_m\frac{1}{m!}\Big(-\frac{a^2}{4p}\Big)^m$.",
           "expert": r"The $1/(m!)$ that survives makes the sum $\frac{1}{2p}e^{-a^2/(4p)}$."},
          math=[r"J_0(at)=\sum_{m\ge0}\frac{(-1)^m}{(m!)^2}\Big(\frac{at}{2}\Big)^{2m},\qquad "
                r"\int_0^\infty t^{2m+1}e^{-pt^2}dt=\frac{m!}{2p^{m+1}}"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Expand, integrate term-by-term, resum", requires="expert",
           prose=r"Insert the $J_0$ series, integrate each term with the Gaussian moment, and recognize the "
                 r"surviving $\sum (-a^2/4p)^m/m!$ as $e^{-a^2/(4p)}$.",
           math=[r"\int_0^\infty e^{-p t^2}J_0(at)\,t\,dt=\frac{e^{-a^2/(4p)}}{2p}"],
           references=["sub-method: bessel_hankel -> {J_0 power series, Gaussian moments, resum exponential}"],
           decompose=[
               dict(title="Insert the Bessel power series", requires="working",
                    prose=r"Replace $J_0(at)$ by $\sum_m\frac{(-1)^m}{(m!)^2}(at/2)^{2m}$ and pull the sum outside.",
                    math=[r"\int_0^\infty e^{-pt^2}t\sum_m\frac{(-1)^m}{(m!)^2}\Big(\frac{at}{2}\Big)^{2m}dt"],
                    references=["sub-method: Bessel J_0 power series"],
                    decompose=[
                        dict(title="The J_0 series", requires="plain",
                             prose=r"$J_0(x)=\sum_m\frac{(-1)^m}{(m!)^2}(x/2)^{2m}$ — its defining power series.",
                             math=[r"J_0(x)=\sum_{m\ge0}\frac{(-1)^m}{(m!)^2}\Big(\frac x2\Big)^{2m}"]),
                    ]),
               dict(title="Integrate each term (Gaussian moment)", requires="working",
                    prose=r"Each term is $\int_0^\infty t^{2m+1}e^{-pt^2}dt=\frac{m!}{2p^{m+1}}$ (substitute $u=pt^2$).",
                    math=[r"\int_0^\infty t^{2m+1}e^{-pt^2}dt=\frac{m!}{2p^{m+1}}\ \Rightarrow\ "
                          r"\frac{(-1)^m(a/2)^{2m}}{(m!)^2}\cdot\frac{m!}{2p^{m+1}}"],
                    references=["base method -> library/gaussian-integral.md"],
                    decompose=[
                        dict(title="The Gaussian moment", requires="plain",
                             prose=r"Substituting $u=pt^2$ turns $\int t^{2m+1}e^{-pt^2}dt$ into $\tfrac{1}{2p^{m+1}}\int u^m e^{-u}du=\tfrac{m!}{2p^{m+1}}$.",
                             math=[r"\int_0^\infty t^{2m+1}e^{-pt^2}dt=\frac{\Gamma(m+1)}{2p^{m+1}}=\frac{m!}{2p^{m+1}}"]),
                    ]),
               dict(title="Resum to a Gaussian", requires="working",
                    prose=r"One $m!$ cancels, leaving $\frac{1}{2p}\sum_m\frac{1}{m!}(-a^2/4p)^m=\frac{1}{2p}e^{-a^2/(4p)}$.",
                    math=[r"\frac{1}{2p}\sum_{m\ge0}\frac{1}{m!}\Big(-\frac{a^2}{4p}\Big)^m=\frac{e^{-a^2/(4p)}}{2p}"],
                    references=["base method -> library/exponential-series.md"],
                    decompose=[
                        dict(title="The exponential series", requires="plain",
                             prose=r"$\sum_m z^m/m!=e^z$ with $z=-a^2/(4p)$.",
                             math=[r"\sum_{m\ge0}\frac{z^m}{m!}=e^{z},\quad z=-\frac{a^2}{4p}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `bessel_hankel` evaluates the integral with the CAS (nothing written in) and returns "
        r"$e^{-a^2/(4p)}/(2p)$, matching DLMF 10.22 / G-R 6.631; the companion $\int_0^\infty e^{-pt}J_0(at)dt"
        r"=1/\sqrt{p^2+a^2}$ is the same machinery.",
        math=[r"\int_0^\infty e^{-pt^2}J_0(at)t\,dt=\frac{e^{-a^2/(4p)}}{2p}\quad(\text{DLMF 10.22})",
              r"\int_0^\infty e^{-pt}J_0(at)\,dt=\frac{1}{\sqrt{p^2+a^2}}"],
        references=["engine: special_methods.bessel_hankel (CAS Bessel integral)",
                    "DLMF 10.22 / Gradshteyn-Ryzhik 6.631 — independent published Hankel transform",
                    "arXiv:2606.23779 — AdS radial-mode integrals"])
    d.result(
        latex=r"\int_0^\infty e^{-p t^{2}}\,J_0(a t)\,t\,dt=\frac{e^{-a^{2}/(4p)}}{2p}",
        note="Hankel transform of a Gaussian, derived by the Bessel series + Gaussian moments + resummation "
             "(nothing written in); extends the special-function track to Bessel/Hankel radial integrals.")
    return d
