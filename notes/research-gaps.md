# Research gaps register + the production-channel equivalence question

*Living open-questions register for the audit. Part A inventories what is left
research-wise (ours + AS's memo + new items). Part B is a deep dive on the
question raised 2026-06-14: does the LHC's pp production transfer to the
neutrino-nucleon production that the neutron-star bound relies on? This is the
single most important open physics question we have found, because it attacks
the load-bearing node (notes/06) directly.*

---

## Part A — What is left, research-wise

Ranked by leverage on the safety argument.

### A1. Production-channel equivalence (pp vs ν-N) — HIGH, see Part B
The NS bound (the only thing that closes the dangerous neutral gravity-only case
at D ≥ 8, notes/06) assumes cosmic neutrinos make BHs the way LHC protons do.
G&M flag the loophole in one sentence (§8.1.2) and dismiss it as "not compelling."
It deserves a proper treatment: when can ν-N production be suppressed relative to
pp, by how much, and does the proton binary-companion channel (Table 3) survive
to plug the gap? → Part B.

### A2. What sets the production rate f_BH — HIGH (AS §6–7)
Our entire capture/accretion chain (notes/02–06) carries f_BH ~ 10⁻⁸ as a free
knob. AS's PDF-cliff analysis shows the rate is set by the high-x parton
luminosity, the threshold convention M_min/M_D, and the trapped fraction κ — not
by the geometric prefactor. Build `analysis/pp_production.py` + a notes layer;
this also feeds the ν-N rate in A1 (one PDF instead of two).

### A3. Modern exclusions shrink the whole scenario — HIGH, cheap
Direct searches (CMS arXiv:2604.10732: M_D-dependent BH masses < 8.4–11.4 TeV
excluded; ATLAS 2604.19495 ~9.4 TeV) and precision tests push M_D up, shrinking
the M_min/√s window where any of this is possible. AS §12: these constrain only
*prompt visible* decays, not the stable/invisible remnant — so they bound the
*premise* (can the LHC make BHs at all) far more than the *hazard*. Quantify how
much of the dangerous parameter space is already gone in 2026.

### A4. 2008 → 2026 astrophysical update pass — MEDIUM
IceCube astrophysical ν flux (TeV–PeV measured; EeV cosmogenic still upper-limit
— matters for A1/Part B), Gaia white-dwarf catalog (ages/masses/B-fields feeding
the D ≤ 7 WD bound, notes/05), LVK GWTC-5.0 NS EOS/population (factor-few, not
decade — per AS §14). Mark each node current/superseded/needs-update.

### A5. G&M Appendix H — bound-solar-orbit channel — MEDIUM, cheap
Verify whether our notes/04 "LHC BH → bound solar orbit → decays into Sun"
channel is novel or already in App. H. Closes an open novelty claim.

### A6. The claim-graph artifact — HIGH (this is the deliverable)
Adopt AS §17's node schema (id/type/status/depends_on/source_refs/code_refs/
update_triggers/superseded_by/correction_history). Every finding in notes/01–06
+ Part B becomes a node tagged OBSERVATION / CALCULATION / ASSUMPTION / MODEL.
This is what the competition actually judges.

### A7. Voloshin-type exponential suppression — LOW/MEDIUM
Disputed claim that semiclassical BH production carries e^{−I_E}. If real it
suppresses pp AND ν-N alike (≈ species-independent) → weakens the premise, not
the bound asymmetry. Note status (Eardley–Giddings / Hsu vs Voloshin), park it.

### A8. Charge/colour retention vs Schwinger discharge — LOW (mostly done)
We have the Schwinger⇔Hawking correlation (notes/05). A small OOM note on
colour neutralization time (G&M §8.2: t_abs ~ 10⁷ fm) would close it.

### A9. Renumbering / repo hygiene — trivial, do first
AS's plan wants notes/06 = production; we used 06 = NS bound. Settle: NS = 06,
production/PDF-cliff = 07, radiation = 08, direct-searches = 09. Move working
memos out of repo root.

---

## Part B — Does pp production transfer to ν-N? (the load-bearing question)

### B0. Why this is the whole ballgame
The chain that closes the dangerous case at D ≥ 8 is:
> LHC (pp) can make BHs  ⇒  cosmic ν (ν-N) make them on neutron stars  ⇒
> NS would be eaten in ≪ Gyr  ⇒  but NSs are old  ⇒  so BHs are safe/absent.
The first arrow is an **inference, not an observation**: it assumes ν-N and pp
produce BHs equivalently at equal √ŝ. If that arrow breaks, the LHC could make
something nature's neutrinos do not, and the strongest D ≥ 8 bound fails.

### B1. Q1 — How does ν-N differ from pp? (kinematics & luminosity)
At the *hard subprocess* level BH formation is **gravitational and democratic**:
two quanta with √ŝ > M_D and impact parameter b < R_S(√ŝ) form a BH with a
geometric cross section σ̂ ≈ π R_S². The colliding species' internal quantum
numbers (colour, charge, weak isospin) do **not** enter the leading
trapped-surface calculation — only energy-momentum does (equivalence principle).
So at fixed √ŝ and b, σ̂(ν q → BH) = σ̂(q q → BH) in the minimal theory.

The differences are in how you *reach* a given √ŝ:
1. **Number of PDFs.** pp: σ = Σ ∫dx₁dx₂ f(x₁)f(x₂) σ̂(x₁x₂s) — **two** parton
   luminosities, both penalised at high x. ν-N (fixed target): the neutrino is
   elementary (x_ν = 1), so σ = Σ ∫dx f(x) σ̂(2x m_N E_ν) — **one** PDF. Fewer
   penalties, but you pay in required beam energy.
2. **Energy needed.** √ŝ = 14 TeV via ν-N needs E_ν = M_min²/(2 x m_N) ≈ **10¹⁷–
   10¹⁸ eV** (x ~ 0.3–0.1) — EeV-scale. Neutrinos easily reach √ŝ *above* the LHC,
   because cosmogenic ν go to EeV. So if democracy holds, neutrinos probe a
   *higher* √ŝ than the LHC — the argument is then *a fortiori*.
3. **Kinematics of the product.** LHC: lab = CM, BH born slow (β ~ 0.2,
   notes/03). Cosmic ν-N (fixed target): BH born with γ ~ E_ν/M_BH ~ 10³–10⁴ in
   the star frame — ultra-relativistic, like the CR case (notes/01). This is why
   it matters that production happens *inside* the dense NS (huge internal column
   stops even the boosted BH; notes/06), whereas the same boosted BH would punch
   straight through ordinary Earth.

**Net:** in the minimal extra-dimensions theory the ν-N vs pp difference is
purely kinematic/PDF and *helps* the safety argument (neutrinos reach higher √ŝ,
and the NS internal density solves the boost problem). The argument is robust —
**conditional on democracy.**

### B2. Q2 — Are neutrinos the most common high-energy cosmic rays?
**No.** High-energy cosmic rays are overwhelmingly **charged hadrons** (protons
and nuclei); neutrinos are a rare *secondary* component, smaller by many orders
of magnitude. They are used in the NS argument **not for abundance but for
penetration**, for two reasons:
- A neutron star's magnetic field (≥10⁸ G, up to 10¹²–10¹⁵ G) deflects/screens
  charged CRs and induces synchrotron losses → G&M give an acceptance reduction
  ~10⁻³ near the surface (their §8.1, App. G). Neutral, weakly-interacting
  neutrinos ignore the field and reach the dense core where a BH would be trapped.
- The relevant flux is the **cosmogenic / GZK neutrino flux**: UHE protons above
  ~5×10¹⁹ eV scatter on CMB photons (p γ → Δ → n π⁺, π⁺ → μ⁺ν → …) producing a
  "guaranteed" EeV neutrino flux. G&M's conservative parametrization (App. E.7):
  dΦ_ν/dE = 10⁻⁷(GeV/E)² m⁻²s⁻¹sr⁻¹GeV⁻¹.

Two consequences for the audit:
- The neutrino channel's **flux normalization at EeV is itself an uncertain,
  partly-unmeasured input.** IceCube has measured the TeV–PeV *astrophysical*
  flux (post-2013), but the **EeV cosmogenic** flux that the NS bound actually
  uses is still essentially upper-limited (next-gen: IceCube-Gen2, GRAND, …).
  → mark UPDATE-ICECUBE node as *partially upgraded, EeV still open*.
- Because neutrinos are rare, when the bound leans on them it leans on a *flux
  model*, not a *count*. The robust, model-free fallback is the proton channels.

### B3. Q3 — Beyond extra dimensions: do alternative theories change ν-N vs pp?
G&M consider only ADD/RS extra dimensions as the mechanism that lowers the
Planck scale to TeV. In that framework BH formation is democratic, so ν-N ≈ pp
(B1). Alternatives can break democracy — **always in the direction of suppressing
ν-N relative to pp**, because pp uses co-located brane partons while neutrinos
are the species most easily delocalized:

1. **Brane localization / split fermions (the real loophole).** In fat-brane or
   split-fermion models (Arkani-Hamed–Schmaltz) SM fields sit at different
   positions in the extra dimensions. BH formation needs the two colliding
   energy packets to lie within ~R_S in the *full* geometry. If the neutrino's
   relevant wavefunction is displaced from the quarks by a bulk distance d ≳ R_S,
   ν-q formation is suppressed (overlap/exponential), while q-q (both on "our"
   brane) is not. G&M's own §8.1.2: *"baryon number conservation … enforced …
   through reduced interactions between neutrinos and quarks by virtue of these
   living on different branes [78] … raise a small possibility that neutrino
   cosmic rays would not produce black holes the same way that nucleons do."*
2. **Bulk right-handed neutrinos (independently motivated!).** A *popular*
   explanation for tiny neutrino masses is a right-handed neutrino propagating in
   the bulk: small wavefunction overlap → small Yukawa. The **same** small overlap
   would suppress ν-quark BH formation. The mechanism that makes neutrinos light
   is the mechanism that could break the NS bound — an elegant, citable tension.
3. **Species-scale gravity (Dvali).** Low effective Planck scale from N light
   species, M_species = M_Pl/√N, rather than geometry. BH formation still couples
   to energy universally → tends to stay democratic; model-dependent. Park.
4. **Composite/emergent graviton, form factors.** If the strong-gravity dynamics
   has non-universal couplings or form factors, species-dependence is possible in
   principle; highly model-dependent, no sharp prediction.

The dangerous direction is specifically **ν-N suppressed while pp normal** (LHC
makes them, neutrinos do not). The reverse (pp enhanced, ν-N normal) does not
break the bound. So the asymmetry to worry about is exactly the one that brane
separation produces.

### B4. Q4 — Can ν-N be *significantly* less likely in some theory? + the backup
**Yes**, in the brane-separation / split-fermion / bulk-neutrino class (B3.1–2)
the suppression can be large (overlap factor, potentially exponential in d·M_*).
The magnitude is model-dependent and unconstrained — could be O(1) or
many orders. So the loophole is genuine, not excluded.

**But it is not the end of the NS bound, because of a second, proton-based
channel.** G&M §8.1.1 + Table 3: cosmic-ray **protons** scatter on the NS's
**binary companion star** (no magnetic screening there), form BHs in ordinary
parton-parton collisions, which then rain onto the NS. This channel:
- uses **protons, not neutrinos** → *immune to neutrino brane-suppression* (B3);
- is field-independent (companion has no NS-strength field);
- rate (Table 3, M_min = 14 TeV): **54 / 74 / 95 / 118 per Myr** for D = 8/9/10/11
  — with the "full-coverage equivalent" FCE ~ 2 Myr from known binaries, even at
  only 10% proton composition giving ~5/Myr for 14 TeV.

Compare to what's needed: a NS is consumed in ≪ Myr once *one* BH is stuck
(notes/06). So even the proton channel alone deposits ≫ 1 BH over a Gyr NS
lifetime. **Therefore, if ν-N is fully suppressed, the D ≥ 8 bound weakens (loses
its strongest, highest-rate, most robust channel) but does not obviously break —
it falls back to the proton binary-companion channel.** The open research
questions that remain:
- Quantify the proton-channel bound *on its own* (no neutrinos): is FCE × Table-3
  rate still ≫ 1 BH per NS lifetime under heavy CR composition + the M_min push
  from A3? Table 3 falls with heavier composition and higher M_min.
- Is there a theory that suppresses **both** ν-N **and** the proton-on-companion
  channel while keeping pp at the LHC alive? That requires suppressing
  quark-quark BH formation in the companion but not at the LHC — same partons,
  same √ŝ — which seems very hard to arrange. **This is the real robustness
  test:** the proton companion channel uses the *identical* parton process as the
  LHC, so any theory that lets the LHC make BHs must let the companion make them
  too. That is a much tighter equivalence than ν-N ↔ pp.

### B5. Bottom line for the claim graph
- NODE `ASSUMPTION-PRODUCTION-DEMOCRACY` (ν-N ≈ pp at fixed √ŝ): **load-bearing
  for the D ≥ 8 NS-neutrino bound; holds in minimal ADD/RS; can be broken by
  brane-separated / bulk neutrinos (independently motivated by ν mass).**
- NODE `CALC-NS-PROTON-COMPANION-BOUND` (Table 3): **backup that does not depend
  on neutrino democracy; uses the same parton process as the LHC, so it is tied
  to the LHC premise itself** → much harder to evade than the neutrino channel.
- Residual after this analysis: the dangerous case at D ≥ 8 survives only in a
  theory that (i) gives stable neutral non-Hawking BHs, (ii) suppresses ν-q
  BH formation, **and** (iii) suppresses q-q BH formation on the companion while
  keeping it alive at the LHC — (iii) being nearly self-contradictory. The
  Ord–Hillerbrand–Sandberg residual is now concentrated on (iii)'s near-
  impossibility plus the EeV cosmogenic-flux normalization for the neutrino
  channel.

### B6. Concrete next calculations
1. `analysis/neutrino_bh_production.py`: one-PDF ν-N rate vs two-PDF pp rate at
   matched √ŝ (quantify the *kinematic* factor, before any suppression).
2. Proton-companion bound stand-alone: FCE × Table-3 vs 1-BH-per-NS, swept over
   composition (proton fraction) and M_min (from A3 exclusions).
3. Toy brane-overlap suppression S(d/R_S) to show the *range* over which the
   neutrino channel degrades but the proton channel holds.
