"""LEVELED Derivation for the EULER-MACLAURIN method  (EXECUTABLE).

Worked target:  H_n = sum_{k=1}^n 1/k  ~  ln n + gamma + 1/(2n) - 1/(12 n^2) + ...

Realization mirrored: special_methods.euler_maclaurin_harmonic. The engine APPLIES Euler-Maclaurin
to f(x)=1/x: it computes the integral (ln n), the endpoint term (1/(2n)), and the Bernoulli-derivative
corrections (B_{2j}/(2j)! * f^{(2j-1)}(n), with B_{2j} from sympy and f^{(2j-1)} differentiated) — so
-1/(12 n^2), +1/(120 n^4), ... EMERGE; gamma is the Euler-Mascheroni constant (the n-independent limit).
Promoted from recognition-only once a non-covering executable existed (the corrections are computed,
not written in); gated on the published H_n asymptotic + a numeric oracle.

The per-level step COUNTS EMERGE from the `decompose` tree:
  expert chunks "apply Euler-Maclaurin to 1/x" into ONE node;
  working sees the standard EM moves (set up the formula, the integral term, the
     1/(2n) boundary term, the Bernoulli correction, collect the constant);
  plain decomposes each of those down to high-school algebra / a base library page.

Run:  python scratch/expl_euler_maclaurin.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = r"H_n=\sum_{k=1}^{n}\frac{1}{k}\ \sim\ \ln n+\gamma+\frac{1}{2n}-\frac{1}{12n^{2}}+\cdots"

def build_euler_maclaurin_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"asymptotics of the harmonic number $H_n$ via Euler-Maclaurin summation",
        goal=Goal.EXPAND,
        integral="Euler-Maclaurin: H_n ~ ln n + gamma + 1/(2n) - 1/(12 n^2)")
    d = Derivation(problem)

    # ---- WHY (recognition / decision) --------------------------------------
    d.why("Why this approach — Euler-Maclaurin summation",
          {"plain": r"We want a formula for the running total $1+\tfrac12+\cdots+\tfrac1n$. A sum is like "
                    r"a staircase and the integral $\int 1/x\,dx=\ln x$ is the smooth ramp underneath it. "
                    r"Euler-Maclaurin says: total $\approx$ the area under the ramp, plus small, "
                    r"shrinking corrections for the gap between the staircase and the ramp.",
           "working": r"$H_n=\sum 1/k$ has no elementary closed form, but $f(k)=1/k$ is smooth and the sum "
                      r"is a Riemann-sum sibling of $\int_1^n dx/x=\ln n$. Euler-Maclaurin makes the "
                      r"sum$-$integral difference EXACT as a series in the boundary derivatives of $f$, "
                      r"so we get $\ln n+\gamma+1/(2n)-\cdots$ to any order.",
           "expert": r"$f(x)=1/x$ is $C^\infty$ on $[1,n]$ with rapidly decaying derivatives, so the "
                     r"Euler-Maclaurin formula's remainder is controlled and the asymptotic series in the "
                     r"Bernoulli numbers converges as an asymptotic expansion — the canonical tool for "
                     r"sum-to-integral asymptotics."},
          forced_by=r"the target is a SUM of a smooth $f(k)=1/k$ with no elementary closed form, but whose "
                    r"continuous analogue $\int dx/x$ is trivial — exactly the sum-vs-integral gap "
                    r"Euler-Maclaurin is built to quantify.",
          payoff=r"it produces the WHOLE asymptotic series ($\ln n$, the constant $\gamma$, $1/(2n)$, "
                 r"$-1/(12n^2)$, ...) in one framework, and it MANUFACTURES the Euler-Mascheroni constant "
                 r"$\gamma$ as the limit of the boundary terms — a bare numerical $H_n$ would hide all of that.",
          relies_on=r"$f\in C^{2m}$ on $[1,n]$ with integrable derivatives so the Bernoulli-number remainder "
                    r"is bounded; here $f^{(j)}(x)=(-1)^j j!\,x^{-j-1}\to0$, so every correction is "
                    r"$O(n^{-j})$ and the expansion is legitimate.")

    # ---- HOW (the machinery) -----------------------------------------------
    d.how("How the approach works — the Euler-Maclaurin formula",
          {"plain": r"For a smooth $f$, the sum and the integral differ by a half-and-the-endpoints term "
                    r"plus a tail built from the derivatives of $f$ at the two ends. Each tail term is "
                    r"smaller than the last, so a few of them give a very accurate answer.",
           "working": r"$\sum_{k=a}^{b}f(k)=\int_a^b f\,dx+\tfrac12(f(a)+f(b))+\sum_{j\ge1}"
                      r"\tfrac{B_{2j}}{(2j)!}\big(f^{(2j-1)}(b)-f^{(2j-1)}(a)\big)+R$, where $B_{2j}$ are "
                      r"the Bernoulli numbers and $R$ is a bounded remainder.",
           "expert": r"Repeated IBP of $\int_a^b f\,\widetilde B_k(x)/k!\,dx$ against the periodic Bernoulli "
                     r"polynomials $\widetilde B_k$ yields the Euler-Maclaurin formula; $B_2=\tfrac16$, "
                     r"$B_4=-\tfrac1{30}$ give the $1/(2n)$ and $-1/(12n^2)$ terms."},
          math=[r"\sum_{k=a}^{b}f(k)=\int_{a}^{b}f(x)\,dx+\frac{f(a)+f(b)}{2}"
                r"+\sum_{j=1}^{m}\frac{B_{2j}}{(2j)!}\Big(f^{(2j-1)}(b)-f^{(2j-1)}(a)\Big)+R_m"])

    # ---- STEP (the worked execution) ---------------------------------------
    # ONE qualification tree. Counts EMERGE from the cut:
    #   expert  -> 1 step  (the whole EM application is one move)
    #   working -> the 5 standard EM sub-moves
    #   plain   -> each sub-move broken to high-school pieces
    d.step("Apply Euler-Maclaurin to f(x)=1/x on [1,n]", requires="expert",
           prose=r"With $f(x)=1/x$: the integral gives $\ln n$, the endpoint term gives $\tfrac12(1+\tfrac1n)$, "
                 r"the $B_2$ term gives $-\tfrac1{12}(\tfrac1{n^2}-1)$; collecting the $n$-independent pieces "
                 r"DEFINES $\gamma$, leaving $H_n=\ln n+\gamma+\tfrac1{2n}-\tfrac1{12n^2}+\cdots$.",
           math=[r"H_n=\underbrace{\ln n}_{\int_1^n dx/x}+\underbrace{\tfrac12\big(1+\tfrac1n\big)}_{\text{endpoints}}"
                 r"-\underbrace{\tfrac1{12}\big(\tfrac1{n^2}-1\big)}_{B_2\text{ term}}+\cdots"
                 r"=\ln n+\gamma+\frac{1}{2n}-\frac{1}{12n^2}+\cdots"],
           relies_on=r"sub-methods: the Euler-Maclaurin formula (IBP against Bernoulli polynomials) + the "
                     r"derivative tower of $1/x$ + the definition of $\gamma$ as the limiting constant.",
           decompose=[
               # --- WORKING move 1: the integral term ---
               dict(title="The integral term gives ln n", requires="working",
                    prose=r"Take $a=1,b=n,f(x)=1/x$ in the formula; the leading $\int_1^n f\,dx$ is the "
                          r"logarithm.",
                    math=[r"\int_{1}^{n}\frac{dx}{x}=\ln n-\ln 1=\ln n"],
                    relies_on=r"sub-method: the antiderivative $\int dx/x=\ln x$.",
                    decompose=[
                        dict(title="Antiderivative of 1/x", requires="plain",
                             prose=r"The area under $1/x$ from $1$ to $n$ is a logarithm — a standard integral.",
                             math=[r"\int_{1}^{n}\frac{dx}{x}=\big[\ln x\big]_{1}^{n}=\ln n"],
                             references=["base method -> library/log-integral.md"]),
                    ]),
               # --- WORKING move 2: the endpoint (half) term -> the 1/(2n) ---
               dict(title="The endpoint term gives 1/2 + 1/(2n)", requires="working",
                    prose=r"The $\tfrac12(f(a)+f(b))$ term evaluates $f$ at the two ends; the moving end "
                          r"$b=n$ supplies the $\tfrac1{2n}$ that survives in the expansion.",
                    math=[r"\frac{f(1)+f(n)}{2}=\frac{1+\tfrac1n}{2}=\frac12+\frac{1}{2n}"],
                    decompose=[
                        dict(title="Evaluate f at the two ends", requires="plain",
                             prose=r"$f(1)=1/1=1$ and $f(n)=1/n$; just substitute.",
                             math=[r"f(1)=1,\qquad f(n)=\tfrac1n"]),
                        dict(title="Average them", requires="plain",
                             prose=r"Add and halve: the $1$ is a constant kept for $\gamma$; the $\tfrac1{2n}$ "
                                   r"is the visible $n$-correction.",
                             math=[r"\tfrac12\big(1+\tfrac1n\big)=\tfrac12+\tfrac1{2n}"]),
                    ]),
               # --- WORKING move 3: the Bernoulli B_2 correction -> -1/(12 n^2) ---
               dict(title="The B_2 term gives -1/(12 n^2) + 1/12", requires="working",
                    prose=r"The first Bernoulli correction uses $B_2=\tfrac16$ and $f'(x)=-1/x^2$ at the two "
                          r"ends, producing the $-\tfrac1{12n^2}$ term (and a constant $+\tfrac1{12}$).",
                    math=[r"\frac{B_2}{2!}\big(f'(n)-f'(1)\big)=\frac{1/6}{2}\Big(-\frac1{n^2}+1\Big)"
                          r"=-\frac{1}{12n^2}+\frac1{12}"],
                    relies_on=r"sub-methods: the Bernoulli number $B_2=\tfrac16$ + the derivative $f'(x)=-1/x^2$.",
                    decompose=[
                        dict(title="The derivative f'(x) = -1/x^2", requires="plain",
                             prose=r"Differentiate $f(x)=x^{-1}$ by the power rule.",
                             math=[r"f'(x)=\frac{d}{dx}x^{-1}=-x^{-2}=-\frac1{x^2}"],
                             references=["base method -> library/power-rule.md"]),
                        dict(title="Evaluate f' at the two ends", requires="plain",
                             prose=r"$f'(n)=-1/n^2$ (the $n$-correction) and $f'(1)=-1$ (a constant).",
                             math=[r"f'(n)=-\tfrac1{n^2},\qquad f'(1)=-1"]),
                        dict(title="Multiply by B_2/2! = 1/12", requires="plain",
                             prose=r"With $B_2=\tfrac16$, the prefactor is $\tfrac{1/6}{2}=\tfrac1{12}$; "
                                   r"multiply the bracket through.",
                             math=[r"\tfrac1{12}\big(-\tfrac1{n^2}+1\big)=-\tfrac1{12n^2}+\tfrac1{12}"]),
                    ]),
               # --- WORKING move 4: collect the n-independent constant = gamma ---
               dict(title="Collect the constants -> this defines gamma", requires="working",
                    prose=r"Gather every $n$-independent leftover ($\tfrac12$ from the endpoint, $\tfrac1{12}$ "
                          r"from $B_2$, and the higher tails). Their total is, by DEFINITION, the "
                          r"Euler-Mascheroni constant $\gamma\approx0.5772$.",
                    math=[r"\gamma:=\lim_{n\to\infty}\Big(H_n-\ln n\Big)"
                          r"=\tfrac12+\tfrac1{12}-\cdots\approx0.5772156649"],
                    relies_on=r"sub-method: the definition of $\gamma$ as $\lim(H_n-\ln n)$.",
                    decompose=[
                        dict(title="Separate n-dependent from constant pieces", requires="plain",
                             prose=r"Every term is either a power of $1/n$ (vanishes as $n\to\infty$) or a pure "
                                   r"number; sort them into two piles.",
                             math=[r"H_n=\ln n+\underbrace{\big(\tfrac12+\tfrac1{12}-\cdots\big)}_{\text{constants}}"
                                   r"+\underbrace{\tfrac1{2n}-\tfrac1{12n^2}+\cdots}_{\to0}"]),
                        dict(title="Name the constant pile gamma", requires="plain",
                             prose=r"As $n\to\infty$ the $1/n$ pile dies, so $H_n-\ln n$ tends to the constant "
                                   r"pile; we call that limit $\gamma$.",
                             math=[r"\lim_{n\to\infty}(H_n-\ln n)=\gamma"]),
                    ]),
               # --- WORKING move 5: assemble the expansion ---
               dict(title="Assemble the expansion", requires="working",
                    prose=r"Put the four pieces back together to order $n^{-2}$.",
                    math=[r"H_n=\ln n+\gamma+\frac{1}{2n}-\frac{1}{12n^2}+O\!\big(n^{-4}\big)"],
                    decompose=[
                        dict(title="Write the surviving terms in order", requires="plain",
                             prose=r"List them largest-to-smallest: $\ln n$, then the constant $\gamma$, then "
                                   r"$\tfrac1{2n}$, then $-\tfrac1{12n^2}$.",
                             math=[r"H_n\approx\ln n+\gamma+\frac{1}{2n}-\frac{1}{12n^2}"]),
                    ]),
           ])

    # ---- VERIFY (the engine executes it; gated on the published asymptotic + numeric oracle) ---
    d.verify(
        r"The engine's `euler_maclaurin_harmonic` BUILDS the expansion from $f=1/x$: $\int_1^n=\ln n$, the "
        r"endpoint $1/(2n)$, and the Bernoulli-derivative corrections $\tfrac{B_{2j}}{(2j)!}f^{(2j-1)}(n)$ "
        r"(computed via sympy `bernoulli` + differentiation, nothing written in), returning "
        r"$\ln n+\gamma+\tfrac1{2n}-\tfrac1{12n^2}+\tfrac1{120n^4}$ — matching the published $H_n$ asymptotic. "
        r"Numeric oracle: at $n=100$, the expansion equals $H_{100}=5.18737752\ldots$ to 1e-8.",
        math=[r"H_n=\ln n+\gamma+\frac{1}{2n}-\frac{1}{12n^2}+\frac{1}{120n^4}+\cdots\quad(\text{DLMF 2.10})",
              r"n=100:\ \text{expansion}=H_{100}=5.1873775176\ldots"],
        references=["engine: special_methods.euler_maclaurin_harmonic (integral + endpoint + Bernoulli corrections)",
                    "DLMF 2.10 / Forster (LMU) — independent published Euler-Maclaurin / H_n asymptotic",
                    "sub-method: library/bernoulli-numbers.md",
                    "mpmath/sympy harmonic — numeric oracle"])
    d.result(
        latex=r"H_n=\sum_{k=1}^{n}\frac1k=\ln n+\gamma+\frac{1}{2n}-\frac{1}{12n^{2}}+O\!\big(n^{-4}\big)",
        note="executable: the engine applies Euler-Maclaurin to 1/x and computes the integral + endpoint + "
             "Bernoulli-derivative corrections (gamma is the Euler-Mascheroni constant); promoted from "
             "recognition-only once a genuinely non-covering executable existed.")
    return d

def main():
    d = build_euler_maclaurin_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level counts (emergent):", counts)
    print("counts differ:", len(set(counts.values())) > 1)
    print("validate_qualification:", qwarn if qwarn else "[] (VALID — no warnings)")
    assert not qwarn, qwarn
    assert len(set(counts.values())) > 1, counts
    print("OK")
