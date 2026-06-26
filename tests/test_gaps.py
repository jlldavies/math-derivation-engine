"""The gap finder must surface real holes (uncovered domains, dangling links, methods
invoked with no page) so a scaling ingestion knows where to aim. State-robust: tests
the MECHANISM on controlled input, plus the live-corpus invariants we want to keep."""
import os
import sys

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "src")))
from integral_explainer import load_patterns, find_gaps, ingest_priorities

PATS = load_patterns()


def test_corpus_covers_all_target_domains():
    """Invariant after the gap-directed waves: no target domain is uncovered."""
    assert find_gaps(PATS)["uncovered_domains"] == [], find_gaps(PATS)["domain_coverage"]


def test_corpus_has_no_dangling_links():
    assert find_gaps(PATS)["dangling_links"] == []


def test_uncovered_domain_is_detected():
    """Mechanism: a target domain with no page is flagged."""
    r = find_gaps(PATS, target_domains=("calculus", "no-such-domain"))
    assert "no-such-domain" in r["uncovered_domains"]


def test_missing_method_is_flagged():
    ts = {"nodes": [{"id": "some_problem", "method": "no-such-method-page"}]}
    assert "no-such-method-page" in find_gaps(PATS, [ts])["missing_methods"]


def test_priorities_lead_with_a_synthetic_gap():
    r = find_gaps(PATS, target_domains=("calculus", "no-such-domain"))
    assert any("OPEN DOMAIN" in m for m in ingest_priorities(r))
