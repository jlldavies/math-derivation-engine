r"""LEVELED Derivation for METHOD confluent_0F1 (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.confluent_0F1_bessel. The engine recognizes
    J_nu(z) = (z/2)^nu / Gamma(nu+1) * 0F1(;nu+1; -z^2/4)
by reducing the 0F1 series with sympy's hyperexpand — the Bessel function emerges, nothing written
in. (Surfaced by arXiv:2606.24382, whose lifted scalar operator carries a 0F1.)

Sub-methods referenced by the steps:
    confluent_0F1 -> { hypergeometric series 0F1, Pochhammer (b)_n = Gamma(b+n)/Gamma(b),
                       Bessel J_nu series definition }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"{}_0F_1\!\left(;\nu+1;-\tfrac{z^{2}}{4}\right)=\Gamma(\nu+1)\left(\tfrac{2}{z}\right)^{\nu}J_\nu(z)")


def build_confluent_0F1_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the confluent-hypergeometric limit ${}_0F_1(;\nu+1;-z^2/4)$ and its identification "
                   r"with the Bessel function $J_\nu$ (the oscillating radial mode of dS/AdS lifts)",
        goal=Goal.SIMPLIFY,
        integral="0F1 confluent-hypergeometric limit recognized as a Bessel function")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — recognize the series as a named special function",
          {"plain": r"A ${}_0F_1$ is just a power series. When its argument is $-z^2/4$, that series is exactly "
                    r"the Bessel series in disguise — so instead of leaving an opaque ${}_0F_1$, we MATCH it to "
                    r"the known Bessel function $J_\nu$, which we understand (its oscillations, zeros, asymptotics).",
           "working": r"${}_0F_1(;b;w)=\sum_n w^n/((b)_n n!)$ and $J_\nu$ has a nearly identical series; lining up "
                      r"the coefficients with $b=\nu+1,\ w=-z^2/4$ identifies the two up to a power prefactor.",
           "expert": r"The $z\to\infty$ behaviour and zero structure of the dS/AdS radial mode are invisible in the "
                     r"${}_0F_1$ form but standard for $J_\nu$; the identification is a coefficient match of two series."},
          forced_by=r"the ${}_0F_1(;\nu+1;-z^2/4)$ series and the $J_\nu$ series have the SAME coefficients up to the "
                    r"$(z/2)^\nu/\Gamma(\nu+1)$ prefactor — a special function hiding inside a generic symbol.",
          payoff=r"a named function ($J_\nu$) with known oscillation, zeros and large-$z$ asymptotics, instead of an "
                 r"opaque ${}_0F_1$ — so downstream WKB / boundary analysis can proceed.",
          relies_on=r"the series definitions of ${}_0F_1$ and $J_\nu$ and the Pochhammer identity "
                    r"$(\nu+1)_n\,\Gamma(\nu+1)=\Gamma(\nu+n+1)$.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — match the two power series coefficient by coefficient",
          {"plain": r"Write both as sums over $n$. The Bessel sum has $1/(n!\,\Gamma(\nu+n+1))$ and a "
                    r"$(z/2)^{2n+\nu}$; the ${}_0F_1$ sum has $(-z^2/4)^n/((\nu+1)_n n!)$. Pulling out "
                    r"$(z/2)^\nu/\Gamma(\nu+1)$ turns one into the other.",
           "working": r"$J_\nu(z)=\sum_n\frac{(-1)^n}{n!\,\Gamma(\nu+n+1)}(z/2)^{2n+\nu}$; factor $(z/2)^\nu/\Gamma(\nu+1)$ "
                      r"and use $(\nu+1)_n=\Gamma(\nu+n+1)/\Gamma(\nu+1)$ to get $\sum_n\frac{(-z^2/4)^n}{(\nu+1)_n n!}={}_0F_1$.",
           "expert": r"$(z/2)^\nu/\Gamma(\nu+1)\cdot{}_0F_1(;\nu+1;-z^2/4)=\sum_n\frac{(-1)^n(z/2)^{2n+\nu}}{n!\,\Gamma(\nu+n+1)}=J_\nu(z)$."},
          math=[r"J_\nu(z)=\sum_{n\ge0}\frac{(-1)^n}{n!\,\Gamma(\nu+n+1)}\Big(\frac z2\Big)^{2n+\nu},\qquad "
                r"{}_0F_1(;b;w)=\sum_{n\ge0}\frac{w^n}{(b)_n\,n!}"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Identify 0F1(;nu+1;-z^2/4) with J_nu by matching series", requires="expert",
           prose=r"Factor $(z/2)^\nu/\Gamma(\nu+1)$ out of the Bessel series and apply the Pochhammer identity; the "
                 r"remaining sum is exactly ${}_0F_1(;\nu+1;-z^2/4)$.",
           math=[r"J_\nu(z)=\frac{(z/2)^{\nu}}{\Gamma(\nu+1)}\,{}_0F_1\!\Big(;\nu+1;-\frac{z^2}{4}\Big)"],
           references=["sub-method: confluent_0F1 -> {0F1 series, Pochhammer (b)_n, Bessel J_nu series}"],
           decompose=[
               dict(title="Write the Bessel series and factor the prefactor", requires="working",
                    prose=r"Pull $(z/2)^\nu/\Gamma(\nu+1)$ out of $J_\nu$'s series, leaving a sum over $(z/2)^{2n}$.",
                    math=[r"J_\nu(z)=\frac{(z/2)^\nu}{\Gamma(\nu+1)}\sum_{n\ge0}\frac{(-1)^n\,\Gamma(\nu+1)}{n!\,\Gamma(\nu+n+1)}\Big(\frac z2\Big)^{2n}"],
                    references=["sub-method: Bessel J_nu series"],
                    decompose=[
                        dict(title="The Bessel series", requires="plain",
                             prose=r"$J_\nu$ is defined by $\sum_n\frac{(-1)^n}{n!\,\Gamma(\nu+n+1)}(z/2)^{2n+\nu}$.",
                             math=[r"J_\nu(z)=\sum_{n\ge0}\frac{(-1)^n}{n!\,\Gamma(\nu+n+1)}\Big(\frac z2\Big)^{2n+\nu}"]),
                        dict(title="Factor out (z/2)^nu/Gamma(nu+1)", requires="plain",
                             prose=r"Take the common $(z/2)^\nu/\Gamma(\nu+1)$ outside the sum.",
                             math=[r"=\frac{(z/2)^\nu}{\Gamma(\nu+1)}\sum_{n}\frac{(-1)^n\Gamma(\nu+1)}{n!\,\Gamma(\nu+n+1)}(z/2)^{2n}"]),
                    ]),
               dict(title="Convert the coefficient to a Pochhammer", requires="working",
                    prose=r"$\Gamma(\nu+1)/\Gamma(\nu+n+1)=1/(\nu+1)_n$, and $(z/2)^{2n}=(z^2/4)^n$, so the sum becomes "
                          r"$\sum_n(-z^2/4)^n/((\nu+1)_n n!)$.",
                    math=[r"\frac{\Gamma(\nu+1)}{\Gamma(\nu+n+1)}=\frac{1}{(\nu+1)_n},\qquad (-1)^n(z/2)^{2n}=\Big(-\tfrac{z^2}{4}\Big)^n"],
                    references=["sub-method: Pochhammer (b)_n = Gamma(b+n)/Gamma(b)"],
                    decompose=[
                        dict(title="The Pochhammer identity", requires="plain",
                             prose=r"$(\nu+1)_n=(\nu+1)(\nu+2)\cdots(\nu+n)=\Gamma(\nu+n+1)/\Gamma(\nu+1)$.",
                             math=[r"(\nu+1)_n=\frac{\Gamma(\nu+n+1)}{\Gamma(\nu+1)}"]),
                        dict(title="Recognize the 0F1 sum", requires="plain",
                             prose=r"$\sum_n\frac{(-z^2/4)^n}{(\nu+1)_n\,n!}$ is exactly ${}_0F_1(;\nu+1;-z^2/4)$.",
                             math=[r"\sum_{n\ge0}\frac{(-z^2/4)^n}{(\nu+1)_n\,n!}={}_0F_1\!\Big(;\nu+1;-\tfrac{z^2}{4}\Big)"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `confluent_0F1_bessel` reduces $(z/2)^\nu/\Gamma(\nu+1)\,{}_0F_1(;\nu+1;-z^2/4)$ with sympy "
        r"`hyperexpand` and returns $J_\nu(z)$ exactly (nothing written in), matching DLMF 10.16.9.",
        math=[r"{}_0F_1\!\Big(;\nu+1;-\tfrac{z^2}{4}\Big)\xrightarrow{\text{hyperexpand}}\Gamma(\nu+1)(2/z)^\nu J_\nu(z)\quad(\text{DLMF 10.16.9})"],
        references=["engine: special_methods.confluent_0F1_bessel (hyperexpand of the 0F1 series)",
                    "DLMF 10.16.9 — independent published J_nu-as-0F1 relation",
                    "arXiv:2606.24382 — the dS lift's 0F1"])
    d.result(
        latex=r"{}_0F_1\!\Big(;\nu+1;-\tfrac{z^2}{4}\Big)=\Gamma(\nu+1)\Big(\tfrac2z\Big)^{\nu}J_\nu(z)",
        note="0F1 recognized as a Bessel function by series matching (hyperexpand-confirmed, nothing written in); "
             "extends the special-function track to confluent-hypergeometric limits (de Sitter #7).")
    return d
