---
id: zeta-regularization
name: Zeta-function regularization of divergent sums
domain: asymptotics
regime: resummation
status: verified
---

## Applies when (recognition signature)
You meet a **divergent sum of the form `Σ n^{−s}`** (or that can be massaged into
one) evaluated outside its region of convergence, and you want the
**finite regularized value**. Tells: `Σ n`, `Σ n²`, `Σ 1` "= ζ(0)", "1+2+3+… = −1/12",
Casimir energy, vacuum-energy / string normal-ordering constants, "regularize this
divergent sum", `ζ(−1)`, `ζ(0)`. The divergent expression is reinterpreted as the
analytic continuation of `ζ(s)`.

## The rule
Define `ζ(s) = Σ_{n≥1} n^{−s}` for `Re s > 1`, then **analytically continue** to the
whole `s`-plane (one simple pole at `s=1`). The regularized value of a formally
divergent sum is its value at the continued argument. Standard data:
`ζ(0) = −1/2`,  `ζ(−1) = −1/12`,  `ζ(−2k) = 0` (`k ≥ 1`),  `ζ(−(2k−1)) = −B_{2k}/(2k)`.
Equivalently via the functional equation `ζ(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ(1−s)`.

## Worked example
The Casimir/string value `1 + 2 + 3 + ⋯ "=" ζ(−1) = −1/12`. Setting the exponent
`s = −1` in the continued `ζ` (where `Σ n^{−s} = Σ n`) gives `−1/12`, matching
`−B_2/2 = −(1/6)/2`. This is the standard regularized sum behind the Casimir energy
and the 26-dimensional bosonic string. Verified with mpmath `zeta(-1)`.

## Explain (altitudes)
- **expert** — `ζ(s)` continues to a meromorphic function via the Riemann functional
  equation / Hermite or Abel–Plana integral; `ζ(−n)` reads off Bernoulli numbers, and
  the continuation is the canonical scheme-independent finite part of the divergent sum.
- **working** — the sum only converges for `Re s > 1`, but the function it defines can
  be extended smoothly to other `s`; the regularized value of `Σ n` is just that
  extended function evaluated at `s = −1`, namely `−1/12`.
- **plain** — you can't add up `1+2+3+…` directly, but there's a single natural curve
  that passes through all the values you *can* add, and following it back gives the
  finite number `−1/12`.

## LaTeX
rule: \zeta(s)=\sum_{n=1}^{\infty}n^{-s}\ (\operatorname{Re}s>1)\ \xrightarrow{\text{analytic continuation}}\ \zeta(0)=-\tfrac12,\quad \zeta(-1)=-\tfrac{1}{12}
example: 1+2+3+\cdots\;\overset{\zeta}{=}\;\zeta(-1)=-\frac{1}{12}
## References
- DLMF 25.2 (definition), 25.4 (functional equation), 25.6 (`ζ(−n)` and Bernoulli numbers).
- Hardy, *Divergent Series*, ch. XIII; Elizalde, *Ten Physical Applications of Spectral Zeta Functions*.
- Library: mpmath `zeta`, SymPy `zeta`.
- Worked example: Casimir sum `ζ(−1) = −1/12`, standard (Elizalde §1).

## Links
[[euler-maclaurin]] · [[gamma-function]] · [[abel-plana]] · [[mellin-barnes]] · [[polylogarithm]]
