"""Testing an explanation means checking the BREAKDOWN is valid at every level
(CLAUDE.md rule 7): the levels must genuinely differ (step count not identical),
and decompose the right way (plain >= expert). `validate_levels` is that check;
these tests exercise it so the rule can't silently regress to one-size-fits-all.
"""
import os
import sys

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "src")))
from integral_explainer import (Derivation, validate_levels, validate_qualification,
                                Problem, Goal)


def _problem():
    return Problem(latex="x", represents="t", goal=Goal.EVALUATE, integral="t")


def test_varying_levels_pass():
    """A genuinely levelled explanation: expert collapses, plain expands."""
    d = Derivation(_problem())
    d.why("why", "because")
    d.how("how", "thus")
    d.step("shared core", levels=("expert", "working", "plain"))
    d.step("working+plain detail", levels=("working", "plain"))
    d.step("plain sub-step a", levels=("plain",))
    d.step("plain sub-step b", levels=("plain",))
    d.verify("checked")
    tracks = d.tracks()
    counts = {k: len(v.steps) for k, v in tracks.items()}
    assert counts["expert"] < counts["working"] < counts["plain"], counts
    assert validate_levels(tracks) == [], validate_levels(tracks)


def test_identical_counts_flagged():
    """The anti-pattern: same steps at every level, only the prose differs."""
    d = Derivation(_problem())
    d.why("why", "x"); d.how("how", "y"); d.step("s", "z")
    warn = validate_levels(d.tracks())
    assert any("identical step count" in w for w in warn), warn


def test_inverted_decomposition_flagged():
    """Plain must not have fewer steps than expert."""
    d = Derivation(_problem())
    d.why("why", "x"); d.how("how", "y")
    d.step("expert heavy 1", levels=("expert",))
    d.step("expert heavy 2", levels=("expert",))
    d.verify("v")
    warn = validate_levels(d.tracks())
    assert any("inverted" in w for w in warn), warn


def test_missing_band_flagged():
    """Every level still needs all three contract bands."""
    d = Derivation(_problem())
    d.step("only a step", "x")
    warn = validate_levels(d.tracks())
    assert any("missing band" in w for w in warn), warn


def test_qualification_tree_emerges():
    """The per-level counts EMERGE from the tree cut, and every shown step is within
    the reader's qualification (validate_qualification passes)."""
    d = Derivation(_problem())
    d.why("why", "x"); d.how("how", "y")
    d.step("big expert move", requires="expert", decompose=[
        dict(title="w1", requires="working",
             decompose=[dict(title="p1a"), dict(title="p1b")]),     # default requires=plain
        dict(title="w2", requires="working", decompose=[dict(title="p2a")]),
        dict(title="stated value", requires="plain"),
    ])
    d.verify("v")
    tracks = d.tracks()
    counts = {k: len(v.steps) for k, v in tracks.items()}
    assert counts["expert"] < counts["working"] < counts["plain"], counts   # 4 < 6 < 7
    assert validate_qualification(tracks) == [], validate_qualification(tracks)


def test_ceiling_flagged():
    """A grad-only step with NO decomposition is an honest ceiling at lower levels."""
    d = Derivation(_problem())
    d.why("why", "x"); d.how("how", "y")
    d.step("grad-only, irreducible", requires="expert")   # no decompose -> can't reach plain
    d.verify("v")
    warn = validate_qualification(d.tracks())
    assert any("ceiling" in w for w in warn), warn
