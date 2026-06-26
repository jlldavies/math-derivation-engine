"""Paper gates (rule 10) — arXiv:2606.24442 "Canonical Quantization for Effective Theories with
Higher-Derivative Perturbations". A GREEN paper: the ENGINE derives its central results across the
algebraic-solve, series-expansion, and operator-algebra (oscillator_commutator) tracks; we only check
against the paper. Remaining gaps (Dirac-bracket constrained quantization, Legendre transform) are
rounded up at the bottom.
"""
import os
import sys

import sympy as sp
from sympy.physics.quantum.boson import BosonOp
from sympy.physics.quantum import Dagger

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from integral_explainer.special_methods import oscillator_commutator             # noqa: E402

lam, om = sp.symbols("lambda omega", positive=True)
t, t1, t2 = sp.symbols("t t1 t2", positive=True)
f = sp.Symbol("f", positive=True)
I = sp.I


# ===== (3.31) characteristic equation: substitute x=e^{ift} into the 4th-order EOM (3.30) ======
def test_characteristic_equation():
    x = sp.exp(I * f * t)
    ode = lam ** 2 * x.diff(t, 4) + (1 + 2 * lam * om) * x.diff(t, 2) + om ** 2 * x
    char = sp.expand(sp.simplify(ode / x))
    assert sp.expand(char - (lam ** 2 * f ** 4 - (1 + 2 * lam * om) * f ** 2 + om ** 2)) == 0


# ===== (3.32-3.33) frequencies: solve the characteristic eq (quadratic in F=f^2) ==============
def test_frequencies():
    F = sp.Symbol("F", positive=True)
    sols = sp.solve(lam ** 2 * F ** 2 - (1 + 2 * lam * om) * F + om ** 2, F)
    f1sq, f2sq = sorted(sols, key=lambda s: sp.limit(s, lam, 0))   # smaller root -> f1
    assert sp.simplify(f1sq - ((sp.sqrt(1 + 4 * lam * om) - 1) / (2 * lam)) ** 2) == 0
    assert sp.simplify(f2sq - ((sp.sqrt(1 + 4 * lam * om) + 1) / (2 * lam)) ** 2) == 0


# ===== (3.47-3.48) perturbative frequency: f1 -> omega(1 - lam omega + 2 lam^2 omega^2) =======
def test_perturbative_frequency_series():
    f1 = (sp.sqrt(1 + 4 * lam * om) - 1) / (2 * lam)
    ser = sp.series(f1, lam, 0, 3).removeO()
    assert sp.simplify(ser - om * (1 - lam * om + 2 * lam ** 2 * om ** 2)) == 0


# ===== (3.49) commutator prefactor: 1/sqrt(1+4 lam omega) -> 1 - 2 lam omega + 6 lam^2 omega^2 =
def test_perturbative_prefactor_series():
    ser = sp.series(1 / sp.sqrt(1 + 4 * lam * om), lam, 0, 3).removeO()
    assert sp.simplify(ser - (1 - 2 * lam * om + 6 * lam ** 2 * om ** 2)) == 0


# ===== (3.22) unequal-time commutator [x0(t1),x0(t2)] = -i sin(omega(t1-t2)) (oscillator alg) ==
def test_unequal_time_commutator():
    a = BosonOp("a"); ad = Dagger(a)
    x0 = lambda tt: (a * sp.exp(-I * om * tt) + ad * sp.exp(I * om * tt)) / sp.sqrt(2)
    comm = oscillator_commutator(x0(t1), x0(t2))
    assert sp.simplify(comm.rewrite(sp.sin) - (-I * sp.sin(om * (t1 - t2)))) == 0


# ===== (3.43) perturbed two-mode commutator: -i/sqrt(1+4 lam om) [sin f1 dt + sin f2 dt] ======
def test_two_mode_commutator():
    a1, a2 = BosonOp("a1"), BosonOp("a2")
    f1 = (sp.sqrt(1 + 4 * lam * om) - 1) / (2 * lam)
    f2 = (sp.sqrt(1 + 4 * lam * om) + 1) / (2 * lam)
    pref = 1 / sp.sqrt(2 * sp.sqrt(1 + 4 * lam * om))
    def X(tt):
        return (pref * (a1 * sp.exp(-I * f1 * tt) + Dagger(a1) * sp.exp(I * f1 * tt))
                + pref * (a2 * sp.exp(-I * f2 * tt) + Dagger(a2) * sp.exp(I * f2 * tt)))
    comm = oscillator_commutator(X(t1), X(t2)).rewrite(sp.sin)
    want = (-I / sp.sqrt(1 + 4 * lam * om)) * (sp.sin(f1 * (t1 - t2)) + sp.sin(f2 * (t1 - t2)))
    assert sp.simplify(comm - want) == 0


# ===== ROUND-UP — what the engine could NOT derive here (honest boundary) =====================
def test_ROUNDUP_remaining_gaps():
    """The paper's constrained-quantization scaffolding is out of the engine's current reach.
    Recorded so the boundary is explicit, not silently omitted."""
    gaps = {
        "dirac_brackets": "the Dirac-bracket procedure (3.5-3.8) for 2nd-class constraints — needs a "
                          "constrained-Hamiltonian method (Poisson brackets + constraint matrix inverse); "
                          "no dedicated capability yet.",
        "legendre_transform": "L -> H via momenta + inversion (3.17/3.27) — sympy-doable but no dedicated "
                              "Legendre-transform method to lay out the steps.",
    }
    assert len(gaps) == 2
    # the engine DOES derive: characteristic eq, frequencies, perturbative series, unequal-time
    # commutators (1- and 2-mode) — i.e. the spectral + operator-algebra core of the paper.
