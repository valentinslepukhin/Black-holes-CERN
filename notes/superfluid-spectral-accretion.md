# Neutron-Star Condensates and Spectral Accretion

Working note added from the AS/Codex discussion on 2026-06-19.

## 1. Question

Can neutron-star condensates suppress accretion of a microscopic stable black
hole relative to the naive gas/Bondi estimate?

The point is not simply that a superfluid has zero viscosity. The sharper
question is:

```text
What operator does the black hole couple to, and what spectral weight does the
neutron-star medium have at the required (q, omega)?
```

This matters because the Giddings-Mangano neutron-star bound uses an accretion
clock after a seed is trapped. If the relevant accretion rate is suppressed by
many-body coherence, pairing gaps, or the absence of available excitations, the
neutron-star consumption time could be longer than the naive estimate.

## 2. Hawking Versus Absorption Assumption

There is a tension between the ordinary Hawking picture and the stable-remnant
branch.

If normal Hawking radiation exists, a microscopic BH is hot. Matter near the
horizon does not remain a cold condensate; the condensate is locally destroyed
or strongly excited. Then the dangerous long-lived branch mostly disappears
because the BH evaporates.

The interesting branch is explicitly nonstandard:

```text
Hawking emission is absent or suppressed,
but semiclassical horizon absorption remains meaningful.
```

That is an assumption and should be a claim-graph node. It is not ordinary
thermal equilibrium QFT around a hot micro-BH.

## 3. Feynman-Bijl / Structure-Factor Logic

For a condensate, one cannot assume that momentum `q` is deposited into one
ordinary particle. The response is controlled by collective modes and spectral
weight.

For density perturbations:

```text
S(q, omega) =
  sum_n |<n|rho_q|0>|^2 delta(omega - (E_n - E_0)/hbar)
```

In a single-mode/Feynman-Bijl approximation:

```text
E(q) ~= hbar^2 q^2 / [2 m S(q)]
```

Small static structure factor `S(q)` means that the corresponding density kick
is hard to realize. The medium responds through phonons, rotons, pair-breaking
continua, vortex/fluxtube modes, and other collective channels, not through a
free-particle gas spectrum.

For stopping of a moving compact object:

```text
P_loss ~ int d^3q |V_BH(q)|^2 omega S(q, omega)
omega = q . v
```

At zero temperature, if:

```text
v < v_c = min_q [omega(q)/q]
```

ordinary quasiparticle emission is kinematically forbidden. This is the
Landau/Feynman obstruction.

Sources:

- Steinhauer et al., BEC excitation spectrum and Feynman's relation:
  https://arxiv.org/abs/cond-mat/0111438
- Minguzzi, Ferrari, Castin, dynamic structure factor of a superfluid Fermi gas:
  https://arxiv.org/abs/cond-mat/0103591
- Zou, Hu, Liu, low-momentum dynamic structure factor of a strongly interacting
  Fermi gas:
  https://arxiv.org/abs/1712.08318
- Castin, Sinatra, Kurkjian, Landau phonon-roton theory for helium and Fermi
  gases:
  https://arxiv.org/abs/1707.09774

## 4. Stopping Is Not The Same As Accretion

Stopping is energy/momentum loss to excitations outside the horizon. Accretion
is net energy/particle flux through an absorbing boundary.

For a bosonic condensate with:

```text
psi = sqrt(n) exp(i theta)
```

a horizon-like sink can be modeled schematically by:

```text
i hbar d_t psi =
[-hbar^2 nabla^2/(2m) + g |psi|^2 + m Phi_BH - i W(r)] psi
```

where `W(r)` is an absorbing boundary or sink term. In hydrodynamic variables,
the condensate can develop inward phase flow:

```text
j = n hbar grad(theta) / m
```

Therefore direct absorption of the coherent order parameter does not
automatically require creating a real phonon outside the BH. The "break the
condensate first" intuition is right for some quasiparticle channels, but it is
not automatically right for all horizon-absorption channels.

## 5. Two Limits

Define a Bondi/gravitational influence radius:

```text
r_B = G M_BH / c_s^2
```

and a coherence/healing length:

```text
xi
```

### Hydrodynamic condensate limit

If:

```text
r_B >> xi
```

the condensate behaves approximately as an inviscid barotropic fluid. A
Bondi-like rate is plausible:

```text
dot M ~ 4 pi lambda rho (G M_BH)^2 / c_s^3
```

For stiff equations of state and relativistic sound speeds, the numerical
coefficient and scaling need a relativistic treatment.

Sources:

- Richards, Baumgarte, Shapiro, relativistic Bondi accretion for stiff EOS:
  https://arxiv.org/abs/2101.08797
- Feng et al., self-interacting dark scalar accretion via relativistic Bondi:
  https://arxiv.org/abs/2112.05160
- Glavan, Vikman, Zlosnik, complex scalar-field Bondi accretion beyond the
  perfect-fluid limit:
  https://arxiv.org/abs/2511.04650

### Quantum/coherence-limited absorber

If:

```text
r_h << xi
```

the BH is a tiny absorber inside one coherent patch. Naive fluid Bondi accretion
is no longer guaranteed. The rate should be treated as a wave/many-body
absorption problem:

```text
dot M ~ rho v_eff sigma_abs
sigma_abs = A_h F(omega r_h, r_h/xi, gap, spin, D, interactions)
```

The suppression could be power-like:

```text
S_cond ~ (r_h / xi)^alpha
```

or channel-dependent through spectral functions.

## 6. Neutron-Star Superfluid Content

Neutron-star matter is not a simple dilute BEC. A minimal schematic inventory is:

```text
neutron BCS superfluid
proton superconductor
electron/muon normal components
possible hyperon/quark/color-superconducting phases
vortices and magnetic fluxtubes
```

For a neutron BCS condensate, rough scales are:

```text
Delta ~ 0.1-1 MeV
p_F ~ 300-600 MeV
xi_BCS ~ hbar v_F / (pi Delta) ~ 20-200 fm
```

A microscopic TeV-scale higher-dimensional BH can have `r_h` far below such
coherence lengths. Then possible absorption channels include:

```text
single-particle absorption  -> single-particle spectral function, gap sensitive
pair absorption             -> anomalous/pair spectral function
density absorption          -> phonon and pair-breaking continuum
stress-tensor absorption    -> collective modes and high-q response
vortex/fluxtube channels    -> if the BH intersects quantized defects
```

Only the thermal quasiparticle part is naturally Boltzmann suppressed:

```text
S_thermal ~ exp(-Delta/T)
```

That factor should not be applied blindly to coherent pair/order-parameter
absorption.

Sources for neutron-star superfluid and dense phases:

- Gezerlis, Pethick, Schwenk, pairing and superfluid neutron matter:
  https://arxiv.org/abs/1406.6109
- Chamel, superfluidity and superconductivity in neutron stars:
  https://arxiv.org/abs/1709.07288
- Alford, Schmitt, Rajagopal, Schafer, color superconductivity in dense quark
  matter:
  https://arxiv.org/abs/0709.4635

## 7. Required Suppression

Parametrize the accretion correction by:

```text
dot M_NS = dot M_naive * S_cond
```

To make old neutron stars survive:

```text
t_naive / S_cond > t_NS_age
```

or:

```text
S_cond < t_naive / t_NS_age
```

Using the repo/Giddings-Mangano-scale consumption times:

```text
D=11: t_naive ~ 10 Myr
      t_NS_age ~ 1-10 Gyr
      S_cond must be below ~10^-3-10^-2

D=8:  t_naive ~ 4 kyr
      S_cond must be below ~10^-6-10^-5

D<=7: t_naive is much shorter
      required suppression is much stronger
```

Thus modest spectral/coherence suppression only matters for the slowest
high-dimensional branches. Strong power suppression in `r_h/xi` could matter
more broadly, but it must be derived from the absorption channel, not assumed.

## 8. Toy Model For A Future Script

Add a future script:

```text
analysis/superfluid_accretion_suppression.py
```

Inputs:

```text
M_BH
D
M_D
rho
c_s
Delta
p_F
xi
alpha
t_NS_age
```

Compare:

```text
dot M_Bondi
dot M_hydro_superfluid
dot M_quantum_absorption = rho v_eff A_h F
dot M_power_suppressed = dot M_Bondi * (r_h/xi)^alpha
dot M_gap_limited = thermal_quasiparticle_fraction * dot M_normal
```

Output:

```text
S_required(D)
S_candidate(r_h/xi, alpha)
whether t_consume exceeds old NS ages
```

## 9. Claim-Graph Node

Suggested node:

```text
MODEL-NS-SUPERFLUID-SPECTRAL-ACCRETION
type: MODEL
status: needs_update
statement: Naive Bondi/geometric accretion may overestimate micro-BH growth in
  a paired neutron-star condensate. Replace gas accretion by absorption through
  the relevant superfluid spectral functions: density phonons, pair-breaking
  continuum, anomalous pair absorption, stress response, and possible
  vortex/fluxtube channels.
depends_on:
  - ASSUMPTION-STABLE-BH-NO-HAWKING
  - CALC-NS-BH-CAPTURE
  - CALC-NS-ACCRETION-CLOCK
update_triggers:
  - microscopic calculation of BH absorption in BCS neutron matter
  - improved NS pairing-gap and phase-structure constraints
  - simulation of sub-coherence-length horizon sink in paired matter
```

Related node:

```text
MODEL-NS-SUPERFLUID-SPECTRAL-STOPPING
```

Stopping and accretion should be kept separate: stopping is controlled by
energy loss to excitations, while accretion is controlled by the absorbing
boundary and the available many-body spectral channels.
