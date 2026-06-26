"""metric -> curvature tensors: the reusable Christoffel -> Riemann -> Ricci -> Einstein
pipeline, promoted from code we hand-wrote five times (Bondi, D'Inverno 6.31, the 2-sphere,
flat-space checks). The engine executes; the agent supplies the metric and reads the result.

D'Inverno conventions (validated against his Answers, ch.6):
    Gamma^a_bc = 1/2 g^ad (d_b g_dc + d_c g_db - d_d g_bc)
    R^a_bcd    = d_c Gamma^a_bd - d_d Gamma^a_bc + Gamma^a_ce Gamma^e_bd - Gamma^a_de Gamma^e_bc
    R_bd       = R^a_bad                         (Ricci: contract 1st & 3rd)
    R          = g^bd R_bd
    G_ab       = R_ab - 1/2 R g_ab

LESSON BAKED IN: `is_zero`/`equal` use structural -> trig+radical simplify -> numeric
spot-check, so the false "MISMATCH" class (un-simplified nested radicals / trig: D'Inverno
6.22, 8.11) cannot recur. Always compare tensors with `equal`, never bare `== 0`.
"""
import sympy as sp


def is_zero(expr):
    """Robust 'is this expression identically zero?'.

    Order: cheap structural test -> simplify(trigsimp(radsimp(.))) -> high-precision
    numeric spot-check at random rational points (only when every free symbol is a plain
    Symbol, i.e. no undefined functions like nu(t,r)). Returns a definite bool."""
    expr = sp.sympify(expr)
    if expr == 0:
        return True
    s = sp.simplify(sp.trigsimp(sp.radsimp(sp.expand(expr))))
    if s == 0:
        return True
    # Polynomial-in-derivatives with rational-function coefficients (e.g. a geodesic
    # equation): replace each Derivative / undefined-function atom with a fresh symbol so
    # the whole thing becomes an ordinary expression the checks below can settle.
    if expr.atoms(sp.Derivative) or expr.atoms(sp.core.function.AppliedUndef):
        # Replace Derivatives FIRST as whole nodes (xreplace is bottom-up, so doing this in
        # one pass with the bare functions would rewrite r(s) inside Derivative(r(s),s) and
        # collapse it to 0). Then the remaining functions. Result: an ordinary expression.
        e = expr.xreplace({d: sp.Dummy() for d in expr.atoms(sp.Derivative)})
        e = e.xreplace({fn: sp.Dummy() for fn in e.atoms(sp.core.function.AppliedUndef)})
        return is_zero(e)
    syms = s.free_symbols
    if syms and not s.atoms(sp.core.function.AppliedUndef):
        # deterministic spot-check: a few coprime-ish rational points in (0, 1)
        pts = [sp.Rational(p, q) for p, q in ((3, 10), (2, 7), (5, 11), (1, 3))]
        ok = True
        for k in range(3):
            sub = {sym: pts[(k + i) % len(pts)] for i, sym in enumerate(sorted(syms, key=str))}
            try:
                val = sp.N(s.subs(sub), 30)
            except (TypeError, ValueError):
                ok = False
                break
            if val == sp.nan or abs(val) > sp.Float("1e-20"):
                ok = False
                break
        if ok:
            return True
    return False


def equal(a, b):
    """True iff a and b are the same expression OR the same matrix/tensor (element-wise,
    robust; see `is_zero`). Handles the matrix-valued claims that pervade GR (metrics,
    inverses, Einstein tensor)."""
    a, b = sp.sympify(a), sp.sympify(b)
    if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
        a, b = sp.Matrix(a), sp.Matrix(b)
        return a.shape == b.shape and all(is_zero(a[i] - b[i]) for i in range(len(a)))
    return is_zero(a - b)


class Curvature:
    """All curvature tensors of a metric, lazily computed and cached.

    g : sympy Matrix (n x n) ; coords : list of n coordinate Symbols.
    Indices are 0-based. Christoffel/Riemann are nested lists; Ricci/Einstein are Matrices."""

    def __init__(self, g, coords, simplify=True):
        self.g = sp.Matrix(g)
        self.x = list(coords)
        self.n = len(self.x)
        self.gi = self.g.inv()
        self._simp = (lambda e: sp.simplify(e)) if simplify else (lambda e: e)
        self._G = self._R = self._Rlo = self._Ric = self._Rs = None

    # ---- Christoffel Gamma^a_bc -------------------------------------------------
    @property
    def christoffel(self):
        if self._G is None:
            n, g, gi, x, S = self.n, self.g, self.gi, self.x, self._simp
            self._G = [[[S(sum(gi[a, d] * (sp.diff(g[d, b], x[c]) + sp.diff(g[d, c], x[b])
                        - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
                        for c in range(n)] for b in range(n)] for a in range(n)]
        return self._G

    # ---- Riemann R^a_bcd and R_abcd --------------------------------------------
    @property
    def riemann(self):
        if self._R is None:
            n, G, x, S = self.n, self.christoffel, self.x, self._simp
            self._R = [[[[S(sp.diff(G[a][b][d], x[c]) - sp.diff(G[a][b][c], x[d])
                         + sum(G[a][c][e] * G[e][b][d] - G[a][d][e] * G[e][b][c] for e in range(n)))
                         for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
        return self._R

    @property
    def riemann_lower(self):
        if self._Rlo is None:
            n, g, R, S = self.n, self.g, self.riemann, self._simp
            self._Rlo = [[[[S(sum(g[a, e] * R[e][b][c][d] for e in range(n)))
                          for d in range(n)] for c in range(n)] for b in range(n)] for a in range(n)]
        return self._Rlo

    # ---- Ricci R_bd = R^a_bad, scalar, Einstein --------------------------------
    @property
    def ricci(self):
        if self._Ric is None:
            n, R, S = self.n, self.riemann, self._simp
            self._Ric = sp.Matrix(n, n, lambda b, d: S(sum(R[a][b][a][d] for a in range(n))))
        return self._Ric

    @property
    def ricci_scalar(self):
        if self._Rs is None:
            n, gi, Ric = self.n, self.gi, self.ricci
            self._Rs = self._simp(sum(gi[b, d] * Ric[b, d] for b in range(n) for d in range(n)))
        return self._Rs

    @property
    def einstein(self):                          # G_ab
        Ric, R, g = self.ricci, self.ricci_scalar, self.g
        return sp.Matrix(self.n, self.n, lambda a, b: self._simp(Ric[a, b] - R * g[a, b] / 2))

    @property
    def einstein_mixed(self):                    # G^a_b
        return sp.Matrix(self._simp(self.gi * self.einstein))

    def is_flat(self):
        R = self.riemann
        return all(is_zero(R[a][b][c][d]) for a in range(self.n) for b in range(self.n)
                   for c in range(self.n) for d in range(self.n))

    def is_ricci_flat(self):                     # vacuum Einstein eqn
        Ric = self.ricci
        return all(is_zero(Ric[a, b]) for a in range(self.n) for b in range(self.n))

    def geodesic_equations(self, param="s"):
        """The geodesic ODEs  d2x^a/ds2 + Gamma^a_bc dx^b/ds dx^c/ds = 0, with each
        coordinate promoted to a function of the affine parameter. Auto-generated from the
        metric alone — no hand-derivation."""
        s = sp.Symbol(param)
        f = [sp.Function(str(self.x[a]))(s) for a in range(self.n)]
        sub = {self.x[a]: f[a] for a in range(self.n)}
        d = [sp.diff(f[a], s) for a in range(self.n)]
        G = self.christoffel
        return [sp.Eq(sp.diff(f[a], s, 2)
                      + sum(G[a][b][c].subs(sub) * d[b] * d[c]
                            for b in range(self.n) for c in range(self.n)), 0)
                for a in range(self.n)]


def line_element(ds2, diffs, coords):
    """Build a metric matrix from a line element. `ds2` is the quadratic form in the
    differential symbols `diffs` (e.g. dt, dr, ...); `coords` the matching coordinates.
    Lets a user type ds^2 the way a textbook prints it instead of hand-assembling g_ab."""
    ds2 = sp.expand(ds2)
    n = len(diffs)
    g = sp.zeros(n, n)
    for a in range(n):
        g[a, a] = ds2.coeff(diffs[a], 2)
        for b in range(a + 1, n):
            g[a, b] = g[b, a] = ds2.coeff(diffs[a], 1).coeff(diffs[b], 1) / 2
    return Curvature(g, coords)


def audit(pairs):
    """Declarative checker. `pairs` = [(label, computed, expected), ...]; prints
    MATCH/MISMATCH via `equal` and returns (n_match, mismatches). This is the replacement
    for hand-written per-exercise drivers: state the CLAIM, let the engine check it."""
    nmatch, bad = 0, []
    for label, got, want in pairs:
        good = equal(got, want)
        print(("MATCH   " if good else "MISMATCH"), label)
        if good:
            nmatch += 1
        else:
            bad.append((label, sp.simplify(got), sp.simplify(want)))
    return nmatch, bad
