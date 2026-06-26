"""LEVELED Derivation for METHOD gamma_ratio_asymptotic (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.gamma_ratio_asymptotic. The engine COMPUTES
    gamma_ratio_asymptotic([z+a], [z+b], z, 1)  ->  z^{a-b} (1 + (a-b)(a+b-1)/(2z))
by routing through the LOGARITHM (gamma.aseries raises PoleError; loggamma.aseries — the Stirling
series — works): take logs, expand each loggamma, subtract, exponentiate, re-expand in 1/z. THIS
derivation walks exactly that computation, and ends by applying it to the paper's chi-moment
μ = 2^{p/2} Γ((k+p)/2)/Γ(k/2) ~ k^{p/2} (arXiv:2606.23785, App. B).

Sub-methods referenced by the steps:
    gamma_ratio_asymptotic -> { Stirling series of log-gamma, log -> difference of logs,
                                exponentiate-a-series (exp of a 1/z expansion) }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"\frac{\Gamma(z+a)}{\Gamma(z+b)}\ \sim\ z^{\,a-b}\left(1+\frac{(a-b)(a+b-1)}{2z}"
       r"+\cdots\right),\qquad z\to\infty")


def build_gamma_ratio_asymptotic_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"large-parameter ratio of Gamma functions $\Gamma(z+a)/\Gamma(z+b)$ "
                   r"(e.g. a chi-distribution moment as the degrees of freedom grow)",
        goal=Goal.EXPAND,
        integral="asymptotic expansion of Gamma(z+a)/Gamma(z+b) as z -> infinity")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — expand via the logarithm of the ratio",
          {"plain": r"We want how $\Gamma(z+a)/\Gamma(z+b)$ behaves when $z$ is huge. The Gamma "
                    r"function itself has no tidy large-$z$ series the computer can hand us, but its "
                    r"LOGARITHM does (the famous Stirling formula). A ratio becomes a SUBTRACTION once "
                    r"you take logs, so we work with $\ln\Gamma$, subtract, then undo the log at the end.",
           "working": r"$\Gamma$ has no elementary closed form, and the CAS cannot expand $\Gamma$ at "
                      r"$\infty$ directly. But $\ln\Gamma(w)$ has the Stirling asymptotic series, and "
                      r"$\ln\frac{\Gamma(z+a)}{\Gamma(z+b)}=\ln\Gamma(z+a)-\ln\Gamma(z+b)$ turns the ratio "
                      r"into a difference of two series we can expand term-by-term in $1/z$.",
           "expert": r"We need the $z\to\infty$ Poincaré expansion of a Gamma ratio. `gamma.aseries`/"
                     r"`series(...,\infty)` is unimplemented (PoleError), but `loggamma.aseries` (Stirling) "
                     r"is available; the logarithm linearises the quotient into a difference of Stirling "
                     r"series, after which exponentiation recovers the ratio's expansion."},
          forced_by=r"$\Gamma(z+a)/\Gamma(z+b)$ has no elementary large-$z$ form and the CAS cannot expand "
                    r"$\Gamma$ at $\infty$, yet $\ln\Gamma$ HAS a known asymptotic (Stirling) series and "
                    r"$\ln$ converts the ratio into a difference.",
          payoff=r"yields the full series $z^{a-b}\!\left(1+\frac{(a-b)(a+b-1)}{2z}+\cdots\right)$ — the leading "
                 r"POWER $z^{a-b}$ and every correction; a single number would hide the power-law scaling and the "
                 r"delicate cancellations (e.g. a variance where the leading terms cancel).",
          relies_on=r"$z\to\infty$ and arguments linear in $z$ (so each $\ln\Gamma(z+\cdot)$ has a Stirling "
                    r"expansion); the series is asymptotic, read by truncation.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — Stirling series of log-gamma, subtracted then exponentiated",
          {"plain": r"Stirling says $\ln\Gamma(w)\approx (w-\tfrac12)\ln w - w + \tfrac12\ln 2\pi + \frac{1}{12w}-\cdots$. "
                    r"Put $w=z+a$ and $w=z+b$, subtract, and tidy up in powers of $1/z$. The $\ln z$ part becomes a "
                    r"power $z^{a-b}$ when we undo the log; the rest becomes the correction bracket.",
           "working": r"Using $\ln\Gamma(z+c)=(z+c-\tfrac12)\ln(z+c)-(z+c)+\tfrac12\ln2\pi+\frac{1}{12(z+c)}-\cdots$ "
                      r"and $\ln(z+c)=\ln z+\frac{c}{z}-\frac{c^2}{2z^2}+\cdots$, the difference collapses to "
                      r"$(a-b)\ln z+\frac{(a-b)(a+b-1)}{2z}+O(z^{-2})$. Exponentiating gives the ratio.",
           "expert": r"$\ln R=\sum_{w\in\text{num}}\ln\Gamma(w)-\sum_{w\in\text{den}}\ln\Gamma(w)$; the Stirling "
                     r"series of each, re-expanded in $1/z$, contributes a $\log z$ term (the exponent $s=\sum a-\sum b$) "
                     r"plus a regular $1/z$ tail $\rho(1/z)$. Then $R=z^{s}\exp\rho=z^{s}(1+\rho+\tfrac12\rho^2+\cdots)$."},
          math=[r"\ln\Gamma(w)\sim\Big(w-\tfrac12\Big)\ln w-w+\tfrac12\ln 2\pi+\frac{1}{12w}-\cdots",
                r"\ln\frac{\Gamma(z+a)}{\Gamma(z+b)}=(a-b)\ln z+\frac{(a-b)(a+b-1)}{2z}+O(z^{-2})"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Expand the Gamma ratio by the log-Stirling route", requires="expert",
           prose=r"Take $\ln$ of the ratio, expand each $\ln\Gamma(z+c)$ by Stirling and re-expand in $1/z$, "
                 r"then exponentiate: the $\ln z$ coefficient $a-b$ becomes the power $z^{a-b}$ and the $1/z$ "
                 r"remainder exponentiates to the bracket $1+\frac{(a-b)(a+b-1)}{2z}+\cdots$.",
           math=[r"\frac{\Gamma(z+a)}{\Gamma(z+b)}\sim z^{\,a-b}\Big(1+\frac{(a-b)(a+b-1)}{2z}+O(z^{-2})\Big)"],
           references=["sub-method: gamma_ratio_asymptotic -> {log-gamma Stirling series, "
                       "log of a ratio, exponentiate a series}"],
           decompose=[
               # ---- working 1: log + Stirling on each factor ----
               dict(title="Take the log and apply Stirling to each factor", requires="working",
                    prose=r"$\ln\frac{\Gamma(z+a)}{\Gamma(z+b)}=\ln\Gamma(z+a)-\ln\Gamma(z+b)$; replace each "
                          r"$\ln\Gamma$ by its Stirling series.",
                    math=[r"\ln\Gamma(z+c)=\Big(z+c-\tfrac12\Big)\ln(z+c)-(z+c)+\tfrac12\ln2\pi+\frac{1}{12(z+c)}-\cdots"],
                    references=["sub-method: log-gamma Stirling series"],
                    decompose=[
                        dict(title="A ratio becomes a difference of logs", requires="plain",
                             prose=r"$\ln(P/Q)=\ln P-\ln Q$ — the quotient turns into a subtraction we can expand piece by piece.",
                             math=[r"\ln\frac{\Gamma(z+a)}{\Gamma(z+b)}=\ln\Gamma(z+a)-\ln\Gamma(z+b)"],
                             references=["base method -> library/log-rules.md"]),
                        dict(title="What the Stirling series says", requires="plain",
                             prose=r"For large $w$, $\ln\Gamma(w)$ is $(w-\tfrac12)\ln w-w$ plus a constant and small "
                                   r"$1/w$ corrections — a known, standard expansion.",
                             math=[r"\ln\Gamma(w)\sim(w-\tfrac12)\ln w-w+\tfrac12\ln2\pi+\frac{1}{12w}-\cdots"],
                             references=["base method -> library/stirling-formula.md"]),
                    ]),
               # ---- working 2: subtract and collect powers of 1/z ----
               dict(title="Subtract and collect in powers of 1/z", requires="working",
                    prose=r"Use $\ln(z+c)=\ln z+\frac{c}{z}-\frac{c^2}{2z^2}+\cdots$ in each Stirling series; the big "
                          r"$z\ln z$ and $z$ pieces CANCEL between the two factors, leaving a clean $1/z$ expansion.",
                    math=[r"\ln\frac{\Gamma(z+a)}{\Gamma(z+b)}=(a-b)\ln z+\frac{(a-b)(a+b-1)}{2z}+O(z^{-2})"],
                    references=["sub-method: log of (z+c) expanded in 1/z"],
                    decompose=[
                        dict(title="Expand each ln(z+c) around large z", requires="plain",
                             prose=r"Factor $\ln(z+c)=\ln z+\ln(1+c/z)$ and use $\ln(1+u)\approx u-\tfrac{u^2}{2}$.",
                             math=[r"\ln(z+c)=\ln z+\frac{c}{z}-\frac{c^{2}}{2z^{2}}+\cdots"],
                             references=["base method -> library/taylor-series.md"]),
                        dict(title="The leading z·ln z and z terms cancel", requires="plain",
                             prose=r"Both factors carry the same $z\ln z$ and $-z$ growth, so their difference removes "
                                   r"them — only the $\ln z$ coefficient and $1/z$ tail survive.",
                             math=[r"\big[(z+a-\tfrac12)\ln(z+a)\big]-\big[(z+b-\tfrac12)\ln(z+b)\big]"
                                   r"\to(a-b)\ln z+\frac{(a-b)(a+b-1)}{2z}+\cdots"]),
                        dict(title="Read off the power and the first correction", requires="plain",
                             prose=r"The coefficient of $\ln z$ is $a-b$ (the exponent); the coefficient of $1/z$ is "
                                   r"$\tfrac12(a-b)(a+b-1)$.",
                             math=[r"s=a-b,\qquad c_1=\frac{(a-b)(a+b-1)}{2}"]),
                    ]),
               # ---- working 3: exponentiate back ----
               dict(title="Exponentiate to recover the ratio", requires="working",
                    prose=r"$R=\exp(\ln R)$: the $(a-b)\ln z$ exponentiates to $z^{a-b}$, and the small $1/z$ remainder "
                          r"$\rho$ gives $e^{\rho}=1+\rho+\cdots$, i.e. the correction bracket.",
                    math=[r"R=z^{\,a-b}\exp\!\Big(\frac{(a-b)(a+b-1)}{2z}+\cdots\Big)"
                          r"=z^{\,a-b}\Big(1+\frac{(a-b)(a+b-1)}{2z}+\cdots\Big)"],
                    references=["sub-method: exponentiate a series"],
                    decompose=[
                        dict(title="e^{(a-b)ln z} is a power", requires="plain",
                             prose=r"Exponentiating a logarithm undoes it: $e^{(a-b)\ln z}=z^{a-b}$.",
                             math=[r"e^{(a-b)\ln z}=z^{\,a-b}"]),
                        dict(title="e^{small} ≈ 1 + small", requires="plain",
                             prose=r"The remaining exponent is $O(1/z)$, so $e^{\rho}=1+\rho+\tfrac12\rho^2+\cdots$ "
                                   r"keeps the bracket to the order wanted.",
                             math=[r"e^{\rho}=1+\rho+\tfrac12\rho^{2}+\cdots,\qquad \rho=O(1/z)"]),
                    ]),
               # ---- working 4: apply to the paper's chi moment ----
               dict(title="Apply it: the chi-distribution moment μ ~ k^{p/2}", requires="working",
                    prose=r"For arXiv:2606.23785, $\mu=2^{p/2}\Gamma(\tfrac{k+p}{2})/\Gamma(\tfrac{k}{2})$. With "
                          r"$z=\tfrac{k}{2}$, $a-b=\tfrac{p}{2}$, the ratio $\sim(\tfrac{k}{2})^{p/2}$, so "
                          r"$\mu\sim k^{p/2}$ — the paper's stated leading behaviour.",
                    math=[r"\mu=2^{p/2}\frac{\Gamma(\tfrac{k+p}{2})}{\Gamma(\tfrac{k}{2})}"
                          r"\sim 2^{p/2}\Big(\tfrac{k}{2}\Big)^{p/2}=k^{\,p/2}"],
                    references=["application: arXiv:2606.23785 App. B (chi-distribution moments)"],
                    decompose=[
                        dict(title="Match to z, a, b", requires="plain",
                             prose=r"Read $\Gamma(\tfrac{k+p}{2})/\Gamma(\tfrac{k}{2})$ as $\Gamma(z+a)/\Gamma(z+b)$ with "
                                   r"$z=\tfrac{k}{2}$, $a=\tfrac{p}{2}$, $b=0$, so $a-b=\tfrac{p}{2}$.",
                             math=[r"z=\tfrac{k}{2},\ a=\tfrac{p}{2},\ b=0\ \Rightarrow\ a-b=\tfrac{p}{2}"]),
                        dict(title="The 2^{p/2} cancels", requires="plain",
                             prose=r"$2^{p/2}(\tfrac{k}{2})^{p/2}=2^{p/2}\,2^{-p/2}k^{p/2}=k^{p/2}$.",
                             math=[r"2^{p/2}\Big(\tfrac{k}{2}\Big)^{p/2}=k^{\,p/2}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"Two independent checks. The engine's `gamma_ratio_asymptotic([z+a],[z+b],z,1)` REGENERATES "
        r"$z^{a-b}(1+(a-b)(a+b-1)/(2z))$ from sympy's Stirling series (no terms written in), matching "
        r"DLMF 5.11.13; and the paper's leading term is confirmed by $\lim_{k\to\infty}\mu/k^{p/2}=1$.",
        math=[r"\frac{\Gamma(z+a)}{\Gamma(z+b)}\sim z^{a-b}\Big(1+\frac{(a-b)(a+b-1)}{2z}\Big)\quad\text{(DLMF 5.11.13)}",
              r"\lim_{k\to\infty}\frac{2^{p/2}\Gamma(\tfrac{k+p}{2})/\Gamma(\tfrac{k}{2})}{k^{p/2}}=1"],
        references=["engine: special_methods.gamma_ratio_asymptotic (loggamma Stirling series)",
                    "DLMF 5.11.13 — independent published Gamma-ratio asymptotic",
                    "arXiv:2606.23785 App. B — the chi-moment application"])
    d.result(
        latex=r"\frac{\Gamma(z+a)}{\Gamma(z+b)}\sim z^{\,a-b}\left(1+\frac{(a-b)(a+b-1)}{2z}+\cdots\right),"
              r"\quad z\to\infty",
        note="derived via the Stirling series of log-gamma (gamma's own series is unavailable in the CAS); "
             "closes the Gamma-ratio asymptotic hole found in arXiv:2606.23785.")
    return d
