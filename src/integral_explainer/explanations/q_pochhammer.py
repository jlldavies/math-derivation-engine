r"""LEVELED Derivation for METHOD q_pochhammer (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.q_pochhammer_log. The engine DERIVES the Lambert series
    log (a;q)_inf = - sum_{n>=1} a^n / (n (1 - q^n))      (|q| < 1)
for the infinite q-Pochhammer product (a;q)_inf = prod_{k>=0}(1 - a q^k), by taking the log,
expanding each log, and RESUMMING the geometric series sum_{k>=0} q^{kn} = 1/(1 - q^n). The
1/(1-q^n) is computed, never written in. (Euler / DLMF 17; this is arXiv:2606.24497 eq.18.)

Sub-methods referenced by the steps:
    q_pochhammer -> { log of a product -> sum of logs, log(1-u) series, geometric series sum }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"\log\,(a;q)_\infty=\log\prod_{k\ge0}(1-a q^{k})=-\sum_{n\ge1}\frac{a^{n}}{n\,(1-q^{n})}")


def build_q_pochhammer_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"the infinite q-Pochhammer product $(a;q)_\infty=\prod_{k\ge0}(1-aq^k)$ — the q-series "
                   r"kernel under q-exponentials, localization partition functions and Jacobi/Jack dressing factors",
        goal=Goal.SIMPLIFY,
        integral="log of the q-Pochhammer product as a Lambert series")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — take logs to turn the product into a resummable sum",
          {"plain": r"An infinite PRODUCT is awkward to handle. Taking its logarithm turns it into a SUM of "
                    r"logs, and each log is a simple series. Adding those up in the right order collapses the "
                    r"whole product into one tidy series.",
           "working": r"$(a;q)_\infty$ is an infinite product; $\log$ converts it to $\sum_k\log(1-aq^k)$. Each "
                      r"$\log(1-u)$ is a power series, and swapping the two sums leaves a geometric series in $k$ "
                      r"that resums in closed form.",
           "expert": r"Passing to $\log$ linearises the product; the double sum $\sum_k\sum_n$ is reorganised so the "
                     r"inner geometric series $\sum_k q^{kn}$ resums to $1/(1-q^n)$, giving the Lambert series."},
          forced_by=r"a product resists term-by-term manipulation, but $\log$ makes it a sum of $\log(1-aq^k)$ — each "
                    r"a geometric-type series whose $k$-sum is closed-form.",
          payoff=r"the closed Lambert series $-\sum_n a^n/(n(1-q^n))$ — exact in $a$ and $q$, the form every q-series "
                 r"identity (q-exponential, dressing factors) is built from; a truncated product would hide it.",
          relies_on=r"$|q|<1$ (so $\sum_k q^{kn}=1/(1-q^n)$ converges) and $|a|<1$ for the log expansion.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — log of a product, expand, swap sums, resum the geometric",
          {"plain": r"Three moves: $\log$ of a product is a sum of logs; $\log(1-u)=-(u+\tfrac{u^2}{2}+\cdots)$; and "
                    r"$1+q^n+q^{2n}+\cdots=\frac{1}{1-q^n}$. Put together they give $-\sum_n a^n/(n(1-q^n))$.",
           "working": r"$\log(a;q)_\infty=\sum_k\log(1-aq^k)=-\sum_k\sum_n\frac{(aq^k)^n}{n}=-\sum_n\frac{a^n}{n}\sum_k q^{kn}"
                      r"=-\sum_n\frac{a^n}{n}\cdot\frac{1}{1-q^n}$.",
           "expert": r"Interchange $\sum_k$ and $\sum_n$ (absolute convergence for $|a|,|q|<1$); the inner geometric "
                     r"series gives $1/(1-q^n)$, yielding the Lambert series."},
          math=[r"\log(1-u)=-\sum_{n\ge1}\frac{u^{n}}{n},\qquad \sum_{k\ge0}q^{kn}=\frac{1}{1-q^{n}}\ (|q|<1)"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Log, expand, and resum to the Lambert series", requires="expert",
           prose=r"$\log(a;q)_\infty=\sum_k\log(1-aq^k)$; expand each log, swap the sums, and resum the geometric "
                 r"$\sum_k q^{kn}=1/(1-q^n)$ to get $-\sum_n a^n/(n(1-q^n))$.",
           math=[r"\log(a;q)_\infty=-\sum_{n\ge1}\frac{a^{n}}{n\,(1-q^{n})}"],
           references=["sub-method: q_pochhammer -> {log of a product, log(1-u) series, geometric sum}"],
           decompose=[
               dict(title="Log of the product is a sum of logs", requires="working",
                    prose=r"$\log\prod_k(1-aq^k)=\sum_k\log(1-aq^k)$ — the log of a product is the sum of the logs.",
                    math=[r"\log\prod_{k\ge0}(1-aq^k)=\sum_{k\ge0}\log(1-aq^k)"],
                    references=["sub-method: log of a product -> sum of logs"],
                    decompose=[
                        dict(title="The product-to-sum log rule", requires="plain",
                             prose=r"$\log(AB)=\log A+\log B$, extended to the whole product.",
                             math=[r"\log\prod_k X_k=\sum_k\log X_k"]),
                    ]),
               dict(title="Expand each log and swap the sums", requires="working",
                    prose=r"Use $\log(1-u)=-\sum_n u^n/n$ with $u=aq^k$, then interchange $\sum_k$ and $\sum_n$ "
                          r"(legal for $|a|,|q|<1$), pulling $a^n/n$ out front.",
                    math=[r"\sum_k\log(1-aq^k)=-\sum_k\sum_n\frac{(aq^k)^n}{n}=-\sum_n\frac{a^n}{n}\sum_k q^{kn}"],
                    references=["sub-method: log(1-u) series"],
                    decompose=[
                        dict(title="Series for log(1-u)", requires="plain",
                             prose=r"$\log(1-u)=-(u+\tfrac{u^2}{2}+\tfrac{u^3}{3}+\cdots)$ for $|u|<1$.",
                             math=[r"\log(1-u)=-\sum_{n\ge1}\frac{u^n}{n}"]),
                        dict(title="Separate the k- and n-dependence", requires="plain",
                             prose=r"$(aq^k)^n=a^n q^{kn}$, so $a^n/n$ comes outside the $k$-sum.",
                             math=[r"(aq^k)^n=a^n q^{kn}\ \Rightarrow\ -\sum_n\frac{a^n}{n}\sum_k q^{kn}"]),
                    ]),
               dict(title="Resum the geometric series over k", requires="working",
                    prose=r"$\sum_{k\ge0}q^{kn}$ is geometric with ratio $q^n$, so it sums to $1/(1-q^n)$. Substituting "
                          r"gives the Lambert series.",
                    math=[r"\sum_{k\ge0}q^{kn}=\frac{1}{1-q^n}\ \Rightarrow\ \log(a;q)_\infty=-\sum_n\frac{a^n}{n(1-q^n)}"],
                    references=["sub-method: geometric series sum"],
                    decompose=[
                        dict(title="Geometric series", requires="plain",
                             prose=r"$1+r+r^2+\cdots=\frac{1}{1-r}$ for $|r|<1$; here $r=q^n$.",
                             math=[r"\sum_{k\ge0}(q^n)^k=\frac{1}{1-q^n}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"The engine's `q_pochhammer_log` resums $\sum_k q^{kn}=1/(1-q^n)$ for each $n$ (nothing written in) "
        r"and returns $-\sum_n a^n/(n(1-q^n))$, matching Euler / DLMF 17. Independent NUMERIC check: at "
        r"$q=\tfrac12,a=\tfrac1{10}$ the truncated series agrees with $\log\prod_{k=0}^{200}(1-aq^k)$ to 1e-10.",
        math=[r"\log(a;q)_\infty=-\sum_{n\ge1}\frac{a^n}{n(1-q^n)}\quad(\text{Euler, DLMF 17.2})",
              r"q=\tfrac12,\,a=\tfrac1{10}:\ \ \text{series}=-0.20707653\ldots=\log\!\prod_k(1-aq^k)"],
        references=["engine: special_methods.q_pochhammer_log (geometric resummation of the log-product)",
                    "DLMF 17.2 / Euler — independent published q-Pochhammer log identity",
                    "mpmath infinite-product evaluation — numeric oracle"])
    d.result(
        latex=r"\log\,(a;q)_\infty=-\sum_{n\ge1}\frac{a^{n}}{n\,(1-q^{n})},\qquad |q|<1",
        note="Lambert series derived by log-product + geometric resummation (1/(1-q^n) computed, nothing "
             "written in); opens the q-series kernel under localization, Jack polynomials and knot invariants.")
    return d
