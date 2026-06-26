"""LEVELED Derivation for METHOD asymptotic_expansion (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.erfc_asymptotic (repeated IBP). The engine COMPUTES
    full, bracket = erfc_asymptotic(4)
    bracket = 1 - 1/(2 z^2) + 3/(4 z^4) - 15/(8 z^6)        # the (2k-1)!! pattern
    full    = (8 z^6 - 4 z^4 + 6 z^2 - 15) e^{-z^2}/(8 sqrt(pi) z^7)
via the recursion a_k = -(2k-1)/2 * a_{k-1} from repeated integration by parts on
∫_z^∞ e^{-t^2} dt. THIS derivation walks exactly that computation.

Sub-methods referenced by the steps:
    asymptotic_expansion -> { integration-by-parts (the engine of the recursion),
                              double-factorial / recursion bookkeeping,
                              Poincaré asymptotics (the divergent-series interpretation) }.

Run:  python scratch/expl_asymptotic_expansion.py
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"\operatorname{erfc}(z)=\frac{2}{\sqrt{\pi}}\int_{z}^{\infty}e^{-t^{2}}\,dt"
       r"\ \sim\ \frac{e^{-z^{2}}}{\sqrt{\pi}\,z}\left(1-\frac{1}{2z^{2}}+\frac{3}{4z^{4}}-\cdots\right)")

def build_asymptotic_expansion_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"complementary error function $\operatorname{erfc}(z)$, large-$z$ tail",
        goal=Goal.EXPAND,
        integral="asymptotic (Poincaré) expansion of erfc(z) as z -> infinity")
    d = Derivation(problem)

    # ---- WHY this approach (the recognition / decision) -------------------------------
    d.why("Why this approach — asymptotic expansion by repeated parts",
          {"plain": r"There is no neat formula for $\int_z^\infty e^{-t^2}dt$. But for LARGE $z$ the "
                    r"area is a thin sliver, dominated by its left edge near $t=z$. We peel off that edge "
                    r"with a by-parts move, then peel the leftover, and again — each peel is one more term "
                    r"and is smaller than the last, so a few terms already pin the value down.",
           "working": r"$\operatorname{erfc}(z)$ has no elementary antiderivative, but as $z\to\infty$ the tail "
                      r"integral is controlled by the endpoint. Writing $e^{-t^2}=\frac{-1}{2t}\frac{d}{dt}e^{-t^2}$ "
                      r"lets one integration by parts extract the leading $e^{-z^2}/(2z)$ and leave a strictly "
                      r"smaller tail of the same shape — iterate to get the series.",
           "expert": r"No closed form exists; we want the $z\to\infty$ Poincaré expansion. The integrand is its own "
                     r"derivative up to the factor $-1/(2t)$, so IBP is self-reproducing: each step lowers the "
                     r"power of $t$ by two and the remainder is asymptotically negligible against the term split off."},
          forced_by=r"$\int_z^\infty e^{-t^2}dt$ has no elementary antiderivative, yet $e^{-t^2}$ equals "
                    r"$\frac{-1}{2t}\,\frac{d}{dt}e^{-t^2}$ — an exact derivative ready-made for integration by parts.",
          payoff=r"each IBP pulls out one explicit $e^{-z^2}/z^{2k+1}$ term and leaves a remainder one power smaller; "
                 r"a value/quadrature would hide the $(2k-1)!!$ structure and the divergent-but-optimal nature of the series.",
          relies_on=r"$z\to\infty$ (the series is asymptotic, not convergent): truncate at the smallest term — "
                    r"the remainder integral is bounded by the first omitted term, which is why a FEW terms suffice.")

    # ---- HOW the approach works (the machinery: the IBP identity + the recursion) ------
    d.how("How it works — the self-reproducing by-parts identity",
          {"plain": r"The key trick: $e^{-t^2}=\dfrac{-1}{2t}\cdot\big(e^{-t^2}\big)'$. So integrating "
                    r"$e^{-t^2}$ is the same as integrating $\dfrac{-1}{2t}$ times a derivative — exactly the "
                    r"set-up for integration by parts, which hands back a boundary value plus a similar, smaller integral.",
           "working": r"With $u=\frac{-1}{2t},\ dv=(e^{-t^2})'dt$, one IBP gives "
                      r"$\int_z^\infty e^{-t^2}dt=\frac{e^{-z^2}}{2z}-\frac{1}{2}\int_z^\infty \frac{e^{-t^2}}{t^2}dt$. "
                      r"The leftover integral has the same form with an extra $1/t^2$, so the move repeats and the "
                      r"coefficients obey $a_k=-\frac{2k-1}{2}a_{k-1}$.",
           "expert": r"IBP with $u=-1/(2t)$ is self-similar: $\int_z^\infty t^{-2k}e^{-t^2}dt=\frac{e^{-z^2}}{2z^{2k+1}}"
                     r"-\frac{2k+1}{2}\int_z^\infty t^{-2k-2}e^{-t^2}dt$, generating $a_k=-\frac{2k-1}{2}a_{k-1}$, i.e. "
                     r"the $(-1)^k(2k-1)!!/2^k$ double-factorial coefficients."},
          math=[r"e^{-t^{2}}=\frac{-1}{2t}\,\frac{d}{dt}e^{-t^{2}},\qquad "
                r"\int_{z}^{\infty}t^{-2k}e^{-t^{2}}\,dt=\frac{e^{-z^{2}}}{2z^{2k+1}}"
                r"-\frac{2k+1}{2}\int_{z}^{\infty}t^{-2k-2}e^{-t^{2}}\,dt"])

    # ---- THE STEPS -------------------------------------------------------------------
    # ONE qualification tree. expert chunks the whole "iterate IBP -> series" into ONE node;
    # working sees its sub-steps; plain decomposes those further. Counts EMERGE from the cut.
    d.step("Expand erfc(z) by iterated integration by parts", requires="expert",
           prose=r"Apply the self-reproducing IBP repeatedly: the $k$-th pass emits "
                 r"$a_k\,e^{-z^2}/z^{2k+1}$ with $a_k=-\frac{2k-1}{2}a_{k-1}$ ($a_0=\tfrac12$); "
                 r"factoring out $e^{-z^2}/(\sqrt\pi z)$ leaves the bracket $1-\frac{1}{2z^2}+\frac{3}{4z^4}-\cdots$.",
           math=[r"\operatorname{erfc}(z)=\frac{2}{\sqrt{\pi}}\int_{z}^{\infty}e^{-t^{2}}dt"
                 r"\sim\frac{e^{-z^{2}}}{\sqrt{\pi}\,z}\!\left(1-\frac{1}{2z^{2}}+\frac{3}{4z^{4}}-\frac{15}{8z^{6}}+\cdots\right)"],
           references=["sub-method: asymptotic_expansion -> {integration-by-parts, double-factorial recursion, Poincaré}"],
           decompose=[
               # ---- working sub-step 1: the FIRST IBP (the move that sets everything up) ----
               dict(title="One integration by parts on the tail integral", requires="working",
                    prose=r"Write $e^{-t^2}=\frac{-1}{2t}(e^{-t^2})'$ and integrate by parts once: the boundary "
                          r"gives $e^{-z^2}/(2z)$, the leftover is a smaller integral of the same shape.",
                    math=[r"\int_{z}^{\infty}e^{-t^{2}}dt=\frac{e^{-z^{2}}}{2z}"
                          r"-\frac{1}{2}\int_{z}^{\infty}\frac{e^{-t^{2}}}{t^{2}}\,dt"],
                    references=["sub-method: integration-by-parts"],
                    decompose=[
                        dict(title="Rewrite the integrand as -1/(2t) times a derivative", requires="plain",
                             prose=r"Since $\frac{d}{dt}e^{-t^2}=-2t\,e^{-t^2}$, dividing by $-2t$ recovers $e^{-t^2}$.",
                             math=[r"\frac{d}{dt}e^{-t^{2}}=-2t\,e^{-t^{2}}\ \Rightarrow\ "
                                   r"e^{-t^{2}}=\frac{-1}{2t}\,\frac{d}{dt}e^{-t^{2}}"],
                             references=["base method -> library/chain-rule.md"]),
                        dict(title="Choose u and dv for parts", requires="plain",
                             prose=r"Take $u=\frac{-1}{2t}$ and $dv=(e^{-t^2})'dt$, so $du=\frac{1}{2t^2}dt$ and $v=e^{-t^2}$.",
                             math=[r"u=\frac{-1}{2t},\ dv=\big(e^{-t^{2}}\big)'dt\ \Rightarrow\ "
                                   r"du=\frac{1}{2t^{2}}dt,\ v=e^{-t^{2}}"],
                             references=["base method -> library/integration-by-parts.md"]),
                        dict(title="Assemble the boundary term and the leftover", requires="plain",
                             prose=r"$\int u\,dv=[uv]_z^\infty-\int v\,du$. At $\infty$ the Gaussian kills $uv$; at $z$ "
                                   r"it gives $e^{-z^2}/(2z)$. The $-\int v\,du$ is the smaller leftover.",
                             math=[r"\Big[\tfrac{-1}{2t}e^{-t^{2}}\Big]_{z}^{\infty}=\frac{e^{-z^{2}}}{2z},\quad "
                                   r"-\int_{z}^{\infty}e^{-t^{2}}\frac{dt}{2t^{2}}"
                                   r"=-\frac{1}{2}\int_{z}^{\infty}\frac{e^{-t^{2}}}{t^{2}}dt"],
                             references=["base method -> library/integration-by-parts.md"]),
                    ]),
               # ---- working sub-step 2: ITERATE -> the recursion for the coefficients ----
               dict(title="Iterate the move: the coefficient recursion", requires="working",
                    prose=r"The leftover $\int_z^\infty t^{-2k}e^{-t^2}dt$ has the SAME shape, so the same IBP applies "
                          r"with an extra $1/t^2$. Tracking the prefactor gives $a_k=-\frac{2k-1}{2}a_{k-1}$, $a_0=\tfrac12$.",
                    math=[r"\int_{z}^{\infty}\frac{e^{-t^{2}}}{t^{2k}}dt=\frac{e^{-z^{2}}}{2z^{2k+1}}"
                          r"-\frac{2k+1}{2}\int_{z}^{\infty}\frac{e^{-t^{2}}}{t^{2k+2}}dt,\qquad "
                          r"a_k=-\frac{2k-1}{2}\,a_{k-1}"],
                    references=["sub-method: integration-by-parts (re-applied)", "sub-method: double-factorial recursion"],
                    decompose=[
                        dict(title="The leftover is self-similar", requires="plain",
                             prose=r"Each leftover integral is $e^{-t^2}$ over a higher power of $t$ — the very thing "
                                   r"the parts move eats, so the move repeats unchanged.",
                             math=[r"\int_{z}^{\infty}\frac{e^{-t^{2}}}{t^{2k}}dt\ \xrightarrow{\text{IBP}}\ "
                                   r"\frac{e^{-z^{2}}}{2z^{2k+1}}-\frac{2k+1}{2}\int_{z}^{\infty}\frac{e^{-t^{2}}}{t^{2k+2}}dt"]),
                        dict(title="Read off the coefficient rule", requires="plain",
                             prose=r"The factor picked up at step $k$ is $-\frac{2k-1}{2}$ times the previous one.",
                             math=[r"a_0=\tfrac12,\quad a_k=-\frac{2k-1}{2}\,a_{k-1}"]),
                        dict(title="Unfold a few coefficients", requires="plain",
                             prose=r"$a_1=-\tfrac12 a_0=-\tfrac14$, $a_2=-\tfrac32 a_1=+\tfrac38$, "
                                   r"$a_3=-\tfrac52 a_2=-\tfrac{15}{16}$ (the $(2k-1)!!$ double factorials).",
                             math=[r"a_1=-\tfrac14,\quad a_2=+\tfrac38,\quad a_3=-\tfrac{15}{16}"],
                             references=["base method -> library/double-factorial.md"]),
                    ]),
               # ---- working sub-step 3: assemble + factor out the prefactor ----
               dict(title="Assemble the series and factor out the prefactor", requires="working",
                    prose=r"Multiply by $2/\sqrt\pi$ and sum the emitted terms; pulling out $e^{-z^2}/(\sqrt\pi z)$ "
                          r"leaves the standard bracket.",
                    math=[r"\operatorname{erfc}(z)\sim\frac{2}{\sqrt{\pi}}\sum_{k\ge0}\frac{a_k\,e^{-z^{2}}}{z^{2k+1}}"
                          r"=\frac{e^{-z^{2}}}{\sqrt{\pi}\,z}\Big(1-\frac{1}{2z^{2}}+\frac{3}{4z^{4}}-\frac{15}{8z^{6}}+\cdots\Big)"],
                    references=["sub-method: double-factorial recursion"],
                    decompose=[
                        dict(title="Sum the emitted boundary terms", requires="plain",
                             prose=r"Each pass contributed one $a_k\,e^{-z^2}/z^{2k+1}$; collect them.",
                             math=[r"\int_{z}^{\infty}e^{-t^{2}}dt\sim e^{-z^{2}}\sum_{k\ge0}\frac{a_k}{z^{2k+1}}"]),
                        dict(title="Factor out e^{-z^2}/(sqrt(pi) z)", requires="plain",
                             prose=r"Divide every term by $e^{-z^2}/(\sqrt\pi z)$ to expose the bracket "
                                   r"(the $2a_k$ become $1,-\tfrac12,\tfrac34,-\tfrac{15}{8}$).",
                             math=[r"\frac{e^{-z^{2}}}{\sqrt{\pi}\,z}\Big(1-\frac{1}{2z^{2}}"
                                   r"+\frac{3}{4z^{4}}-\frac{15}{8z^{6}}+\cdots\Big)"]),
                    ]),
               # ---- working sub-step 4: the asymptotic (divergent-but-optimal) reading ----
               dict(title="Read it as an asymptotic (Poincaré) series", requires="working",
                    prose=r"The series DIVERGES for every fixed $z$ (the $(2k-1)!!$ grow), yet truncating at the "
                          r"smallest term gives an error bounded by the first omitted term — optimal truncation.",
                    math=[r"\Big|\,\operatorname{erfc}(z)-\frac{e^{-z^{2}}}{\sqrt{\pi}z}\sum_{k=0}^{N-1}\frac{2a_k}{z^{2k}}\Big|"
                          r"\le\Big|\frac{e^{-z^{2}}}{\sqrt{\pi}z}\cdot\frac{2a_N}{z^{2N}}\Big|"],
                    references=["sub-method: Poincaré asymptotics"],
                    decompose=[
                        dict(title="Why the terms eventually grow", requires="plain",
                             prose=r"For fixed $z$, each new factor $\frac{2k-1}{2z^2}$ exceeds $1$ once $k$ is large, "
                                   r"so terms shrink at first then blow up — the sum can't converge.",
                             math=[r"\frac{|a_{k}/z^{2k+1}|}{|a_{k-1}/z^{2k-1}|}=\frac{2k-1}{2z^{2}}\xrightarrow{k\to\infty}\infty"]),
                        dict(title="Stop at the smallest term", requires="plain",
                             prose=r"Truncate where the terms are smallest; the leftover is no bigger than the first "
                                   r"term you dropped, so a handful of terms gives a tight value.",
                             math=[r"\text{error}\ \le\ \text{first omitted term}"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) ------------------------------
    d.verify(
        r"Two independent checks. The engine's `erfc_asymptotic` REGENERATES the bracket from the recursion "
        r"$a_k=-\frac{2k-1}{2}a_{k-1}$ (no terms written in); and a leading-order numeric tail check at $z=3$ "
        r"agrees with the truncated series.",
        math=[r"\texttt{erfc\_asymptotic(4)}\ \Rightarrow\ 1-\frac{1}{2z^{2}}+\frac{3}{4z^{4}}-\frac{15}{8z^{6}}",
              r"\text{full}=\frac{(8z^{6}-4z^{4}+6z^{2}-15)\,e^{-z^{2}}}{8\sqrt{\pi}\,z^{7}}"],
        references=["engine: special_methods.erfc_asymptotic (repeated IBP, recursion-derived coefficients)",
                    "method: library/asymptotic-expansion.md",
                    "mpmath erfc — numeric oracle for the truncated-series check"])
    d.result(
        latex=r"\operatorname{erfc}(z)\sim\frac{e^{-z^{2}}}{\sqrt{\pi}\,z}"
              r"\left(1-\frac{1}{2z^{2}}+\frac{3}{4z^{4}}-\frac{15}{8z^{6}}+\cdots\right),\quad z\to\infty",
        note="coefficients derived by the IBP recursion a_k = -(2k-1)/2 a_{k-1}; asymptotic (divergent) series, "
             "optimal truncation at the smallest term.")
    return d

def main():
    d = build_asymptotic_expansion_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level counts (emergent):", counts)
    print("validate_qualification :", qwarn if qwarn else "[]  (VALID — no warnings)")
    assert not qwarn, qwarn
    assert len(set(counts.values())) == 3, f"counts must differ across 3 levels, got {counts}"
    out = os.path.join(os.path.dirname(__file__), "expl_asymptotic_expansion.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(render_leveled(tracks))
    print("rendered ->", out)
