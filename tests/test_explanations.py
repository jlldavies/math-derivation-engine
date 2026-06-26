"""Every method must carry a VALID leveled explanation (rule 7 + 11): a Derivation whose
why/how/step bands all exist, whose per-level step counts genuinely differ, and that passes
validate_qualification. Plus the method-completeness gate: every method COMPLETE.
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.explanations import EXPLANATIONS                       # noqa: E402
from integral_explainer.trace import validate_qualification                   # noqa: E402
from integral_explainer import strategies as S                                # noqa: E402
from integral_explainer import coverage                                       # noqa: E402


def test_every_method_has_an_explanation():
    missing = set(S.COVERAGE) - set(EXPLANATIONS)
    assert not missing, f"methods with NO leveled explanation: {missing}"


@pytest.mark.parametrize("key", sorted(EXPLANATIONS))
def test_explanation_is_valid_and_leveled(key):
    tracks = EXPLANATIONS[key]().tracks()
    assert set(tracks) >= {"plain", "working", "expert"}, f"{key}: missing a level band"
    assert not validate_qualification(tracks), f"{key}: fails validate_qualification"
    counts = {lvl: len(tr.steps) for lvl, tr in tracks.items()}
    assert len(set(counts.values())) > 1, f"{key}: per-level step counts do not differ ({counts})"


def test_all_methods_complete_rule_11():
    incomplete = {k: r for k, r in coverage.method_status().items() if not r["complete"]}
    assert not incomplete, f"INCOMPLETE methods (Definition of Done): {incomplete}"
