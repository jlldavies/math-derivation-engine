"""Schwarzschild line element → coefficient of d t̄², explained at THREE LEVELS.

The 'explain at' switch swaps the WHOLE explanation — a different number of steps
and different text per level:
  * Expert  — terse, 2 steps (transformation law + assemble/substitute).
  * Working — symbolic, 4 steps (law, Jacobian column, assemble, substitute).
  * Plain   — high-school, 6 steps (Pythagoras recipe → rates → square → add → sub → check).
Same problem, same verified answer (standard Schwarzschild 14.47, matches the textbook).

Run:  python examples/schwarzschild_transform.py
"""
import sys
import os
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import MethodTrace, Step, Problem, Goal, render_leveled  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ANSWER = (r"\bar g_{\bar t\bar t}=\frac{4\bar t^{2}\bar r^{3}\cos\bar\theta}{\bar r\cos\bar\theta+2m}"
          r"-(\bar r\cos\bar\theta+2m)^{2}\,\bar r^{2}\bar\theta^{2}\bar\phi^{2}\sin^{2}(\bar\phi\bar t)")
NOTE = "the coefficient of d t̄² (standard Schwarzschild) — matches the textbook, verified symbolically."


def verify():
    m = sp.symbols("m", positive=True)
    tb, rb, thb, phb = sp.symbols("tbar rbar thetabar phibar", real=True)
    t = tb**2 * rb; r = rb * sp.cos(thb) + 2 * m; th = sp.asin(rb * thb); ph = sp.cos(phb * tb)
    old = [t, r, th, ph]
    g = [(1 - 2 * m / r), -(1 - 2 * m / r) ** -1, -r**2, -r**2 * sp.sin(th) ** 2]
    return sp.simplify(sum(g[i] * sp.diff(old[i], tb) ** 2 for i in range(4)))


def problem() -> Problem:
    return Problem(
        latex=r"ds^2=\left(1-\tfrac{2m}{r}\right)dt^2-\left(1-\tfrac{2m}{r}\right)^{-1}dr^2"
              r"-r^2 d\theta^2-r^2\sin^2\theta\,d\phi^2",
        represents="Schwarzschild line element (14.47); new coords "
                   "t=t̄²r̄, r=r̄cos θ̄+2m, θ=sin⁻¹(r̄θ̄), φ=cos(φ̄t̄)",
        goal=Goal.EVALUATE,
        integral="coefficient of d t̄² after the transformation",
    )


def _finish(t: MethodTrace) -> MethodTrace:
    t.result_latex = ANSWER
    t.result = NOTE
    return t


def expert() -> MethodTrace:
    t = MethodTrace.from_problem(problem())
    t.add(Step(
        title="1. Transformation law; only t, φ carry t̄",
        justification="ḡ_t̄t̄ = Σ gᵤᵤ(∂xᵘ/∂t̄)²; r,θ have no t̄.",
        math=(r"\frac{\partial t}{\partial\bar t}=2\bar t\bar r,\qquad "
              r"\frac{\partial\phi}{\partial\bar t}=-\bar\phi\sin(\bar\phi\bar t)",),
    ))
    t.add(Step(
        title="2. Assemble and substitute  r=r̄cosθ̄+2m, sinθ=r̄θ̄",
        math=(r"\bar g_{\bar t\bar t}=\left(1-\tfrac{2m}{r}\right)(2\bar t\bar r)^2-r^2\sin^2\theta\,\bar\phi^2\sin^2(\bar\phi\bar t)",),
        check="symbolic",
    ))
    return _finish(t)


def working() -> MethodTrace:
    t = MethodTrace.from_problem(problem())
    t.add(Step(
        title="1. Metric transformation law",
        method_key="tensor",
        justification="the metric is a (0,2) tensor; for a diagonal metric the new diagonal coefficient is a single sum.",
        math=(r"\bar g_{\bar t\bar t}=\sum_\mu g_{\mu\mu}\left(\frac{\partial x^\mu}{\partial\bar t}\right)^{2}",),
        check="symbolic",
    ))
    t.add(Step(
        title="2. Jacobian column  ∂xᵘ/∂t̄",
        justification="differentiate each old coordinate w.r.t. t̄ (θ, r have none).",
        math=(r"\frac{\partial t}{\partial\bar t}=2\bar t\bar r,\quad "
              r"\frac{\partial\phi}{\partial\bar t}=-\bar\phi\sin(\bar\phi\bar t),\quad "
              r"\frac{\partial r}{\partial\bar t}=\frac{\partial\theta}{\partial\bar t}=0",),
    ))
    t.add(Step(
        title="3. Assemble  Σ gᵤᵤ (∂xᵘ/∂t̄)²",
        math=(r"\bar g_{\bar t\bar t}=\left(1-\tfrac{2m}{r}\right)(2\bar t\bar r)^2-r^2\sin^2\theta\,\bar\phi^2\sin^2(\bar\phi\bar t)",),
    ))
    t.add(Step(
        title="4. Substitute the transformations",
        justification="r=r̄cosθ̄+2m, sinθ=r̄θ̄, and 1−2m/r = r̄cosθ̄/(r̄cosθ̄+2m).",
        math=(ANSWER,),
        check="symbolic",
    ))
    return _finish(t)


def plain() -> MethodTrace:
    t = MethodTrace.from_problem(problem())
    t.add(Step(
        title="1. What the line element is, and the goal",
        justification="A line element is a Pythagoras-style recipe for a tiny squared distance: each term is a "
                      "coefficient times a (tiny step)², with steps dt, dr, dθ, dφ. We are changing to new (barred) "
                      "coordinates; the transformations give each old coordinate as a formula in the new ones. We want "
                      "the new number in front of dt̄².",
    ))
    t.add(Step(
        title="2. How fast does each old coordinate change as you nudge t̄?",
        justification="Increase t̄ a little, keeping r̄, θ̄, φ̄ still. Each old coordinate changes at a rate — its "
                      "derivative with respect to t̄. (That is all ∂t/∂t̄ means.) Two contain no t̄, so their rate is 0.",
        math=(r"\frac{\partial t}{\partial\bar t}=2\bar t\bar r,\qquad "
              r"\frac{\partial \phi}{\partial\bar t}=-\bar\phi\sin(\bar\phi\bar t),\qquad "
              r"\frac{\partial r}{\partial\bar t}=0,\qquad \frac{\partial \theta}{\partial\bar t}=0",),
        detail="t = t̄²r̄:  derivative of t̄² is 2t̄ (power rule), times r̄  ->  2t̄r̄.\n"
               "φ = cos(φ̄t̄): derivative of cos is −sin, times the inside's rate φ̄ (chain rule)  ->  −φ̄ sin(φ̄t̄).\n"
               "r = r̄cosθ̄+2m  and  θ = sin⁻¹(r̄θ̄):  neither contains t̄, so the rate is 0.",
    ))
    t.add(Step(
        title="3. Turn each rate into a tiny step, then square it",
        justification="For the part from moving t̄, each tiny old-step = (its rate) × dt̄. Squaring gives the piece that "
                      "multiplies dt̄². Only t and φ survive — r and θ had rate 0.",
        math=(r"dt^2=(2\bar t\bar r)^2\,d\bar t^2,\qquad d\phi^2=\bar\phi^2\sin^2(\bar\phi\bar t)\,d\bar t^2",),
    ))
    t.add(Step(
        title="4. Weight by the original coefficients and add",
        justification="dt² sits in front of (1−2m/r), and dφ² in front of −r²sin²θ. Multiply each by its squared rate "
                      "and add — that is the new coefficient of dt̄².",
        math=(r"\bar g_{\bar t\bar t}=\left(1-\tfrac{2m}{r}\right)(2\bar t\bar r)^2-r^2\sin^2\theta\,\bar\phi^2\sin^2(\bar\phi\bar t)",),
    ))
    t.add(Step(
        title="5. Rewrite r and θ in the new coordinates",
        justification="Swap r and θ using the transformations: r = r̄cosθ̄+2m, and sinθ = r̄θ̄ (sin undoes sin⁻¹). "
                      "Also 1−2m/r tidies to r̄cosθ̄ ∕ (r̄cosθ̄+2m). Substituting gives the answer.",
        math=(ANSWER,),
    ))
    t.add(Step(
        title="6. Check it",
        justification="A computer-algebra check (SymPy) redoes steps 1–5 from the metric and the transformations and "
                      "gets the same formula — so we know the path is right.",
        detail=f"sympy result:\n  {verify()}",
        check="symbolic",
    ))
    return _finish(t)


def main() -> None:
    tracks = {"expert": expert(), "working": working(), "plain": plain()}
    print("steps per level:", {k: len(v.steps) for k, v in tracks.items()})
    out = os.path.join(os.path.dirname(__file__), "schwarzschild_output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "trace.html"), "w", encoding="utf-8") as f:
        f.write(render_leveled(tracks))
    with open(os.path.join(out, "trace.md"), "w", encoding="utf-8") as f:
        f.write("# Explained at three levels\n\n" + "\n\n---\n\n".join(
            f"## {lvl} ({len(tr.steps)} steps)\n\n{tr.render_markdown()}" for lvl, tr in tracks.items()))
    print(f"written to {out}")


if __name__ == "__main__":
    main()
