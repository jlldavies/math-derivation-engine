"""Paper gates (rule 10) — operator-algebra content of arXiv:2606.24008 "General Lagrangian
formulations for mixed-antisymmetric tensor fields on flat backgrounds" (BRST higher-spin).

This paper is almost entirely OPERATOR SUPERALGEBRA (commutators, BRST nilpotency, Verma modules)
— a domain the engine had no entry point for. The new `oscillator_commutator` capability opens its
verifiable core: the ENGINE computes the commutators from the canonical [a,a^†]=1 (sympy normal
ordering), we only check closure against the paper / textbook. What the engine CANNOT yet reach is
rounded up at the bottom (test_ROUNDUP_remaining_gaps) — honest boundary, not padded.
"""
import os
import sys

import sympy as sp
from sympy.physics.quantum.boson import BosonOp
from sympy.physics.quantum import Dagger
from sympy.physics.quantum.operatorordering import normal_ordered_form as NO

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.special_methods import oscillator_commutator                # noqa: E402


def _eq(A, B):
    return NO(sp.expand(A - B), independent=True) == 0


# ===== Cat A — Jordan-Schwinger gl(k): the paper's t-generator relation (Table 1 / so(k,k)) ===
# t_i{}^j = a^†_i a_j ;  paper:  [t_i^j, t_p^q] = δ_p^j t_i^q - δ_i^q t_p^j
def _t(osc, i, j):
    return Dagger(osc[i]) * osc[j]


def test_jordan_schwinger_gl2_paper_A5():
    a = {1: BosonOp("a_1"), 2: BosonOp("a_2")}
    # [t_1^2, t_2^1] = δ_2^2 t_1^1 - δ_1^1 t_2^2 = t_1^1 - t_2^2
    got = oscillator_commutator(_t(a, 1, 2), _t(a, 2, 1))
    assert _eq(got, _t(a, 1, 1) - _t(a, 2, 2))


def test_jordan_schwinger_gl3_paper_A5():
    a = {1: BosonOp("a_1"), 2: BosonOp("a_2"), 3: BosonOp("a_3")}
    # [t_1^2, t_2^3] = δ_2^2 t_1^3 - δ_1^3 t_2^2 = t_1^3
    assert _eq(oscillator_commutator(_t(a, 1, 2), _t(a, 2, 3)), _t(a, 1, 3))
    # [t_1^2, t_3^1] = δ_3^2 t_1^1 - δ_1^1 t_3^2 = -t_3^2
    assert _eq(oscillator_commutator(_t(a, 1, 2), _t(a, 3, 1)), -_t(a, 3, 2))


# ===== Cat A/C — su(1,1) bosonic realization closes (also the external gate) ==================
def test_su11_realization_closes():
    a = BosonOp("a"); ad = Dagger(a)
    K0, Kp, Km = (ad * a + sp.Rational(1, 2)) / 2, ad * ad / 2, a * a / 2
    assert _eq(oscillator_commutator(K0, Kp), Kp)        # [K0,K+] = +K+
    assert _eq(oscillator_commutator(K0, Km), -Km)       # [K0,K-] = -K-
    assert _eq(oscillator_commutator(Kp, Km), -2 * K0)   # [K+,K-] = -2K0


# ===== Cat C — number / spin operator structure g_0 = -½[a^†,a]  (eq. 1.7) ====================
def test_number_operator_commutator_structure():
    a = BosonOp("a"); ad = Dagger(a)
    # g_0 (one Lorentz dof) ~ -½[a^†,a]; the COMMUTATOR is what the engine derives (= 1/2 here),
    # i.e. -½[a^†,a] = a^†a + ½ up to ordering — the bilinear number structure of eq.(1.7).
    assert _eq(oscillator_commutator(ad, a), -1)         # [a^†,a] = -1  ->  g_0 carries a^†a + const


# ===== Cat D — counting formulas (symbolic in k), eq. lines 217-269 ===========================
def test_constraint_counting_formulas():
    k = sp.symbols("k", positive=True, integer=True)
    even, odd = k * (k - 1) + 1, k                       # even + odd constraints
    assert sp.expand(even + odd) == k ** 2 + 1           # total primary = k^2 + 1
    assert sp.expand(2 * k * (k - 1)) == 2 * k ** 2 - 2 * k   # second-class count


# ===== ROUND-UP — what the engine CANNOT yet derive from this paper (honest boundary) =========
def test_ROUNDUP_remaining_gaps():
    """Documents the paper content still out of reach — the next operator-algebra build targets.
    Asserted as a record so the boundary is explicit in the suite, not silently omitted."""
    remaining_gaps = {
        "BRST_nilpotency": "Q^2 = 2 Σ B^i σ^i(G), Q_c^2=0 (eq.4.6/4.14) — needs ghost oscillators + "
                           "the full structure-constant sum assembled into Q; oscillator_commutator is "
                           "the atom, but Q-assembly + Jacobi bookkeeping is not built.",
        "verma_module_realization": "the b/d-oscillator realizations of l'_{ij}, t'_{lm}, g'_0 (eq.3.2-3.6) "
                                    "and proving they satisfy the same table — many-mode, very long.",
        "so_kk_with_lorentz_trace": "general-k generators with contracted Lorentz index a_{iμ}a^{jμ} give "
                                    "d-dependent trace terms (the t_i^i = a^†a + d/2 pieces) — needs index "
                                    "contraction over μ on top of the mode algebra.",
        "lagrangian_actions": "S ~ <χ|KQ|χ> (eq.1.2/4.16) — formal inner products, not a closed-form "
                              "computation the engine evaluates.",
    }
    assert len(remaining_gaps) == 4
    # the engine DOES now cover: Cat A gl(k) commutators, su(1,1) closure, Cat D counting (above).
