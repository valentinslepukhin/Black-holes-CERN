# Capture statistics and the accretion clock

*Layer 2 of the audit: given case A–D interaction hypotheses, how many cosmic-ray
BHs are resident in Earth/Sun after 4.5 Gyr, and how fast would a trapped one eat
its host? Calculation: `analysis/capture_and_accretion.py`.*

## (i) Expected number captured over 4.5 Gyr

(Scales linearly with f_BH ≈ σ_BH/σ_inel ~ 10⁻⁸; production-at-rest is kinematically
impossible since the CM frame itself moves with γ ≈ 7×10³.)

| Case | Earth | Sun |
|---|---|---|
| A (gravity only) | **0** | **0** |
| B (+ weak) | **0** | **0** |
| C (+ strong) | ~10¹⁴ (P_cap ≈ 1) | ~3×10¹⁸ |
| D (+ EM) | ~10¹³ (catches γ < 1.4×10³ tail) | ~3×10¹⁸ (stops all) |

**The asymmetry is the whole story.** For C/D, capture over geological history is a
*certainty*, in astronomical numbers — so Earth/Sun survival is a direct, overwhelming
empirical bound, and the LHC's ~10⁹ additional BHs are a 10⁻⁵ perturbation on what
nature already deposited. For A/B the expected count is identically ~zero: **the
survival of Earth and Sun carries no information whatsoever about the gravity-only
or weak-only scenarios.** Every gram of empirical weight for the *dangerous* case
rests on white dwarfs / neutron stars.

## (ii) Consumption clock (trapped BH at host center)

All cases share gravitational accretion; strong adds only a QCD-fixed 40 mb channel
(12 mg per 4.5 Gyr — σ does not grow with M), EM neutralizes immediately. The speed
is set by n (extra dimensions) through the reach of the steep potential, b_c ~
r_H(c/v)^{2/(n+1)} capped at R_extra, then 4D Bondi. Flat ADD, M_D = 1 TeV, no
Eddington throttling (fast times are lower bounds):

| n | R_extra | Earth: M(4.5 Gyr) | Earth: consume | Sun: M(4.5 Gyr) | Sun: consume |
|---|---|---|---|---|---|
| 1 | 3×10¹³ m | — | ~ms (excluded flat) | — | ~0.1 s (excluded) |
| 2 | 2.4 mm | — | **120 kyr** | — | **2.3 Myr** |
| 3 | 10 nm | 1.5 Mt | **25 Gyr (marginal!)** | 83 Mt | 470 Gyr |
| 4 | 22 pm | 56 kg | 10⁴ Gyr | 24 t | 2×10⁵ Gyr |
| 5 | 0.5 pm | 16 g | ≫ Hubble | 12 kg | ≫ Hubble |
| 6 | 45 fm | 0.1 g | ≫ Hubble | 130 g | ≫ Hubble |
| 7 | 8 fm | 5 mg | ≫ Hubble | 6 g | ≫ Hubble |

**Finding 4 — the complementarity that makes G&M work:** accretion is dangerous only
for small n (long-reach steep potential), but small n is *also* when stopping power is
large, so cosmic-ray BHs get trapped in white dwarfs and the WD-survival bound bites.
Large n escapes the WD bound but accretes absurdly slowly (a trapped n=6 BH eats
~0.1 g in the age of the Earth). Danger and empirical testability switch on together.
**The pivot of the entire safety case is the middle, n ≈ 3–4 (D = 7–8), where Earth
consumption times are ~10–10⁴ Gyr** — uncomfortably finite — and one must check that
the WD/NS argument still covers exactly this window. (G&M's paper does claim this;
auditing their D = 7–8 stopping/accretion sections is the highest-value next step.)

**Finding 5 — empirical inversion (model-independent):** *given* capture (case C),
host survival bounds per-BH accretion: < 1.7×10⁻⁷ kg/s (Earth, 10¹⁴ residents),
< 5×10⁻⁶ kg/s (Sun). No accretion theory needed — a clean bound to feature in the artifact.

**Finding 6 — even the LHC traps almost nothing in the dangerous case:** gravity-only
BHs produced at the LHC have β ~ 0.1–0.3; P(β < β_esc) ~ 10⁻¹¹ → expected trapped
over the whole program ≪ 1. The doomsday scenario requires *both* the no-Hawking
worst case *and* conditioning on a ~10⁻²-probability slow-production tail. (Caveat:
multi-BH production tails, BH production spectrum shape — quote G&M's own number here.)

## Assumptions log (this layer)
- f_BH ~ 10⁻⁸ per inelastic collision (σ_BH ~ 1 nb at M_D = 1 TeV); all counts ∝ f_BH.
- Steep-potential capture radius with O(1) factors dropped; lattice binding (~eV)
  gives the same OOM cap as thermal KE (~0.05 eV) — checked, factor 34 vs 38 for n=6.
- No radiation-pressure throttling: G&M's Eddington-limited phases lengthen the
  fast (n ≤ 2) times to ~Myr–Gyr; does not change which n are dangerous. VERIFY vs paper.
- Case-D Earth capture fraction 0.1 is a rapidity-tail estimate; refine from
  production spectra if it ever becomes load-bearing (it isn't: Sun catches all).
- Endgame (final M_body/2 → M_body collapse dynamics) not modeled; irrelevant to timescales.
