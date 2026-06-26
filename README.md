# math-derivation-engine

A tool for **solving hard maths by recognizing structure — then explaining the solution step by step.**

Most computer-algebra systems give you *an answer*. This engine is built to give you *a derivation you
can follow and trust*: it recognizes which method applies, executes it **symbolically** (so the result
keeps its analytic structure — symmetries, singularities, asymptotics, geometry), **verifies** it, and
**explains** it as a leveled, step-by-step argument — from a graduate sketch down to high-school algebra.

It started life as an integral solver (the hardest case to crack first), but it now spans **many domains
of mathematics** — and every method is held to the same bar.

```python
>>> from integral_explainer.special_methods import conformal_casimir, wigner_surmise
>>> conformal_casimir(3)                 # quadratic Casimir of SO(4,1) on a scalar primary
Delta**2 - 3*Delta                       #  = Delta(Delta - 3)
>>> wigner_surmise(1)                     # GOE level-spacing law, constants derived by moment-matching
pi*s*exp(-pi*s**2/4)/2
```

## What it covers

**32 methods across ten domains**, each one a genuine computation (nothing hard-coded):

| Domain | Examples |
|---|---|
| Integrals | by-parts, partial fractions, Meijer-G, complete-the-square, hyperbolic/inverse rewrites |
| Special functions | dilogarithm, ₀F₁→Bessel, Gamma-ratio asymptotics, Bessel/Hankel transforms, Airy (WKB) |
| Asymptotics | erfc by repeated IBP, Stirling, Euler–Maclaurin (harmonic-number expansion) |
| q-series | q-Pochhammer product → Lambert series |
| Random matrices | Wigner surmise & level-spacing laws by moment-matching |
| Representation theory | su(2) Casimir `J²=j(j+1)`, conformal Casimir `Δ(Δ−d)`, SL(2) conformal block |
| Symmetric functions | Schur polynomials via the Jacobi–Trudi determinant |
| PDE | Sturm–Liouville boundary eigenproblems |
| Operator algebra | canonical oscillator commutators, Jordan–Schwinger / su(1,1) realizations |
| General relativity | curvature (Christoffel/Riemann/Ricci/Einstein), Komar mass, tensor identities |

These were built and stress-tested by **deriving results from real, recent physics papers** and checking
the engine reproduces them — surfacing (and closing) genuine gaps along the way.

## The quality bar (the "Definition of Done")

A method is only "done" when **all** of these hold — enforced by the test suite, not by good intentions:

1. **Genuinely computes** — the result is *derived* by the CAS, never written in.
2. **Externally gated** — it reproduces an **independent published value** (DLMF, a textbook, a paper),
   cited by URL. We check *someone else's* homework, not our own.
3. **Explained** — it carries a leveled `Derivation` (why this approach / how it works / the steps) that
   re-pitches at three reader levels, validated so each step is followable at its level.
4. **Grounded** — it links to an established **published step-by-step guide** for the same derivation
   (see [`METHOD_STEP_SOURCES.md`](METHOD_STEP_SOURCES.md)).

## Quickstart

```bash
python -m venv .venv && . .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e .
python examples/solve_integral.py                 # recognize -> derive -> verify -> explain, end to end
pytest -m "not slow"                              # fast test subset; `pytest` runs everything
```

## How it works

`recognize → execute (symbolically) → verify (numerically) → explain`

- **recognize / search** — solving is a best-first *search* over `(state, method)`; it decomposes
  sub-problems, backtracks dead ends, and uses complexity as the cost heuristic (`src/.../search.py`,
  `strategies.py`).
- **execute** — the transformation runs in SymPy; the engine supplies the recognition and orchestration.
- **verify** — symbolic where possible, plus a high-precision numeric oracle (mpmath) for the hard cases.
- **explain** — a `Derivation` renders to an interactive HTML trace **and** exportable LaTeX, with the
  working shown above each result (`src/.../derivation.py`, `trace.py`).

## Layout

- `src/integral_explainer/` — the engine (methods, search/strategies, curvature, special_methods,
  explanations, the coverage harness that proves every method meets the bar).
- `tests/` — the gates and the full-suite runner; `coverage.assert_complete()` enforces the Definition of Done.
- `examples/` — runnable demos (`solve_integral.py`, `bondi_christoffel.py`, `schwarzschild_transform.py`, …).
- `library/` — a small wiki of method/reference pages the explanations link into.

*(The Python package is named `integral_explainer` for historical reasons — the engine is now broad-domain.)*

## Contributing

Contributions welcome — adding a method, a domain, or a paper-derivation. The one rule: **meet the bar
above** (genuine computation + external gate + complete leveled explanation + a step-by-step source).
See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

[MIT](LICENSE). Open source — use it, fork it, build on it.
