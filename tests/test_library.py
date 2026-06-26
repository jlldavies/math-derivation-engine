"""Tests for the pattern library: structural validation (V20) + recognition
golden corpus (V16). The wiki pages are the test corpus — each must parse, be
schema-complete, link cleanly, and be retrievable from a plain-language query.
"""
import os
import pytest

from integral_explainer.library import load_patterns, recognize

LIB = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "library"))
PATS = load_patterns(LIB)


# ---- V20: structural validation -------------------------------------------
def test_pages_load():
    assert len(PATS) >= 14, f"only {len(PATS)} pages loaded"


@pytest.mark.parametrize("p", PATS, ids=[p.id for p in PATS])
def test_schema_complete(p):
    assert p.id and p.name and p.domain, f"{p.id}: missing frontmatter"
    assert p.applies_when, f"{p.id}: no recognition signature"
    assert p.rule, f"{p.id}: no rule"
    assert p.worked_example, f"{p.id}: no worked example (golden test)"
    assert p.references, f"{p.id}: no references"


def test_link_integrity():
    ids = {p.id for p in PATS}
    dangling = {(p.id, l) for p in PATS for l in p.links if l not in ids}
    assert not dangling, f"dangling cross-links: {sorted(dangling)}"


# ---- V16: recognition golden corpus ---------------------------------------
GOLDEN = {
    "curl of a gradient": "sym-antisym-contraction",
    "divergence of a curl": "div-of-curl",
    "levi-civita epsilon delta cross product": "epsilon-delta-identity",
    "laplacian divergence of a gradient": "laplacian-from-div-grad",
    "gaussian integral over the whole line": "gaussian-integral",
    "integration by parts": "integration-by-parts",
    "reverse chain rule substitution": "u-substitution",
    "error function partial gaussian": "error-function",
    "fresnel oscillatory integral cos x squared": "fresnel-integral",
    "tricomi confluent hypergeometric power exponential": "tricomi-u-reduction",
    "meijer g function product reduction": "meijer-g-reduction",
    "mellin transform barnes contour": "mellin-barnes",
    "gamma function factorial non-integer": "gamma-function",
    "endpoint asymptotics of a laplace integral": "watsons-lemma",
    # --- expanded corpus (asymptotics / regularization / special-fn / transform / GR) ---
    "saddle point steepest descent large parameter integral": "saddle-point-method",
    "stationary phase oscillatory integral rapidly varying": "method-of-stationary-phase",
    "borel summation of a divergent asymptotic series": "borel-summation",
    "zeta function regularization divergent sum": "zeta-regularization",
    "euler maclaurin sum to integral bernoulli": "euler-maclaurin",
    "abel plana sum to integral formula": "abel-plana",
    "dimensional regularization loop integral epsilon pole": "dimensional-regularization",
    "feynman parametrization combine propagator denominators": "feynman-parametrization",
    "schwinger parametrization exponentiate the denominator": "schwinger-parametrization",
    "hadamard finite part divergent integral continuation": "hadamard-finite-part",
    "beta function integral t power one minus t power": "beta-function",
    "incomplete gamma function tail of exponential": "incomplete-gamma",
    "bessel function cylinder oscillatory": "bessel-function",
    "gauss hypergeometric two f one series": "hypergeometric-2f1",
    "polylogarithm dilogarithm iterated log": "polylogarithm",
    "digamma polygamma log derivative of gamma": "digamma-polygamma",
    "contour integration residues close the contour": "contour-residues",
    "differentiation under the integral sign feynman trick": "differentiation-under-integral",
    "one sided laplace transform table": "laplace-transform",
    "fourier transform frequency": "fourier-transform",
    "gamma reflection formula sine": "gamma-reflection",
    "christoffel symbols metric connection coefficients": "christoffel-symbols",
    "riemann curvature tensor from the connection": "riemann-curvature",
    "ricci tensor scalar contraction of riemann": "ricci-tensor-scalar",
    "geodesic equation straightest path": "geodesic-equation",
    "covariant derivative connection correction": "covariant-derivative",
    "raising lowering indices with the metric": "raising-lowering-indices",
}


@pytest.mark.parametrize("query,expected", list(GOLDEN.items()))
def test_recognition_top3(query, expected):
    hits = recognize(query, PATS, k=3)
    ids = [p.id for p, _ in hits]
    assert expected in ids, f"{query!r} -> {ids} (expected {expected} in top 3)"


def test_recognition_top1_rate():
    """Report the share that land top-1 — the recognizer's headline quality."""
    top1 = sum(1 for q, e in GOLDEN.items()
               if (h := recognize(q, PATS, k=1)) and h[0][0].id == e)
    rate = top1 / len(GOLDEN)
    assert rate >= 0.7, f"top-1 rate {rate:.0%} below 70%"
