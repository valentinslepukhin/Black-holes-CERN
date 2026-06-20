# Summary from AS

Date: 2026-06-17

This file is a working handoff compiled from the AS/Codex thread for
`valentinslepukhin/Black-holes-CERN`. It replaces the previous AS summary and
folds in the later discussion on nonlinear/exotic semiclassical gravity,
black-hole-like states, heavy-ion angular momentum, magnetically charged black
holes, slow neutron-star consumption, pp versus neutrino production, and
heavy-ion magnetic-field production.

This is not meant to be a polished final essay. It is a research and
implementation memo for the next project round.

## 1. Project Frame

The repository is an entry for the Future of Life Foundation epistemic case
study competition, based on the LessWrong "Lab leaks, black holes, and eggs"
prompt.

The headline question is:

```text
Will the LHC create a dangerous black hole?
```

The judged object should not be only a physics essay. It should be a navigable
epistemic artifact:

- an updateable knowledge base,
- a claim/dependency graph,
- explicit assumptions and parameter scopes,
- source attribution,
- algebraic/order-of-magnitude calculations,
- correction history,
- update triggers,
- and a way for readers to see which parts are observational, calculational,
  model-dependent, disputed, or superseded.

The black-hole-safety case is valuable because the conclusion is already
strong, while the dependency structure is subtle. The artifact should make that
structure visible.

## 2. Repository and Git State

Remote:

```text
https://github.com/valentinslepukhin/Black-holes-CERN
```

Local workspace:

```text
/Users/sadofyev/Documents/BHs_compete
```

Current branch:

```text
main
```

Current AS handoff file:

```text
summary_from_AS.md
```

GitHub Desktop is installed and provides the credential helper used for pushes.
The terminal push command that worked earlier was:

```text
git -c credential.helper= \
  -c "credential.helper=!'/Applications/GitHub Desktop.app/Contents/Resources/app/git/libexec/git-core/git-credential-manager'" \
  push origin main
```

## 3. Existing Repository Structure

The repo currently contains:

```text
analysis/   order-of-magnitude Python calculations, stdlib only
notes/      layer-by-layer write-ups with assumptions logs
sources/    intended home for primary sources
README.md
PROJECT_SUMMARY.md
CLAUDE.md
summary_from_AS.md
```

Important files:

- `analysis/cosmic_ray_flux.py`
  - cosmic-ray versus LHC collision counts.

- `analysis/bh_earth_passage.py`
  - stopping/escape estimates for four interaction hypotheses:
    gravity only, gravity plus weak, gravity plus strong, and gravity plus EM.

- `analysis/capture_and_accretion.py`
  - capture statistics and Earth accretion clocks.

- `analysis/lhc_bh_fate.py`
  - older LHC capture estimate. It still contains superseded slow-tail logic.

- `analysis/lhc_first_capture.py`
  - older "who captures first" estimate. Also superseded by the
    Giddings-Mangano Appendix F correction.

- `analysis/ns_capture_consumption.py`
  - neutron-star capture and consumption OOM estimates.

- `notes/01-cosmic-ray-argument.md`
  - cosmic-ray comparator.

- `notes/02-capture-and-accretion.md`
  - stopping and accretion.

- `notes/03-lhc-produced-bh.md`
  - LHC-produced BH fate.

- `notes/04-lhc-first-probability.md`
  - LHC first-capture probability with correction box.

- `notes/05-comparison-giddings-mangano.md`
  - direct comparison with Giddings-Mangano.

- `notes/06-neutron-star-bound.md`
  - neutron-star bound module.

- `notes/research-gaps.md`
  - best current list of load-bearing unresolved questions.

- `notes/review-of-AS-summary.md`
  - review notes from the first AS summary.

Current local source limitation:

```text
sources/ currently contains only README.md, not the PDFs.
```

For page/table-level work, download at least Giddings-Mangano 2008 and LSAG
2008 into `sources/`.

## 4. Core Safety Claim

Avoid the compressed slogan:

```text
Cosmic rays prove the LHC is safe.
```

Use the more precise form:

```text
Earth/Sun cosmic-ray survival closes branches where produced black holes are
stopped in ordinary matter. The neutral gravity-only stable branch is not
closed by ordinary Earth cosmic-ray survival, because cosmic-ray-produced black
holes are ultra-relativistic and pass through ordinary matter. That branch is
handled by accretion slowness plus white-dwarf and neutron-star survival.
```

Compact dependency:

```text
fast danger -> astrophysically testable -> excluded
not astrophysically excluded -> too slow to be dangerous
```

The most robust safety statement is:

```text
LHC-produced stable black holes are safe not because capture is impossible, but
because branches with fast Earth accretion are excluded by dense-star survival,
while branches not excluded by dense-star survival have Earth accretion times
far longer than the age of the Solar System.
```

Important correction:

```text
The safety case must not rest on LHC capture being improbable.
```

Giddings-Mangano Appendix F shows that low-velocity accretion drag and the
rapidity distribution can make capture of light stable LHC black holes much
larger than the early project estimate. Earlier scripts that print small LHC
capture probabilities should be marked superseded or rewritten.

## 5. Literature Spine

Primary safety and production sources:

- Giddings and Mangano, "Astrophysical implications of hypothetical stable
  TeV-scale black holes", arXiv:0806.3381.
  URL: https://arxiv.org/abs/0806.3381

- LSAG, "Review of the Safety of LHC Collisions", arXiv:0806.3414.
  URL: https://arxiv.org/abs/0806.3414

- Eardley and Giddings, "Classical Black Hole Production in High-Energy
  Collisions", arXiv:gr-qc/0201034.
  URL: https://arxiv.org/abs/gr-qc/0201034

- Yoshino and Rychkov, "Improved analysis of black hole formation in
  high-energy particle collisions", arXiv:hep-th/0503171.
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

Recent direct searches checked in this thread:

- CMS 2026, microscopic black holes, string balls, and sphalerons in 13 TeV pp,
  arXiv:2604.10732.
  URL: https://arxiv.org/abs/2604.10732

- ATLAS 2026, quantum black holes in lepton+jet final states at 13.6 TeV,
  arXiv:2604.19495.
  URL: https://arxiv.org/abs/2604.19495

Astrophysical update areas:

- IceCube diffuse astrophysical neutrino flux, including 2024 updates.
  URL: https://arxiv.org/abs/2402.18026

- Pierre Auger / Telescope Array UHECR spectrum and composition updates.
  URLs: https://arxiv.org/abs/2210.05745 and
  https://arxiv.org/abs/2406.19286

- LIGO/Virgo/KAGRA GWTC-3 and GWTC-5 population updates.
  URLs: https://arxiv.org/abs/2111.03634 and
  https://arxiv.org/abs/2605.27226

Magnetic and exotic branches:

- Lee, Nair, Weinberg, black holes in magnetic monopoles,
  arXiv:hep-th/9112008.
  URL: https://arxiv.org/abs/hep-th/9112008

- Gould and Rajantie, monopole Schwinger production in heavy-ion collisions,
  arXiv:1705.07052.
  URL: https://arxiv.org/abs/1705.07052

- MoEDAL monopole searches, including heavy-ion/Schwinger-production searches.
  URLs: https://arxiv.org/abs/1903.08491,
  https://arxiv.org/abs/2106.11933, https://arxiv.org/abs/2402.15682

- ATLAS highly ionizing particle / monopole searches.
  URLs: https://arxiv.org/abs/2308.04835 and
  https://arxiv.org/abs/2408.11035

- Born-Infeld-inspired gravity review.
  URL: https://arxiv.org/abs/1704.03351

- EiBI phenomenology.
  URL: https://arxiv.org/abs/1201.2814

- Higher-curvature collider BH corrections.
  URL: https://arxiv.org/abs/hep-ph/0503163

- Rychkov critique of TeV BH production.
  URL: https://arxiv.org/abs/hep-ph/0401116

- Asymptotic-safety black holes.
  URL: https://arxiv.org/abs/1002.0260

- Asymptotic-safety review.
  URL: https://arxiv.org/abs/2212.09495

- Noncommutative / regular BH collider phenomenology.
  URLs: https://arxiv.org/abs/1003.1798 and
  https://arxiv.org/abs/1111.5830

## 6. BH Production Cross Section

The standard collider estimate is a geometric black-disk cross section at
parton level:

```text
hat_sigma_ij->BH(hat_s) ~= F(D) pi R_S^2(M_BH)
M_BH = kappa sqrt(hat_s)
```

where:

- `D = 4 + n` is spacetime dimension,
- `M_D` is the higher-dimensional Planck scale,
- `M_BH` is the trapped black-hole mass,
- `kappa` is the trapped-energy fraction,
- `F(D)` is an order-one form factor,
- `R_S` is the higher-dimensional Schwarzschild radius.

Giddings-Mangano convention:

```text
R(M) = (1/M_D) * (k_D M/M_D)^(1/(D-3))
k_D = 2(2pi)^(D-4) / [(D-2) Omega_(D-2)]
Omega_m = 2 pi^((m+1)/2) / Gamma((m+1)/2)
```

Thus:

```text
hat_sigma ~ M_BH^(2/(D-3))
```

The geometric factor is a slow power of mass. Near the LHC endpoint, the main
rate sensitivity comes from parton luminosities and threshold conventions, not
from the slow radius power.

Core approximations:

1. Classical gravity is reliable once `M_BH >> M_D`.
2. Incoming partons can be approximated as ultra-relativistic localized
   gravitational sources.
3. Formation is controlled by a hoop/trapped-surface criterion.
4. Proton collision rates factorize into PDFs times a parton-level geometric
   cross section.
5. A threshold `M_BH >= M_min = q M_D` is imposed, often with `q = 3` or `5`.
6. Energy not trapped into the hole is summarized by `kappa`.

Leading correction if the geometric picture is accepted:

```text
trapped-surface / inelasticity / angular-momentum corrections
```

Eardley-Giddings supplied the classical trapped-surface basis. Yoshino-Rychkov
improved the apparent-horizon slice and found order-one changes in the
production prefactor. Near threshold, even order-one changes in trapped mass can
turn into order-of-magnitude rate changes because of the PDF cliff.

## 7. PDF Cliff Algebra

Hadronic production rate:

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

and:

```text
dL_ij/dtau =
  int_tau^1 dx/x f_i(x,Q) f_j(tau/x,Q)
```

Near the endpoint:

```text
f_i(x,Q) ~= A_i(Q) (1 - x)^b_i
```

so for `tau -> 1`:

```text
dL_ij/dtau proportional to (1 - tau)^(b_i + b_j + 1)
```

Define:

```text
p = b_i + b_j + 1
```

Ignoring slow geometric variation:

```text
ln sigma ~= p ln(1 - tau_min)
```

Since:

```text
tau_min = M_min^2 / (kappa^2 S^2)
```

the threshold sensitivity is:

```text
d ln sigma / d ln M_min ~= - 2 p tau_min / (1 - tau_min)
d ln sigma / d ln S     ~= + 2 p tau_min / (1 - tau_min)
d ln sigma / d ln kappa ~= + 2 p tau_min / (1 - tau_min)
```

Example:

```text
S = 13 TeV
M_min = 10 TeV
kappa = 1
tau_min = (10/13)^2 = 0.592
2 tau/(1 - tau) = 2.90
p = 8
d ln sigma / d ln M_min ~= -23.2
```

A 5 percent threshold increase gives:

```text
Delta ln sigma ~= -23.2 * 0.05 = -1.16
sigma factor ~= exp(-1.16) ~= 0.31
```

A 10 percent threshold increase gives:

```text
Delta ln sigma ~= -2.32
sigma factor ~= 0.10
```

An energy increase from 13.0 to 13.6 TeV is 4.6 percent, so at the same point:

```text
Delta ln sigma ~= 23.2 * 0.046 ~= 1.07
sigma factor ~= 2.9
```

The trapped-energy fraction enters through:

```text
tau_min(kappa) = tau_min(kappa=1) / kappa^2
```

If `kappa = 0.8`, then:

```text
tau_min -> 1.56 tau_min
```

At high mass this can move a benchmark from rare to impossible. Therefore:

```text
PDF uncertainty + threshold convention + kappa dominate LHC endpoint rates.
```

## 8. Hawking Radiation, Directionality, and Medium-Induced Radiation

If ordinary Hawking radiation exists, the dangerous stable-BH branch mostly
disappears because the microscopic BH evaporates.

For motion through the lab:

- In the BH rest frame, emission from a neutral non-rotating hole is
  approximately isotropic, up to greybody and spin corrections.
- In the lab frame, radiation is Lorentz-beamed forward.
- But if rest-frame emission is isotropic, the 4-force is parallel to the
  4-momentum:

```text
dP^mu/dtau = - (Gamma_H/M) P^mu
```

So mass and lab momentum fall proportionally. This is not ordinary friction
that strongly drives the speed to zero.

With both accretion and Hawking loss:

```text
dM/dt = Mdot_acc - Mdot_H
```

If `Mdot_H > Mdot_acc`, the BH evaporates. If `Mdot_acc > Mdot_H`, it grows.

For neutron-star estimates:

```text
Hawking-radiating branch -> evaporation / no long-lived hazard
stable-or-remnant branch -> dense-star stopping and accretion analysis
```

Medium-induced radiation:

- For a neutral gravity-only remnant, the QCD jet-quenching analogy is not the
  leading model.
- A QCD jet radiates strongly because it carries color through a colored
  medium.
- The dangerous remnant branch is neutralized and interacts mainly
  gravitationally.

For weak scattering with deflection angle `theta`:

```text
Delta E_elastic ~ (1/2) m v^2 theta^2
```

Radiative gravitational loss from acceleration is a higher-order correction
unless the scattering is already strong. If elastic gravitational stopping is
tiny, medium-induced gravitational radiation is tinier. If scattering is strong,
ordinary stopping/capture is already efficient.

Charged or colored remnants are different. EM/QCD radiation can be relevant
there, but those are not the neutral gravity-only branch.

## 9. pp Production Versus Neutrino-Nucleon Production

The local parton-level cross section may be the same function of `hat_s`, but
the convolution is different.

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

Differences:

1. pp has two PDFs; neutrino-nucleon has one nucleon PDF.
2. pp and nu-N can probe different initial-state assumptions if matter fields
   are localized differently on a brane or in flavor space.
3. Neutrino flavor is not the leading issue for gravity-mediated production;
   UHE flux normalization is more important.
4. Neutrino-produced BHs inside dense stars are born inside large column
   density, making capture more plausible than for Earth atmosphere events.

Important fallback:

```text
Even if nu-N production is suppressed or absent, cosmic p-N and nucleus-N
collisions still test pp-like partonic production.
```

For a cosmic proton hitting a stationary proton:

```text
s ~= 2 m_p E_CR
sqrt(s) ~= sqrt(2 m_p E_CR)
```

The LHC at `sqrt(s)=14 TeV` corresponds to:

```text
E_CR ~= (14 TeV)^2 / (2 m_p) ~= 1e17 eV
```

Observed UHE cosmic rays reach `~10^20 eV`, giving:

```text
sqrt(s) ~= 430 TeV
```

For an iron nucleus with total energy `10^20 eV`, the per-nucleon energy is
`~1.8e18 eV`, giving nucleon-nucleon:

```text
sqrt(s_NN) ~= 58 TeV
```

So if `pp` works but `nu-N` does not, the cosmic-ray argument is weakened in
the neutron-star neutrino channel, but it is not gone. The project should keep
two separate branches:

```text
nu-N dense-star production branch
p-N / nucleus-N cosmic-ray pp-like branch
```

## 10. Direct Searches and Decay Channels

Modern ATLAS/CMS searches constrain specific prompt visible benchmarks. They do
not cover every possible BH-like object.

Event-count equation:

```text
N_seen = L_int * sigma_BH * BR_visible * A * epsilon
```

where:

- `L_int` is integrated luminosity,
- `sigma_BH` is production cross section,
- `BR_visible` is branching ratio into the searched final state,
- `A` is detector acceptance,
- `epsilon` is reconstruction/selection efficiency.

If:

```text
BR_visible << 1
```

then prompt visible searches weaken.

Search gaps include:

- mostly invisible decays to neutrinos, gravitons, or hidden sectors,
- stable neutral remnants,
- long-lived decays outside the detector,
- low-visible-energy decays,
- unusual displaced signatures,
- stable charged remnants unless heavy-stable-particle/high-ionization searches
  are applied,
- model variants with suppressed brane emission.

For ordinary semiclassical ADD Hawking evaporation, visible SM emission is
expected to dominate because many SM degrees of freedom live on the brane. That
is a model assumption, not a theorem covering every exotic branch.

Claim-graph wording:

```text
Modern direct searches strongly constrain prompt visible benchmark branches.
They do not replace the stable/invisible-remnant astrophysical safety argument.
```

## 11. Dense-Star Bounds and Slow Consumption

The neutron-star bound is not:

```text
No black-hole seed can exist inside a neutron star.
```

It is:

```text
N_captured * 1[t_consume < t_NS_age] should not be large.
```

If a captured seed consumes the star only on a time longer than observed
neutron-star ages, the bound weakens. But then the same model is normally safe
for Earth, because:

```text
t_consume = int dM / dotM(M)
dotM ~ rho * v * sigma_acc(M)
```

and Earth has vastly lower density and pressure than a neutron star.

The "collapse takes infinite time to a distant Schwarzschild observer" point is
mostly a coordinate issue. The exterior gravitational mass and astrophysical
appearance can change on finite exterior timescales. If an exotic model makes
the whole consumption process only asymptotic and unobservable over stellar
ages, then it is also not a practical LHC danger.

Possible loophole class:

```text
NS accretion is suppressed by exotic high-density physics, but Earth accretion
is not suppressed.
```

That is logically possible but highly non-generic. It should be a claim-graph
node requiring an explicit model, not a default assumption.

## 12. Astrophysical Updates from GW, IceCube, and UHECR

GW observations update:

- neutron-star radii and dense-matter EOS,
- maximum mass constraints,
- binary neutron-star and neutron-star-black-hole merger rates,
- compact-object population rates.

They do not obviously undermine the old "old neutron stars exist" survival
argument. The expected impact is mostly factor-of-few parameter changes, not
multi-decade changes.

IceCube wording should be precise:

```text
IceCube observed TeV-PeV astrophysical neutrinos and improved the neutrino-flux
picture, but it does not automatically settle the EeV cosmogenic flux node that
matters for some neutron-star BH-production bounds.
```

UHECR wording:

```text
Cosmic rays above the LHC fixed-target equivalent energy exist. Composition
matters because for nuclei the relevant nucleon-nucleon energy is set by
energy per nucleon, not total nuclear energy.
```

## 12A. Neutron-Star Condensates and Spectral Accretion

Later AS/Codex discussion added a sharper version of the neutron-star
microphysics loophole:

```text
Naive gas/Bondi accretion may overestimate micro-BH growth if the BH is much
smaller than the coherence length of paired neutron-star matter.
```

The correct question is not simply whether a superfluid has zero viscosity. It
is:

```text
What operator does the BH couple to, and what spectral weight does the medium
have at the required (q, omega)?
```

For stopping of a moving BH:

```text
P_loss ~ int d^3q |V_BH(q)|^2 omega S(q, omega)
omega = q . v
```

For accretion, the issue is different: a horizon is an absorbing boundary. A
bosonic condensate can in principle feed an inward coherent phase flow without
first producing an ordinary real phonon outside the horizon. But if:

```text
r_h << xi
```

where `xi` is a healing or BCS coherence length, the BH is a sub-coherence-scale
absorber and Bondi hydrodynamics is not automatically valid. A possible
parameterization is:

```text
dot M_NS = dot M_naive * S_cond
S_cond ~ 1                         hydrodynamic condensate limit
S_cond ~ (r_h/xi)^alpha             coherence-limited absorber
S_cond ~ exp(-Delta/T)              thermal quasiparticle limited only
S_cond ~ spectral integral          correct many-body formulation
```

For old neutron stars, the suppression required is roughly:

```text
D=11: t_naive ~ 10 Myr  -> need S_cond < 10^-3-10^-2
D=8:  t_naive ~ 4 kyr   -> need S_cond < 10^-6-10^-5
D<=7: much stronger suppression required
```

This branch is now documented in:

```text
notes/superfluid-spectral-accretion.md
```

Claim nodes:

```text
MODEL-NS-SUPERFLUID-SPECTRAL-ACCRETION
MODEL-NS-SUPERFLUID-SPECTRAL-STOPPING
```

## 13. Nonlinear and Exotic Semiclassical Gravity

The project should not treat the ADD geometric model as the only possible
semiclassical branch. A useful model-agnostic parameterization is:

```text
R_h(M; theta)
M_crit(theta)
kappa(theta)
b_max(M; theta)
T_H(M; theta)
sigma_acc(M,v,rho; theta)
species_overlap(theta)
```

Production then becomes:

```text
hat_sigma ~= pi b_max^2 * Theta(kappa sqrt(hat_s) - M_crit)
```

The PDF cliff means small shifts in `M_crit` or `kappa` can dominate the LHC
event rate.

Important classes:

1. Lovelock / Gauss-Bonnet / higher-curvature gravity.

   Rough mass-radius structure:

   ```text
   M ~ r_h^(D-3) + alpha_2 r_h^(D-5) + alpha_3 r_h^(D-7) + ...
   ```

   These terms can change radius, threshold, spin bounds, temperature, and
   remnants.

2. Born-Infeld and EiBI-like gravity.

   In common Palatini EiBI versions, vacuum can reduce to GR, while dense
   matter and charged/regular solutions change more. That means these theories
   may alter neutron-star accretion assumptions more than the neutral exterior
   horizon solution. If they suppress NS accretion, they often suppress the
   dangerous branch rather than strengthen it, unless Earth accretion remains
   fast for model-specific reasons.

3. Asymptotic safety / running Newton constant / nonlocal gravity.

   Often suppresses near-threshold production or gives remnants. The safety
   question becomes whether the remnant is inert, charged, hidden, or still
   accreting.

4. Noncommutative / regular black holes.

   Typically introduce a minimum mass, a finite-size core, modified Hawking
   temperature, and possible cold remnants. These weaken prompt visible LHC
   signatures and move load onto stable-remnant bounds.

5. GUP / minimal-length models.

   Similar effect: higher threshold, modified evaporation, possible remnants.

6. Brane/bulk localization and split fermions.

   This is one of the more dangerous argument-structure branches because it can
   make pp and nu-N production differ. The fallback is the pp-like cosmic-ray
   channel from protons/nuclei.

Suggested claim nodes:

```text
MODEL-LOVELOCK-HIGHER-CURVATURE
MODEL-BORN-INFELD-DENSE-MATTER-COUPLING
MODEL-ASYMPTOTIC-SAFETY-RUNNING-G
MODEL-NONCOMMUTATIVE-REGULAR-BH
MODEL-MINIMAL-LENGTH-GUP
MODEL-BRANE-SPECIES-SEPARATION
```

## 14. Other BH-Like States

Not every horizon-like or compact object is produced like a spherical
Schwarzschild-Tangherlini BH.

Black rings / black tori:

- Higher-dimensional black rings exist, with non-spherical horizon topology.
- Ordinary two-parton collisions are localized and naturally produce a
  spherical/high-spin Myers-Perry-like trapped surface or no BH.
- Rings need extended/ring-like/multi-source initial data and are not obviously
  easier to make in pp.
- If a stable ring-like object is formed, it should be treated as a remnant
  branch with modified `R_eff`, `b_max`, and accretion law.

String balls / p-branes:

- More relevant than literal black rings for collider phenomenology.
- Can alter thresholds, visible signatures, multiplicities, and remnant
  behavior.

ER bridges / wormholes:

- A nontraversable ER bridge is an interior description of an entangled or
  extended BH state, not a separate ordinary final-state particle.
- Traversable wormholes need exotic negative energy or boundary conditions and
  are not generic two-parton products.

White holes:

- White-hole formation is the time reverse of collapse and requires a
  fine-tuned low-entropy final-state condition.
- A BH-to-white-hole bounce would be a decay/ejection endpoint, not an
  accretion hazard.

Horizonless geons / fuzzballs / topological stars:

- If no absorbing horizon exists, they are usually less dangerous.
- If they behave as absorbing horizon-like remnants, astrophysical bounds
  re-enter with modified parameters.

Suggested claim nodes:

```text
MODEL-BLACK-RING-HORIZON-TOPOLOGY
MODEL-STRING-BALL-PBRANE
MODEL-HORIZONLESS-FUZZBALL-GEON
MODEL-TRAVERSABLE-WORMHOLE-ER-BRIDGE
MODEL-WHITE-HOLE-TIME-REVERSE
MODEL-OVERSPINNING-NAKED-SINGULARITY
```

## 15. Heavy-Ion Angular Momentum

Heavy-ion collision angular momentum does not directly constrain the rotating
microscopic BH regime.

HIC global angular momentum:

```text
J_HIC = global orbital angular momentum of extended QCD matter and spectators
```

Microscopic BH spin in a parton collision:

```text
J_BH ~ b sqrt(hat_s) / 2
b <= b_max ~ O(R_h)
J_BH / (M R_h) ~ O(1)
```

The total HIC angular momentum cannot coherently feed one microscopic BH in the
standard partonic channel. It is distributed across spectators and the QCD
fluid. Large global angular momentum generally means less compact initial data,
not easier microscopic collapse.

HIC data on vorticity and global hyperon polarization are useful mainly as a
guardrail:

```text
Do not overcount total nuclear energy or total nuclear angular momentum as
available for one microscopic horizon.
```

Suggested node:

```text
MODEL-HIC-GLOBAL-ANGULAR-MOMENTUM:
  HIC global OAM does not coherently enhance microscopic BH spin or black-ring
  production in the standard partonic channel.
```

## 16. Magnetic Fields, Magnetic Charge, and Monopole-Stabilized BHs

Separate three cases:

1. External magnetic fields around a neutral BH.

   A neutral BH can sit in an externally supplied magnetic field, for example
   from an accretion disk or plasma. This is not intrinsic hair and does not
   stabilize a microscopic BH by itself.

2. Kerr-Newman magnetic dipole from electric charge and spin.

   A rotating charged BH has a magnetic dipole moment. Ordinary electric charge
   is rapidly neutralized in plasma, so this is not a plausible long-lived
   magnetar replacement without extra structure.

3. Conserved magnetic charge.

   If the theory contains magnetic monopoles, a Reissner-Nordstrom-like BH can
   carry magnetic charge `P`.

For electric and magnetic charge:

```text
r_pm = M +/- sqrt(M^2 - Q^2 - P^2)
T_H = (r_+ - r_-) / (4 pi r_+^2)
```

Near extremality:

```text
M^2 -> Q^2 + P^2
T_H -> 0
```

If the lightest monopole has mass:

```text
m_mon >> T_H
```

then magnetic-charge loss through Hawking emission is Boltzmann suppressed:

```text
Gamma_mon ~ exp(-m_mon / T_H)
```

Schwinger-like magnetic discharge can also be suppressed for heavy monopoles.
This creates a plausible stable or long-lived remnant branch.

But ordinary magnetic charge is not mainly a detector-search issue. The primary
safety consequence is stopping:

- it is highly ionizing,
- it stops strongly in matter,
- if naturally produced, Earth/Sun/WD/NS survival gives strong capture bounds,
- it is directly targeted by MoEDAL and ATLAS high-ionization searches,
- it is not the neutral gravity-only dangerous branch.

Hidden-sector magnetic charge behaves more like the neutral branch for ordinary
stopping unless it couples to ordinary matter. But if it is decoupled enough to
avoid ordinary stopping, ordinary visible heavy-ion magnetic fields may also fail
to produce it efficiently, and it will not generate ordinary magnetar-like
fields without additional mixing.

Suggested nodes:

```text
MODEL-MAGNETICALLY-CHARGED-BH
MODEL-MONOPOLE-CORE-BH
MODEL-HIDDEN-MAGNETIC-CHARGE-REMNANT
SEARCH-MOEDAL-ATLAS-HIGH-IONIZATION
```

## 17. Could Monopole-Stabilized BHs Be Collider-Only?

A generic single magnetically charged BH cannot be made from ordinary pp
initial states unless magnetic charge is balanced elsewhere. Charge conservation
requires something like:

```text
pp -> BH(+g) + BH(-g) + X
```

or:

```text
pp -> BH(+g) + monopole(-g) + X
```

This raises the threshold and worsens the PDF cliff.

Luminosity alone usually does not make the LHC beat cosmic rays for a pp-like
process. A rough count:

```text
N_LHC = L_LHC * sigma_X * A * epsilon
```

Run-2-scale integrated luminosity:

```text
L_LHC ~ 150 fb^-1
one event -> sigma_X ~ 1/L ~ 7 ab
```

HL-LHC:

```text
L ~ 3000 fb^-1 = 3 ab^-1
one event -> sigma_X ~ 0.3 ab
```

For ordinary cosmic pp-like production, Earth/Sun/stellar exposure is enormous.
So "LHC luminosity beats cosmic rays" is not the default. It requires a special
production condition, such as:

```text
requires coherent heavy-ion magnetic field
requires hidden-sector initial state present at the LHC but not in cosmic rays
requires low boost / special beam geometry
requires pp but not nu-N, with charged cosmic rays excluded from the relevant
compact-star environment
requires strong visible-sector B field for dual Schwinger production
```

Direct searches can miss rare or invisible events because:

```text
N_seen = L * sigma_X * A * epsilon * BR_visible
```

But ordinary visible magnetic charge also has large stopping/capture in
ordinary matter. Thus the first safety question is whether nature produces the
same object and captures it in Earth/Sun/WD/NS environments. MoEDAL/ATLAS
high-ionization and monopole trapping searches are additional constraints, not
the primary closure of the branch.

Hidden magnetic charge can evade ordinary high-ionization searches and stopping,
but then the heavy-ion visible-B enhancement is also lost unless the hidden
magnetic sector couples to ordinary EM.

## 18. Could Magnetized BHs Replace Neutron Stars?

This is a useful loophole to state explicitly, but it is weak for ordinary
semiclassical BHs.

A neutron star is not just "compact mass plus magnetic field." Observations
involve matter outside a horizon:

- pulsar timing and spin-down,
- glitches and crust/superfluid behavior,
- thermonuclear Type-I X-ray bursts,
- thermal surface emission and radius inference,
- tidal deformability in binary neutron-star mergers,
- kilonova ejecta from neutron-rich matter.

A BH can have external magnetic fields supplied by plasma, but it cannot
generically retain an arbitrary intrinsic magnetic dipole like a material star.

The seed-charge algebra is especially damaging to the simple replacement idea.
If a TeV-scale magnetically charged seed consumes a neutron star, then in
geometric units:

```text
P_seed <= M_seed
```

After eating the star:

```text
P_final / M_final <= M_seed / M_NS
```

For:

```text
M_seed ~ 10^4 GeV
M_NS ~ 10^57 GeV
```

one gets:

```text
P_final / M_final <= 10^-53
```

So the final stellar-mass BH is essentially uncharged relative to its mass.
It cannot be a magnetar-strength object unless it acquires enormous additional
magnetic charge or stores external flux by a separate mechanism.

Therefore:

```text
Observed neutron stars are all magnetized BHs
```

is not a small loophole in the safety argument. It is a replacement of large
parts of compact-star astrophysics and must reproduce surfaces, crust physics,
ejecta, tidal response, pulsar phenomenology, and magnetospheres.

Slower-consumption variant:

```text
Observed NSs are in a long-lived partial-consumption phase.
```

This weakens the dense-star bound only if `t_consume > t_NS_age`. But then the
Earth danger is normally also weakened because Earth accretion is vastly slower.
It becomes dangerous only in a special model where dense nuclear matter slows
growth while ordinary matter does not.

Suggested nodes:

```text
MODEL-NS-AS-MAGNETIZED-BH
MODEL-SLOW-NS-CONSUMPTION
CALC-SEED-MAGNETIC-CHARGE-DILUTION
OBS-NS-SURFACE-AND-EJECTA-PHENOMENA
```

## 19. Heavy-Ion Magnetic-Field Production

This is the most interesting magnetic loophole raised late in the thread.

Relativistic heavy-ion collisions create enormous transient electromagnetic
fields. Magnetic monopoles can be produced through a dual Schwinger-like
mechanism:

```text
Gamma ~ exp[- pi m^2 / (g B)]
```

For a magnetically charged BH-like object, schematically:

```text
Pb Pb -> BH(+g) + BH(-g) + X
```

or:

```text
Pb Pb -> BH(+g) + monopole(-g) + X
```

This can evade the ordinary pp cosmic-ray equivalence if production is driven
by coherent `B`, not by parton luminosity. It is therefore a separate branch,
not just another pp cross-section correction.

However, it pays three prices:

1. Magnetic charge conservation requires a pair or compensating magnetic-sector
   object.
2. The Schwinger exponent is severe for TeV-scale masses unless `gB` is huge or
   the model supplies an enhancement.
3. Ordinary magnetic charge is directly constrained by high-ionization and
   monopole searches.

Important distinction:

```text
ordinary magnetic charge -> HIC B fields can help production, but charge makes
                            stopping/capture strong if nature produces it too
hidden magnetic charge   -> ordinary stopping/searches weaker, but ordinary HIC
                            B fields may not couple enough to produce it
```

Suggested node:

```text
MODEL-HIC-B-ENHANCED-MAGNETIC-BH-PRODUCTION:
  coherent heavy-ion electromagnetic fields create a production mode not
  identical to pp or nu-N geometric BH production. Needs explicit coupling,
  mass, charge, Schwinger exponent, and search-limit calculation.
```

## 20. Future Machines

HL-LHC:

- changes luminosity and statistics,
- not the fundamental pp energy frontier,
- planned integrated luminosity around `3000 fb^-1`,
- does not qualitatively change the 14 TeV safety structure.

FCC-hh:

- changes the energy frontier, roughly 85-100 TeV pp class,
- must be a separate claim-graph branch.

FCC-ee:

- is a precision/high-luminosity lepton machine at roughly 88-365 GeV,
- is far below TeV-gravity microscopic-BH thresholds in the standard scenario,
- is not a material stable-BH danger branch unless one assumes already-excluded
  sub-TeV quantum gravity.

Fixed-target cosmic-ray comparator:

```text
E_CR ~= S^2 / (2 m_p)
```

So:

```text
S = 14 TeV  -> E_CR ~ 1e17 eV
S = 85 TeV  -> E_CR ~ 3.9e18 eV
S = 100 TeV -> E_CR ~ 5e18 eV
```

If the integral flux scales roughly as:

```text
Phi(>E_min) ~ E_min^-2 ~ S^-4
```

going from 14 TeV to 100 TeV reduces the simple comparator flux by:

```text
(100/14)^4 ~ 2600
```

Therefore LHC numerical margins should not be copied blindly to FCC. The logic
may transfer, but the numbers must be recalculated.

For FCC-hh, UHECR composition becomes load-bearing. Heavy nuclei must be treated
per nucleon:

```text
E_nucleon = E_nucleus / A
```

so an iron nucleus must have total energy near or above the observed cutoff to
match an 85-100 TeV nucleon-nucleon collision.

Correct charged-BH framing for FCC:

```text
visible charged stable BH:
  charge strengthens stopping/capture. If cosmic rays or stars naturally produce
  the same object, Earth/Sun/WD/NS survival gives a stronger bound.

hidden charged stable BH:
  ordinary stopping/capture is not guaranteed, so it behaves more like the
  neutral branch. But visible FCC heavy-ion magnetic fields may not produce it
  efficiently either.
```

The distinctive FCC-HI branch is:

```text
coherent heavy-ion electromagnetic fields produce stable charged/magnetic
BH-like objects
AND the natural astrophysical analogue is absent or much rarer
AND charge is not radiated or neutralized
AND post-capture accretion remains dangerous.
```

This is a production-equivalence plus accretion question, not a detector
invisibility question.

## 21. Current Implementation Problems

These are the main issues discovered after pulling the repo and comparing it
with the literature structure:

1. Superseded LHC capture scripts still print old small probabilities.

   Files:

   ```text
   analysis/lhc_bh_fate.py
   analysis/lhc_first_capture.py
   ```

   They should either implement the Giddings-Mangano Appendix F behavior or
   print a clear superseded warning.

2. Iron cosmic-ray composition convention is inconsistent.

   Some text/scripts count primary nuclei, while Giddings-Mangano-style
   arguments count relevant nucleon-nucleon opportunities. Harmonize the
   convention.

3. IceCube wording should be cleaned up.

   Use "TeV-PeV astrophysical flux observed; EeV/cosmogenic flux still
   upper-limited/model-dependent" rather than "IceCube settles the old neutrino
   node."

4. Top-level docs are stale.

   `README.md` and `PROJECT_SUMMARY.md` should mention the neutron-star module
   and later research-gap structure.

5. The main deliverable is still missing.

   Add a machine-readable claim graph.

## 22. Claim Graph Schema

Recommended node fields:

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

Useful nodes:

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
MODEL-LOVELOCK-HIGHER-CURVATURE
MODEL-BORN-INFELD-DENSE-MATTER-COUPLING
MODEL-ASYMPTOTIC-SAFETY-RUNNING-G
MODEL-NONCOMMUTATIVE-REGULAR-BH
MODEL-MINIMAL-LENGTH-GUP
MODEL-BRANE-SPECIES-SEPARATION
MODEL-HIC-GLOBAL-ANGULAR-MOMENTUM
MODEL-MAGNETICALLY-CHARGED-BH
MODEL-HIDDEN-MAGNETIC-CHARGE-REMNANT
MODEL-HIC-B-ENHANCED-MAGNETIC-BH-PRODUCTION
MODEL-FCC-HH-85TEV-RECALCULATE-CR-COMPARATOR
MODEL-FCC-HH-COMPOSITION-SENSITIVE-UHECR-BOUND
MODEL-FCC-HI-B-FIELD-MAGNETIC-BH-PRODUCTION
MODEL-VISIBLE-CHARGED-BH-ASTRO-CAPTURE-BOUND
MODEL-HIDDEN-CHARGED-BH-NEUTRAL-LIKE-STOPPING
MODEL-NS-AS-MAGNETIZED-BH
MODEL-SLOW-NS-CONSUMPTION
MODEL-NS-SUPERFLUID-SPECTRAL-ACCRETION
MODEL-NS-SUPERFLUID-SPECTRAL-STOPPING
CALC-SEED-MAGNETIC-CHARGE-DILUTION
SEARCH-MOEDAL-ATLAS-HIGH-IONIZATION
```

## 23. Files/Sources to Download Into `sources/`

Priority:

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

Magnetic/exotic branch:

9. Lee-Nair-Weinberg magnetic monopole BH PDF:
   https://arxiv.org/pdf/hep-th/9112008

10. Gould-Rajantie HIC monopole Schwinger PDF:
    https://arxiv.org/pdf/1705.07052

11. MoEDAL HIC monopole search PDF:
    https://arxiv.org/pdf/2402.15682

12. Born-Infeld-inspired gravity review PDF:
    https://arxiv.org/pdf/1704.03351

13. Asymptotic safety review PDF:
    https://arxiv.org/pdf/2212.09495

14. Noncommutative/regular BH collider papers:
    https://arxiv.org/pdf/1003.1798
    https://arxiv.org/pdf/1111.5830

## 24. Next Implementation Tasks

Highest priority:

1. Mark or rewrite superseded LHC capture scripts:

   ```text
   analysis/lhc_bh_fate.py
   analysis/lhc_first_capture.py
   ```

2. Harmonize cosmic-ray iron/nucleon counting in:

   ```text
   analysis/cosmic_ray_flux.py
   notes/01-cosmic-ray-argument.md
   notes/05-comparison-giddings-mangano.md
   README.md
   ```

3. Fix IceCube/EeV wording in:

   ```text
   notes/06-neutron-star-bound.md
   notes/research-gaps.md
   ```

4. Update `README.md` and `PROJECT_SUMMARY.md` for layer 6 and research-gap
   status.

5. Add claim graph:

   ```text
   notes/claim_graph.yaml
   ```

6. Add a toy suppression script for neutron-star condensate accretion:

   ```text
   analysis/superfluid_accretion_suppression.py
   ```

Then add focused notes:

```text
notes/07-production-and-pdf-cliff.md
notes/08-radiation-and-stopping.md
notes/09-direct-searches-and-decay-channels.md
notes/10-exotic-semiclassical-gravity.md
notes/11-magnetic-bh-and-heavy-ion-fields.md
notes/superfluid-spectral-accretion.md
```

Then add calculations:

```text
analysis/bh_geometry.py
analysis/pp_production.py
analysis/neutrino_bh_production.py
analysis/hic_magnetic_schwinger.py
analysis/superfluid_accretion_suppression.py
```

## 25. Bottom Line

The best final artifact should let a reader navigate this structure:

```text
1. Production is model-dependent and suffers a high-x PDF cliff near the LHC
   endpoint.

2. Direct LHC searches constrain prompt visible benchmark decays, not every
   stable/invisible remnant branch.

3. If ordinary Hawking radiation works, microscopic BHs evaporate and are not a
   hazard.

4. The pessimistic stable-remnant branch is handled by stopping, accretion, and
   dense-star survival.

5. Earth/Sun survival closes stopped-in-ordinary-matter branches.

6. Neutral gravity-only cosmic-ray-produced BHs pass through ordinary matter,
   so white dwarfs and neutron stars are the load-bearing astrophysical tests.

7. If pp works but nu-N fails, cosmic p-N/nucleus-N production remains a
   fallback comparator, though capture and compact-star access must be treated
   carefully.

8. Exotic semiclassical models mostly shift threshold, trapped fraction,
   evaporation/remnants, accretion law, or species overlap. The claim graph
   should expose which node each model attacks.

9. Magnetic-charge branches are real but split sharply:
   ordinary visible magnetic charge strengthens stopping/capture and therefore
   astrophysical bounds if naturally produced; hidden magnetic charge behaves
   more like the neutral branch but may not couple to visible heavy-ion fields.

10. Heavy-ion magnetic-field production is a separate loophole class, not
    covered by pp luminosity equivalence, but it pays magnetic-charge
    conservation, Schwinger suppression, and high-ionization-search costs.

11. Replacing observed neutron stars with magnetized BHs is not a small patch;
    it must reproduce surface, crust, ejecta, tidal, and pulsar phenomenology.

12. Fast danger implies astrophysical testability. Branches not excluded by
    astrophysical tests are normally too slow to matter on Solar-System
    timescales.
```

That decomposition is the real case-study value: not the slogan that the LHC is
safe, but the explicit map of why confidence is warranted, what the argument
depends on, and which nodes must be updated as the literature changes.
