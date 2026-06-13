# The cosmic-ray argument, decomposed

*Independent re-derivation (order-of-magnitude) of the empirical safety argument for
LHC black holes, with its dependency structure made explicit.
Calculations: `analysis/cosmic_ray_flux.py`, `analysis/bh_earth_passage.py`.*

## Part 1 — Nature's collision count at LHC energies

**Kinematics.** CR nucleus (energy E, mass number A) on an atmospheric nucleon:
√s per nucleon pair = √(2(E/A)m_p). Matching √s = 14 TeV requires
**E = 1.0×10¹⁷ eV** per nucleon.

| Quantity | Protons | Iron (worst case) |
|---|---|---|
| Threshold lab energy | 1.0×10¹⁷ eV | 5.9×10¹⁸ eV |
| Rate on Earth's atmosphere | ~1.8×10⁵ /s | ~30 /s |
| Events over Earth's 4.5 Gyr | **2.5×10²²** | 4.2×10¹⁸ |
| Ratio to full LHC program (2.4×10¹⁷ collisions) | ~10⁵ | **~17** |
| Same, on the Sun | ~10⁹ | ~2×10⁵ |

Cross-check: our 2.5×10²² matches Giddings–Mangano (2008), who quote ~3×10²². ✓

**Finding 1 (weak point):** the popular "Earth has survived 10⁵ LHC programs" framing
silently assumes proton primaries. Under a pure-iron composition (allowed by
Auger Xmax data at these energies, which favor *mixed/heavy*), Earth alone gives only
a ~17× margin. The argument's real strength then comes from the Sun (×10⁴ area)
and other stars — a dependency on astronomical, not terrestrial, survival.

**Finding 2:** the comparison is *time-asymmetric*: LHC at design luminosity produces
~10⁹ collisions/s vs nature's ~10⁵/s on all of Earth. Nature wins only by integrating
over Gyr and over many bodies. (Relevant for "how fast would a disaster manifest" reasoning.)

**Boost at production:** the nucleon–nucleon CM frame moves with γ ≈ E/√s ≈ 7×10³.
A BH produced in such a collision enters Earth ultra-relativistically — hence Part 2.
At the LHC, by contrast, the lab *is* the CM frame: products can be slow. This
asymmetry is the entire reason the naive cosmic-ray argument has a hole in it.

## Part 2 — Does a cosmic-ray-produced BH escape Earth?

Setup: M = 10 TeV, γ₀ = 7.4×10³, escape requires staying above β_esc = 3.7×10⁻⁵.
Capture requires shedding ~30 e-folds of kinetic energy within one chord
(Earth diametric column: 7×10⁹ g/cm²).

| Case | Cross section / mechanism | Interactions per chord | Column needed to capture | Outcome on Earth |
|---|---|---|---|---|
| **A: gravity only** | σ = πr_H² ≈ 10⁻³³–10⁻³² cm² (n=2–6) | ~10–24 absorptions | ~10²¹ g/cm² (absorption only) | **Escapes** by ~11 orders |
| **B: + weak** | ν-like, σ ≈ 4×10⁻³³ cm² at γ₀M | ~10 (Earth ≈ 1 interaction length!) | ≳5×10¹³ g/cm² | **Escapes** with γ ~ 600 |
| **C: + strong** | σ ≈ 40 mb, λ = 7.5 cm | ~10⁸ available, ~10⁵ needed | 5×10⁶ g/cm² | **Trapped in ~9 km of rock** |
| **D: + EM (charge e)** | Bethe dE/dx ≈ 2 MeV/(g/cm²) | continuous | range 3.7×10¹⁰ g/cm² at γ₀ | **Escapes (marginal, ×5)**; trapped if γ < 1.4×10³ |

Available columns: Earth 7×10⁹ | Sun 2×10¹¹ | white dwarf ~10¹⁵ | neutron star ~10²¹ g/cm².

**Escape conditions (answer to the headline question):**
- A BH escapes Earth iff its stopping column exceeds ~7×10⁹ g/cm² — true for
  gravity-only (huge margin), weak (margin 10⁴), and charged BHs with γ ≳ 1400.
- Capture mechanics differ by case: absorption conserves momentum (E grows by m_p
  per nucleon eaten; capture needs ~2×10¹² absorptions vs ~10 available), while
  elastic scattering sheds fraction ~γm_p/M (relativistic) then ~2m_p/M (slow) per collision.
- Only a *strongly interacting* BH is stopped by Earth — and then Earth's own
  4.5 Gyr survival under 10²² cosmic-ray events applies **directly**. Same for slow charged BHs;
  fast charged ones are stopped by the Sun (and charge retention is itself doubtful — Schwinger
  discharge — but discharge physics is a theoretical cousin of Hawking emission, so the
  "no Hawking radiation" worst case arguably weakens it too: flag as correlated assumption).

**Finding 3 (the load-bearing step):** for the dangerous scenario (neutral,
gravity-only, stable BH), *nothing in the solar system stops cosmic-ray-produced ones*.
The empirical argument must migrate to white dwarfs / neutron stars. Our crude
absorption-only estimate gives a needed column ~10²¹ g/cm² — comparable to a NS radius
and *above* a WD radius. G&M close this gap with (i) enhanced low-velocity gravitational
elastic scattering off nuclei, (ii) BHs produced *inside* NS by cosmic-ray neutrinos,
(iii) dimension-dependent analysis (WD stopping works for small n). **This is the most
delicate link in the entire safety case**: it depends on TeV-gravity stopping-power
modeling and on astrophysical assumptions (WD/NS ages, B-field screening of CRs at NS).
→ Next session: reproduce G&M's WD stopping calculation and its n-dependence.

## Dependency graph (this argument only)

```
"LHC BHs are safe (empirical branch, no Hawking assumption)"
├── requires: nature performs ≥ LHC-equivalent collisions  [✓ robust; ×17–×10⁵ on Earth,
│     └── caveat: composition at 1e17 eV (iron vs proton)     ×10⁵+ with Sun]
├── requires: CR-produced BHs end up captured SOMEWHERE observable
│     ├── strong-interacting BH  → Earth itself      [✓ robust, 9 km stopping]
│     ├── charged BH             → Sun, partly Earth [✓ modulo charge retention]
│     ├── weak-interacting BH    → WD / NS only      [depends on WD/NS modeling]
│     └── gravity-only BH        → WD / NS only      [WEAKEST LINK: n-dependent,
│                                                      needs G&M stopping analysis]
└── requires: captured-BH accretion would be observable (star destruction
      timescales < stellar ages)                     [next layer to audit]
```

## Assumptions log
- Spectrum: piecewise power law anchored at E³J(10¹⁸ eV) = 1.5×10²⁴ eV²m⁻²s⁻¹sr⁻¹; OOM only.
- σ_abs = πr_H² with O(1) factors dropped; partonic structure of nucleon ignored.
- Elastic energy loss: ⟨ΔE⟩ = W_max/2 (isotropic CM); real angular distributions differ.
- Earth treated as uniform mean density; diametric chord (worst case for escape).
- BH mass growth during traversal neglected for σ (grows ~M^{2/(n+1)}, ≤ ×60 effect).
