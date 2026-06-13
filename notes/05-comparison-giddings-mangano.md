# Diff: our independent re-derivation vs. Giddings–Mangano (arXiv:0806.3381v2)

*Layer 5: verification against the primary source (PDF in `sources/`, 97 pp).
Read directly: §4.5–4.6 (pp. 27–28), §5.3.2 + Table 1 + Figs. 1–2 (pp. 35–37),
§7.4–8.1 (pp. 44–45), §9 conclusions (pp. 50–53), App. F + Tables 11–12 + Fig. 12
(pp. 79–83). WebFetch summaries were used for orientation only — one of them
mis-stated the D=7 Earth time and the WD stopping direction; the PDF settles both.*

## 1. Validations (ours vs. theirs)

| Quantity | Ours | G&M | Verdict |
|---|---|---|---|
| CR threshold | E = 1.04×10¹⁷ eV (×A) | E_min(A) = A·E²_LHC/2m_p ~ 10¹⁷A eV (§5) | identical formula ✓ |
| Collisions on Earth, 4.5 Gyr, protons | 2.5×10²² | ~10²² (eq. 5.2) | ✓ |
| LHC program collisions | 2.4×10¹⁷ | ~10⁹/s × 10⁸ s = 10¹⁷ | ✓ |
| Min boost of CR-made BH | γ ≥ M/2m_p ≈ 5300, **exactly zero slow tail** | E₁ > M²/2m_p (§5.1, App. F) | identical ✓ |
| Neutral BH energy loss crossing Earth | ~10 nucleons absorbed | "accretion of at most a few GeV" over δ_E = 1.1×10¹⁰ g/cm² (App. F) | ✓ |
| Charged BH: Earth stops | M = 10 TeV iff γ < 1.4×10³ | up to ~7 TeV at γ ~ 10³ (§2) | ✓ within ×1.5 |
| Charged BH: Sun stops | all (γ ≲ 4×10⁴) | "well in excess of 100 TeV" | ✓ |
| Earth accretion, D=6 | 1.2×10⁵ yr | ~tens of kyr (§9; eq. 4.49) | ✓ factor ~2 |
| Earth accretion, D=7 | 25 Gyr | **6–80 Gyr** (§4.6) | ✓ inside their range |
| Earth accretion, D≥8 | 10⁴ Gyr → ≫Hubble | ≳10¹¹ yr; BH still <Mt after 10¹¹ yr | ✓ same conclusion |
| LHC→Sun direct geometry | 5.4×10⁻⁶ (full disk) | 2.2×10⁻⁷ (core, 0.2 R_☉) | ✓ exactly: ×(0.2)² |
| Schwinger ⇔ Hawking correlation | flagged as correlated assumption | "no concrete framework where neutralization occurs without Hawking decay" (§1) | ✓ confirmed, stronger |
| Eddington throttle | omitted, flagged | **no Eddington limit found** (§4.5; spherical accretion radiatively inefficient); if one existed, t_Edd ≈ 2.3η×10⁸ yr | our omission was their conservative choice ✓ |
| Danger↔testability complementarity | our Finding 4 | R_C < 200 Å ⇒ Earth-slow; R_C > 15 Å ⇒ WD/NS bite; **15–200 Å double-covered** (§9) | ✓ same structure, they quantify the seam |
| The pivot at n = 3–4 (D = 7–8) | our Findings 4, 7 | WD stops D=5,6 (all), **D=7 only if M_WD ≥ 1.1 M_☉**, D≥8 not stopped → NS-neutrino channel (Table 1, Fig. 2) | ✓ pivot confirmed precisely |

## 2. Corrections to our analysis (the valuable part)

**C1 — LHC trapping probability: we were wrong by orders of magnitude (Part 5).**
We required birth below v_esc (P ~ 6.5×10⁻¹², cubic phase-space tail). G&M App. F:
the **1/v low-velocity enhancement of accretion drag** means Earth's column can stop
BHs born below v_max ~ (0.3–1)×10⁻³c ≈ **8–25× v_esc** (Table 11); and the
longitudinal spectrum is **flat in rapidity** (parton luminosities), so the slow tail
is ~linear, not cubic. Result (Table 12, Herwig-convolved): P_trap ~ (0.2–14)×10⁻⁴;
**expected trapped BHs at 1000 fb⁻¹ exceeds 1 for M ≲ 5–7 TeV** (Fig. 12), up to ~10⁴
for light masses at D=11.
⇒ Our "3% LHC-first window" becomes **~certainty** (μ ≫ 1) for light BHs at D ≥ 8.
The joint event "nature trapped none in Earth/Sun AND LHC traps some" is not a tail
risk — it is the *expected outcome* in the dangerous scenario. Consequently G&M's
safety case leans 0% on capture improbability and 100% on: slowness (R_C < 200 Å)
+ WD survival (D ≤ 7) + NS survival via cosmic neutrinos (D ≥ 8). Our audit
priority was right; our Part-5 probability was not. *Methodological lesson for the
artifact: naive isotropic phase-space tails underestimate collider slow tails;
production spectra are flat in rapidity.*

**C2 — Iron-composition margin: our "17×" was too pessimistic.** G&M count A
nucleon–nucleon collisions per nucleus and use an E⁻³ lower-bound flux below GZK:
Earth-lifetime count ~10²²/A ≈ 2×10²⁰ for Fe → margin ~10³ over the LHC program
(not 17×). Substance of the caveat survives (composition costs 2–3 orders off the
proton margin of 10⁵), magnitude revised. They also assume Fe-only as *baseline*
worst case throughout.

**C3 — Neutral stopping column: 10²¹ → ~10¹⁶ g/cm².** Our absorption-only,
capture-below-11-km/s criterion overstated the needed column. Their treatment:
gravitational *scattering* with quantum capture radius b̂_min ≫ r_H (App. C),
and the criterion is slowing to γ ~ 1 inside a WD (whose own v_esc ~ 0.02c then
binds). Table 1: δ_T = (0.25, 2.1, 6.2, 11.9)×10¹⁵ g/cm² for D = 5,6,7,8 at
M = 10 TeV, vs. WD columns 13–38×10¹⁵ g/cm². Conclusions unchanged (Earth/Sun
hopeless, WD works for D ≤ 7), magnitudes now correct.

## 3. New load-bearing dependencies surfaced by the primary source

- **The D ≥ 8 case rests on the cosmic-neutrino flux** (App. E.7: dΦ/dE = 10⁻⁷(GeV/E)²,
  called "very conservative"): neutrinos evade NS magnetic screening (B ≥ 10⁸ G cuts
  charged CRs; acceptance ×10⁻³ at poles) and make 1–6×10⁴ BHs/Myr *inside* a NS
  (Table 10) → NS consumed in ~10 Myr → Gyr-old X-ray binaries exclude. G&M's own
  caveat #3 (§9): the argument fails only if cosmic-ray composition is very heavy
  **and** the UHE neutrino flux "doesn't exist or has unusual gravitational couplings."
  **In 2008 no astrophysical UHE neutrino had been observed. IceCube has since
  detected the astrophysical flux (2013+, up to ~10 PeV) — the weakest empirical
  link of 2008 has strengthened; cosmogenic (GZK) EeV neutrinos remain unobserved.**
  → Perfect demonstration of a *living* knowledge base: this node's status changed.
- **WD argument inputs**: existence of old, massive, low-B white dwarfs — they cite
  named stars (WD0346-011: 1.25 M_☉, B < 1.2×10⁵ G, ~100 Myr; WD2159-754: 1.17 M_☉,
  ~2.5 Gyr; ...) via Zeeman spectropolarimetry + cooling ages. D=7 needs M_WD ≥ 1.1 M_☉.
- **Accretion-parameter conservatism**: stopping bounds robust to c_ac,p ∈ [1/4, 1]
  within 25% (§5.3.2); they flag c_ac,M = c_ac,p as the conservative choice.
- Their philosophy stated explicitly: every uncertainty replaced by worst case;
  bounds "can likely be improved."

## 4. What our audit adds beyond G&M (candidates for the artifact)

- The **joint-Poisson "LHC-first" framing** (P(nature=0 AND LHC≥1)) — implicit in
  their logic, never computed as a probability statement; with their App.-F numbers
  it sharpens to: *the dangerous scenario predicts LHC-first capture with near
  certainty, which is exactly why the accretion+WD/NS layers carry all the weight.*
- The **empirical inversion bound** (host survival → per-BH ⟨Ṁ⟩ < 10⁻⁷ kg/s without
  accretion theory).
- The **bound-solar-orbit decay channel** (LHC BH → solar orbit → loss cone →
  orbital decay into Sun in 10²–10³ yr): not treated in App. F (they compute only
  direct Sun-core transit, 2.2×10⁻⁷, and the Moon); appears genuinely novel —
  verify against App. H before claiming.
- Explicit **dependency-graph + assumptions-log format**, and the quantified
  composition/f_BH sensitivity sliders.

## 5. Updated audit verdict

Our three independent convergences on "WD/NS at D = 7–8 is the load-bearing node"
are confirmed by the primary source — and sharpened: the node splits into
(a) WD stopping at D=7 requiring M_WD ≥ 1.1 M_☉ low-B old white dwarfs (a handful
of named stars), and (b) the NS-neutrino channel for D ≥ 8 (cosmic neutrino flux,
2008-era unobserved → now partially observed). The Ord-style residual is now
concrete: P(error) concentrates in WD mass/age/B-field astronomy and in the
1/v accretion-drag physics that underlies both trapping and stopping.
