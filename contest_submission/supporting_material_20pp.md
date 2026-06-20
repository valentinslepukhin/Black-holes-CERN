# Supporting Material

This document is the optional supporting material for the contest submission.
It should fit within the contest's suggested ~20-page supporting-material
budget. Appendices and the repository itself can be longer.

## 1. Suggested Judge Reading Path

Recommended order:

1. Read the core submission:

   ```text
   contest_submission/submission_core_10pp.md
   ```

2. Skim the top-level repo overview:

   ```text
   README.md
   PROJECT_SUMMARY.md
   ```

3. Inspect the central physics decomposition:

   ```text
   notes/01-cosmic-ray-argument.md
   notes/02-capture-and-accretion.md
   notes/06-neutron-star-bound.md
   ```

4. Inspect the correction trail:

   ```text
   notes/04-lhc-first-probability.md
   notes/05-comparison-giddings-mangano.md
   ```

5. Inspect the research-gap register:

   ```text
   notes/research-gaps.md
   ```

6. Inspect selected AS memo sections:

   ```text
   summary_from_AS.md
   ```

   Most useful sections:

   ```text
   7. PDF Cliff Algebra
   9. pp Production Versus Neutrino-Nucleon Production
   10. Direct Searches and Decay Channels
   13. Nonlinear and Exotic Semiclassical Gravity
   16. Magnetic Fields, Magnetic Charge, and Monopole-Stabilized BHs
   19. Heavy-Ion Magnetic-Field Production
   notes/superfluid-spectral-accretion.md
   21. Current Implementation Problems
   22. Claim Graph Schema
   ```

## 2. Repository Inventory

Top-level files:

```text
README.md
PROJECT_SUMMARY.md
CLAUDE.md
summary_from_AS.md
contest_submission/
analysis/
notes/
sources/
```

Calculation scripts:

```text
analysis/cosmic_ray_flux.py
analysis/bh_earth_passage.py
analysis/capture_and_accretion.py
analysis/lhc_bh_fate.py
analysis/lhc_first_capture.py
analysis/ns_capture_consumption.py
```

Main notes:

```text
notes/01-cosmic-ray-argument.md
notes/02-capture-and-accretion.md
notes/03-lhc-produced-bh.md
notes/04-lhc-first-probability.md
notes/05-comparison-giddings-mangano.md
notes/06-neutron-star-bound.md
notes/research-gaps.md
notes/review-of-AS-summary.md
```

## 3. What The Calculation Scripts Are For

The Python files are not intended as polished final simulations. They serve
three purposes:

1. Reproduce the order-of-magnitude skeleton of the published safety argument.
2. Make assumptions explicit enough to criticize.
3. Preserve the correction trail from first-pass reasoning to source-checked
   reasoning.

The final submission should mark two old scripts as superseded in their printed
output:

```text
analysis/lhc_bh_fate.py
analysis/lhc_first_capture.py
```

Those files still contain an early capture-tail estimate that was corrected by
comparison with Giddings-Mangano Appendix F. Keeping them is useful; presenting
their output without a warning is not.

## 4. Compact Physics Map

The case branches as follows:

```text
Hypothetical LHC black hole
|-- Hawking-radiating
|   `-- evaporates; not the pessimistic hazard branch
`-- stable or remnant
    |-- strongly/EM interacting
    |   `-- stopped in ordinary matter; Earth/Sun cosmic-ray survival applies
    `-- neutral gravity-only
        |-- cosmic-ray BHs pass through ordinary matter
        |-- Earth/Sun survival alone is insufficient
        |-- slow Earth accretion excludes many branches as practical hazards
        |-- white-dwarf survival handles lower-dimensional branches
        `-- neutron-star survival handles higher-dimensional branches
```

Key slogan:

```text
fast danger -> astrophysically testable -> excluded
not astrophysically excluded -> too slow to be dangerous
```

## 5. Representative Numerical Anchors

Current repository-level anchors:

1. LHC-equivalent cosmic-ray threshold:

   ```text
   E_CR ~= S^2 / (2 m_p)
   S = 14 TeV -> E_CR ~= 1e17 eV
   ```

2. Cosmic-ray exposure:

   ```text
   Earth has received ~2.5e22 LHC-equivalent proton collisions over its history.
   ```

3. Cosmic-ray-produced BHs are boosted:

   ```text
   gamma ~ 7e3 for LHC-equivalent fixed-target events
   ```

4. LHC-produced BHs are comparatively slow:

   ```text
   lab frame ~= parton CM frame
   ```

5. Neutron-star consumption once a dangerous BH is captured:

   ```text
   repository script reproduces Giddings-Mangano-scale results:
   years to ~10 Myr across D = 5..11, depending on dimension/model
   ```

These numbers are not the final artifact. Their purpose is to anchor the claim
graph.

## 6. PDF Cliff

The hadronic production rate can be written:

```text
sigma_pp->BH(S) =
  sum_ij int_(tau_min)^1 d tau
    dL_ij/dtau
    hat_sigma_ij(tau S^2)
```

with:

```text
tau_min = M_min^2 / (kappa^2 S^2)
```

Near the endpoint:

```text
f_i(x,Q) ~= A_i(Q) (1 - x)^b_i
dL_ij/dtau ~ (1 - tau)^(b_i + b_j + 1)
p = b_i + b_j + 1
```

Thus:

```text
d ln sigma / d ln M_min ~= - 2 p tau_min / (1 - tau_min)
d ln sigma / d ln S     ~= + 2 p tau_min / (1 - tau_min)
d ln sigma / d ln kappa ~= + 2 p tau_min / (1 - tau_min)
```

This is why threshold convention, trapped-energy fraction, and beam energy can
matter more than the slow geometric black-disk radius prefactor.

## 7. Direct Searches

The direct-search logic is:

```text
N_seen = L_int * sigma_BH * BR_visible * A * epsilon
```

Modern ATLAS/CMS searches strongly constrain prompt visible benchmark branches.
They do not automatically cover:

- stable neutral remnants,
- invisible decays,
- hidden-sector decays,
- long-lived decays outside the detector,
- low-visible-energy decays,
- exotic charged or magnetic states unless the appropriate high-ionization or
  heavy-stable-particle searches apply.

Therefore direct searches are a major production-premise constraint, but not a
replacement for the stable-remnant safety argument.

## 8. pp Versus Neutrino-Nucleon

For pp:

```text
sigma_pp =
  sum_ij int dx1 dx2
    f_i(x1,Q) f_j(x2,Q)
    hat_sigma(x1 x2 S^2)
```

For neutrino-nucleon fixed-target production:

```text
sigma_nuN =
  sum_i int_(x_min)^1 dx
    f_i(x,Q)
    hat_sigma(2 x m_N E_nu)
```

with:

```text
x_min = M_min^2 / (2 m_N E_nu kappa^2)
```

Minimal gravitational production is approximately species-democratic at fixed
`hat_s`, but brane-localization, split-fermion, or bulk-neutrino models can
suppress `nu-q` production relative to `q-q` production.

The artifact therefore separates:

```text
ASSUMPTION-PRODUCTION-DEMOCRACY
CALC-NS-NEUTRINO-PRODUCTION
CALC-NS-PROTON-COMPANION-BOUND
```

The proton companion channel is important because it uses the same quark-quark
parton process as the LHC, making it harder to evade while keeping LHC
production alive.

## 9. Exotic and Magnetic Branches

Useful model parameters:

```text
R_h(M; theta)
M_crit(theta)
kappa(theta)
b_max(M; theta)
T_H(M; theta)
sigma_acc(M,v,rho; theta)
species_overlap(theta)
```

Production becomes:

```text
hat_sigma ~= pi b_max^2 * Theta(kappa sqrt(hat_s) - M_crit)
```

Important classes:

- Lovelock / Gauss-Bonnet / higher-curvature gravity,
- Born-Infeld or EiBI-like gravity,
- asymptotic safety / running Newton constant,
- noncommutative or regular black holes,
- GUP / minimal-length models,
- brane/bulk localization,
- string balls and p-branes,
- black rings or other higher-dimensional horizon topologies,
- magnetically charged or monopole-stabilized black holes,
- heavy-ion magnetic-field production.

Current qualitative conclusion:

```text
Most exotic branches shift threshold, trapped fraction, evaporation/remnant
behavior, accretion law, or species overlap. The claim graph should expose
which node each model attacks rather than treating all exotic physics as one
undifferentiated objection.
```

## 10. Magnetic and Heavy-Ion Notes

A magnetically charged black hole can be stabilized near extremality:

```text
r_pm = M +/- sqrt(M^2 - Q^2 - P^2)
T_H = (r_+ - r_-) / (4 pi r_+^2)
T_H -> 0 as M^2 -> Q^2 + P^2
```

If the lightest monopole is heavy:

```text
m_mon >> T_H
```

then magnetic-charge loss through Hawking emission is suppressed.

But:

```text
ordinary magnetic charge -> highly ionizing and strongly stopped; if naturally
                            produced, Earth/Sun/WD/NS survival is a strong
                            constraint, with searches as an extra constraint
hidden magnetic charge   -> ordinary stopping/capture is not guaranteed, but
                            ordinary heavy-ion magnetic fields may also fail to
                            produce it efficiently
```

Heavy-ion fields create a distinct production branch:

```text
Gamma ~ exp[- pi m^2 / (g B)]
```

This branch is not covered by ordinary pp luminosity equivalence. It requires
separate assumptions about magnetic charge, coupling to visible EM fields, pair
production, post-capture accretion, and direct high-ionization search limits.

## 10A. Future Machines And FCC

FCC-ee is not a relevant microscopic-BH danger path in the standard TeV-gravity
logic:

```text
sqrt(s) ~= 88-365 GeV
```

This is far below TeV-scale BH thresholds unless one assumes already-excluded
sub-TeV gravity.

FCC-hh is different:

```text
sqrt(s) ~= 85 TeV baseline, often rounded to 100 TeV in older studies
```

The fixed-target cosmic-ray equivalent is:

```text
E_CR ~= S^2 / (2 m_p)
14 TeV  -> ~1e17 eV
85 TeV  -> ~3.9e18 eV
100 TeV -> ~5.3e18 eV
```

These cosmic-ray energies exist, but the flux is much lower than at the LHC
equivalent threshold and composition is more important. Heavy nuclei must be
treated per nucleon:

```text
E_nucleon = E_nucleus / A
```

so FCC-hh safety margins must be recomputed rather than copied from LHC.

Corrected charged-BH framing:

```text
visible charged stable BH:
  charge enhances stopping/capture in ordinary matter.
  If naturally produced, astrophysical survival bounds strengthen.

hidden charged stable BH:
  behaves more like the neutral branch for ordinary stopping.
  But ordinary visible heavy-ion fields may not produce it efficiently.
```

The more specific FCC exotic branch is:

```text
FCC heavy-ion coherent EM fields produce stable visible-charged or magnetic
BH-like objects,
AND natural astrophysical analogues are absent or much rarer,
AND charge is not radiated/neutralized,
AND post-capture accretion is not suppressed.
```

That branch is not mainly about detector invisibility. It is a
production-equivalence question plus a post-capture accretion question.

Suggested nodes:

```text
MODEL-FCC-HH-85TEV-RECALCULATE-CR-COMPARATOR
MODEL-FCC-HH-COMPOSITION-SENSITIVE-UHECR-BOUND
MODEL-FCC-HI-B-FIELD-MAGNETIC-BH-PRODUCTION
MODEL-VISIBLE-CHARGED-BH-ASTRO-CAPTURE-BOUND
MODEL-HIDDEN-CHARGED-BH-NEUTRAL-LIKE-STOPPING
```

## 11. Draft Claim-Graph Schema

Suggested node fields:

```text
id
title
type: OBSERVATION | CALCULATION | ASSUMPTION | MODEL | CORRECTION | UPDATE
status: current | superseded | disputed | marginal | needs_update
statement
depends_on
supports
contradicts
source_refs
code_refs
parameter_scope
last_validated
update_triggers
superseded_by
correction_history
notes
```

Example nodes:

```text
CALC-PP-BH-PRODUCTION-GEOMETRIC
CALC-PDF-CLIFF-HIGH-X
CALC-CR-FIXED-TARGET-THRESHOLD
OBS-CR-EARTH-COUNT
CALC-NEUTRAL-CR-PASS-THROUGH
OBS-OLD-NEUTRON-STARS
CALC-NS-NEUTRINO-PRODUCTION-DGE8
ASSUMPTION-PRODUCTION-DEMOCRACY
CALC-NS-PROTON-COMPANION-BOUND
UPDATE-ICECUBE-TEV-PEV-FLUX
UPDATE-LHC-RUN3-DIRECT-LIMITS
CORR-LHC-CAPTURE-TAIL
MODEL-MAGNETICALLY-CHARGED-BH
MODEL-HIC-B-ENHANCED-MAGNETIC-BH-PRODUCTION
MODEL-FCC-HH-85TEV-RECALCULATE-CR-COMPARATOR
MODEL-FCC-HH-COMPOSITION-SENSITIVE-UHECR-BOUND
MODEL-FCC-HI-B-FIELD-MAGNETIC-BH-PRODUCTION
MODEL-VISIBLE-CHARGED-BH-ASTRO-CAPTURE-BOUND
MODEL-HIDDEN-CHARGED-BH-NEUTRAL-LIKE-STOPPING
MODEL-SLOW-NS-CONSUMPTION
MODEL-NS-SUPERFLUID-SPECTRAL-ACCRETION
MODEL-NS-SUPERFLUID-SPECTRAL-STOPPING
MODEL-CHIRAL-CONDENSATE-PHASE-FRONT
ASSUMPTION-NS-ACCRETION-UV-VS-SOFT-DOMINATED
SEARCH-MOEDAL-ATLAS-HIGH-IONIZATION
```

## 12. Neutron-Star Condensate Accretion

The latest qualitative branch concerns the accretion clock inside neutron
stars. Neutron-star interiors are not ordinary gases; they likely contain
neutron superfluidity, proton superconductivity, and possibly quark or other
paired phases.

The compact formulation is:

```text
What operator does the BH couple to, and what spectral weight does the medium
have at the required (q, omega)?
```

For stopping of a moving BH:

```text
P_loss ~ int d^3q |V_BH(q)|^2 omega S(q, omega)
omega = q . v
```

For accretion, the issue is not identical. A horizon is an absorbing boundary.
In a bosonic condensate, coherent phase flow can feed the sink without first
creating a real phonon outside the horizon. But if the BH is much smaller than
the coherence length of paired matter:

```text
r_h << xi
```

then naive hydrodynamic Bondi accretion is not automatically valid. A useful
parameterization is:

```text
dot M_NS = dot M_naive * S_cond
S_cond ~ 1                      hydrodynamic condensate limit
S_cond ~ (r_h/xi)^alpha          coherence-limited absorber
S_cond ~ exp(-Delta/T)           thermal quasiparticle limited only
S_cond ~ spectral integral       correct many-body formulation
```

For old neutron stars, the rough suppression needed is:

```text
D=11: t_naive ~ 10 Myr  -> need S_cond < 10^-3-10^-2
D=8:  t_naive ~ 4 kyr   -> need S_cond < 10^-6-10^-5
D<=7: much stronger suppression required
```

Detailed note:

```text
notes/superfluid-spectral-accretion.md
```

## 12A. Vacuum Condensates And Chiral Response

A later Valentin/Claude-style note sharpened this branch by separating
Fermi-surface pairing condensates from vacuum order parameters such as the QCD
chiral condensate, the Higgs VEV, and possible dark-energy scalar backgrounds.
The useful correction is:

```text
Hawking-on:
  thermal disruption/melting can occur, but the micro-BH evaporates.

Hawking-off:
  no thermal melting should be assumed. The BH is a nonthermal absorbing sink,
  and condensate response must be treated through dense-medium QFT response.
```

For the chiral condensate, a local disturbance of:

```text
<qbar q>
```

should propagate through color-singlet QCD channels, not as a macroscopic color
wave:

```text
sigma / scalar-isoscalar response
pions and in-medium pion modes
sound, particle-hole, and possible phase-front modes
```

The chiral condensate itself is not an energy density; the relevant QCD
vacuum/bag contribution is of order:

```text
B_QCD ~ (150-250 MeV)^4
```

This is comparable to, but not vastly larger than, neutron-star matter density.
So it can modify the EOS, sound speed, latent heat, or phase-front energetics,
but it should not be counted as an extra universal fluid reservoir on top of
baryonic matter.

The main open fork is:

```text
A) UV/horizon-dominated absorption:
   the relevant scale is set by the small absorbing horizon, and chiral
   coherence gives little protection.

B) soft supply / EOS / phase-response dominated accretion:
   the relevant scale is set by p_F, c_s, r_B, gaps, and in-medium QCD response.
   Then chiral/EOS/phase-front physics can change the accretion law.
```

This should be tracked as an assumption, not silently decided:

```text
ASSUMPTION-NS-ACCRETION-UV-VS-SOFT-DOMINATED
MODEL-CHIRAL-CONDENSATE-PHASE-FRONT
MODEL-NS-BH-CATALYZED-CONVERSION
```

The current assessment is that vacuum condensates do not provide an obvious
many-order suppression or enhancement by themselves. Their plausible role is in
the dense-matter EOS and possible phase-conversion front around the absorbing
sink.

## 13. Current Implementation Problems

Before final submission:

1. Add superseded warnings to old LHC capture scripts.
2. Harmonize the cosmic-ray iron/nucleon-counting convention.
3. Clean IceCube wording: TeV-PeV flux observed; EeV/cosmogenic flux remains
   model-dependent and upper-limited.
4. Update README/PROJECT_SUMMARY from five layers to six layers.
5. Add `notes/claim_graph.yaml`.
6. Add focused notes on production/PDF cliff, direct searches, and exotic
   magnetic branches.
7. Add a toy suppression script for superfluid/condensate accretion.

## 14. Collaboration and Provenance

The project combines two investigation paths.

Valentin Slepukhin led much of the coding and conceptual decomposition work in
Claude Code, bringing a modeling background that now sits closer to soft
condensed matter and biophysics.

Andrey Sadofyev then added a particle-physics expert pass using Codex. His
current work is mainly QCD jets, jet quenching, and heavy-ion physics rather
than TeV-gravity model building, but the old BSM/LHC-safety literature was a
natural adjacent domain from earlier high-energy-theory training.

The workflow uses this division intentionally:

```text
AI-assisted reconstruction -> executable checks -> primary-source comparison ->
domain-adjacent expert/adversarial loophole search -> claim graph
```

The shared earlier institutional context and historical links through mentors
are optional background, not load-bearing evidence. The contest-facing point is
the complementary workflow, not biography.

## 15. Final Submission Plan

Early feedback package:

```text
contest_submission/submission_core_10pp.md
contest_submission/supporting_material_20pp.md
GitHub repository URL
contest_submission/form_answers.md
```

Final package:

```text
submission_core_10pp.md, revised
supporting_material_20pp.md, revised
notes/claim_graph.yaml
cleaned README/PROJECT_SUMMARY
script superseded warnings
one-page reuse protocol
```
