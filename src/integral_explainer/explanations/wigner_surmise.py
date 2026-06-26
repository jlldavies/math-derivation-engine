r"""LEVELED Derivation for METHOD wigner_surmise (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.wigner_surmise. The engine DERIVES the normalized, unit-mean
Wigner surmise rho_beta(s) = c1 s^beta e^{-c2 s^2} by SOLVING the two moment conditions
int_0^inf rho = 1 and int_0^inf s rho = 1 for (c1, c2). For beta=1 it returns (pi/2) s e^{-(pi/4)s^2}
(GOE); beta=2,4 give the GUE/GSE forms — constants derived, never written in. Reproduces
arXiv:2606.23785 eq.(338-343).

Sub-methods referenced by the steps:
    wigner_surmise -> { Gaussian moment integral int s^n e^{-c s^2} (Gamma function),
                        2x2 linear-ish solve for the two constants, level-repulsion ansatz }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"\rho_\beta(s)=c_1\,s^{\beta}e^{-c_2 s^{2}},\qquad "
       r"\int_0^\infty\rho_\beta=1,\ \ \int_0^\infty s\,\rho_\beta=1\ \Rightarrow\ "
       r"\rho_1(s)=\tfrac{\pi}{2}s\,e^{-\frac{\pi}{4}s^{2}}")


def build_wigner_surmise_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the Wigner surmise — the level-spacing distribution $\rho_\beta(s)$ of a chaotic "
                   r"spectrum / 2$\times$2 random-matrix ensemble (Dyson index $\beta=1,2,4$)",
        goal=Goal.SIMPLIFY,
        integral="normalized unit-mean Wigner surmise by moment-matching")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — fix the constants by the physical normalizations, don't guess them",
          {"plain": r"Chaotic energy levels REPEL: the chance of a tiny gap $s$ vanishes like $s^\beta$, and "
                    r"big gaps are exponentially rare, so the spacing law looks like $s^\beta$ times a Gaussian. "
                    r"That fixes the SHAPE; the two leftover constants are pinned by two facts — the total "
                    r"probability is 1, and the average gap is 1 (we measure $s$ in units of the mean).",
           "working": r"Level repulsion + a Gaussian tail force $\rho_\beta(s)=c_1 s^\beta e^{-c_2 s^2}$. The two "
                      r"constants are not free: impose $\int_0^\infty\rho=1$ (a probability density) and "
                      r"$\int_0^\infty s\rho=1$ (unit mean spacing, the standard unfolding) and solve.",
           "expert": r"Given the $2\times2$-ensemble ansatz $c_1 s^\beta e^{-c_2 s^2}$, the normalization and "
                     r"unit-first-moment conditions are two equations in $(c_1,c_2)$ whose solution yields the "
                     r"$\beta=1,2,4$ surmise constants."},
          forced_by=r"level repulsion gives the $s^\beta$ prefactor and the ensemble gives the $e^{-c_2 s^2}$ tail, "
                    r"so only two constants remain — and two moment conditions determine them exactly.",
          payoff=r"the closed-form $\rho_\beta$ with the exact GOE/GUE/GSE constants ($\pi/2,\pi/4$; $32/\pi^2,4/\pi$; "
                 r"$2^{18}/3^6\pi^3,64/9\pi$) — a fit would only approximate them and hide that they're forced.",
          relies_on=r"the $s^\beta$/Gaussian ansatz (2$\times$2 surmise) and the unit-mean convention; the moment "
                    r"integrals converge for $\beta\ge0,\ c_2>0$.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — two Gaussian moment integrals, then a 2x2 solve",
          {"plain": r"Both conditions are simple areas under $s^n e^{-c_2 s^2}$, which have a standard value "
                    r"(a Gamma-function formula). Writing the two areas $=1$ gives two equations; solving them "
                    r"hands back $c_1$ and $c_2$.",
           "working": r"$\int_0^\infty s^{n}e^{-c_2 s^2}ds=\tfrac12 c_2^{-(n+1)/2}\Gamma\!\big(\tfrac{n+1}{2}\big)$. "
                      r"Use $n=\beta$ (normalization) and $n=\beta+1$ (mean); divide the two equations to isolate "
                      r"$c_2$, then back-substitute for $c_1$.",
           "expert": r"The ratio of the $n{=}\beta{+}1$ and $n{=}\beta$ moment equations cancels $c_1$ and gives "
                     r"$c_2=\big[\Gamma(\tfrac{\beta+2}{2})/\Gamma(\tfrac{\beta+1}{2})\big]^2$; then "
                     r"$c_1=2c_2^{(\beta+1)/2}/\Gamma(\tfrac{\beta+1}{2})$."},
          math=[r"\int_0^\infty s^{n}e^{-c_2 s^{2}}\,ds=\frac{\Gamma\!\big(\frac{n+1}{2}\big)}{2\,c_2^{(n+1)/2}}",
                r"c_1\!\int_0^\infty s^{\beta}e^{-c_2 s^2}=1,\qquad c_1\!\int_0^\infty s^{\beta+1}e^{-c_2 s^2}=1"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Fix (c1,c2) from the two moment conditions and read off rho_beta", requires="expert",
           prose=r"Impose $\int\rho=1$ and $\int s\rho=1$ using the Gaussian moment formula, solve the pair for "
                 r"$(c_1,c_2)$, and substitute back: $\beta=1$ gives $\rho_1=\tfrac{\pi}{2}s\,e^{-\frac{\pi}{4}s^2}$.",
           math=[r"\rho_1(s)=\frac{\pi}{2}\,s\,e^{-\frac{\pi}{4}s^{2}},\quad "
                 r"\rho_2(s)=\frac{32}{\pi^2}s^{2}e^{-\frac{4}{\pi}s^{2}},\quad "
                 r"\rho_4(s)=\frac{2^{18}}{3^6\pi^3}s^{4}e^{-\frac{64}{9\pi}s^{2}}"],
           references=["sub-method: wigner_surmise -> {Gaussian moment integral, 2x2 constant solve, repulsion ansatz}"],
           decompose=[
               dict(title="Write down the two moment conditions", requires="working",
                    prose=r"Normalization and unit mean give two equations in $c_1,c_2$ via the Gaussian moment formula.",
                    math=[r"c_1\frac{\Gamma(\frac{\beta+1}{2})}{2c_2^{(\beta+1)/2}}=1,\qquad "
                          r"c_1\frac{\Gamma(\frac{\beta+2}{2})}{2c_2^{(\beta+2)/2}}=1"],
                    references=["sub-method: Gaussian moment integral (Gamma function)"],
                    decompose=[
                        dict(title="The Gaussian moment integral", requires="plain",
                             prose=r"$\int_0^\infty s^n e^{-c s^2}ds$ is a standard area, equal to "
                                   r"$\tfrac12 c^{-(n+1)/2}\Gamma(\tfrac{n+1}{2})$ (substitute $u=cs^2$).",
                             math=[r"\int_0^\infty s^{n}e^{-c s^{2}}ds=\frac{\Gamma(\frac{n+1}{2})}{2c^{(n+1)/2}}"],
                             references=["base method -> library/gaussian-integral.md"]),
                        dict(title="Plug n=beta and n=beta+1", requires="plain",
                             prose=r"Normalization uses $n=\beta$; the mean $\int s\rho$ uses $n=\beta+1$.",
                             math=[r"n=\beta\ (\text{norm}),\qquad n=\beta+1\ (\text{mean})"]),
                    ]),
               dict(title="Solve: divide to get c2, back-substitute for c1", requires="working",
                    prose=r"Dividing the mean equation by the normalization cancels $c_1$ and leaves $c_2$ as a ratio "
                          r"of Gammas; then the normalization gives $c_1$.",
                    math=[r"c_2=\Big[\frac{\Gamma(\frac{\beta+2}{2})}{\Gamma(\frac{\beta+1}{2})}\Big]^{2},\qquad "
                          r"c_1=\frac{2\,c_2^{(\beta+1)/2}}{\Gamma(\frac{\beta+1}{2})}"],
                    references=["sub-method: 2x2 constant solve"],
                    decompose=[
                        dict(title="Divide the two equations", requires="plain",
                             prose=r"The ratio of the two conditions is $\sqrt{c_2}\,\Gamma(\frac{\beta+1}{2})/\Gamma(\frac{\beta+2}{2})=1$, "
                                   r"giving $c_2$.",
                             math=[r"\frac{\Gamma(\frac{\beta+2}{2})}{c_2^{1/2}\,\Gamma(\frac{\beta+1}{2})}=1"]),
                        dict(title="Back-substitute for c1", requires="plain",
                             prose=r"Put $c_2$ into the normalization equation to solve for $c_1$.",
                             math=[r"c_1=\frac{2\,c_2^{(\beta+1)/2}}{\Gamma(\frac{\beta+1}{2})}"]),
                        dict(title="Evaluate at beta=1", requires="plain",
                             prose=r"$\Gamma(1)=1,\ \Gamma(\tfrac32)=\tfrac{\sqrt\pi}{2}$ give $c_2=\pi/4,\ c_1=\pi/2$.",
                             math=[r"c_2=\Big(\tfrac{\sqrt\pi/2}{1}\Big)^2=\frac{\pi}{4},\qquad c_1=2\cdot\frac{\pi}{4}=\frac{\pi}{2}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `wigner_surmise` SOLVES the two moment equations and returns $\rho_\beta$ with the "
        r"constants derived (nothing written in); they match the standard GOE/GUE/GSE surmise (and "
        r"arXiv:2606.23785 eq.338-343). Independent check: each returned $\rho_\beta$ re-satisfies "
        r"$\int\rho=\int s\rho=1$.",
        math=[r"\rho_1=\tfrac{\pi}{2}s\,e^{-\frac{\pi}{4}s^2},\ \rho_2=\tfrac{32}{\pi^2}s^2e^{-\frac{4}{\pi}s^2},\ "
              r"\rho_4=\tfrac{2^{18}}{3^6\pi^3}s^4e^{-\frac{64}{9\pi}s^2}",
              r"\int_0^\infty\rho_\beta\,ds=1,\quad \int_0^\infty s\,\rho_\beta\,ds=1"],
        references=["engine: special_methods.wigner_surmise (moment-matching solve)",
                    "Wikipedia, Random matrix — Wigner surmise (independent published constants)",
                    "arXiv:2606.23785 eq.(338-343)"])
    d.result(
        latex=r"\rho_1(s)=\frac{\pi}{2}s\,e^{-\frac{\pi}{4}s^{2}},\quad "
              r"\rho_2(s)=\frac{32}{\pi^{2}}s^{2}e^{-\frac{4}{\pi}s^{2}},\quad "
              r"\rho_4(s)=\frac{2^{18}}{3^{6}\pi^{3}}s^{4}e^{-\frac{64}{9\pi}s^{2}}",
        note="constants derived by solving int rho = int s rho = 1 (nothing written in); opens the RMT / "
             "level-statistics (probability) track used by 2606.23785 and 2606.24490.")
    return d
