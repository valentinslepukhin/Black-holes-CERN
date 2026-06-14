# Summary from AS

Date: 2026-06-14

This file is a detailed working handoff compiled from the AS/Codex thread for
`valentinslepukhin/Black-holes-CERN`. It records the project frame, GitHub
state, literature map, physics questions discussed today, and concrete update
tasks. It intentionally overwrites the earlier short summary.

This is not a polished competition write-up. It is a working memo for the next
round of implementation and literature checking.

## 1. Project Frame

The repository is an entry for the Future of Life Foundation epistemic case
study competition, based on the LessWrong "Lab leaks, black holes, and eggs"
prompt.

The topic is:

```text
Will the LHC create a dangerous black hole?
```

But the judged object is not mainly a physics essay. The judged object is a
methodology plus an artifact:

- an updateable knowledge base,
- a claim/dependency graph,
- explicit assumptions,
- source attribution,
- algebraic/order-of-magnitude calculations,
- correction history,
- update triggers,
- and a way for readers to navigate where the argument is observational,
  calculational, model-dependent, or superseded.

The LHC black-hole case is useful because the headline conclusion is already
settled, while the dependency structure is subtle enough to expose weak links.

## 2. Repository State

Remote:

```text
https://github.com/valentinslepukhin/Black-holes-CERN
```

Local workspace used by Codex:

```text
/Users/sadofyev/Documents/BHs_compete
```

GitHub Desktop was installed and used to make GitHub authentication available.
The terminal push finally worked using GitHub Desktop's bundled Git Credential
Manager.

Current file:

```text
summary_from_AS.md
```

Earlier version of this file was created, committed, and pushed. This version is
the expanded replacement.

## 3. Existing Repository Structure

The repo contains:

```text
analysis/   order-of-magnitude Python calculations, stdlib only
notes/      layer-by-layer write-ups with assumptions logs
sources/    intended home for primary sources
README.md
PROJECT_SUMMARY.md
CLAUDE.md
summary_from_AS.md
```

The five implemented layers are:

1. `analysis/cosmic_ray_flux.py` and `notes/01-cosmic-ray-argument.md`
   - cosmic-ray vs. LHC collision rates.

2. `analysis/bh_earth_passage.py` and `notes/01`, `notes/02`
   - whether a cosmic-ray-produced black hole escapes Earth under four
     interaction hypotheses:
     A. gravity only,
     B. gravity plus weak,
     C. gravity plus strong,
     D. gravity plus electromagnetic.

3. `analysis/capture_and_accretion.py` and `notes/02`
   - capture statistics over 4.5 Gyr and accretion clocks versus number of extra
     dimensions.

4. `analysis/lhc_bh_fate.py`, `analysis/lhc_first_capture.py`, `notes/03`,
   `notes/04`
   - collider-produced black holes and the probability that the LHC traps one
     before nature does.

5. `notes/05-comparison-giddings-mangano.md`
   - direct diff against Giddings-Mangano 2008.

Important local limitation observed during this thread:

```text
sources/ currently contains only README.md, not the Giddings-Mangano PDF.
```

For future table/page-level work, download the Giddings-Mangano PDF and LSAG PDF
into `sources/`.

## 4. Primary Claim Structure

Do not write:

```text
Cosmic rays prove the LHC is safe.
```

That is too compressed.

Better:

```text
Earth/Sun cosmic-ray survival closes branches where produced black holes are
stopped in ordinary matter. The neutral gravity-only stable branch is not closed
by ordinary Earth cosmic-ray survival, because cosmic-ray-produced black holes
are ultra-relativistic and pass through ordinary matter. That branch is handled
by accretion slowness plus white-dwarf and neutron-star survival.
```

Compact dependency:

```text
fast danger -> astrophysically testable -> excluded
not astrophysically excluded -> too slow to be dangerous
```

The central safety statement:

```text
LHC-produced stable black holes are safe not because capture is impossible, but
because branches with fast Earth accretion are excluded by dense-star survival,
while branches not excluded by dense-star survival have Earth accretion times
far longer than the age of the Solar System.
```

## 5. Literature Spine Checked in This Thread

Primary safety and production sources:

- Giddings and Mangano, "Astrophysical implications of hypothetical stable
  TeV-scale black holes", arXiv:0806.3381.
  URL: https://arxiv.org/abs/0806.3381

- LSAG, "Review of the Safety of LHC Collisions", arXiv:0806.3414.
  URL: https://arxiv.org/abs/0806.3414

- Eardley and Giddings, "Classical Black Hole Production in High-Energy
  Collisions", arXiv:gr-qc/0201034.
  URL: https://arxiv.org/abs/gr-qc/0201034

- Yoshino and Rychkov, "Improved analysis of black hole formation in high-energy
  particle collisions", arXiv:hep-th/0503171.
  URL: https://arxiv.org/abs/hep-th/0503171

- Yoshino and Nambu, "Black hole formation in the grazing collision of
  high-energy particles", arXiv:gr-qc/0209003.
  URL: https://arxiv.org/abs/gr-qc/0209003

- Voloshin, "Semiclassical suppression of black hole production in particle
  collisions", arXiv:hep-ph/0107119.
  URL: https://arxiv.org/abs/hep-ph/0107119

Reviews and phenomenology:

- Park, "Black holes and the LHC: A review", arXiv:1203.4683.
  URL: https://arxiv.org/abs/1203.4683

- Bleicher and Nicolini, "Large extra dimensions and small black holes at the
  LHC", arXiv:1001.2211.
  URL: https://arxiv.org/abs/1001.2211

- Wondrak, Bleicher, Nicolini, "Black Holes and High Energy Physics: From
  Astrophysics to Large Extra Dimensions", arXiv:1708.06763.
  URL: https://arxiv.org/abs/1708.06763

Event generators and search modeling:

- CHARYBDIS, arXiv:hep-ph/0307305.
  URL: https://arxiv.org/abs/hep-ph/0307305

- BlackMax, arXiv:0711.3012.
  URL: https://arxiv.org/abs/0711.3012

- BlackMax manual, arXiv:0902.3577.
  URL: https://arxiv.org/abs/0902.3577

Recent direct searches:

- CMS 2026, "A search for microscopic black holes, string balls, and sphalerons
  in proton-proton collisions at sqrt(s)=13 TeV", arXiv:2604.10732.
  URL: https://arxiv.org/abs/2604.10732

- ATLAS 2026, "Search for quantum black holes in lepton+jet final states using
  proton-proton collisions at sqrt(s)=13.6 TeV", arXiv:2604.19495.
  URL: https://arxiv.org/abs/2604.19495

Astrophysical update areas checked:

- IceCube diffuse astrophysical neutrino flux, including 2024 and 2025 updates.
- Pierre Auger / Telescope Array UHECR spectrum and composition updates.
- LIGO/Virgo/KAGRA GWTC-3, GWTC-4, GWTC-5 population updates.
- Gaia-era white-dwarf catalog and magnetic/age/systematic updates.

## 6. BH Production Cross Section: Actual Approximation

The collider BH cross section is usually modeled as a geometric black-disk
cross section at parton level:

```text
hat_sigma_ij->BH(hat_s) ~= F(D) pi R_S^2(M_BH)
```

with

```text
M_BH = kappa sqrt(hat_s)
```

where:

- `D = 4 + n` is spacetime dimension,
- `M_D` is the higher-dimensional Planck scale,
- `M_BH` is the formed black-hole mass,
- `kappa` is the trapped-energy fraction,
- `F(D)` is an order-one form factor,
- `R_S` is the higher-dimensional Schwarzschild radius.

In Giddings-Mangano conventions:

```text
R(M) = (1/M_D) * (k_D M/M_D)^(1/(D-3))
```

with

```text
k_D = 2(2pi)^(D-4) / [(D-2) Omega_(D-2)]
Omega_m = 2 pi^((m+1)/2) / Gamma((m+1)/2)
```

Thus

```text
hat_sigma ~ M_BH^(2/(D-3))
```

which is a slow power of mass. Most rate sensitivity near the LHC endpoint does
not come from this slow power; it comes from the parton luminosity.

Core approximations:

1. Classical gravity is reliable once `M_BH >> M_D`.
2. The incoming partons are approximated as ultra-relativistic localized sources.
3. Formation is controlled by a hoop/trapped-surface criterion.
4. The proton collision factorizes into PDFs times a parton-level geometric
   cross section.
5. Threshold is imposed by `M_BH >= M_min = q M_D`, often with `q = 3` or `5`.
6. Energy not trapped into the hole is represented by `kappa`.

Leading correction if the zeroth-order geometric picture is accepted:

```text
trapped-surface / inelasticity / angular-momentum corrections
```

Eardley-Giddings supplied the classical apparent-horizon basis. Yoshino-Rychkov
improved the apparent-horizon slice and found production cross-section prefactor
increases of about 40-70 percent in higher-dimensional cases, relative to
earlier estimates. That is an order-one correction.

However, near LHC threshold, an order-one shift in trapped mass can cause an
order-of-magnitude shift in event rate because of the PDF cliff.

## 7. The PDF Cliff: Algebra

The hadronic production rate is

```text
sigma_pp->BH(S) =
  sum_ij int_(tau_min)^1 d tau
    dL_ij/dtau
    hat_sigma_ij(tau S^2)
```

where

```text
tau_min = M_min^2 / (kappa^2 S^2)
```

and

```text
dL_ij/dtau =
  int_tau^1 dx/x f_i(x,Q) f_j(tau/x,Q).
```

Near the endpoint, approximate a PDF as

```text
f_i(x,Q) ~= A_i(Q) (1 - x)^b_i
```

for `x -> 1`.

Then for `tau -> 1`,

```text
dL_ij/dtau proportional to (1 - tau)^(b_i + b_j + 1).
```

Define

```text
p = b_i + b_j + 1.
```

Ignoring the slow geometric mass dependence for the moment:

```text
ln sigma ~= p ln(1 - tau_min) + slowly varying terms.
```

Since

```text
tau_min = M_min^2 / (kappa^2 S^2),
```

the logarithmic sensitivity to threshold mass is

```text
d ln sigma / d ln M_min ~= - 2 p tau_min / (1 - tau_min).
```

The sensitivity to collider energy is

```text
d ln sigma / d ln S ~= + 2 p tau_min / (1 - tau_min).
```

The sensitivity to trapped fraction is

```text
d ln sigma / d ln kappa ~= + 2 p tau_min / (1 - tau_min).
```

Example:

```text
S = 13 TeV
M_min = 10 TeV
kappa = 1
tau_min = (10/13)^2 = 0.592
2 tau/(1 - tau) = 2.90
```

If `p = 8`, then:

```text
d ln sigma / d ln M_min ~= -23.2.
```

A 5 percent increase in effective threshold gives

```text
Delta ln sigma ~= -23.2 * 0.05 = -1.16
sigma factor ~= exp(-1.16) ~= 0.31.
```

A 10 percent increase gives

```text
Delta ln sigma ~= -2.32
sigma factor ~= 0.10.
```

This is the PDF cliff.

It also explains why small increases in beam energy matter near threshold. At
fixed `M_min`, increasing `S` decreases `tau_min`. The same derivative changes
sign:

```text
d ln sigma / d ln S ~= +23.2
```

so a 4.6 percent energy increase, such as 13.0 to 13.6 TeV, can plausibly give

```text
Delta ln sigma ~= 23.2 * 0.046 ~= 1.07
sigma factor ~= 2.9
```

For even higher threshold, say `M/S` closer to 0.85-0.90, the factor can become
larger, consistent with ATLAS noting order-of-magnitude effects at the highest
masses.

Effect of trapped-energy fraction:

```text
tau_min(kappa) = tau_min(kappa=1) / kappa^2.
```

If `kappa = 0.8`, then

```text
tau_min -> 1.56 tau_min.
```

At high masses this can move a point from rare to impossible. Therefore:

```text
PDF uncertainty + threshold convention + kappa dominate LHC endpoint rates.
```

The geometric radius prefactor is much less steep:

```text
hat_sigma ~ M^(2/(D-3)).
```

For `D = 8`, this is `M^0.4`, negligible compared with the high-x PDF falloff.

## 8. Hawking Radiation While the BH Is Flying

Question:

```text
If Hawking radiation exists, does it stop a flying microscopic BH faster? Does
directional beaming matter? Does it change neutron-star lifetime estimates?
```

Answer:

If ordinary Hawking radiation exists, the dangerous stable-BH branch largely
disappears, because the object evaporates. That is why Giddings-Mangano analyze
the extreme pessimistic branch where Hawking decay is absent or ineffective.

For the kinematics:

- In the BH rest frame, emission is approximately isotropic for a neutral,
  non-rotating hole, up to greybody and spin effects.
- In the lab frame, the radiation is forward-beamed by Lorentz boost.
- But if rest-frame emission is isotropic, the 4-force is parallel to the
  4-momentum:

```text
dP^mu/dtau = - (Gamma_H/M) P^mu.
```

This reduces rest mass and lab momentum in the same proportion. It does not
act like ordinary friction that drives the velocity to zero.

Thus:

```text
Hawking emission lowers M and total energy.
It does not, by itself, strongly reduce v for isotropic rest-frame emission.
```

If there is both accretion and Hawking loss:

```text
dM/dt = Mdot_acc - Mdot_H.
```

If `Mdot_H > Mdot_acc`, the BH evaporates. If `Mdot_acc > Mdot_H`, it grows.

For neutron-star lifetime estimates:

- A captured BH with normal Hawking radiation may evaporate or fail to grow.
- Then neutron-star survival is not needed to exclude catastrophe.
- Including Hawking radiation weakens the need for the dense-star exclusion
  argument, but strengthens safety.

Claim-graph implication:

```text
Hawking-radiating branch -> direct evaporation / no long-lived hazard.
Stable-or-remnant branch -> requires Giddings-Mangano accretion and dense-star
survival analysis.
```

## 9. Medium-Induced Radiation

Question:

```text
Could medium-induced radiation, analogous to jet quenching, cause important
additional BH energy loss?
```

For the dangerous neutral gravity-only branch, the QCD jet analogy is not the
right leading model. A QCD jet radiates because it carries color and repeatedly
scatters through strong interactions in a colored medium. The dangerous branch
is specifically a neutralized BH interacting only gravitationally.

For weak gravitational scattering with deflection angle `theta`, the elastic
energy transfer scales like

```text
Delta E_elastic ~ (1/2) m v^2 theta^2.
```

Radiative loss from the acceleration is an additional higher-order correction.
Parametrically:

```text
Delta E_radiative <= correction to Delta E_elastic
```

unless the scattering is already strong.

So:

- If elastic gravitational stopping is tiny, medium-induced gravitational
  radiation is tinier.
- If scattering is strong enough that radiation is large, ordinary capture and
  accretion drag are already efficient.
- If the BH remains charged or colored, medium-induced EM/QCD radiation could be
  substantial, but that is not the neutral gravity-only dangerous branch.

Useful claim-graph node:

```text
Medium-induced radiation is probably a subleading correction to stopping for
neutral gravity-only remnants, but can be relevant in charged/colored branches.
```

Next calculation target:

```text
Add an OOM bound comparing radiative gravitational loss per scattering with the
elastic gravitational energy transfer already used in stopping estimates.
```

## 10. pp BH Production Versus Neutrino-Nucleon/Nucleus BH Production

Question:

```text
Does BH formation from pp differ substantially from BH formation from
neutrino+nucleon or neutrino+nucleus?
```

Yes. The local parton-level geometric cross section may be the same function of
`hat_s`, but the convolution and kinematics differ.

For pp:

```text
sigma_pp =
  sum_ij int dx1 dx2
    f_i(x1,Q) f_j(x2,Q)
    hat_sigma(x1 x2 S^2).
```

Two PDFs enter. Near high mass, both incoming partons may require large `x`.

For neutrino-nucleon fixed-target production:

```text
sigma_nuN =
  sum_i int_(x_min)^1 dx
    f_i(x,Q)
    hat_sigma(2 x m_N E_nu).
```

Only one nucleon PDF enters. Threshold:

```text
x_min = M_min^2 / (2 m_N E_nu kappa^2).
```

For a nuclear target:

```text
sigma_nuA ~= sum_N int d geometry * nuclear PDFs * sigma_nuN
```

with nuclear modifications and shadowing at relevant `x,Q`, but the energy does
not coherently add over the whole nucleus into one microscopic BH.

Key differences:

1. pp has two parton-luminosity penalties; neutrino-nucleon has one.
2. Neutrino production needs enormous lab-frame `E_nu`.
3. The produced BH in a cosmic fixed-target event is highly boosted in the star
   frame.
4. In ordinary Earth matter, a neutral boosted BH passes through.
5. In a neutron star, the production point is inside enormous density/column, so
   capture can be much more plausible.
6. Neutrino flavor matters much less than the total high-energy flux, because
   gravity is flavor-universal at the hard process level.

Therefore:

```text
Do not reuse pp rates for neutrino-star production.
Use the same hat_sigma, but a different luminosity integral, flux integral, and
capture/stopping model.
```

For cosmic-ray nuclei:

```text
E_CR,min(A) ~= A S^2 / (2 m_p)
```

because the relevant energy is per nucleon. This is why proton versus iron
composition matters for cosmic-ray comparators.

## 11. Beam/Ray "Flavor" and Composition

For LHC pp:

- Gravity is approximately flavor-blind at the parton-level BH formation step.
- Quark/gluon identity matters through PDFs and through the initial conserved
  charges/color/angular momentum that must be shed.
- High-mass production probes high `x`; quark channels become more important
  relative to gluons than at low `x`.

For cosmic rays:

- Proton versus iron matters because the per-nucleon energy differs.
- Pure-proton assumptions maximize the high-energy nucleon flux.
- Heavy composition weakens ordinary Earth cosmic-ray comparator margins.
- White dwarfs and neutron stars are the relevant dense-body branches.

For neutrinos:

- Flavor is not the leading issue for BH production.
- The key issue is the UHE/cosmogenic flux normalization and spectrum.
- IceCube has observed TeV-PeV astrophysical neutrinos, partly upgrading the
  old neutrino-flux node, but it does not automatically settle every EeV or
  cosmogenic flux assumption used in 2008.

## 12. Direct LHC Searches and Decay Channels

Modern ATLAS/CMS searches do not cover "all possible black holes". They cover
specific prompt visible benchmark signatures.

CMS 2026:

- searches for microscopic black holes, string balls, and sphalerons in 13 TeV
  pp data,
- uses high-multiplicity energetic final states,
- sets model-independent limits on multi-object final states,
- interprets model-dependent limits for ADD semiclassical black holes and string
  balls,
- excludes semiclassical BH masses below about 8.4-11.4 TeV in the benchmark
  models.

ATLAS 2026:

- searches for quantum black holes in high-mass lepton+jet final states at
  13.6 TeV,
- uses 2022-2024 Run 3 data,
- sets limits on cross section times branching ratio,
- reaches mass scales around 9.4 TeV in benchmark models,
- explicitly notes that the 13.0 to 13.6 TeV energy increase can raise the
  highest-mass cross section by up to an order of magnitude.

The event-count equation is:

```text
N_seen = L_int * sigma_BH * BR_visible * A * epsilon.
```

where:

- `L_int` is integrated luminosity,
- `sigma_BH` is production cross section,
- `BR_visible` is branching ratio into the searched visible final state,
- `A` is detector acceptance,
- `epsilon` is reconstruction/selection efficiency.

If the BH decays mostly invisibly:

```text
BR_visible << 1
```

then prompt visible searches weaken directly.

Searches do not fully cover:

- mostly invisible decays to neutrinos, gravitons, or hidden sectors,
- stable neutral remnants,
- long-lived decays outside the detector,
- low-visible-energy decays,
- unusual displaced signatures,
- stable charged remnants unless a dedicated heavy-stable-charged-particle
  search is applied,
- model variants with suppressed brane emission.

In standard semiclassical ADD Hawking models, visible SM emission is expected to
dominate because many SM degrees of freedom live on the brane. But that is a
model assumption, not a universal theorem for every exotic remnant branch.

Claim-graph wording:

```text
Modern direct searches strongly constrain prompt visible semiclassical/quantum
BH benchmark branches. They do not replace the stable/invisible dangerous-
remnant astrophysical safety argument.
```

## 13. Other Mechanisms That Change the LHC BH Rate

Rate-changing inputs:

1. `M_D` convention and numerical definition.
2. `M_min/M_D` threshold choice.
3. Trapped-energy fraction `kappa`.
4. Impact-parameter cutoff and form factor `F(D)`.
5. Angular momentum of produced BH.
6. Brane tension or brane thickness.
7. Split fermions or nontrivial localization in extra dimensions.
8. Warped geometry versus flat ADD geometry.
9. Bulk graviton channels.
10. String-ball phase below true semiclassical BH threshold.
11. Quantum-BH phase near threshold.
12. Possible Voloshin-type exponential suppression.
13. PDF uncertainties at high `x`.
14. Beam energy.
15. Integrated luminosity.

Things unlikely to help:

- Pileup does not coherently combine many pp collisions into one microscopic BH.
- Total heavy-ion energy does not coherently form one microscopic BH in the
  standard partonic channel; local `sqrt(hat_s)` matters.

Beam energy is especially important near threshold because of the PDF cliff:

```text
d ln sigma / d ln S ~= 2 p tau/(1 - tau).
```

Luminosity scales event count linearly:

```text
N_BH = L_int sigma_BH.
```

But luminosity does not change the per-collision physics.

## 14. Neutron Stars, White Dwarfs, and GW Updates

Giddings-Mangano use dense astrophysical objects as natural detectors:

- white dwarfs for some lower-D branches,
- neutron stars for higher-D branches, especially with neutrino production.

Modern gravitational-wave observations update:

- neutron-star radius constraints,
- maximum mass / equation-of-state constraints,
- binary neutron-star and neutron-star-black-hole merger rates,
- compact-object population rates.

But they do not obviously undermine the old "old neutron stars exist" survival
argument.

Relevant update points from the literature scan:

- GW170817 improved constraints on neutron-star radii and dense-matter EOS.
- GWTC-3 inferred broad BNS rates around 10-1700 Gpc^-3 yr^-1.
- Later analyses push BNS rates lower; one 2026 GWTC-4-based paper quotes
  roughly 28-300 Gpc^-3 yr^-1.
- GWTC-5.0 in May 2026 reported no new neutron-star sources and mainly updated
  black-hole population properties.

Impact on the safety argument:

```text
Mostly factor-of-few parameter updates, not multi-decade changes.
```

The branch should still be marked update-sensitive because:

- neutron-star EOS affects radius/compactness/density profiles,
- old neutron-star population assumptions matter,
- magnetic-field and binary-companion environments matter,
- UHE/cosmogenic neutrino flux remains a load-bearing input for the D >= 8
  branch.

## 15. Future Machines

HL-LHC:

- changes luminosity/statistics,
- not the fundamental pp energy frontier,
- planned integrated luminosity around 3000 fb^-1,
- does not qualitatively change the 14 TeV safety structure.

FCC-hh:

- changes energy frontier, roughly 85-100 TeV pp class,
- must be a separate claim-graph branch.

Fixed-target cosmic-ray comparator:

```text
E_CR ~= S^2 / (2 m_p)
```

So:

```text
S = 14 TeV  -> E_CR ~ 1e17 eV
S = 100 TeV -> E_CR ~ 5e18 eV
```

If the integral flux scales like an `E^-3` differential spectrum:

```text
Phi(>E_min) ~ E_min^-2 ~ S^-4.
```

Going from 14 TeV to 100 TeV reduces the simple comparator flux by about:

```text
(100/14)^4 ~ 2600.
```

Therefore the old LHC numerical margins should not be blindly copied to FCC.
The dependency logic may transfer, but the numbers must be recalculated.

Heavy ions:

- Standard microscopic BH production is local/partonic.
- Relevant energy is parton-parton `sqrt(hat_s)`, not total `A sqrt(s_NN)`.
- A coherent many-body gravitational-collapse mechanism would be a separate
  model assumption.

## 16. Corrections and Guardrails

Preserve these expert-safe wordings:

```text
conditional on TeV-gravity/stable-remnant assumptions
order-of-magnitude regression
load-bearing node
update-sensitive input
branch of the dependency graph
not a replacement for the safety proof
```

Avoid:

```text
Cosmic rays prove the LHC is safe.
IceCube settles the old neutrino node.
Modern LHC limits replace the safety proof.
Heavy-ion total energy can make one huge microscopic BH.
Capture is impossible.
```

Use:

```text
Earth/Sun survival closes stopped-in-ordinary-matter branches.
IceCube partially upgrades the astrophysical-neutrino node.
Modern direct searches constrain prompt visible benchmark branches.
Heavy-ion BH production is local/partonic unless a separate coherent mechanism
is specified.
Capture can happen for light stable BHs; the safety case rests on accretion
slowness and astrophysical exclusion.
```

Important correction from Giddings-Mangano Appendix F:

```text
The earlier project estimate that LHC trapping was about 3 percent was wrong.
Low-velocity accretion drag and flat rapidity behavior can make trapping much
larger for light BHs. The safety argument should not rest on capture being
improbable.
```

## 17. Claim Graph Schema Recommendation

Use a machine-readable node schema like:

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

Example load-bearing nodes:

```text
CALC-PP-BH-PRODUCTION-GEOMETRIC
CALC-PDF-CLIFF-HIGH-X
MODEL-VOLOSHIN-SUPPRESSION-DISPUTED
CALC-CR-FIXED-TARGET-THRESHOLD
OBS-CR-EARTH-COUNT
CALC-NEUTRAL-CR-PASS-THROUGH
OBS-WD-OLD-MASSIVE-LOW-B
CALC-WD-CAPTURE-DLE7
OBS-OLD-NEUTRON-STARS
CALC-NS-NEUTRINO-PRODUCTION-DGE8
UPDATE-ICECUBE-TEV-PEV-FLUX
UPDATE-LVK-NS-EOS-RATES
UPDATE-LHC-RUN3-DIRECT-LIMITS
CORR-LHC-CAPTURE-TAIL
```

## 18. Files/Sources to Download Into `sources/`

Priority downloads:

1. Giddings-Mangano 2008 PDF:
   https://arxiv.org/pdf/0806.3381

2. LSAG 2008 PDF:
   https://arxiv.org/pdf/0806.3414

3. Eardley-Giddings 2002 PDF:
   https://arxiv.org/pdf/gr-qc/0201034

4. Yoshino-Rychkov 2005 PDF:
   https://arxiv.org/pdf/hep-th/0503171

5. Park 2012 review PDF:
   https://arxiv.org/pdf/1203.4683

6. Wondrak-Bleicher-Nicolini 2017 PDF:
   https://arxiv.org/pdf/1708.06763

7. CMS 2026 BH/string-ball/sphaleron search PDF:
   https://arxiv.org/pdf/2604.10732

8. ATLAS 2026 quantum-BH lepton+jet search PDF:
   https://arxiv.org/pdf/2604.19495

Possible update-source PDFs:

- IceCube diffuse astrophysical flux 2024:
  https://arxiv.org/abs/2402.18026

- Pierre Auger UHECR review after 15 years:
  https://arxiv.org/abs/2309.01259

- GWTC-3 compact-binary population:
  https://arxiv.org/abs/2111.03634

- GWTC-5.0 population properties:
  https://arxiv.org/abs/2605.27226

## 19. Next Implementation Tasks

1. Add `analysis/bh_geometry.py`
   - `omega_sphere(dim)`
   - `k_D(D)`
   - `schwarzschild_radius(M, M_D, D)`
   - regression values from Giddings-Mangano if available.

2. Add or update `analysis/pp_production.py`
   - geometric cross section,
   - threshold/inelasticity,
   - toy PDF mode,
   - optional tabulated PDF hook,
   - explicit PDF-cliff sensitivity derivatives.

3. Add `analysis/neutrino_bh_production.py`
   - fixed-target neutrino-nucleon threshold,
   - one-PDF convolution,
   - nuclear target notes,
   - flux integration hooks.

4. Add `notes/06-production-and-pdf-cliff.md`
   - derive the formulas in Sections 6-7 above,
   - include clean examples for 13, 13.6, and 14 TeV.

5. Add `notes/07-radiation-and-stopping.md`
   - Hawking radiation branch,
   - medium-induced radiation estimate,
   - why neutral gravity-only medium radiation is subleading,
   - what changes if the BH remains charged/colored.

6. Add `notes/08-direct-searches-and-decay-channels.md`
   - prompt visible searches,
   - invisible/stable/long-lived loopholes,
   - relation to astrophysical safety proof.

7. Add a claim graph file:

```text
claims/claim_graph.json
```

or

```text
notes/claim_graph.yaml
```

8. Verify Giddings-Mangano Appendix H:
   - determine whether the bound-solar-orbit decay-into-Sun channel in
     `notes/04-lhc-first-probability.md` is new or already covered.

9. Run the 2008-to-2026 update pass:
   - IceCube flux,
   - Gaia white dwarfs,
   - LVK neutron-star constraints,
   - ATLAS/CMS direct BH limits,
   - UHECR composition/spectrum.

## 20. Bottom Line

The strongest artifact should make this structure navigable:

```text
1. Production is model-dependent and suffers a high-x PDF cliff near the LHC
   endpoint.

2. Direct LHC searches constrain prompt visible benchmark decays, not every
   stable/invisible remnant branch.

3. If Hawking radiation works normally, microscopic BHs evaporate and are not a
   hazard.

4. The pessimistic stable-remnant branch is handled by stopping, accretion, and
   dense-star survival.

5. Earth/Sun survival closes stopped-in-ordinary-matter branches.

6. Neutral gravity-only cosmic-ray-produced BHs pass through ordinary matter, so
   white dwarfs and neutron stars are the load-bearing astrophysical tests.

7. Fast danger implies astrophysical testability; unexcluded branches are too
   slow to matter on Solar-System timescales.
```

That is the case study's real value: not the slogan "the LHC is safe", but the
explicit decomposition of why confidence is warranted, what depends on what,
and which nodes must be updated as the literature changes.
