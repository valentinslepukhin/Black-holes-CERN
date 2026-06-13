# Fate of collider-produced black holes (cases A–D)

*Layer 3: same four interaction hypotheses, but production at the LHC, where the
lab frame ≈ CM frame. Calculation: `analysis/lhc_bh_fate.py`.*

## Setup
A 10 TeV BH at √s = 14 TeV needs x₁x₂ ≳ 0.5 → x₁ ≈ x₂ ≈ 0.7: born **slow**,
β_typ ~ 0.2 (parton imbalance + recoil), slow tail modeled as P(β<x) = (x/0.2)³.
N_BH over the HL-LHC program: ~2.4×10⁹ (f_BH ~ 10⁻⁸; all counts ∝ f_BH).
The ring sits ~100 m underground.

## Capture (the inversion of the cosmic-ray case)

| Case | Stopping in Earth | P(capture) | Expected trapped |
|---|---|---|---|
| A gravity only | impossible (10²¹ g/cm² needed) | P(born β<β_esc) = 6.5×10⁻¹² | **0.016 — likely zero ever** |
| B + weak | impossible (≳10¹⁸ g/cm² at low β) | same slow-tail only | **0.016** |
| C + strong | 3.8×10⁶ g/cm² ≈ 14 km rock | downward ½: yes; **upward: escapes to space at β≈0.19** (only 0.13 e-folds shed in 100 m rock + atmosphere) | **~1.2×10⁹** |
| D + EM | range ~8×10³ g/cm² ≈ 30 m rock at β=0.2 (Bethe ∝ 1/β²) | stops in the cavern wall in any direction | **~2.4×10⁹** |

Note the exact mirror of the cosmic-ray table: the cases nature *couldn't* trap
(A, B) the LHC *also* can't trap (born-slow tail ~10⁻¹¹); the cases the LHC traps
copiously (C, D) nature has already trapped 10⁵× more of, for 10⁸× longer.
Curiosity: ~4 case-A/B BHs would end up in bound solar orbits (lab speed ⊕ Earth's
30 km/s < 42 km/s solar escape) — harmless Earth-crossing orbiters.

## Consumption
Identical to Part 3 (arrival mode irrelevant once at rest): dangerous only for
n ≤ 2 (excluded by gravity tests + WD), marginal at n = 3 (25 Gyr), absurdly slow
for n ≥ 4 (a trapped n=6 BH eats 0.1 g per age-of-Earth; all 10⁹ case-C LHC BHs
together: ~150 t per 4.5 Gyr).

## Risk closure by case
- **C, D — closed empirically by Earth/Sun.** Nature's resident population
  (10¹⁴ Earth / 3×10¹⁸ Sun) with a 4.5 Gyr head start: any accretion fast enough
  to matter would have consumed Earth ~40,000× over (n=2 clock). The LHC raises
  exposure by ~10⁻⁵, with zero new physics dependencies.
- **A, B — NOT closed by Earth/Sun (Part 3), and not closed by counting either:**
  the statement "expected trapped = 0.016" is probabilistic (98–99% chance the
  program traps none), not an exclusion. The safety case for the genuinely
  dangerous configuration (neutral, gravity-only, stable, n = 3–4) is a chain:
  1. no Hawking radiation (assumed away, worst case),
  2. born-slow tail ~10⁻¹¹ → ~10⁻² expected captures (phase-space model — *audit
     the β-spectrum*; G&M computed it properly),
  3. even if captured: accretion ≥ 10 Gyr at n = 3 (our model; *Eddington/atomic
     physics could shift either way*),
  4. independent exclusion of n = 3–4 from white-dwarf/neutron-star survival.
  Links 2–4 are each individually strong but all are *calculations*, not
  observations. In Ord–Hillerbrand–Sandberg terms: P(disaster) is dominated not
  by these small numbers but by P(all three calculations are wrong in correlated
  ways). This is the irreducible core of the LHC black-hole question.

## Assumptions log (this layer)
- β_typ = 0.2 and the cubic slow-tail are kinematic estimates; the real BH
  velocity spectrum from parton luminosities is the right input (G&M App. — check).
- Charged-BH range uses Bethe with 1/β² scaling from MIP; Lindhard regime
  corrections at β ≲ 0.01 irrelevant (already stopped).
- Case-C upward escape assumes no large-angle hard scatters reversing it (OOM fine).
- f_BH ~ 10⁻⁸ cancels in all nature-vs-LHC *ratios* — the closure arguments are
  composition-independent except through Part 1's iron caveat (factor 17 vs 10⁵ on Earth;
  Sun restores 10⁵).
