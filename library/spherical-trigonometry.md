---
id: spherical-trigonometry
name: Spherical trigonometry — the spherical law of cosines
domain: trigonometry
regime: trig
status: drafted
---

## Applies when (recognition signature)
Distances or angles on a sphere, not a plane — navigation, geodesy, astronomy, or any
triangle whose sides are arcs of great circles. Tells: "great-circle distance",
"latitude/longitude", "bearing", a triangle on a globe, sides measured as angles
(radians) rather than lengths, the breakdown of the flat Pythagorean rule.

## The rule
On a unit sphere a triangle has vertices joined by great-circle arcs; its **sides**
`a, b, c` are themselves angles (the arc subtended at the centre) and its **angles**
`A, B, C` are the dihedral angles at the vertices. The spherical law of cosines for
sides is
`cos c = cos a cos b + sin a sin b cos C`,
with `C` the angle opposite side `c`. As all the sides shrink (`a,b,c → 0`),
`cos ≈ 1 − ½(·)²` and `sin ≈ (·)` recover the planar `c² = a² + b² − 2ab cos C`. On a
sphere of radius `R`, a physical arc length `s` corresponds to the angle `s/R`.

## Worked example
Great-circle distance between two points given as latitude/longitude
`(φ₁,λ₁)`, `(φ₂,λ₂)`. Form the spherical triangle with vertices the North Pole `P` and
the two points. The two sides from `P` are the colatitudes `a = 90°−φ₁`,
`b = 90°−φ₂`, and the included angle at `P` is the longitude difference
`C = λ₂−λ₁`. The third side `c` is the angular separation. The law of cosines gives,
using `cos(90°−φ)=sin φ` and `sin(90°−φ)=cos φ`,
`cos c = sin φ₁ sin φ₂ + cos φ₁ cos φ₂ cos(λ₂−λ₁)`,
and the distance is `R c` with `c = arccos(·)` (e.g. `R = 6371 km` for Earth). This is
the standard spherical-law-of-cosines distance formula (Smart, *Spherical Astronomy*, ch. 1).

## Explain (altitudes)
- **expert** — the identity is the unit-sphere instance of the metric geometry of a
  space of constant positive curvature; writing each vertex as a unit vector, it is the
  dot-product `cos c = u·v` re-expressed through the two colatitude vectors and the
  azimuthal angle between them, i.e. a rotation composition in SO(3).
- **working** — place unit vectors to the three vertices; the cosine of an arc is the
  dot product of its endpoints. Expanding `u·v` with the colatitudes and the longitude
  gap between the two vectors gives `cos c = cos a cos b + sin a sin b cos C` directly.
- **plain** — on a globe you can't use the flat triangle rules. Sides are measured as
  angles from the centre, and this formula plays the role of the cosine rule, letting
  you turn two latitudes and a longitude gap into the true over-the-surface distance.

## LaTeX
rule: \cos c=\cos a\,\cos b+\sin a\,\sin b\,\cos C
example: \cos c=\sin\varphi_{1}\sin\varphi_{2}+\cos\varphi_{1}\cos\varphi_{2}\cos\!\left(\lambda_{2}-\lambda_{1}\right),\quad d=R\,c

## References
- Smart, *Textbook on Spherical Astronomy*, ch. 1.
- Todhunter, *Spherical Trigonometry*, §§37–40.
- Library: `astropy.coordinates` angular separation; or NumPy with the haversine form for small `c`.
- Worked example: Smart ch. 1 (pole–point–point triangle, lat/long distance).

## Links
[[cosine-rule]] · [[dot-product]] · [[cross-product]] · [[pythagorean-identity]]
