r"""LEVELED Derivation for METHOD airy (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.airy_asymptotic. The engine DERIVES the large-x asymptotic
    Ai(x) ~ e^{-2/3 x^{3/2}} / (2 sqrt(pi) x^{1/4})   (x -> +inf)
by WKB on the Airy ODE y'' = x y: with y=e^S, S''+(S')^2=x; the leading balance gives the exponent
-2/3 x^{3/2}, the next order gives the x^{-1/4} prefactor. The exponent and prefactor are computed
from the ODE; the constant 1/(2 sqrt(pi)) is the standard connection constant (numeric-oracle
confirmed). (DLMF 9.7.5; the large-N ABJM/Airy partition function of arXiv:2606.23893.)

Sub-methods referenced by the steps:
    airy -> { WKB ansatz y=e^S, leading-order balance, next-order transport equation }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"y''=x\,y\ \xrightarrow{\text{WKB}}\ \mathrm{Ai}(x)\sim\frac{e^{-\frac23 x^{3/2}}}{2\sqrt{\pi}\,x^{1/4}}")


def build_airy_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the Airy function $\mathrm{Ai}(x)$ for large $x$ — the universal turning-point / "
                   r"large-$N$ partition-function profile",
        goal=Goal.EXPAND,
        integral="large-x asymptotic of Ai(x) by WKB on the Airy equation")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — WKB turns the ODE into the exponential rate directly",
          {"plain": r"The Airy function solves $y''=xy$ and has no elementary formula. For large $x$ it decays "
                    r"like a stretched exponential. WKB is the trick of writing the solution as $e^{S}$ and reading "
                    r"the decay rate $S$ straight off the equation, instead of solving it exactly.",
           "working": r"$\mathrm{Ai}$ has no closed form, but for $x\to\infty$ the equation $y''=xy$ is "
                      r"'slowly varying', so the WKB ansatz $y=e^{S}$ converts it into an algebraic balance for "
                      r"$S'$ that gives the exponential rate and the algebraic prefactor order by order.",
           "expert": r"$y''=xy$ has an irregular singular point at $\infty$; the WKB/Liouville-Green expansion "
                     r"$y=e^{S_0+S_1+\cdots}$ yields the dominant exponential and the transport (prefactor) correction."},
          forced_by=r"$\mathrm{Ai}$ is non-elementary, but the ODE $y''=xy$ directly constrains the logarithmic "
                    r"derivative $S=\log y$, which WKB expands for large $x$.",
          payoff=r"the explicit decay $e^{-2/3 x^{3/2}}$ and prefactor $x^{-1/4}$ — the data that fix, e.g., the "
                 r"$N^{3/2}$ free energy of the ABJM partition function; a number would hide both.",
          relies_on=r"$x\to+\infty$ (the decaying branch) and the WKB hierarchy (each order smaller than the last); "
                    r"the overall constant is fixed separately by connection to the integral representation.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — substitute y=e^S, balance leading then next order",
          {"plain": r"Put $y=e^{S}$, so $y''=(S''+(S')^2)e^S$ and the equation becomes $S''+(S')^2=x$. For large "
                    r"$x$ the biggest term is $(S')^2=x$, giving $S'=-\sqrt x$; the next correction fixes the "
                    r"prefactor.",
           "working": r"$S''+(S')^2=x$. Leading: $(S')^2\approx x\Rightarrow S_0'=-\sqrt x\Rightarrow S_0=-\tfrac23 x^{3/2}$. "
                      r"Next: $2S_0'S_1'+S_0''=0\Rightarrow S_1'=-\tfrac{1}{4x}\Rightarrow S_1=-\tfrac14\log x$.",
           "expert": r"$S_0=-\tfrac23 x^{3/2}$ (decaying branch), $S_1=-\tfrac14\log x$ from the transport equation, "
                     r"so $y\sim x^{-1/4}e^{-\frac23 x^{3/2}}$; the connection constant is $1/(2\sqrt\pi)$."},
          math=[r"y=e^{S}:\ \ S''+(S')^{2}=x;\qquad S_0'=-\sqrt{x},\quad 2S_0'S_1'+S_0''=0"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("WKB the Airy equation to the leading asymptotic", requires="expert",
           prose=r"Write $y=e^S$, balance $(S')^2=x$ for the exponent $-\tfrac23 x^{3/2}$, solve the next-order "
                 r"transport for the $x^{-1/4}$ prefactor, and attach the connection constant $1/(2\sqrt\pi)$.",
           math=[r"\mathrm{Ai}(x)\sim\frac{e^{-\frac23 x^{3/2}}}{2\sqrt{\pi}\,x^{1/4}}"],
           references=["sub-method: airy -> {WKB ansatz y=e^S, leading balance, transport equation}"],
           decompose=[
               dict(title="Substitute y=e^S into the Airy equation", requires="working",
                    prose=r"$y''=(S''+(S')^2)e^{S}$, so $y''=xy$ becomes $S''+(S')^2=x$.",
                    math=[r"y=e^{S}\ \Rightarrow\ y''=\big(S''+(S')^{2}\big)e^{S}\ \Rightarrow\ S''+(S')^{2}=x"],
                    references=["sub-method: WKB ansatz y=e^S"],
                    decompose=[
                        dict(title="Differentiate e^S twice", requires="plain",
                             prose=r"$\frac{d}{dx}e^S=S'e^S$ and $\frac{d^2}{dx^2}e^S=(S''+(S')^2)e^S$ by the product/chain rule.",
                             math=[r"(e^{S})''=(S''+(S')^{2})e^{S}"]),
                    ]),
               dict(title="Leading balance: the exponent", requires="working",
                    prose=r"For large $x$, $(S')^2$ dominates $S''$, so $(S')^2\approx x$; the decaying branch is "
                          r"$S_0'=-\sqrt x$, hence $S_0=-\tfrac23 x^{3/2}$.",
                    math=[r"(S_0')^{2}=x\ \Rightarrow\ S_0'=-\sqrt{x}\ \Rightarrow\ S_0=-\tfrac23 x^{3/2}"],
                    references=["sub-method: leading-order balance"],
                    decompose=[
                        dict(title="Pick the decaying branch and integrate", requires="plain",
                             prose=r"$Ai$ decays at $+\infty$, so take $S_0'=-\sqrt x$ and integrate: $\int-\sqrt x\,dx=-\tfrac23 x^{3/2}$.",
                             math=[r"\int(-\sqrt{x})\,dx=-\tfrac23 x^{3/2}"]),
                    ]),
               dict(title="Next order: the prefactor", requires="working",
                    prose=r"Writing $S=S_0+S_1$, the order-balance $2S_0'S_1'+S_0''=0$ gives $S_1'=-\tfrac{1}{4x}$, so "
                          r"$S_1=-\tfrac14\log x$, i.e. a factor $x^{-1/4}$.",
                    math=[r"2S_0'S_1'+S_0''=0\ \Rightarrow\ S_1'=-\frac{S_0''}{2S_0'}=-\frac{1}{4x}\ \Rightarrow\ e^{S_1}=x^{-1/4}"],
                    references=["sub-method: next-order transport equation"],
                    decompose=[
                        dict(title="Solve the transport equation", requires="plain",
                             prose=r"$S_0''=-\tfrac{1}{2\sqrt x}$ and $S_0'=-\sqrt x$, so $S_1'=-S_0''/(2S_0')=-1/(4x)$; integrate to $-\tfrac14\log x$.",
                             math=[r"S_1'=-\frac{-1/(2\sqrt x)}{2(-\sqrt x)}=-\frac{1}{4x}\ \Rightarrow\ S_1=-\tfrac14\log x"]),
                    ]),
               dict(title="Assemble and attach the connection constant", requires="working",
                    prose=r"$y\sim x^{-1/4}e^{-\frac23 x^{3/2}}$; the overall constant $1/(2\sqrt\pi)$ is fixed by matching "
                          r"to the integral representation (numeric-oracle confirmed).",
                    math=[r"\mathrm{Ai}(x)\sim\frac{1}{2\sqrt{\pi}}\,x^{-1/4}e^{-\frac23 x^{3/2}}"],
                    references=["application: connection to the oscillatory region / DLMF 9.7"],
                    decompose=[
                        dict(title="Why a constant remains", requires="plain",
                             prose=r"WKB gives the SHAPE (exponent and power); one overall constant is undetermined and "
                                   r"set by matching the known integral form of $Ai$.",
                             math=[r"\mathrm{Ai}(x)\sim C\,x^{-1/4}e^{-\frac23 x^{3/2}},\quad C=\frac{1}{2\sqrt\pi}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `airy_asymptotic` builds $e^{S_0+S_1}/(2\sqrt\pi)$ from the WKB recursion (exponent and "
        r"prefactor computed from the ODE) and returns $e^{-2/3 x^{3/2}}/(2\sqrt\pi x^{1/4})$, matching DLMF "
        r"9.7.5; a numeric check against $\mathrm{Ai}(x)$ gives ratio $\to1$ ($1.009$ at $x=5$, $1.001$ at $x=20$).",
        math=[r"\mathrm{Ai}(x)\sim\frac{e^{-2/3 x^{3/2}}}{2\sqrt{\pi}\,x^{1/4}}\quad(\text{DLMF 9.7.5})",
              r"\frac{\text{asymp}}{\mathrm{Ai}(x)}\to1:\ x=5\!:1.009,\ x=10\!:1.003,\ x=20\!:1.001"],
        references=["engine: special_methods.airy_asymptotic (WKB on the Airy ODE)",
                    "DLMF 9.7.5 — independent published Airy asymptotic",
                    "mpmath/sympy airyai — numeric oracle"])
    d.result(
        latex=r"\mathrm{Ai}(x)\sim\frac{e^{-\frac23 x^{3/2}}}{2\sqrt{\pi}\,x^{1/4}},\qquad x\to+\infty",
        note="exponent and prefactor derived by WKB on y''=xy (connection constant numeric-oracle confirmed); "
             "extends the special-function track to Airy / turning-point asymptotics.")
    return d
