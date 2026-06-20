# Condensates, vacuum fields, and micro-BH accretion in a neutron star

*Working note, 2026-06-20. Extends `notes/superfluid-spectral-accretion.md`.
That note asked whether a paired neutron-star condensate can suppress accretion
of a stable micro black hole below the naive Bondi/geometric rate. This note
sharpens the question for the **specific** condensates and background fields that
are actually present: (1) the chiral QCD condensate, (2) the Higgs / electroweak
condensate, (3) the ubiquitous scalar carrying the cosmological constant. The
recurring lesson is that the suppression loophole only has teeth for a narrow
class of condensates, and the chiral/Higgs/Λ fields mostly fail the test — they
**weaken** the loophole rather than strengthen it.*

*Status: CALCULATION/argument-backed at OOM level, not yet validated against a
primary in-medium absorption calculation. Tag `needs_update`.*

---

## CORRECTION 2026-06-20 (AS/Codex review) — thermal melting, color waves, condensate energy

*Appended, not overwritten. Three revisions from a collaborator pass. The first
is a genuine fix; it does not overturn the note's main conclusion. The other two
sharpen the framing of questions raised by the collaborator.*

**(C1) The "near-horizon chiral restoration" argument was wrong in the dangerous
branch.** Part 1.3 (third bullet) and assumption-log item 3 invoked local
restoration of ⟨q̄q⟩ "near the BH." That silently assumed **near-horizon thermal
heating**, which exists only in the *Hawking-ON* branch — and that branch is not
dangerous (the BH evaporates). The dangerous *Hawking-OFF* branch has no thermal
bath, so thermal melting must not be invoked. Treat it as a zero-temperature /
nonthermal sink problem instead:

```text
HAWKING-ON:  hot micro-BH, condensate thermally disrupted, BH evaporates → not dangerous
HAWKING-OFF: no thermal melting; condensate responds as a T=0 / dense-medium QFT
             to a local absorbing boundary. Response:
                 δ⟨q̄q⟩(x) = ∫ d⁴y G_R^{q̄q,q̄q}(x−y) J_abs(y)
             and accretion is a spectral-absorption problem, not thermal melting:
                 dot M ~ ∫ d³q dω  K_BH(q,ω) ρ_QCD(q,ω)
```

→ Part 1.3 bullet 3 and assumption 3 are **SUPERSEDED** (marked inline below).

**(C2) The main conclusion survives, because the load-bearing argument was
already T=0.** Part 1.2 (asymptotic-freedom floor, `S(q) → 1` at `q ~ 1/r_h`) is
a zero-temperature/UV statement and lives entirely inside the Hawking-OFF branch.
It *is* the spectral-absorption formula above, evaluated in the large-q limit:
the in-medium spectral density ρ_QCD(q,ω) at TeV momentum is the free-parton one,
condensate or not. So C1 removes a non-load-bearing sub-argument only; the
conclusion (chiral condensate gives ≈ no NS-specific accretion suppression in the
UV-dominated regime) stands.

**(C3) "Color wave" propagation — no long-range color wave; and it is a STOPPING
channel, not accretion.** A local condensate disturbance is color-singlet and
propagates only through color-singlet modes (σ/scalar, in-medium pions,
particle-hole/sound), which are gapped/screened → short-ranged (σ ~ 0.4 fm,
π ~ 1.4 fm, medium-modified). There is no long-range colored wave in confined
matter. Crucially, this outgoing singlet response carries energy *away* from the
sink, so it is a **stopping/dissipation** channel, not an accretion-enhancement
channel. Keep stopping ≠ accretion.

**(C4) Condensate energy density does NOT speed up growth enough to move bounds.**
The premise "condensate energy density is high vs regular matter" is overstated.
⟨q̄q⟩ ~ −(250 MeV)³ is dimension-3, not an energy density; the *energy* of
chiral/gluon condensation is bag-constant scale:

```text
B ~ (150–200 MeV)^4 ~ 60–210 MeV/fm³
NS-core baryonic energy density ~ 500–1500 MeV/fm³  (few × saturation)
→ condensate energy is COMPARABLE TO or BELOW baryonic, not "pretty high"
```

And it is **not an independent reservoir**: the condensate is a property of the
ground state the matter lives in, so a swallowed region contributes its *total*
T_00 — which already includes the local condensate/bag energy. No double
counting. Including it is at most an **O(1)** correction to dot M, and the bounds
need orders of magnitude (S_cond < 1e−3 at D=11, < 1e−6 at D=8) → bounds unmoved.
The legitimate residual is an **EOS / phase-front effect on c_s** (hence
`r_B = GM/c_s²` and the soft-Bondi rate) — factor-level, and only in the
soft/Bondi-dominated regime; in the UV/horizon-dominated regime it drops out.
A separate, more speculative branch (BH-catalyzed chiral-restoration/deconfinement
conversion front, à la strangelet conversion) is *not* what the simple
energy-density argument gives and is tracked separately if pursued.

→ New nodes: `MODEL-CHIRAL-CONDENSATE-PHASE-FRONT` (factor-level, soft regime;
alias `MODEL-NS-CONDENSATE-EOS-PHASEFRONT`),
`MODEL-NS-BH-CATALYZED-CONVERSION` (speculative, separate). The UV-vs-soft fork
is tracked as `ASSUMPTION-NS-ACCRETION-UV-VS-SOFT-DOMINATED`.

*Node names harmonized 2026-06-20 with AS's contest-doc §12A (his names are
canonical, ours kept as aliases).*

---

## 0. The error the original note half-makes

`superfluid-spectral-accretion.md` §6 lumps "chiral / color-superconducting
phases" together with the neutron BCS superfluid, as if all condensates supply
the same coherence protection. They do not. The suppression mechanism it relies
on — `r_h ≪ ξ` → "BH inside one coherent patch" → `S_cond ~ (r_h/ξ)^α` — is
borrowed from the **BCS (Fermi-surface pairing)** case, where the gap is small
and ξ is large. Vacuum condensates are a different kind of object and must be
treated separately.

### Reference scales (OOM, ħc = 0.197 GeV·fm)

```text
object                     order parameter   gap/scale       length ξ
neutron BCS superfluid     <nn> (pairing)    Δ ~ 0.1-1 MeV   ξ_BCS ~ 20-200 fm
diquark (2SC/CFL)          <qq> (pairing)    Δ ~ 10-100 MeV  ξ ~ 1-10 fm
chiral QCD condensate      <q-bar q> (vac)   ~4πf_π ~ 1 GeV  ξ_χ ~ 0.2-1.4 fm
Higgs / EW condensate      <H> = v = 246 GeV m_h = 125 GeV   ξ_H ~ 1.6e-3 fm
cosmological-const scalar  <φ> (dark energy) m_φ ≲ H_0       ξ_Λ ~ 1e41 fm (Hubble)
```

```text
micro-BH horizon (TeV-scale, ADD): r_h ~ 1/M_D ~ 1e-4 fm
momentum it probes:                q_probe ~ 1/r_h ~ TeV
```

```text
r_h / ξ_BCS ~ 1e-6
r_h / ξ_χ   ~ 1e-4
r_h / ξ_H   ~ 0.06   (~ m_h / M_D)   <- NOT a small number anymore
r_h / ξ_Λ   ~ 1e-45
```

### Accretable energy densities (what is actually there to absorb)

```text
NS core matter   ρ_NS ~ 1 GeV/fm³ ~ (300 MeV)^4   ~ 8e-3 GeV^4
chiral condensate contribution                    ~ (250 MeV)^4 (mostly bound in mass)
Higgs VEV (NOT accretable; ground state)          v^4 ~ (246 GeV)^4 ~ 4e9 GeV^4
dark energy      ρ_Λ ~ (2.3 meV)^4                ~ 3e-47 GeV^4
```

```text
ρ_NS / ρ_Λ ~ (300 MeV / 2.3 meV)^4 ~ 1e44   -> dark energy is ~44 decades below NS matter
```

---

## Part 1 — Chiral QCD condensate

**Net: recognizing the dominant QCD condensate is *chiral* weakens the
suppression loophole.** Three compounding reasons.

### 1.1 It is a vacuum condensate, not Fermi-surface pairing
The `S_cond ~ (r_h/ξ)^α` coherence factor needs a Fermi-surface BCS condensate
with a finite gap and a large ξ. The chiral condensate ⟨q̄q⟩ ≈ −(250 MeV)³ is
the QCD *vacuum* order parameter (present even at zero density). Its structural
scale is set by the σ/π sector, ξ_χ ~ 0.2–1.4 fm — **~100× shorter than ξ_BCS.**
Substituting ξ_χ for ξ_BCS in `(r_h/ξ)^α` removes ~2 decades per power of α,
eating directly into the suppression budget the note needs (S_cond < 1e−3 at
D=11, < 1e−6 at D=8).

### 1.2 The BH probes q ≫ Λ_QCD, where the condensate is invisible
The Feynman–Bijl protection is a small-`S(q)` statement at `q ~ 1/ξ`. But the
sub-fermi horizon couples at `q ~ 1/r_h ~ TeV`. At `q ≫ Λ_QCD`, asymptotic
freedom gives `S(q) → 1`: the medium responds as nearly-free quarks and gluons,
with abundant spectral weight. The chiral condensate is an IR phenomenon
(scale ≲ 1 GeV) and simply does not exist as coherent structure at TeV momentum
transfer. Physically the BH is far smaller than the inter-quark spacing
(~0.5–1 fm), so "immersed in a condensate" is the wrong picture: it is a tiny
sink capturing individual high-virtuality partons. The Landau/Feynman
obstruction is soft-q/IR; the accretion problem is hard-q/UV. They barely
overlap.

### 1.3 No Boltzmann gap; partial in-medium restoration; scalar coupling
- The chiral excitation is the **pion**, a (pseudo-)Goldstone — *not* gapped in
  the BCS sense, so the note's `exp(−Δ/T)` protection does not apply to the
  chiral channel. (Caveat: m_π ≠ 0; slow-source single-pion Landau kinematics
  still need care.)
- ⟨q̄q⟩ already drops with density (~30% at n₀, → restoration in the core), so
  the "cold coherent condensate" premise is weak in the NS core to begin with.
  **[SUPERSEDED by C1 — the original bullet also claimed near-horizon thermal
  restoration; that holds only in the Hawking-ON branch and must not be used in
  the dangerous Hawking-OFF branch. The in-medium density-driven reduction above
  is retained; the thermal near-horizon clause is withdrawn.]**
- Gravity couples to T_μν, and the chiral sector carries a large scalar response
  (broad σ ~ 500 MeV) that a gravitational sink taps directly — anti-suppression.

### 1.4 Where chiral suppression could still hide (narrow)
Only **diquark/BCS pairing** (neutron superfluid, color superconductivity) has
the Fermi-surface coherence + finite gap the argument needs, and those gaps are
MeV–tens of MeV → only the thermal-quasiparticle channel is Boltzmann-limited,
and even there the high-q channel stays open. Consistent with the note's §7:
modest coherence suppression survives only for the slowest branch (D=11,
S_cond ≲ 1e−2), not for D ≤ 8.

---

## Part 2 — Higgs / electroweak condensate

The Higgs VEV ⟨H⟩ = v = 246 GeV fills all of space and gives masses to the W, Z,
and fermions. Its effect on the accretion loophole is essentially **null**, for
reasons that also generalize (Part 4).

### 2.1 It is universal, not NS-specific — the cleanest kill
The whole suppression loophole needs the condensate to protect *the NS-trapped
branch specifically*, because the competing branches (Earth passage, cosmic-ray
production) are already excluded. The Higgs field is the same in a neutron star,
in the Earth, and in a cosmic-ray shower. **A universal background cannot
differentially protect the NS branch** — whatever it does is already baked into
ordinary micro-BH physics everywhere else. So it cannot reopen the case the way
an NS-specific dense-matter condensate in principle could.

### 2.2 At the probed scale, EW symmetry is restored
Here `r_h/ξ_H ~ m_h/M_D ~ 0.01–0.1` — the horizon is *not* much smaller than the
Higgs Compton wavelength; it is comparable to or below it. Probing
`q ~ 1/r_h ~ TeV ≫ v` means probing **above** the electroweak scale, where the
condensate is effectively restored (symmetric phase). The medium at the relevant
q is unbroken EW fields, not a protective coherent order parameter.

### 2.3 You cannot accrete a VEV; only gapped excitations
The Higgs VEV is the ground state — absorbing it does not lower the energy.
The BH can only couple to Higgs *excitations* (the 125 GeV boson), which are
heavily gapped relative to NS temperatures (T ~ keV–MeV), so any "Higgs channel"
carries `exp(−m_h/T)` ≈ 0 weight. The EW vacuum energy ~ v⁴ is large but is
ground-state energy already absorbed into the cosmological-constant bookkeeping
(Part 3); it is not a local accretable reservoir.

### 2.4 One genuine but orthogonal effect
At `q ≳ v` near the horizon the BH sits at electroweak-restoration / sphaleron
energies, so EW-baryon-number-violating processes could in principle occur
around it. That is a possible *decay/signature* node (B-violation), **not** an
accretion-suppression mechanism, and if anything it is a danger-reducing
(matter-destroying) effect, not a protective one. Track separately if at all.

---

## Part 3 — The cosmological-constant scalar (dark energy)

If the cosmological constant is carried by a light scalar (quintessence) with
⟨φ⟩ everywhere and m_φ ≲ H₀, its effect on the accretion clock is negligible by
~40+ decades, but it is instructive because it exposes why the naive
`(r_h/ξ)^α` heuristic is the wrong physics.

### 3.1 Nothing there to accrete
ρ_Λ ~ (2.3 meV)⁴ is ~44 orders of magnitude below NS-core energy density. As an
accretable medium it is irrelevant to a clock that runs in years–10 Myr.

### 3.2 The real GR effect exists but is ~40 decades too slow
There is a legitimate effect: a BH in a dark-energy background lives in a
Schwarzschild–de Sitter (or quintessence) spacetime, and accretion of dark
energy changes its mass — for phantom EOS (w < −1) it can even *decrease* it
(Babichev–Dokuchaev–Eroshenko). But the rate scales with ρ_Λ, giving
cosmological (Hubble-time) timescales — utterly negligible next to the
NS-consumption clock. Net effect on the safety argument: zero.

### 3.3 Why it breaks the `(r_h/ξ)^α` heuristic
Formally `r_h/ξ_Λ ~ 1e−45`, so the naive coherence factor would predict the
*most* extreme "suppression" of all. That is obviously physical nonsense: a
near-massless field with negligible energy density is not "coherently
protecting" anything — there is simply almost nothing to absorb, and the field
is far too soft to exchange TeV momentum with a sub-fermi sink. This shows the
`(r_h/ξ)^α` form conflates two distinct things — *coherent protection* and
*absence of accretable weight* — and must be replaced by the spectral integral
`Γ_abs ~ ∫ d³q dω |M_BH|² S_op(q,ω)` evaluated at the q the horizon actually
probes.

---

## Part 4 — General criterion (the reusable output)

Adding the Higgs and Λ cases yields a checklist any "condensate X suppresses NS
accretion" claim must pass. This is the methodologically useful product.

```text
(i)   NS-SPECIFIC: present in the dense NS interior but not in the Earth /
      cosmic-ray branches (else the effect is already in the baseline and cannot
      reopen the already-excluded branches).
(ii)  SPECTRAL WEIGHT AT q ~ 1/r_h: meaningful response at the ~TeV momentum the
      sub-fermi horizon couples to (not just at the soft q ~ 1/ξ collective scale).
(iii) DOMINANT ACCRETABLE DENSITY: carries energy density comparable to NS matter
      (not vacuum ground-state energy, not negligible dark energy).
(iv)  GAP STRUCTURE: a real Boltzmann gap is needed for exp(−Δ/T) protection;
      Goldstone/gapless sectors give none.
(v)   FERMI-SURFACE PAIRING: only pairing condensates give a coherence length /
      Landau-critical-velocity protection at all.
```

```text
field/condensate     (i) NS-spec  (ii) q~TeV  (iii) density  (iv) gap   (v) pairing  verdict
neutron BCS          partial      no(UV open) yes            small Δ    YES          weak help, D=11 only
diquark / color-SC   partial      no(UV open) yes(if quark)  Δ~10-100   YES          weak help, narrow
chiral QCD           no(in vac)   no(asympt.) no(bound mass) no(π Gold) NO           negligible / anti
Higgs / EW           NO(univ.)    restored>v  no(VEV)        m_h gapped NO           null
cosmological Λ       NO(univ.)    no(soft)    no(~1e-47)     ultralight NO           null (~40 dec too slow)
```

Only the **Fermi-surface pairing** condensates (neutron superfluid, color
superconductor) pass enough tests to matter, and only for the slowest D=11
branch — exactly the conclusion of `superfluid-spectral-accretion.md` §7, now
with a derivation of *why* the vacuum fields drop out.

---

## Claim-graph nodes

```text
MODEL-NS-CONDENSATE-SUPPRESSION-CRITERION
  type: MODEL
  status: current
  statement: A condensate can suppress NS accretion of a stable micro-BH only if
    it is NS-specific, carries spectral weight at q ~ 1/r_h ~ TeV, dominates the
    accretable energy density, and is a Fermi-surface pairing condensate. Vacuum
    condensates (chiral, Higgs, cosmological-constant scalar) fail these and do
    not reopen the bound.
  depends_on:
    - ASSUMPTION-STABLE-BH-NO-HAWKING
    - CALC-NS-ACCRETION-CLOCK
  supersedes_framing_in: MODEL-NS-SUPERFLUID-SPECTRAL-ACCRETION (§6 lumping)

MODEL-CHIRAL-CONDENSATE-ACCRETION     type: MODEL  status: needs_update  -> Part 1 (+C1/C2)
MODEL-HIGGS-CONDENSATE-ACCRETION      type: MODEL  status: current       -> Part 2 (null)
MODEL-DARKENERGY-SCALAR-ACCRETION     type: MODEL  status: current       -> Part 3 (null, ~40 dec)
MODEL-CHIRAL-CONDENSATE-PHASE-FRONT   type: MODEL  status: needs_update  -> C4 (factor-level, soft regime; alias MODEL-NS-CONDENSATE-EOS-PHASEFRONT)
MODEL-NS-BH-CATALYZED-CONVERSION      type: MODEL  status: disputed      -> C4 (speculative, separate branch)

ASSUMPTION-NS-ACCRETION-UV-VS-SOFT-DOMINATED  type: ASSUMPTION  status: current  -> C2/C4 (which regime sets dot M; AS §12A canonical)
ASSUMPTION-HAWKING-OFF-T0-SINK        type: ASSUMPTION  status: current   -> C1 (dangerous branch is nonthermal; distinct from the fork above)
```

---

## Assumptions log

1. **Horizon-/UV-dominated accretion.** The central argument assumes the flux is
   set at `q ~ 1/r_h` (sub-fermi horizon), not at the soft Bondi scale r_B. If
   accretion is instead dominated by soft collective response near r_B, the IR
   condensates re-enter. Pinning which (q, ω) dominates is the job of the planned
   `analysis/superfluid_accretion_suppression.py` and decides the whole branch.
2. **ADD-scale horizon.** r_h ~ 1/M_D ~ TeV⁻¹ is the minimal higher-dimensional
   estimate; exotic-gravity models (note §9 of the supporting material) shift it.
3. **Stable, non-Hawking BH → treat as a T=0 nonthermal sink.** Inherited from
   the loophole's premise. **[REVISED by C1]** The dangerous branch is Hawking-OFF,
   so there is no thermal bath: condensate response must be computed as
   zero-temperature/dense-medium QFT to an absorbing boundary (linear response +
   spectral absorption), NOT as thermal melting. Thermal disruption belongs only
   to the Hawking-ON branch, which is not the dangerous one.
4. **OOM only.** All scales and the suppression-budget comparisons are
   order-of-magnitude; the σ/π and pairing-gap numbers carry factor-few spread.
5. **Quintessence interpretation of Λ.** Part 3 assumes a light dynamical scalar;
   a pure constant Λ has no excitation to accrete at all (an even stronger null).
6. **Not yet primary-source validated.** The in-medium high-q absorption claim
   (Part 1.2, the asymptotic-freedom floor) should be checked against an explicit
   spectral-function / structure-factor calculation before being promoted from
   `needs_update` to `current`.
