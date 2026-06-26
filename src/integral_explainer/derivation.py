"""Derivation: the reusable recorder that turns a SOLVED problem into the levelled
explanation contract (CLAUDE.md rule 7).

A solver (integral, tensor, …) records its steps — why this approach / how it works /
each step with its term-by-term working — and `Derivation.tracks()` builds the
{expert, working, plain} MethodTraces for `render_leveled()`. This is the engine
*lifting* the explanation: the solver supplies the domain maths (per-level prose,
math, working); Derivation supplies the contract structure, the why/how/step bands,
and the reader-levelling. It promotes the bespoke pattern in
`examples/bondi_christoffel.py` into a reusable capability so a NEW recognised
problem can get the same depth without a hand-written script.

Per-level content: `prose`, `math` and `work` may each be a plain value (shared by
all levels) OR a dict `{level: value}` (e.g. extra per-summand `work` only at the
high-school level). Nothing is taken on faith — every step carries its working.
"""
from __future__ import annotations

from .trace import MethodTrace, Step

_LEVELS = ("expert", "working", "plain")


def _pick(val, level):
    """A per-level value: dict -> that level (fallback working/first); else as-is."""
    if isinstance(val, dict):
        return val.get(level) if level in val else (val.get("working") or next(iter(val.values()), None))
    return val


def _seq(val, level):
    v = _pick(val, level)
    return tuple(v) if v else ()


class Derivation:
    """Fluent recorder. Example:
        d = Derivation(problem)
        d.why("Why this approach", {"plain": "...", "working": "...", "expert": "..."},
              forced_by="...", payoff="...", relies_on="...")
        d.how("How it works", "...", math=[r"..."])
        d.step("1. ...", "...", math=[r"..."], work=[r"...", r"..."])
        d.verify("checked symbolically + numerically", math=[r"..."], references=[...])
        d.result(latex=r"...", note="...")
        render_leveled(d.tracks())
    """

    def __init__(self, problem):
        self.problem = problem
        self._entries = []
        self._result = (None, None)

    def _add(self, section, title, prose="", *, requires="plain", decompose=(),
             math=(), work=(), detail="", references=(), forced_by="", payoff="",
             relies_on="", check="symbolic", levels=None):
        # `requires`: the qualification (plain<working<expert) a reader needs to grasp
        # this step as ONE unit. If the reader is below it, the step is REPLACED by its
        # `decompose` (a list of sub-step dicts, each a tree node) — so the per-level
        # step count EMERGES from the tree, never set by hand. `levels=` is the legacy
        # explicit-set escape hatch (still honoured if given).
        self._entries.append(_node(section, title, prose, requires, decompose, math,
                                   work, detail, references, forced_by, payoff,
                                   relies_on, check, levels))
        return self

    def why(self, title, prose="", **kw):
        return self._add("why", title, prose, **kw)

    def how(self, title, prose="", **kw):
        return self._add("how", title, prose, **kw)

    def step(self, title, prose="", **kw):
        return self._add("step", title, prose, **kw)

    def verify(self, prose="", **kw):
        return self._add("step", "Verify", prose, **kw)

    def result(self, latex=None, note=None):
        self._result = (latex, note)
        return self

    def tracks(self) -> dict:
        """{level: MethodTrace}, contract-banded, ready for render_leveled(). Each level
        is the FRONTIER of the qualification tree at that reader (cut by `requires`)."""
        def build(level):
            t = MethodTrace.from_problem(self.problem)
            for e in self._entries:
                _emit(e, level, e["section"], t.add)
            lx, note = self._result
            if lx:
                t.result_latex = lx
            if note:
                t.result = note
            return t
        return {lvl: build(lvl) for lvl in _LEVELS}


_QUAL = {"plain": 1, "working": 2, "expert": 3}


def _node(section, title, prose, requires, decompose, math, work, detail,
          references, forced_by, payoff, relies_on, check, levels):
    return dict(section=section, title=title, prose=prose, requires=requires,
                decompose=tuple(decompose), math=math, work=work, detail=detail,
                references=tuple(references), forced_by=forced_by, payoff=payoff,
                relies_on=relies_on, check=check, levels=levels)


def _sub(d):
    """Normalise a decompose child dict into a full node (defaults: plain, no kids)."""
    return _node(d.get("section"), d.get("title", ""), d.get("prose", ""),
                 d.get("requires", "plain"), d.get("decompose", ()), d.get("math", ()),
                 d.get("work", ()), d.get("detail", ""), d.get("references", ()),
                 d.get("forced_by", ""), d.get("payoff", ""), d.get("relies_on", ""),
                 d.get("check", "symbolic"), d.get("levels"))


def _emit(e, level, section, add):
    """Frontier cut: show e as a unit if the reader can grasp it (requires<=level), else
    REPLACE it with its decomposition; a step too hard with no decomposition is a ceiling
    (emitted as-is so `validate_qualification` flags it)."""
    if e.get("levels") is not None and level not in e["levels"]:   # legacy escape hatch
        return
    graspable = _QUAL.get(e["requires"], 1) <= _QUAL[level]
    if graspable or not e["decompose"]:
        add(Step(section=section, title=e["title"], requires=e["requires"],
                 justification=_pick(e["prose"], level) or "",
                 math=_seq(e["math"], level), work=_seq(e["work"], level),
                 detail=e["detail"], references=e["references"], forced_by=e["forced_by"],
                 payoff=e["payoff"], relies_on=e["relies_on"], check=e["check"]))
    else:
        for child in e["decompose"]:
            _emit(_sub(child), level, section, add)   # decompose inherits the band
