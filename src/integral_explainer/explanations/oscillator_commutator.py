r"""LEVELED Derivation for METHOD oscillator_commutator (CLAUDE.md rule 7 + rule 11).

Realization mirrored: special_methods.oscillator_commutator. The engine COMPUTES, from the single
canonical rule [a, a^†]=1, the normal-ordered commutator of operators built from oscillators — e.g.
the su(1,1) realization K_+ = a^{\dagger 2}/2, K_- = a^2/2, K_0 = (a^\dagger a + 1/2)/2 closes with
[K_+,K_-] = -2K_0, and the Jordan-Schwinger map t_i{}^j = a^\dagger_i a_j reproduces the paper's
gl(k) relation [t_1{}^2, t_2{}^1] = t_1{}^1 - t_2{}^2 (arXiv:2606.24008, Table 1 / so(k,k)).
THIS derivation walks exactly that computation.

Sub-methods referenced by the steps:
    oscillator_commutator -> { canonical commutator [a,a^†]=1, commutator bilinearity/Leibniz,
                               normal ordering }.
"""
from ..derivation import Derivation
from ..problem import Problem, Goal
from ..trace import validate_qualification  # noqa: F401

HDR = (r"[K_+,K_-]=\Big[\tfrac12 a^{\dagger 2},\tfrac12 a^{2}\Big]=-2K_0,\qquad [a,a^{\dagger}]=1")


def build_oscillator_commutator_derivation() -> Derivation:
    problem = Problem(
        latex=HDR,
        represents=r"closure of an oscillator (Fock) Lie-algebra realization — does $[A,B]$ of "
                   r"operators built from $a,a^\dagger$ reproduce the claimed generator?",
        goal=Goal.SIMPLIFY,
        integral="normal-ordered commutator of bosonic-oscillator operators (su(1,1) / Jordan-Schwinger)")
    d = Derivation(problem)

    # ---- WHY this approach -------------------------------------------------------------------
    d.why("Why this approach — compute the commutator from the one canonical rule, then normal-order",
          {"plain": r"A symmetry algebra is really just a table of 'who fails to commute with whom'. To "
                    r"check that operators built from a ladder pair $a,a^\dagger$ form the claimed algebra, "
                    r"we compute each bracket $[A,B]$ using the SINGLE rule $a a^\dagger-a^\dagger a=1$, then "
                    r"tidy every term into one standard order so we can read off the answer.",
           "working": r"The generators are given as oscillator bilinears; their Lie brackets are fixed once we "
                      r"know $[a,a^\dagger]=1$. Computing $[A,B]$ and NORMAL-ordering it (all $a^\dagger$ to the "
                      r"left) yields a unique polynomial we can compare to the claimed $f^K{}_{IJ}o_K$.",
           "expert": r"For a Fock realization of a Lie (super)algebra, closure is a normal-ordering computation: "
                     r"each $[o_I,o_J]$ reduces, via the canonical $[a_i,a_j^\dagger]=\delta_{ij}$, to a unique "
                     r"Wick-ordered expression, which must equal $f^K{}_{IJ}o_K$."},
          forced_by=r"a Lie algebra is DEFINED by its commutators, and the realization gives each generator as a "
                    r"polynomial in $a,a^\dagger$; the bracket is therefore determined entirely by $[a,a^\dagger]=1$, "
                    r"but only AFTER a common ordering is fixed.",
          payoff=r"normal ordering makes $[A,B]$ a unique canonical form, so closure $[o_I,o_J]=f^K{}_{IJ}o_K$ is "
                 r"PROVED, not asserted; a numeric/matrix truncation would destroy the exact algebra.",
          relies_on=r"bosonic canonical relations $[a_i,a_j^\dagger]=\delta_{ij}$ and finitely many modes; "
                    r"Grassmann-odd (ghost) generators need the anticommutator analogue.")

    # ---- HOW the approach works --------------------------------------------------------------
    d.how("How it works — bilinearity + Leibniz, reduced by [a,a†]=1",
          {"plain": r"Two rules do all the work: brackets are linear and obey a product (Leibniz) rule, "
                    r"$[AB,C]=A[B,C]+[A,C]B$; and whenever an $a$ sits left of an $a^\dagger$ we swap them, "
                    r"paying a $+1$. Repeating the swap until everything is ordered gives the answer.",
           "working": r"Expand the bracket with $[AB,C]=A[B,C]+[A,C]B$ (and its mirror), reducing every piece to "
                      r"the atomic $[a,a^\dagger]=1$; then move all $a^\dagger$ left, each transposition emitting "
                      r"a $1$, until the expression is normal-ordered.",
           "expert": r"$[a^{\dagger 2},a^2]$ telescopes through $[a^\dagger,a^2]=-2a$ and $[a^{\dagger2},a]=2a^\dagger$ "
                     r"to $-2(2a^\dagger a+1)$; halving twice gives $[K_+,K_-]=-(2a^\dagger a+1)/1=-2K_0$."},
          math=[r"[AB,C]=A[B,C]+[A,C]B,\qquad [A,BC]=[A,B]C+B[A,C],\qquad [a,a^{\dagger}]=1",
                r"[a^{\dagger2},a^{2}]=-4a^{\dagger}a-2"])

    # ---- THE STEPS (one qualification tree; counts EMERGE from the frontier cut) -------------
    d.step("Compute [K+,K-] and normal-order to recognize -2K0", requires="expert",
           prose=r"Apply Leibniz to $[\tfrac12a^{\dagger2},\tfrac12a^2]$, reduce with $[a,a^\dagger]=1$, and "
                 r"normal-order: the result $-(a^\dagger a+\tfrac12)\cdot2=-2K_0$ — the realization closes.",
           math=[r"[K_+,K_-]=\tfrac14[a^{\dagger2},a^{2}]=\tfrac14(-4a^{\dagger}a-2)=-\Big(a^{\dagger}a+\tfrac12\Big)=-2K_0"],
           references=["sub-method: oscillator_commutator -> {canonical [a,a†]=1, Leibniz, normal ordering}"],
           decompose=[
               dict(title="Expand the bracket by the Leibniz rule", requires="working",
                    prose=r"Pull the constants out and apply $[AB,C]=A[B,C]+[A,C]B$ to split $[a^{\dagger2},a^2]$ "
                          r"into atomic brackets.",
                    math=[r"[K_+,K_-]=\tfrac14[a^{\dagger2},a^{2}],\quad "
                          r"[a^{\dagger2},a^{2}]=a^{\dagger}[a^{\dagger},a^{2}]+[a^{\dagger},a^{2}]a^{\dagger}"],
                    references=["sub-method: commutator bilinearity/Leibniz"],
                    decompose=[
                        dict(title="Brackets are linear and pull out constants", requires="plain",
                             prose=r"$[\tfrac12X,\tfrac12Y]=\tfrac14[X,Y]$ — scalars come straight out of a bracket.",
                             math=[r"[\tfrac12a^{\dagger2},\tfrac12a^{2}]=\tfrac14[a^{\dagger2},a^{2}]"]),
                        dict(title="The product (Leibniz) rule for brackets", requires="plain",
                             prose=r"A bracket of a product splits: $[AB,C]=A[B,C]+[A,C]B$, like a derivative.",
                             math=[r"[a^{\dagger2},a^{2}]=a^{\dagger}[a^{\dagger},a^{2}]+[a^{\dagger},a^{2}]a^{\dagger}"]),
                    ]),
               dict(title="Reduce every piece with [a,a†]=1", requires="working",
                    prose=r"The atomic brackets are $[a^\dagger,a^2]=-2a$ and $[a^{\dagger2},a]=2a^\dagger$ (each one "
                          r"swap of an adjacent $a,a^\dagger$ pair). Substituting gives $-4a^\dagger a-2$ after ordering.",
                    math=[r"[a^{\dagger},a^{2}]=-2a,\quad [a^{\dagger 2},a]=2a^{\dagger}\ \Rightarrow\ "
                          r"[a^{\dagger2},a^{2}]=-4a^{\dagger}a-2"],
                    references=["sub-method: canonical commutator [a,a†]=1"],
                    decompose=[
                        dict(title="The single swap rule", requires="plain",
                             prose=r"Whenever $a$ is left of $a^\dagger$, swap and add one: $aa^\dagger=a^\dagger a+1$.",
                             math=[r"[a,a^{\dagger}]=1\ \Leftrightarrow\ aa^{\dagger}=a^{\dagger}a+1"]),
                        dict(title="Apply it to the atomic brackets", requires="plain",
                             prose=r"$[a^\dagger,a^2]=a^\dagger a^2-a^2a^\dagger=-2a$ after two swaps; similarly "
                                   r"$[a^{\dagger2},a]=2a^\dagger$.",
                             math=[r"a^{2}a^{\dagger}=a(a^{\dagger}a+1)=a^{\dagger}a^{2}+2a\ \Rightarrow\ [a^{\dagger},a^{2}]=-2a"]),
                        dict(title="Collect the normal-ordered result", requires="plain",
                             prose=r"Putting the pieces together and ordering $a^\dagger$ left of $a$ gives $-4a^\dagger a-2$.",
                             math=[r"[a^{\dagger2},a^{2}]=-4a^{\dagger}a-2"]),
                    ]),
               dict(title="Recognize the canonical form as -2K0 (closure)", requires="working",
                    prose=r"Divide by 4: $-(a^\dagger a+\tfrac12)$. Since $K_0=(a^\dagger a+\tfrac12)/2$, this is "
                          r"exactly $-2K_0$ — the bracket lands back inside the generator set, so su(1,1) closes.",
                    math=[r"\tfrac14(-4a^{\dagger}a-2)=-\Big(a^{\dagger}a+\tfrac12\Big)=-2K_0"],
                    references=["application: su(1,1) bosonic realization; arXiv:2606.24008 Table 1 closure"],
                    decompose=[
                        dict(title="Match the result to the generator", requires="plain",
                             prose=r"$K_0=\tfrac12(a^\dagger a+\tfrac12)$, so $a^\dagger a+\tfrac12=2K_0$ and the answer is $-2K_0$.",
                             math=[r"K_0=\tfrac12\Big(a^{\dagger}a+\tfrac12\Big)\ \Rightarrow\ -(a^{\dagger}a+\tfrac12)=-2K_0"]),
                    ]),
           ])

    # ---- VERIFY (independent checks, not used to derive) -------------------------------------
    d.verify(
        r"Two independent checks via the engine's `oscillator_commutator` (sympy normal ordering, nothing "
        r"written in): the su(1,1) triple closes — $[K_0,K_\pm]=\pm K_\pm$, $[K_+,K_-]=-2K_0$ (matches the "
        r"standard bosonic realization); and the Jordan-Schwinger map $t_i{}^j=a^\dagger_i a_j$ reproduces the "
        r"paper's gl(k) relation $[t_1{}^2,t_2{}^1]=t_1{}^1-t_2{}^2$ (arXiv:2606.24008, Table 1).",
        math=[r"[K_+,K_-]=-2K_0,\quad [K_0,K_\pm]=\pm K_\pm\quad(\text{su}(1,1))",
              r"[t_1{}^2,t_2{}^1]=t_1{}^1-t_2{}^2\quad(\text{Jordan-Schwinger }gl(k))"],
        references=["engine: special_methods.oscillator_commutator (canonical [a,a†]=1 + normal ordering)",
                    "Jordan-Schwinger transformation — independent published gl(k) realization",
                    "arXiv:2606.24008 Table 1 / so(k,k) — the paper's constraint superalgebra"])
    d.result(
        latex=r"[K_+,K_-]=-2K_0,\qquad K_0=\tfrac12\Big(a^{\dagger}a+\tfrac12\Big),\ "
              r"K_\pm=\tfrac12a^{(\dagger)2}\quad(\text{su}(1,1)\text{ closes})",
        note="commutator derived from [a,a†]=1 by normal ordering (nothing written in); the same engine "
             "reproduces the paper's Jordan-Schwinger gl(k) table entry. Opens operator-algebra (Cat A/C) of "
             "arXiv:2606.24008; BRST nilpotency + Verma realizations remain as rounded-up gaps.")
    return d
