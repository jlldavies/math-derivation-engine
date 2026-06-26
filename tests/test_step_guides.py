"""Every method must be GROUNDED in an established published step-by-step derivation guide
(methods.STEP_GUIDES), so its leveled Derivation can be corroborated against how authoritative
sources teach the steps. Where the literature is THIN, the entry says so — those are where the
engine's Derivation fills the gap, not where it is unsupported. (Found 2026-06-26; see
METHOD_STEP_SOURCES.md.)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.methods import METHODS, STEP_GUIDES                     # noqa: E402


def test_every_method_has_a_step_guide():
    missing = set(METHODS) - set(STEP_GUIDES)
    extra = set(STEP_GUIDES) - set(METHODS)
    assert not missing, f"methods with no step-by-step guide grounding: {missing}"
    assert not extra, f"STEP_GUIDES entries for unknown methods: {extra}"


def test_each_guide_has_a_grade_and_url():
    for k, g in STEP_GUIDES.items():
        assert "http" in g, f"{k}: step guide has no URL"
        assert g.split(" ", 1)[0].rstrip(":") in {"FULL", "partial", "partial->FULL", "THIN"}, \
            f"{k}: step guide must start with a grade (FULL/partial/THIN), got {g[:20]!r}"


def test_step_sources_doc_exists():
    doc = os.path.join(os.path.dirname(__file__), "..", "METHOD_STEP_SOURCES.md")
    assert os.path.exists(doc), "METHOD_STEP_SOURCES.md (the kept method->step-guide map) is missing"
