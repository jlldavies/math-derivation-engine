"""Tensor vertical slice: prove ∇×(∇φ) = 0 — the engine beyond integrals.

Demonstrates the whole vision on a tensor identity (PLAN.md):
  * structured INPUT (Problem: expression + what it represents + goal);
  * pattern RECOGNITION, not numerics — rewrite in index form, spot
    "symmetric × antisymmetric contraction = 0";
  * symbolic VERIFY (SymPy: curl(grad φ) = 0, exact — no numerics);
  * EXPLAIN at altitudes (expert d²=0 / working index argument / plain "no swirl");
  * OUTPUT: HTML (copy-LaTeX + altitude toggle), markdown, JSON.

Run:  python examples/tensor_curl_grad.py
"""
import sys
import os
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer import MethodTrace, Step, Problem, Goal  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def verify_symbolically() -> bool:
    """Oracle as a CHECK: curl(grad φ) for a generic scalar field is the zero vector."""
    x, y, z = sp.symbols("x y z")
    phi = sp.Function("phi")(x, y, z)
    g = [sp.diff(phi, v) for v in (x, y, z)]
    curl = [sp.diff(g[2], y) - sp.diff(g[1], z),
            sp.diff(g[0], z) - sp.diff(g[2], x),
            sp.diff(g[1], x) - sp.diff(g[0], y)]
    return all(sp.simplify(c) == 0 for c in curl)


def build_trace() -> MethodTrace:
    problem = Problem(
        latex=r"\nabla\times(\nabla\phi)",
        represents="the curl (rotation) of a gradient field",
        goal=Goal.PROVE,
        integral="∇×(∇φ)  — curl of a gradient",
    )
    t = MethodTrace.from_problem(problem)

    t.add(Step(
        title="1. Rewrite in index notation",
        justification="vector notation hides the structure; index notation exposes the symmetry that settles it.",
        math=(r"\big(\nabla\times(\nabla\phi)\big)_i=\varepsilon_{ijk}\,\partial_j\partial_k\phi",),
    ))

    t.add(Step(
        title="2. Recognize the pattern: symmetric × antisymmetric = 0",
        method_key="sym_antisym",
        forced_by=r"$\partial_j\partial_k\phi$ is symmetric in $(j,k)$ (mixed partials commute — Clairaut), while "
                  r"$\varepsilon_{ijk}$ is antisymmetric in $(j,k)$. Contracting a symmetric tensor with an "
                  r"antisymmetric one over the same index pair gives identically zero.",
        payoff=r"One line, for every $\phi$, coordinate-free — no computation and no numbers.",
        relies_on=r"$\phi\in C^2$ (its mixed second partials commute).",
        math=(r"\varepsilon_{ijk}\,\partial_j\partial_k\phi=0\qquad\text{since }"
              r"S_{jk}=\partial_j\partial_k\phi=S_{kj}\ \text{and}\ \varepsilon_{ijk}=-\varepsilon_{ikj}",),
        altitudes={
            "expert": r"This is $d^2=0$: $\phi$ is a 0-form, $d\phi$ its gradient (an exact 1-form), and "
                      r"$d(d\phi)=0$ — exact $\Rightarrow$ closed. The curl identity is the 3-D shadow of the "
                      r"exterior derivative squaring to zero; every gradient field is irrotational (trivial "
                      r"de Rham class).",
            "working": r"Sum over $j,k$ of (antisymmetric in $j,k$) $\times$ (symmetric in $j,k$). Relabel the dummy "
                       r"indices $j\leftrightarrow k$: the symmetric factor is unchanged, the antisymmetric one flips "
                       r"sign, so the sum equals minus itself — therefore it is zero.",
            "plain": r"A gradient points straight downhill everywhere, and 'curl' measures swirl. Pure downhill has "
                     r"no swirl — water running down a smooth slope doesn't start spinning on its own. So the curl of "
                     r"a gradient is always zero.",
        },
        check="symbolic",
    ))

    ok = verify_symbolically()
    t.add(Step(
        title="3. Verify symbolically (the oracle as a check)",
        justification="SymPy takes the curl of the gradient of a generic scalar field, component by component.",
        math=(r"\nabla\times(\nabla\phi)=\big(\partial_y\partial_z\phi-\partial_z\partial_y\phi,\ \ldots\big)=\mathbf{0}",),
        detail=f"sympy: curl(grad φ) for a generic φ(x,y,z)  ->  (0, 0, 0).   all components zero: {ok}",
        check="symbolic" if ok else "unverified",
    ))

    t.result_latex = r"\nabla\times(\nabla\phi)=\mathbf{0}\qquad(\forall\,\phi\in C^2)"
    t.result = "the curl of any gradient vanishes — gradient fields are irrotational (d²=0)."
    return t


def main() -> None:
    t = build_trace()
    out = os.path.join(os.path.dirname(__file__), "tensor_output")
    os.makedirs(out, exist_ok=True)
    for name, content in (("trace.md", t.render_markdown()),
                          ("trace.json", t.render_json()),
                          ("trace.html", t.render_html())):
        with open(os.path.join(out, name), "w", encoding="utf-8") as f:
            f.write(content)
    print(t.render_markdown())
    print(f"\nwritten to: {out}")


if __name__ == "__main__":
    main()
