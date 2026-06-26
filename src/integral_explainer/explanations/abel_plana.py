"""LEVELED Derivation for the Abel-Plana formula (RECOGNITION-ONLY method).

Worked target: the Hurwitz-zeta integral representation. Apply the Abel-Plana
formula to f(n) = (n+a)^{-s} to turn the defining series

    zeta(s, a) = sum_{n>=0} (n+a)^{-s}        (Re s > 1)

into

    zeta(s, a) = a^{-s}/2 + a^{1-s}/(s-1)
                 + 2 * int_0^inf  sin( s * arctan(t/a) ) / ((a^2+t^2)^{s/2} (e^{2*pi*t}-1)) dt

which analytically continues zeta(s,a) to Re s > -1 (all s != 1), the payoff of
the formula: the divergent tail is replaced by a convergent oscillatory integral.

HONESTY / CEILING (CLAUDE.md rules 10, 11): abel_plana is RECOGNITION-ONLY. The
engine has NO honest generic transform that takes f and emits the Abel-Plana
right-hand side, and NO external gate has been executed for it. So the executable
move ("apply Abel-Plana to f(n)=(n+a)^{-s} and simplify the boundary integrand")
is recorded as an HONEST CEILING: requires='expert', NO decompose, prose states
what the method WOULD do and what is missing. validate_qualification therefore
only complains if that ceiling node were shown to a reader below expert — which is
exactly correct: plain/working cannot reach the engine-executed transform because
the engine cannot execute it. The why / how / recognition + the surrounding
manual worked steps ARE decomposed to high-school, so the per-level counts still
emerge and differ.

Local-only scratch (rule 1): NOT in src/, not wired, just the explanation tree.
"""

from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"\zeta(s,a)=\sum_{n=0}^{\infty}(n+a)^{-s}"
       r"\;\xrightarrow{\text{Abel--Plana}}\;"
       r"\frac{a^{-s}}{2}+\frac{a^{1-s}}{s-1}"
       r"+2\!\int_{0}^{\infty}\!\frac{\sin\!\big(s\arctan\tfrac{t}{a}\big)}"
       r"{(a^{2}+t^{2})^{s/2}\,(e^{2\pi t}-1)}\,dt")

def build_abel_plana_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"Hurwitz zeta $\zeta(s,a)$ via the Abel--Plana sum-to-integral formula; "
                   r"goal is its integral representation / analytic continuation",
        goal=Goal.EVALUATE,
        integral="Hurwitz zeta integral representation (Abel-Plana)")
    d = Derivation(problem)

    # ----- WHY (recognition / decision) -------------------------------------
    d.why("Why Abel--Plana — convert a divergent sum into a convergent integral",
          {"plain": r"We want a single formula for the infinite sum $\zeta(s,a)=\sum_{n\ge0}(n+a)^{-s}$. "
                    r"Adding up infinitely many terms is awkward, and for many $s$ the sum even blows up. "
                    r"Abel--Plana is a rule that rewrites such a sum as a smooth integral plus a couple of "
                    r"simple correction terms — an integral is far easier to study and to extend.",
           "working": r"The defining series converges only for $\mathrm{Re}\,s>1$. Abel--Plana trades the sum "
                      r"for $\int_0^\infty f(x)\,dx+\tfrac12 f(0)$ plus a correction integral built from the "
                      r"imaginary-axis values of $f$; with $f(n)=(n+a)^{-s}$ the leading integral is elementary "
                      r"and the correction integral converges on a much larger $s$-region.",
           "expert": r"$f(z)=(z+a)^{-s}$ is holomorphic and of suitable decay in the right half-plane, so "
                     r"Abel--Plana applies; it exchanges the conditionally/divergent tail for a contour-borne "
                     r"correction $i\int_0^\infty\frac{f(iy)-f(-iy)}{e^{2\pi y}-1}\,dy$ that furnishes the "
                     r"analytic continuation to $\mathrm{Re}\,s>-1$."},
          forced_by=r"the object is a SUM whose convergence region ($\mathrm{Re}\,s>1$) is too small, and whose "
                    r"summand $f(z)=(z+a)^{-s}$ is holomorphic with controlled growth in the right half-plane — "
                    r"exactly the hypotheses Abel--Plana needs.",
          payoff=r"the divergent tail is replaced by an integral that converges for $\mathrm{Re}\,s>-1$, "
                 r"giving the analytic continuation past the series' wall and an exact, computable "
                 r"representation; a naive Euler--Maclaurin truncation would only give an asymptotic, not an "
                 r"exact, continuation.",
          relies_on=r"Abel--Plana's hypotheses: $f$ holomorphic on $\mathrm{Re}\,z\ge0$ and "
                    r"$|f(x+iy)|=o(e^{2\pi|y|})$ uniformly as $|y|\to\infty$ — true for $(z+a)^{-s}$ with "
                    r"$a>0$, which has its branch cut on the negative axis, away from the contour.")

    # ----- HOW (the machinery: the formula itself) --------------------------
    d.how("How Abel--Plana works — the sum-to-integral identity",
          {"plain": r"The formula says: a sum equals the matching integral, plus half the first term, plus a "
                    r"correction made from the function's values on the imaginary axis. We just plug "
                    r"$f(n)=(n+a)^{-s}$ into this ready-made rule.",
           "working": r"Abel--Plana: $\sum_{n\ge0}f(n)=\int_0^\infty f(x)\,dx+\tfrac12 f(0)"
                      r"+i\int_0^\infty\frac{f(iy)-f(-iy)}{e^{2\pi y}-1}\,dy$. It comes from contour-integrating "
                      r"$f(z)\cot(\pi z)$ / $f(z)/(e^{-2\pi i z}-1)$ and collecting residues at the integers.",
           "expert": r"$\sum_{n=0}^{\infty}f(n)=\int_0^\infty f+\tfrac12 f(0)+i\!\int_0^\infty"
                     r"\frac{f(iy)-f(-iy)}{e^{2\pi y}-1}dy$, the residue/contour identity from "
                     r"$\frac{1}{e^{-2\pi i z}-1}$ having unit residues at $z\in\mathbb{Z}$."},
          math=[r"\sum_{n=0}^{\infty}f(n)=\int_{0}^{\infty}f(x)\,dx+\frac{f(0)}{2}"
                r"+i\int_{0}^{\infty}\frac{f(iy)-f(-iy)}{e^{2\pi y}-1}\,dy"])

    # ----- STEPS (worked execution for f(n) = (n+a)^{-s}) -------------------
    # The single EXECUTABLE move is an HONEST CEILING (recognition-only: no engine
    # transform, no external gate). It carries requires="expert" and NO decompose,
    # so it is shown only to the expert reader. The surrounding MANUAL steps (the
    # leading integral, f(0), the correction integrand) ARE decomposed down to
    # high-school, so plain/working still expand and the counts differ.

    d.step("Apply the Abel--Plana transform to f(n) = (n+a)^{-s}  [engine ceiling]",
           requires="expert",
           prose=r"This is the one move the ENGINE would own: feed $f(z)=(z+a)^{-s}$ to a generic Abel--Plana "
                 r"transformer, which checks the holomorphy/decay hypotheses and emits the three right-hand "
                 r"terms. HONEST CEILING: abel_plana is RECOGNITION-ONLY — there is no executable generic "
                 r"transform in the engine yet and no external gate has been run, so the engine cannot itself "
                 r"produce this line. The sub-steps below carry out the SAME three terms by hand so a reader "
                 r"can still check the result; only the *automated* transform is missing.",
           math=[r"\zeta(s,a)=\underbrace{\int_0^\infty\!\!(x+a)^{-s}dx}_{\text{leading}}"
                 r"+\underbrace{\tfrac12 a^{-s}}_{f(0)/2}"
                 r"+\underbrace{i\!\int_0^\infty\!\frac{(a+iy)^{-s}-(a-iy)^{-s}}{e^{2\pi y}-1}dy}_{\text{correction}}"],
           decompose=[
               # --- term 1: the leading integral (decomposes to high-school) ---
               dict(title="Leading term: the elementary integral of (x+a)^{-s}",
                    requires="working",
                    prose=r"The $\int_0^\infty f$ piece is a plain power integral; it converges for "
                          r"$\mathrm{Re}\,s>1$ and gives $a^{1-s}/(s-1)$.",
                    math=[r"\int_0^\infty (x+a)^{-s}\,dx=\frac{a^{1-s}}{s-1}\qquad(\mathrm{Re}\,s>1)"],
                    references=["base method -> library/power-rule-integral.md"],
                    decompose=[
                        dict(title="Antiderivative of (x+a)^{-s}", requires="plain",
                             prose=r"Raise the power by one and divide: the antiderivative is "
                                   r"$(x+a)^{1-s}/(1-s)$ (the reverse power rule).",
                             math=[r"\int (x+a)^{-s}dx=\frac{(x+a)^{1-s}}{1-s}"],
                             references=["base method -> library/power-rule-integral.md"]),
                        dict(title="Evaluate the limits 0 and infinity", requires="plain",
                             prose=r"For $\mathrm{Re}\,s>1$ the top limit vanishes; the bottom gives $a^{1-s}$. "
                                   r"Flipping the sign of $1-s$ turns it into $a^{1-s}/(s-1)$.",
                             math=[r"\Big[\frac{(x+a)^{1-s}}{1-s}\Big]_0^\infty"
                                   r"=0-\frac{a^{1-s}}{1-s}=\frac{a^{1-s}}{s-1}"]),
                    ]),
               # --- term 2: the f(0)/2 term (high-school grokkable: just half a^{-s}) ---
               dict(title="Boundary term: half the first summand, f(0)/2",
                    requires="plain",
                    prose=r"Abel--Plana's $\tfrac12 f(0)$ correction is just half the $n=0$ term, $\tfrac12 a^{-s}$.",
                    math=[r"\frac{f(0)}{2}=\frac{(0+a)^{-s}}{2}=\frac{a^{-s}}{2}"],
                    references=["base method -> library/abel-plana-formula.md"]),
               # --- term 3: the correction integral (decomposes to high-school) ---
               dict(title="Correction term: the imaginary-axis integral",
                    requires="working",
                    prose=r"The contour correction uses $f(\pm iy)=(a\pm iy)^{-s}$; writing $a\pm iy$ in polar "
                          r"form turns $f(iy)-f(-iy)$ into a real sine, giving the convergent oscillatory "
                          r"integral that carries the continuation.",
                    math=[r"i\!\int_0^\infty\!\frac{(a+iy)^{-s}-(a-iy)^{-s}}{e^{2\pi y}-1}dy"
                          r"=2\!\int_0^\infty\!\frac{\sin\!\big(s\arctan\tfrac{y}{a}\big)}"
                          r"{(a^2+y^2)^{s/2}(e^{2\pi y}-1)}dy"],
                    references=["base method -> library/abel-plana-formula.md"],
                    decompose=[
                        dict(title="Polar form of a + iy", requires="plain",
                             prose=r"Write the complex number $a+iy$ by its length $r$ and angle $\theta$: "
                                   r"$r=\sqrt{a^2+y^2}$, $\theta=\arctan(y/a)$.",
                             math=[r"a+iy=r e^{i\theta},\quad r=\sqrt{a^2+y^2},\ \theta=\arctan\frac{y}{a}"],
                             references=["base method -> library/complex-polar-form.md"]),
                        dict(title="Raise to the power -s", requires="plain",
                             prose=r"Powers multiply the angle and power the length: "
                                   r"$(re^{i\theta})^{-s}=r^{-s}e^{-is\theta}$.",
                             math=[r"(a+iy)^{-s}=r^{-s}e^{-is\theta},\quad (a-iy)^{-s}=r^{-s}e^{+is\theta}"],
                             references=["base method -> library/complex-polar-form.md"]),
                        dict(title="Subtract: the difference is a sine", requires="plain",
                             prose=r"$e^{-is\theta}-e^{+is\theta}=-2i\sin(s\theta)$, so the $i$ out front makes "
                                   r"the whole thing real.",
                             math=[r"i\big[(a+iy)^{-s}-(a-iy)^{-s}\big]"
                                   r"=i\,r^{-s}(e^{-is\theta}-e^{is\theta})=2r^{-s}\sin(s\theta)"],
                             references=["base method -> library/euler-formula.md"]),
                        dict(title="Assemble the real integrand", requires="plain",
                             prose=r"Put $r=\sqrt{a^2+y^2}$ and $\theta=\arctan(y/a)$ back in and divide by "
                                   r"$e^{2\pi y}-1$ to read off the final convergent integral.",
                             math=[r"2\int_0^\infty\frac{\sin\!\big(s\arctan\tfrac{y}{a}\big)}"
                                   r"{(a^2+y^2)^{s/2}(e^{2\pi y}-1)}\,dy"]),
                    ]),
           ])

    # ----- VERIFY -----------------------------------------------------------
    d.verify(
        r"Recognition-only: NO engine execution and NO numeric oracle run is claimed here (rule 10 — we do "
        r"not hand-solve and feed the answer back as the engine's). The result is checkable against the "
        r"literature: it is the standard Hermite / Abel--Plana integral representation of the Hurwitz zeta "
        r"function, and at $a=1$ it reduces to the classical Riemann-$\zeta$ representation. A future "
        r"executable gate would differentiate / numerically integrate the right-hand side against "
        r"$\zeta(s,a)$ at sample $(s,a)$.",
        math=[r"a=1:\ \zeta(s)=\frac12+\frac{1}{s-1}"
              r"+2\int_0^\infty\frac{\sin(s\arctan t)}{(1+t^2)^{s/2}(e^{2\pi t}-1)}\,dt"],
        references=["method: library/abel-plana-formula.md (recognition-only; no executable transform yet)",
                    "target: Hermite integral representation of the Hurwitz zeta function",
                    "GATE STATUS: captured for the future, NOT executed (rule 11 recognition-only criterion)"])

    d.result(
        latex=(r"\zeta(s,a)=\frac{a^{-s}}{2}+\frac{a^{1-s}}{s-1}"
               r"+2\int_{0}^{\infty}\frac{\sin\!\big(s\arctan\tfrac{t}{a}\big)}"
               r"{(a^{2}+t^{2})^{s/2}\,(e^{2\pi t}-1)}\,dt"),
        note="Hurwitz-zeta integral representation via Abel-Plana; valid Re s > -1 (s != 1). "
             "Method is RECOGNITION-ONLY: the automated transform is an honest ceiling, not executed.")
    return d

def main():
    d = build_abel_plana_derivation()
    tracks = d.tracks()
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    qwarn = validate_qualification(tracks)
    print("level counts (emergent):", counts)
    print("validate_qualification:", qwarn if qwarn else "[]  (VALID — no warnings)")
    print("counts differ:", len(set(counts.values())) > 1,
          "| plain>=working>=expert:",
          counts["plain"] >= counts["working"] >= counts["expert"])
    assert not qwarn, qwarn
    assert len(set(counts.values())) > 1, counts
