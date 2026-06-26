"""M1 proposer plumbing tests (deterministic — a mock LLM stands in for the brain).

Tests the retrieval→shortlist→parse loop. The live LLM *judgement* is exercised
separately (examples/m1_recognize_demo.py, answered by the agent / Claude API).
"""
import os

from integral_explainer.library import load_patterns
from integral_explainer.problem import Problem, Goal
from integral_explainer.proposer import propose_with_llm, build_recognition_prompt

LIB = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "library"))
PATS = load_patterns(LIB)

CURL_GRAD = Problem(
    latex=r"\nabla\times(\nabla\phi)",
    represents="the curl of a gradient field",
    goal=Goal.PROVE,
)


def test_prompt_contains_problem_and_candidates():
    from integral_explainer.library import recognize
    shortlist = recognize("curl gradient", PATS, k=5)
    prompt = build_recognition_prompt(CURL_GRAD, shortlist)
    assert "nabla" in prompt and "curl of a gradient" in prompt
    assert "CANDIDATES" in prompt and any(p.id in prompt for p, _ in shortlist)


def test_llm_pick_is_parsed():
    # the LLM names the correct pattern; the proposer must return it
    llm = lambda prompt: "sym-antisym-contraction — d(dφ)=0; symmetric × antisymmetric vanishes"
    chosen, answer, shortlist = propose_with_llm(CURL_GRAD, llm, patterns=PATS)
    assert chosen is not None and chosen.id == "sym-antisym-contraction"
    assert any(p.id == "sym-antisym-contraction" for p, _ in shortlist)


def test_llm_none_answer():
    chosen, answer, _ = propose_with_llm(CURL_GRAD, lambda p: "NONE — unfamiliar", patterns=PATS)
    assert chosen is None


def test_llm_drives_recognize_shortlist():
    # the shortlist the LLM chooses from must come from recognize() (not all 14)
    captured = {}
    def llm(prompt):
        captured["prompt"] = prompt
        return "sym-antisym-contraction — forced"
    propose_with_llm(CURL_GRAD, llm, k=4, patterns=PATS)
    # k=4 candidates max in the prompt
    assert captured["prompt"].count("applies when:") <= 4
