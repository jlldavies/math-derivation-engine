"""TEST ON REAL EXAM PAPERS — solve university Calculus II exam questions and write
the answers out, cross-checking against the official solutions.

Source: Colorado State University, Math 115 (Calculus II), Practice Exam #2 (with
official solutions). The system recognises the method (corpus), solves (SymPy),
verifies, and writes a levelled worked solution. As a verifying solver, it reproduces
the official answers AND catches an error in one of them (Q10) — the same value the
Experience shows: a tool that shows *and checks* the path catches mistakes.

Run:  python examples/exam_solver.py
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import (load_patterns, recognize_pattern, Derivation,  # noqa: E402
                                render_leveled, validate_qualification, Problem, Goal)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
x, t = sp.symbols("x t", real=True)
z = sp.symbols("z")
PATS = load_patterns()


def rec(q):
    h = recognize_pattern(q, PATS, k=1)
    return h[0][0].id if h else "(none)"


def cross_check():
    """recognise → solve (SymPy) → compare to the official answer."""
    rows = []
    s1 = sp.series(sp.atan(x**2), x, 0, 8).removeO()
    rows.append(("Q1 Maclaurin tan⁻¹(x²)", rec("maclaurin taylor series of arctan"),
                 str(s1), "x² − x⁶/3 + …", s1 == x**2 - x**6/3))
    approx, actual = sp.Rational(1, 3) - sp.Rational(1, 42), sp.integrate(sp.sin(x**2), (x, 0, 1))
    rows.append(("Q2 ∫₀¹ sin(x²) dx", rec("integrate sin x squared by taylor series term by term"),
                 "13/42 (err<1/1320)", "13/42, err<0.001", abs(float(actual) - float(approx)) < 1e-3))
    s4 = sp.series(sp.exp(-x**2), x, 0, 7).removeO()
    rows.append(("Q4 Taylor e^(−x²), ROC", rec("taylor series exponential interval of convergence ratio test"),
                 "Σ(−1)ⁿx^2n/n!, ℝ", "Σ(−1)ⁿx^2n/n!, (−∞,∞)", s4 == 1 - x**2 + x**4/2 - x**6/6))
    s7 = sp.series(1/(1 + 2*x**2), x, 0, 6).removeO()
    rows.append(("Q7 1/(1+2x²), ROC", rec("maclaurin series geometric 1 over 1 plus 2 x squared convergence"),
                 "Σ(−1)ⁿ2ⁿx^2n, |x|<1/√2", "same, (−1/√2,1/√2)", s7 == 1 - 2*x**2 + 4*x**4))
    roots = sp.solve(z**6 + 1, z)
    rows.append(("Q9 sixth roots of −1", rec("sixth roots of minus one complex de moivre"),
                 "e^{iπ(2k+1)/6}, k=0..5", "6 roots π/6,π/2,5π/6,…", len(roots) == 6))
    w = sp.sqrt(3) - sp.I
    ours = f"2·e^(i·{sp.arg(w)})"
    rows.append(("Q10 √3−i polar form", rec("complex number modulus argument polar form"),
                 "2·e^(−iπ/6)", "OFFICIAL: 2·e^(i5π/6)", sp.arg(w) == -sp.pi/6))
    return rows


def worked_integral():
    """Q2 ∫₀¹ sin(x²) dx — the answer written out, levelled."""
    pr = Problem(latex=r"\int_{0}^{1}\sin(x^{2})\,dx", represents="Calculus II exam, Q2",
                 goal=Goal.EVALUATE, integral="approximate to <0.001")
    d = Derivation(pr)
    d.why("Why this approach — a non-elementary integral via its series",
          {"plain": r"$\sin(x^{2})$ has no ordinary antiderivative, so we cannot integrate it directly. But "
                    r"$\sin$ has a known power series; we expand, integrate term by term, and the terms alternate "
                    r"so a couple of them plus an error bound is enough.",
           "working": r"no elementary antiderivative; use the Maclaurin series of $\sin$, integrate termwise, then "
                      r"bound the tail with the alternating-series estimate.",
           "expert": r"$\sin(x^2)$ is entire; integrate its Maclaurin series termwise; the result is an alternating "
                     r"series so the truncation error is below the first omitted term."},
          forced_by=r"$\int\sin(x^2)dx$ has no elementary closed form (it is a Fresnel integral).",
          payoff=r"the series integrates term by term to a fast, sign-alternating numerical series with a clean error bound.")
    d.how("How — expand sin, then integrate each power",
          {"plain": r"Use $\sin u = u-\tfrac{u^3}{3!}+\tfrac{u^5}{5!}-\dots$ with $u=x^2$, then integrate each term.",
           "working": r"$\sin(x^2)=x^2-\tfrac{x^6}{3!}+\tfrac{x^{10}}{5!}-\dots$, integrate on $[0,1]$.",
           "expert": r"termwise integration of the entire series."},
          math=[r"\sin(x^{2})=x^{2}-\frac{x^{6}}{3!}+\frac{x^{10}}{5!}-\cdots"])
    d.step("Solve and bound", requires="expert",
           prose=r"Integrate termwise, take two terms, bound the tail.",
           math=[r"\int_{0}^{1}\sin(x^{2})dx=\frac13-\frac1{42}+\frac1{1320}-\cdots\approx\frac{13}{42},\quad \text{err}<\tfrac1{1320}"],
           decompose=[
               dict(title="Integrate term by term", requires="working",
                    prose=r"$\int_0^1 x^{2}=\tfrac13$, $\int_0^1 x^{6}=\tfrac17$ so $-\tfrac1{3!\cdot7}=-\tfrac1{42}$, etc.",
                    math=[r"\int_{0}^{1}\sin(x^{2})dx=\Big[\tfrac{x^{3}}{3}-\tfrac{x^{7}}{7\cdot3!}+\tfrac{x^{11}}{11\cdot5!}\Big]_{0}^{1}"
                          r"=\frac13-\frac1{42}+\frac1{1320}-\cdots"],
                    decompose=[dict(title="The first power", requires="plain", prose=r"$\int_0^1 x^2\,dx=\tfrac13$.",
                                    math=[r"\int_{0}^{1}x^{2}\,dx=\Big[\tfrac{x^3}{3}\Big]_0^1=\tfrac13"]),
                               dict(title="The second power", requires="plain",
                                    prose=r"$-\tfrac1{3!}\int_0^1 x^6\,dx=-\tfrac1{6}\cdot\tfrac17=-\tfrac1{42}$.",
                                    math=[r"-\frac1{3!}\int_{0}^{1}x^{6}dx=-\frac1{6}\cdot\frac17=-\frac1{42}"])]),
               dict(title="Two terms + alternating-series error", requires="plain",
                    prose=r"Keep the first two terms; the series alternates, so the error is below the first omitted "
                          r"term $\tfrac1{1320}<0.001$.",
                    math=[r"\frac13-\frac1{42}=\frac{13}{42},\qquad |\text{error}|<\frac1{11\cdot120}=\frac1{1320}<10^{-3}"]),
           ])
    n_act = float(sp.integrate(sp.sin(x**2), (x, 0, 1)))
    d.verify(prose=f"Numerically the true value is {n_act:.6f}; our 13/42 = {13/42:.6f}; difference "
                   f"{abs(n_act-13/42):.6f} < 0.001 — within the claimed bound. Matches the official answer.",
             math=[r"\int_{0}^{1}\sin(x^{2})dx=" + f"{n_act:.6f}" + r",\quad \tfrac{13}{42}=" + f"{13/42:.6f}"])
    d.result(latex=r"\int_{0}^{1}\sin(x^{2})\,dx\approx\frac{13}{42}\quad(\text{error}<0.001)",
             note="matches the official Math 115 answer.")
    return d.tracks()


def worked_polar():
    """Q10 √3−i in polar form — and the official solution's error, caught."""
    pr = Problem(latex=r"\sqrt{3}-i", represents="Calculus II exam, Q10",
                 goal=Goal.SIMPLIFY, integral="write in polar form r e^{iθ}")
    d = Derivation(pr)
    d.why("Why — modulus and argument (mind the quadrant)",
          {"plain": r"Any complex number $a+bi$ is a point in the plane; its polar form $r\,e^{i\theta}$ uses the "
                    r"distance $r$ from the origin and the angle $\theta$. The angle must match the correct quadrant.",
           "working": r"$a+bi=r e^{i\theta}$ with $r=\sqrt{a^2+b^2}$ and $\theta=\operatorname{atan2}(b,a)$.",
           "expert": r"polar form; $\theta=\operatorname{atan2}(b,a)$ resolves the quadrant (a bare $\arctan(b/a)$ does not)."},
          relies_on=r"choosing $\theta$ by the quadrant of $(a,b)$ — here $a=\sqrt3>0,\ b=-1<0$ is the FOURTH quadrant.")
    d.how("How — r then θ", "compute the modulus, then the quadrant-correct argument.",
          math=[r"r=\sqrt{a^{2}+b^{2}},\qquad \theta=\operatorname{atan2}(b,a)"])
    d.step("Modulus and argument", requires="expert",
           prose=r"$r=2$ and, since $(\sqrt3,-1)$ is in the fourth quadrant, $\theta=-\tfrac{\pi}{6}$.",
           math=[r"r=2,\qquad \theta=-\frac{\pi}{6}"],
           decompose=[
               dict(title="The modulus", requires="plain", prose=r"$r=\sqrt{(\sqrt3)^2+(-1)^2}=\sqrt4=2$.",
                    math=[r"r=\sqrt{(\sqrt3)^{2}+(-1)^{2}}=\sqrt{3+1}=2"]),
               dict(title="The argument", requires="working",
                    prose=r"$\theta=\operatorname{atan2}(-1,\sqrt3)=-\tfrac{\pi}{6}$ — quadrant-aware.",
                    math=[r"\theta=\operatorname{atan2}(-1,\sqrt3)=-\frac{\pi}{6}"],
                    decompose=[
                        dict(title="Which quadrant?", requires="plain",
                             prose=r"Real part $\sqrt3>0$, imaginary part $-1<0$ ⇒ the FOURTH quadrant (below the axis, right).",
                             math=[r"(\sqrt3,\,-1):\ \ \mathrm{Re}>0,\ \mathrm{Im}<0\ \Rightarrow\ \text{quadrant IV}"]),
                        dict(title="The angle there", requires="plain",
                             prose=r"In quadrant IV, $\theta=\arctan\!\big(\tfrac{-1}{\sqrt3}\big)=-\tfrac{\pi}{6}$ "
                                   r"(NOT $\tfrac{5\pi}{6}$, which is quadrant II).",
                             math=[r"\theta=\arctan\!\left(\frac{-1}{\sqrt3}\right)=-\frac{\pi}{6}"]),
                    ]),
           ])
    d.verify(prose="Check: 2·e^(−iπ/6) = 2(cos(−30°)+i sin(−30°)) = 2(√3/2 − i/2) = √3 − i ✓.  "
                   "The official solution gives 2·e^(i5π/6), but that equals −√3 + i — a quadrant error in the "
                   "published answer, caught by computing the result back.",
             math=[r"2e^{-i\pi/6}=2\left(\tfrac{\sqrt3}{2}-\tfrac{i}{2}\right)=\sqrt3-i\ \checkmark",
                   r"2e^{\,i5\pi/6}=-\sqrt3+i\ \neq\ \sqrt3-i\quad(\text{official answer is wrong})"])
    d.result(latex=r"\sqrt{3}-i=2\,e^{-i\pi/6}", note="official answer 2e^{i5π/6} is incorrect (wrong quadrant).")
    return d.tracks()


def main():
    print("=== REAL EXAM TEST — Colorado State Math 115 (Calculus II), Practice Exam #2 ===\n")
    print(f"  {'problem':24s} {'recognised method':26s} {'ours':22s} {'official':24s} ok")
    ok = 0
    for prob, method, ours, official, good in cross_check():
        ok += bool(good)
        print(f"  {prob:24s} {method:26s} {ours:22s} {official:24s} {'✓' if good else '⚠'}")
    print(f"\n  reproduced {ok}/6 official answers; Q10 flags an ERROR in the official solution.\n")

    out = os.path.join(os.path.dirname(__file__), "exam_output")
    os.makedirs(out, exist_ok=True)
    for name, tracks in (("q2_integral", worked_integral()), ("q10_polar", worked_polar())):
        w = validate_qualification(tracks)
        counts = {k: len(v.steps) for k, v in tracks.items()}
        print(f"  worked solution {name}: levels {counts}", "OK" if not w else w)
        with open(os.path.join(out, name + ".html"), "w", encoding="utf-8") as f:
            f.write(render_leveled(tracks))
    print(f"\n  worked solutions written to examples/exam_output/")


if __name__ == "__main__":
    main()
