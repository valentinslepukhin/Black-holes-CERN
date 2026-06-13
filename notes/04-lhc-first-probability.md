# P(LHC traps first): the quantified "nature never ran this experiment" window

> **⚠ UPDATE (post G&M comparison, see [05-comparison-giddings-mangano.md]):**
> the A/B μ_LHC values below are wrong by orders of magnitude. G&M App. F shows
> (i) 1/v accretion drag lets Earth trap BHs born up to v_max ≈ 8–25× v_esc, and
> (ii) the slow tail is ~linear (flat rapidity), not cubic. Their Table 12 gives
> P_trap ~ 10⁻⁵–10⁻³, and expected trapped > 1 for M ≲ 5–7 TeV (Fig. 12).
> The joint "LHC-first" probability for case A/B is therefore **~certainty for
> light BHs at D ≥ 8**, not ~3%. The structural conclusion (C/D impossible;
> A/B is the open channel, closed only by slowness + WD/NS) is unchanged — in
> fact strengthened: G&M never rely on capture being improbable.

*Layer 4: joint probability that cosmic rays trapped NO black hole in Earth+Sun
over 4.5 Gyr AND the LHC traps ≥ 1 within 50 years — for Earth and Sun as the
LHC-capture target. Calculation: `analysis/lhc_first_capture.py`.*

Poisson: P = e^(−μ_nat) · (1 − e^(−μ_LHC)). Conditional on TeV gravity +
production (f_BH = 10⁻⁸) + absolute stability. 50 yr ⇒ N_BH = 4.8×10⁹.

| Case | μ_nat (E+S, 4.5 Gyr) | μ_LHC Earth | μ_LHC Sun | **Joint, Earth** | **Joint, Sun** |
|---|---|---|---|---|---|
| A gravity only | **exactly 0** | 0.031 | 0.014 | **3.1%** | **1.4%** |
| B + weak | **exactly 0** | 0.031 | 0.014 | **3.1%** | **1.4%** |
| C + strong | 3×10¹⁸ | 2.4×10⁹ | 1.3×10⁴ | **10^(−10¹⁸)** | 10^(−10¹⁸) |
| D + EM | 3×10¹⁸ | 4.8×10⁹ | ~0 | **10^(−10¹⁸)** | 10^(−10¹⁸) (zero twice) |

Why μ_nat = 0 *exactly* for A/B: even the most backward-emitted BH inherits
γ_lab ≳ 5×10³ (at production threshold the CM frame itself has γ = √(E_th/2m_p));
CR–CR collisions, the only way nature makes a slow CM, have negligible luminosity.

New physics worked out for the Sun column:
- **A/B bound-orbit channel:** BHs leaving Earth with |v_lab ⊕ 30 km/s| < 42 km/s
  stay solar-bound (~2 over 50 yr); the loss-cone fraction (v_⊥ < 2.9 km/s at 1 AU
  ⇒ perihelion < R_☉) is ~0.7%; once sun-grazing, accretion drag — now strong
  because the low-velocity focusing (c/v)^(4/(n+1)) finally bites — decays the
  orbit into the Sun in ~10²–10³ yr. μ ≈ 0.014. The same velocity dependence that
  makes fast CR BHs untrappable makes slow bound ones sink: complementarity again.
- **C:** the upward-escaping half (β ≈ 0.19) hits the Sun with solid-angle
  fraction 5.4×10⁻⁶ → ~10⁴ stuck in the Sun. Irrelevant: joint already zero.
- **D:** none ever leave the Geneva rock → Sun clause fails too.

## Findings
**7 — The LHC-first window exists only where capture is harmless.** For C/D the
joint event is not merely improbable but *logically dead* (μ_nat ~ 10¹⁸): one cannot
coherently assert "such BHs exist" and "Earth/Sun intact". For A/B the window is
genuinely open — ~3% (Earth), ~1% (Sun) — but these are precisely the scenarios
where a captured BH eats 0.1 g per age-of-Earth (n ≥ 4) or ≥ 25 Gyr (n = 3). The
*dangerous* joint event requires additionally n ≤ 3: P ≈ 3% × P(n ≤ 3 | TeV gravity),
and n ≤ 3 is what the WD/NS argument excludes. The audit target does not move.

**8 — Sensitivity is all in f_BH** (linear in μ_LHC): joint(A, Earth) runs from
0.03% (f_BH = 10⁻¹⁰) to 95% (10⁻⁶). Any honest artifact must display this slider:
the "3%" is conditional shorthand, not a fact about the world.

## Caveats log
- Bound-orbit estimate is the crudest number (phase-space tail × loss cone, each OOM):
  Sun column could be 0.1–3%. Earth column is cleaner (pure kinematic tail).
- A/B Sun capture completes ~10²–10³ yr after the production window (orbital decay).
- Loss-cone refill vs Jupiter ejection on Myr scales: competing, OOM wash.
- Poisson independence of the two clauses is exact here (disjoint populations).
