---
id: gamma-reflection
name: Euler reflection formula for the Gamma function
domain: special-function
regime: special-function
status: verified
---

## Applies when (recognition signature)
A product `Γ(s)Γ(1−s)`, a Gamma at a half-integer, or a `1/sin(πs)` factor you
want to trade for Gammas. Tell: arguments summing to `1`, ratios of Gammas across
the critical line, or evaluating `Γ(1/2)`.

## The rule
**Euler reflection:** `Γ(s)Γ(1−s) = π / sin(πs)` for non-integer `s`. It relates
`Γ` at `s` and `1−s`, exposes the simple poles of `Γ` at the non-positive integers
(from the zeros of `sin`), and underlies functional equations (e.g. the zeta
reflection).

## Worked example
At `s = 1/2`: `Γ(1/2)Γ(1/2) = π / sin(π/2) = π`, so `Γ(1/2)² = π` and
`Γ(1/2) = √π` (positive root). (Known result, consistent with the Gaussian
integral.)

## Explain (altitudes)
- **expert** — it follows from the Weierstrass product for `1/Γ` together with the
  product formula `sin(πs) = πs ∏(1 − s²/n²)`; equivalently from the Beta-function
  integral `B(s,1−s) = ∫_0^∞ t^{s−1}/(1+t) dt = π/sin(πs)`.
- **working** — pair `Γ(s)` with `Γ(1−s)` via the Beta integral, evaluate that
  rational integral by contour/residues to get `π/sin(πs)`, then read off special
  values like `Γ(1/2)`.
- **plain** — the Gamma function (factorial, extended) has a mirror symmetry: its
  values at `s` and `1−s` multiply to a tidy `π/sin`. Setting `s = 1/2` lands you
  exactly halfway and gives `√π`.

## LaTeX
rule: \Gamma(s)\,\Gamma(1-s)=\frac{\pi}{\sin(\pi s)}
example: \Gamma\left(\tfrac{1}{2}\right)^{2}=\frac{\pi}{\sin(\pi/2)}=\pi\ \Rightarrow\ \Gamma\left(\tfrac{1}{2}\right)=\sqrt{\pi}

## References
- Euler reflection formula — Whittaker & Watson §12.14; Abramowitz & Stegun 6.1.17.
- Library: SymPy `gamma`, `reflection`; verify with mpmath.

## Links
[[gamma-function]] · [[beta-function]] · [[contour-residues]]
