"""Coverage harness — proves every method is accounted for AND every executable is really wired,
so expansion can't silently leave a method un-wired, un-reachable, or un-fired.

`gaps()` checks six invariants (all must be empty):
  1. key-completeness   : every methods.METHODS key has exactly one COVERAGE row (none extra).
  2. row consistency    : executable <-> has a Strategy; recognition-only <-> None; valid status.
  3. WIRING PROOF       : every executable row's Strategy is `in` its kind's live solver list
                          (KIND_SOLVERS[kind]). Catches the 'dead row' — marked executable but
                          run by no solver (the sym_antisym bug the completeness critic found).
  4. kind dispatch      : every kind used has BOTH a GOAL and a KIND_SOLVERS entry.
  5. no orphan edges     : every live solver strategy is a declared COVERAGE or GENERIC strategy
                          (the audited registry == the strategy set actually driving solves).
  6. FIRE check          : every live solver strategy has a REP and fires on it. Registry-driven —
                          add a strategy without a representative and assert_complete fails.

Direct executable CAPABILITIES that are not search strategies (the curvature pipeline, executor)
are declared in strategies.DIRECT_CAPABILITIES so they are honestly accounted for, not omitted.
"""
from __future__ import annotations

from .methods import METHODS
from . import strategies as S
from .external_gates import gated_methods, CAPTURED_GATES
from .explanations import EXPLANATIONS
from .trace import validate_qualification


def _live():
    """All (kind, strategy) the solvers actually run."""
    return [(kind, st) for kind, solver in S.KIND_SOLVERS.items() for st in solver()]


def gaps():
    undeclared = [k for k in METHODS if k not in S.COVERAGE]
    extra = [k for k in S.COVERAGE if k not in METHODS]
    inconsistent, dead_rows, kind_no_solver = [], [], []
    for k, (kind, status, strat) in S.COVERAGE.items():
        if status == "executable":
            if kind == S.CAPABILITY:                                   # direct-compute method
                if k not in S.CAPABILITIES:
                    dead_rows.append((k, kind, "capability-executable but no capability registered"))
                if strat is not None:
                    inconsistent.append((k, "capability row must have strategy=None"))
            elif strat is None:
                inconsistent.append((k, "executable but no Strategy"))
            elif kind in S.KIND_SOLVERS and strat not in S.KIND_SOLVERS[kind]():
                dead_rows.append((k, kind, "executable but in no live solver"))   # wiring proof
        elif status == "recognition-only":
            if strat is not None:
                inconsistent.append((k, "recognition-only but has a Strategy"))
        else:
            inconsistent.append((k, f"unknown status {status!r}"))
        # SEARCH kinds need a GOAL + solver list; CAPABILITY is a direct call (exempt)
        if kind != S.CAPABILITY and (kind not in S.KIND_SOLVERS or kind not in S.GOAL):
            kind_no_solver.append((k, kind))

    declared = {st for (_, _, st) in S.COVERAGE.values() if st} | set(S.GENERIC_STRATEGIES)
    orphan_live = [(kind, st.name) for kind, st in _live() if st not in declared]

    fire_failures = []
    for _, st in _live():
        rep = S.REPS.get(st.name)
        if rep is None:
            fire_failures.append((st.name, "no representative input"))
            continue
        try:
            if not list(st.expand(rep)):
                fire_failures.append((st.name, "produced no successor"))
        except Exception as e:                                                   # noqa: BLE001
            fire_failures.append((st.name, f"raised {type(e).__name__}: {e}"))

    # rule 10: every executable method must have an INDEPENDENT external gate
    ungated_executable = [k for k, (kind, status, strat) in S.COVERAGE.items()
                          if status == "executable" and k not in gated_methods()]

    # rule 11: every method must have a VALID leveled explanation (validate_qualification + counts differ)
    unexplained = [k for k in S.COVERAGE if k not in EXPLANATIONS]
    invalid_explanation = []
    for k in S.COVERAGE:
        if k not in EXPLANATIONS:
            continue
        try:
            tracks = EXPLANATIONS[k]().tracks()
            if validate_qualification(tracks):
                invalid_explanation.append((k, "validate_qualification warnings"))
            elif len({len(tr.steps) for tr in tracks.values()}) <= 1:
                invalid_explanation.append((k, "per-level step counts do not differ"))
        except Exception as e:                                                  # noqa: BLE001
            invalid_explanation.append((k, f"build error: {type(e).__name__}: {e}"))

    return {"undeclared": undeclared, "extra": extra, "inconsistent": inconsistent,
            "dead_rows": dead_rows, "kind_no_solver": kind_no_solver,
            "orphan_live": orphan_live, "fire_failures": fire_failures,
            "ungated_executable": ungated_executable,
            "unexplained": unexplained, "invalid_explanation": invalid_explanation}


def matrix():
    def wired(kind, status, strat):
        if strat is not None:
            return "search"
        if status == "executable" and kind == S.CAPABILITY:
            return "capability"
        return "no"
    return [(k, kind, status, wired(kind, status, strat))
            for k, (kind, status, strat) in sorted(S.COVERAGE.items())]


def summary():
    n = len(S.COVERAGE)
    ex = sum(1 for _, (_, st, _) in S.COVERAGE.items() if st == "executable")
    return {"methods": n, "executable_methods": ex, "recognition_only": n - ex,
            "live_strategies": len(_live()), "direct_capabilities": len(S.DIRECT_CAPABILITIES)}


def assert_complete():
    g = gaps()
    bad = {k: v for k, v in g.items() if v}
    assert not bad, f"coverage gaps: {bad}"
    return True


def method_status(g=None):
    """Per-method Definition-of-Done (rule 11): declared / explained / wired / gated -> complete."""
    g = g or gaps()
    dead = {k for k, *_ in g["dead_rows"]}
    bad_expl = {k for k, _ in g["invalid_explanation"]} | set(g["unexplained"])
    captured = {x["method"] for x in CAPTURED_GATES}
    rows = {}
    for k, (kind, status, strat) in S.COVERAGE.items():
        explained = k not in bad_expl
        if status == "executable":
            wired = k not in dead
            gated = k not in g["ungated_executable"]
        else:
            wired = None                                   # n/a for recognition-only
            gated = k in captured                          # captured future gate
        complete = explained and (wired is not False) and gated
        rows[k] = dict(status=status, explained=explained, wired=wired, gated=gated, complete=complete)
    return rows


def report() -> str:
    g, s = gaps(), summary()
    ms = method_status(g)
    n_complete = sum(1 for r in ms.values() if r["complete"])
    lines = [f"COVERAGE: {s['methods']} methods  |  executable {s['executable_methods']}  "
             f"recognition-only {s['recognition_only']}  |  live strategies {s['live_strategies']}",
             f"complete (all invariants hold): {not any(g.values())}   |   "
             f"methods COMPLETE (rule 11: declared+explained+wired+gated): {n_complete}/{s['methods']}",
             "", f"{'method':22} {'kind':10} {'status':16} {'wired':10} {'explained':10} {'gated':7} complete"]
    mat = {k: (kind, status, w) for k, kind, status, w in matrix()}
    for k in sorted(S.COVERAGE):
        kind, status, w = mat[k]
        r = ms[k]
        lines.append(f"{k:22} {kind:10} {status:16} {w:10} "
                     f"{'yes' if r['explained'] else 'NO':10} "
                     f"{('yes' if r['gated'] else 'NO'):7} {'YES' if r['complete'] else 'NO'}")
    if any(g.values()):
        lines += ["", "GAPS:"] + [f"  {kk}: {vv}" for kk, vv in g.items() if vv]
    return "\n".join(lines)
