"""Library: the pattern wiki as a live recognizer (GO4 K12 pages + K1 retrieval).

Loads the markdown pattern pages in `library/` into `Pattern` objects and matches
a problem against their recognition signatures. This is the retrieval substrate the
LLM proposer (M1) will use; for now a deterministic keyword/signature matcher, so
recognition is testable (the wiki is also the golden test corpus). The cross-link
graph in the pages is kept for the K3 (GraphRAG) growth path.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import io
import os
import re
import glob

# package is src/integral_explainer/ ; the wiki is repo-root/library
_LIB_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "library"))


@dataclass
class Pattern:
    id: str
    name: str = ""
    domain: str = ""
    regime: str = ""
    status: str = ""
    applies_when: str = ""
    rule: str = ""
    worked_example: str = ""
    references: str = ""
    links: tuple = ()
    sections: dict = field(default_factory=dict)

    def signature(self) -> str:
        return f"{self.name}  {self.applies_when}  {self.rule}"

    def altitudes(self) -> dict:
        """Parse the '## Explain (altitudes)' bullets into {level: text}."""
        sec = ""
        for k, v in self.sections.items():
            if "explain" in k.lower() or "altitude" in k.lower():
                sec = v
                break
        out = {}
        for m in re.finditer(r"-\s*\*\*([\w-]+)\*\*\s*[—-]\s*(.+?)(?=\n-\s*\*\*|\Z)", sec, re.S):
            out[m.group(1).lower()] = " ".join(m.group(2).split())
        return out

    def references_list(self) -> tuple:
        return tuple(line.lstrip("-* ").strip()
                     for line in self.references.splitlines() if line.strip().startswith("-"))

    def latex_parts(self) -> dict:
        """Parse the '## LaTeX' section (`key: <latex>` lines) for typesetting.
        Keys: `rule`, `example` (and any others). Lets an assembled trace render
        proper math instead of the prose pages' backtick+unicode."""
        sec = ""
        for k, v in self.sections.items():
            if k.strip().lower() == "latex":
                sec = v
                break
        out = {}
        for line in sec.splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                if val.strip():
                    out[key.strip().lower()] = val.strip()
        return out


def _parse_page(path: str) -> Pattern:
    txt = io.open(path, encoding="utf-8").read()
    fm, body = {}, txt
    if txt.startswith("---"):
        _, front, body = txt.split("---", 2)
        for line in front.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    secs, cur = {}, None
    for line in body.splitlines():
        m = re.match(r"##\s+(.*)", line)
        if m:
            cur = m.group(1).strip()
            secs[cur] = []
        elif cur is not None:
            secs[cur].append(line)
    secs = {k: "\n".join(v).strip() for k, v in secs.items()}

    def sec(name: str) -> str:
        for k, v in secs.items():
            if name.lower() in k.lower():
                return v
        return ""

    return Pattern(
        id=fm.get("id", os.path.basename(path)[:-3]),
        name=fm.get("name", ""), domain=fm.get("domain", ""),
        regime=fm.get("regime", ""), status=fm.get("status", ""),
        applies_when=sec("Applies when"), rule=sec("The rule"),
        worked_example=sec("Worked example"), references=sec("References"),
        links=tuple(re.findall(r"\[\[([a-z0-9-]+)\]\]", body)), sections=secs,
    )


def load_patterns(lib_dir: str | None = None) -> list:
    d = lib_dir or _LIB_DIR
    out = []
    for p in sorted(glob.glob(os.path.join(d, "*.md"))):
        if os.path.basename(p).lower() == "readme.md":
            continue
        out.append(_parse_page(p))
    return out


_STOP = set("a an the of to in on for and or is are be with by as it that this from into over "
            "when which not no use used using give gives only same one we you they i its".split())


def _toks(s: str) -> list:
    return [t for t in re.findall(r"[a-zα-ω]+", s.lower()) if len(t) >= 3 and t not in _STOP]


def _score(qtoks: list, sigtoks: set) -> int:
    """Count query tokens that prefix-match some signature token (grad↔gradient)."""
    score = 0
    for t in qtoks:
        for u in sigtoks:
            if t == u or (len(t) >= 3 and len(u) >= 3 and (t.startswith(u) or u.startswith(t))):
                score += 1
                break
    return score


def recognize(query: str, patterns: list | None = None, *, k: int = 3) -> list:
    """Rank pattern pages against a problem description. Returns [(Pattern, score)]
    best-first (score>0 only). Deterministic baseline; the M1 LLM proposer refines."""
    pats = patterns if patterns is not None else load_patterns()
    qt = _toks(query)
    ranked = [(p, _score(qt, set(_toks(p.signature())))) for p in pats]
    ranked.sort(key=lambda x: -x[1])
    return [(p, s) for p, s in ranked[:k] if s > 0]


def _firstline(s: str) -> str:
    for line in (s or "").splitlines():
        if line.strip():
            return line.strip()
    return ""


def trace_from_pattern(problem, pattern: Pattern):
    """Turn a recognized pattern (a wiki page) into a rendered MethodTrace.

    This is the engine's *lifting*: once the agent has RECOGNIZED which page
    applies, the tool assembles the explanation — the rule, the altitude
    explanations, the references, the worked example — with no further LLM call.
    """
    from .trace import MethodTrace, Step  # local import: trace doesn't import library
    lx = pattern.latex_parts()
    t = MethodTrace.from_problem(problem)
    t.add(Step(
        title=f"Recognize: {pattern.name}",
        method_key=pattern.regime or "",
        justification=_firstline(pattern.applies_when),
        forced_by=_firstline(pattern.rule),
        math=((lx["rule"],) if lx.get("rule") else ()),
        altitudes=pattern.altitudes(),
        references=pattern.references_list(),
        detail=("worked example —\n" + pattern.worked_example) if pattern.worked_example else "",
        check="symbolic",
    ))
    if lx.get("example"):
        t.result_latex = lx["example"]
    else:
        we = [l for l in pattern.worked_example.splitlines() if l.strip()]
        t.result = we[0] if we else None
    return t


def leveled_trace_from_pattern(problem, pattern: Pattern) -> dict:
    """The recognition→explain thread: auto-build a LEVELLED explanation from a
    recognized wiki page, in the explanation contract (CLAUDE.md rule 7) — three
    bands (why / how / step) at three reader levels. The page's '## Explain
    (altitudes)' drives the per-level HOW prose; '## LaTeX' gives the typeset rule +
    example; '## Applies when' is the WHY; '## Worked example' is the STEP. Returns
    {level: MethodTrace} ready for render_leveled()."""
    from .trace import MethodTrace, Step  # local import: trace doesn't import library
    alts = pattern.altitudes()
    lx = pattern.latex_parts()
    refs = pattern.references_list()
    we_first = _firstline(pattern.worked_example)

    def build(level: str) -> MethodTrace:
        t = MethodTrace.from_problem(problem)
        why = Step(section="why", title=f"Why this approach — {pattern.name}",
                   method_key=pattern.regime or "",
                   justification=_firstline(pattern.applies_when),
                   forced_by=_firstline(pattern.rule), check="symbolic")
        how = Step(section="how", title="How the approach works — the rule",
                   justification=alts.get(level) or _firstline(pattern.rule),
                   math=((lx["rule"],) if lx.get("rule") else ()),
                   references=refs, check="symbolic")
        stp = Step(section="step", title="Worked example",
                   justification=we_first,
                   math=((lx["example"],) if lx.get("example") else ()),
                   detail=pattern.worked_example, check="symbolic")
        for s in (why, how, stp):
            t.add(s)
        t.result = we_first or pattern.name
        return t

    return {lvl: build(lvl) for lvl in ("expert", "working", "plain")}
