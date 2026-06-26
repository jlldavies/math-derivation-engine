---
id: greens-function
name: Green's function — invert a linear operator with a point source
domain: pde
regime: pde
status: drafted
---

## Applies when (recognition signature)
A linear inhomogeneous problem `L u = f` (ODE or PDE) with homogeneous BCs, and
you want the solution for *arbitrary* forcing `f`. Tells: "fundamental solution",
"response to a point source", `δ(x−ξ)`, "impulse response", an integral
`u = ∫ G f` against a kernel; boundary-value problems for `−u''`, `∇²`, the
Helmholtz operator.

## The rule
Solve the operator against a unit point source: `L_x G(x,ξ) = δ(x−ξ)` with the
same homogeneous BCs. Then for any `f`,
`u(x) = ∫ G(x,ξ) f(ξ) dξ`, because `L` is linear and `f(x) = ∫ δ(x−ξ) f(ξ) dξ`.
`G` is continuous in `x` at `x=ξ` but its derivative jumps by `1/p(ξ)` (from the
leading coefficient), which fixes the matching constants.

## Worked example
`−u'' = f` on `[0,1]`, `u(0)=u(1)=0`. Build `G` from solutions vanishing at each
end (`x` and `1−x`), matched at `x=ξ` with a unit derivative jump:
`G(x,ξ) = x(1−ξ)` for `x<ξ` and `ξ(1−x)` for `x>ξ`. Then
`u(x) = ∫_0^1 G(x,ξ) f(ξ) dξ`. Standard result (Stakgold, *Green's Functions and
Boundary Value Problems*, §1).

## Explain (altitudes)
- **expert** — `G` is the kernel of `L^{−1}` on the BC-constrained domain; the
  delta-source jump condition is the distributional content of `L G = δ`, and
  symmetry `G(x,ξ)=G(ξ,x)` reflects self-adjointness.
- **working** — find two homogeneous solutions satisfying the left and right BCs,
  glue them at `x=ξ` so `G` is continuous but `G'` jumps by `−1/p`; convolve `G`
  against `f` to get `u`.
- **plain** — first solve for a single sharp poke at one spot. Any push is just a
  sum of pokes, so smear that one-poke answer across the whole push and add it up.

## LaTeX
rule: L_x\,G(x,\xi)=\delta(x-\xi)\ \Rightarrow\ u(x)=\int G(x,\xi)\,f(\xi)\,d\xi
example: G(x,\xi)=\begin{cases}x(1-\xi),&x<\xi\\[2pt]\xi(1-x),&x>\xi\end{cases}

## References
- Stakgold & Holst, *Green's Functions and Boundary Value Problems*, §1.
- Arfken & Weber, *Mathematical Methods for Physicists*, ch. 10.
- Library: SymPy (solve homogeneous pieces + match); SciPy for numeric kernels.
- Worked example: Stakgold §1 (`−u''` on the unit interval).

## Links
[[laplace-equation]] · [[sturm-liouville]] · [[fourier-transform]]
