"""Proposer: ranks candidate methods for an integral.

Rule-based for M0 — pattern-matches the integrand string against the method
registry and returns ordered (method_key, reason) candidates. The M1 milestone
replaces the body of `propose()` with an LLM (Claude tool-use) behind this SAME
signature, so the rest of the loop is unchanged.

It is intentionally shallow: the point of the engine is not a clever proposer
but the propose->execute->verify->explain *loop* with a real verification signal.
"""
from __future__ import annotations

from typing import Callable

from .methods import METHODS
from .library import recognize, load_patterns


def propose(integrand: str, a, b) -> list[tuple[str, str]]:
    """Return ordered (method_key, human reason) candidates for this integral.

    Cheap surface heuristics over the integrand string + limits. Order reflects
    what to try first; the executor/verifier decide what actually works.
    """
    s = integrand.replace(" ", "")
    candidates: list[tuple[str, str]] = []
    infinite = str(b) in ("oo", "inf", "+inf") or str(a) in ("-oo", "-inf")

    oscillatory = any(t in s for t in ("cos(", "sin(", "exp(i", "e**(i", "mp.e**(i"))
    has_sqrt = "sqrt(" in s or "**(1/2)" in s or "**0.5" in s or "**(-1/2)" in s
    rational_shift = ("(x+" in s or "(x-" in s) and "**" in s  # (x+c)^p structure

    if has_sqrt and oscillatory:
        candidates.append(("u_sub", "algebraic endpoint singularity (1/sqrt); substitute to remove it"))
    if oscillatory and infinite:
        candidates.append(("stationary_phase", "oscillatory integrand over an infinite range; quadosc / Fourier, not plain quadrature"))
    if rational_shift or (has_sqrt and rational_shift):
        candidates.append(("meijer_g", "power x^a times (x+c)^b (times exp): reduces to a Meijer-G / hypergeometric closed form"))
    if oscillatory:
        candidates.append(("meijer_g", "trig/exponential weight: Mellin/Meijer-G representation gives a named closed form"))
    if infinite:
        candidates.append(("asymptotic_expansion", "infinite range with a regulator: expand the closed form asymptotically to expose leading/divergent behaviour"))

    # de-dup, preserve order, keep only known keys
    seen, ordered = set(), []
    for key, reason in candidates:
        if key in METHODS and key not in seen:
            seen.add(key)
            ordered.append((key, reason))
    return ordered


# ---------------------------------------------------------------------------
# M1 proposer: the LLM drives recognize(). The keyword retriever narrows the 14+
# wiki pages to a shortlist; the LLM judges which one actually applies and why.
# `llm` is an injectable callable str->str (the Claude API, or the agent itself),
# so the engine stays a deterministic Python library and the LLM is the brain.
# ---------------------------------------------------------------------------
def build_recognition_prompt(problem, candidates: list) -> str:
    """The prompt the LLM proposer answers: pick the single pattern that applies."""
    lines = [
        "You are the recognition step of a maths-explanation engine.",
        "From the shortlisted candidate patterns, pick the SINGLE one that best",
        "applies to the problem (or say NONE). Recognition is structural, not numeric.",
        "",
        f"PROBLEM (LaTeX): {problem.latex}",
        f"REPRESENTS:      {problem.represents}",
        f"GOAL:            {problem.goal_str()}",
        "",
        "CANDIDATES (shortlisted by signature match):",
    ]
    for i, (p, score) in enumerate(candidates, 1):
        first = p.applies_when.splitlines()[0] if p.applies_when else ""
        lines.append(f"  {i}. [{p.id}]  {p.name}")
        lines.append(f"       applies when: {first}")
    lines += ["",
              "Answer in one line:  <pattern-id> — <why it is forced>   (or:  NONE — <why>)."]
    return "\n".join(lines)


def propose_with_llm(problem, llm: Callable[[str], str], *, k: int = 5,
                     patterns: list | None = None) -> tuple:
    """M1: the LLM drives recognize() to a shortlist, then picks the pattern.

    Returns (chosen_Pattern_or_None, llm_answer, shortlist). The parse is robust:
    it finds whichever candidate id the LLM names in its answer (longest match).
    """
    pats = patterns if patterns is not None else load_patterns()
    text = f"{problem.latex} {problem.represents}"
    shortlist = recognize(text, pats, k=k)
    if not shortlist:
        return None, "NONE — no candidate patterns matched", []
    answer = (llm(build_recognition_prompt(problem, shortlist)) or "").strip()
    al = answer.lower()
    chosen = max((p for p, _ in shortlist if p.id in al),
                 key=lambda p: len(p.id), default=None)
    return chosen, answer, shortlist
