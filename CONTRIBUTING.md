# Contributing

Thanks for wanting to add to this. The engine is deliberately strict about quality: a method that
isn't genuinely derived, independently checked, and clearly explained doesn't help anyone. That bar is
what makes the output trustworthy.

## The bar every method must meet ("Definition of Done")

A method (a named technique in `src/integral_explainer/methods.py`) is complete only when **all** hold,
and the coverage harness (`coverage.assert_complete()`) enforces it:

1. **Declared** — a `Method(...)` entry in `methods.py`, a row in `strategies.COVERAGE`, and (for an
   executable capability) an entry in `strategies.CAPABILITIES`.
2. **Genuinely computes** — the function in `special_methods.py` *derives* the result with SymPy.
   **Never write the published answer in** and hand it back — the engine does the maths, we only verify.
3. **Externally gated** — it reproduces an **independent published value** via
   `external_gates.CAPABILITY_GATES`, citing a real source URL (DLMF, a textbook, a paper). We check
   someone else's homework, not our own.
4. **Explained** — a leveled `Derivation` in `explanations/<key>.py` (why this approach / how it works /
   the steps), registered in `explanations/__init__.py`. It must pass `trace.validate_qualification`
   (every shown step is followable at its reader level) and the per-level step counts must differ
   (the explanation genuinely re-pitches across levels — it isn't the same text three times).
5. **Grounded** — a `methods.STEP_GUIDES[key]` entry linking an established **published step-by-step
   derivation guide** (grade FULL / partial / THIN + URL). See `METHOD_STEP_SOURCES.md`.

Copy an existing method as a template — e.g. `conformal_casimir`, `dilogarithm`, or `sturm_liouville`
have the full set (function, gate, explanation, step-guide).

## Workflow

```bash
pip install -e .
# add your method (the 5 pieces above), then:
python -c "import sys; sys.path.insert(0,'src'); from integral_explainer import coverage as C; print(C.gaps())"   # must be all-empty
pytest -m "not slow"          # fast subset while iterating
pytest                        # the whole suite — run before opening a PR
```

`pytest` runs **everything** by default (coverage is the default); `-m "not slow"` is the explicit
fast subset for iteration. Don't reduce coverage to gain speed — run the full suite before a PR.

## Principles

- **Symbolic first.** A closed form holds structure (symmetries, singularities, asymptotics, geometry)
  that a number destroys. Numerics are a *check* on a recognized pattern, never the way you find it.
- **Verify, don't trust.** If your result disagrees with a published source, re-derive from scratch
  before concluding the source is wrong — most disagreements are our own non-simplification or a
  transcription slip.
- **Explain for a reader who'll check you.** Every step should be independently verifiable by its target
  reader; no black-box jumps.

Bug reports, new domains, and paper-derivations are all welcome. Open an issue to discuss anything large.
