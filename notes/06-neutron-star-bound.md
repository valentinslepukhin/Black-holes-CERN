# Neutron stars: the decisive bound for gravity-only black holes

*Layer 6: the load-bearing node for D ≥ 8 (where white dwarfs fail, notes/05).
How often a typical neutron star traps a neutral, gravity-only BH, and how long
it then survives. Calculation: `analysis/ns_capture_consumption.py`. Validated
against G&M §8.1–8.2, Tables 3 & 10, read from `sources/` pp. 46–49.*

## The question, made precise
"Gravitational interaction only" = the dangerous case A: a **neutral, stable,
non-Hawking** BH that touches NS matter only through gravity. It is *produced*
by a weak (neutrino–parton) collision, but once it exists it is neutral. So the
NS magnetic field — which screens charged cosmic rays (acceptance ×10⁻³) — is
irrelevant to it. Two things must hold: it must be **made** in/at the NS, and it
must **stay** (be stopped). Then we ask how fast it eats the star.

## (i) How often does a NS trap one?

Production is dominated by ultra-high-energy cosmic **neutrinos** (GZK-guaranteed
flux) hitting nucleons inside the NS — G&M Table 10, conservative flux, 10 km NS,
M_min = 14 TeV:

| D | n=D−4 | ν-channel /Myr | mean gap between captures | binary channel /Myr |
|---|---|---|---|---|
| 5 | 1 | 4.5×10³ | **222 yr** | — |
| 6 | 2 | 1.1×10⁴ | 91 yr | — |
| 7 | 3 | 2.0×10⁴ | 50 yr | — |
| 8 | 4 | 3.0×10⁴ | **33 yr** | 54 |
| 9 | 5 | 4.0×10⁴ | 25 yr | 74 |
| 10 | 6 | 5.1×10⁴ | 20 yr | 95 |
| 11 | 7 | 6.2×10⁴ | **16 yr** | 118 |

**A typical neutron star traps a gravity-only black hole roughly once every
~16–220 years** (every ~few decades for the D ≥ 8 cases that matter).

**Capture efficiency ≈ 1.** The NS column density is ρR ~ (2×10¹⁴ g/cm³)(10⁶ cm)
~ 2×10²⁰ g/cm², versus the gravitational stopping column needed (notes/05,
G&M Table 1 + eq 5.35): (0.7, 6.5, 20, 40)×10¹⁵ g/cm² for D = 5–8, extrapolating
to a few ×10¹⁷ at D = 11 — *needed ≪ available for every D*. And per G&M §8.2.1,
even after slowdown the BH drifts through the ~1 km crust in t_crust ≲ 10 s and
enters the neutron fluid. So **produced ⇒ stuck**, for all D of interest.

## (ii) How long to consume the NS?

Same accretion machinery as Part 3 (`capture_and_accretion.grow`), re-evaluated
at NS conditions (ρ ≈ 2×10¹⁷ kg/m³ ≈ 10³× a white dwarf; c_s ~ 0.1c):

| D | n | our model: consume NS | G&M §8.2.2 |
|---|---|---|---|
| 5 | 1 | ~instant | ≲50 yr |
| 6 | 2 | ~10³ s | ≲50 yr |
| 7 | 3 | **9 yr** | ≲50 yr |
| 8 | 4 | 4 kyr | yr–kyr |
| 9 | 5 | 160 kyr | kyr |
| 10 | 6 | 1.8 Myr | Myr |
| 11 | 7 | **10 Myr** | **~10 Myr** |

Agreement is excellent: our D=11 lands exactly on their longest-phase estimate
(~10 Myr), D≤7 gives years (inside their ≲50 yr), and the monotonic rise with D
tracks theirs. The enormous NS density drives even the slow high-D accretion to
completion in ≤10 Myr — far inside any stellar lifetime. (Cross-check: G&M find a
captured *primordial* 10¹⁵ g BH consumes a NS in ~3×10⁵ yr — same ballpark, and
proposed as a possible GRB mechanism.)

## (iii) The bound

NS birth → destruction = t_first_capture + t_consume:
- D = 8: ~33 yr + ~4 kyr ≈ **4 kyr**
- D = 11: ~16 yr + ~10 Myr ≈ **10 Myr**

Observed neutron stars and their X-ray binary companions are **~Gyr** old. In the
dangerous hypothesis a NS would be eaten **10²–10⁷× faster than its observed age**.
Their continued existence excludes stable neutral gravity-only TeV black holes
across the *entire* D = 5–11 range — **including the D ≥ 8 window where the white
dwarf bound fails** (notes/05). This is exactly why neutron stars, not
Earth/Sun/white-dwarfs, are the decisive object for the gravity-only case, and
why this was our load-bearing node all along.

## Where the residual P(argument-wrong) now sits (Ord–Hillerbrand–Sandberg)
Having traced the chain to the bottom, the gravity-only safety case for D ≥ 8
rests on three explicit dependencies — note their epistemic types:
1. **The cosmic UHE neutrino flux** [CALCULATION→OBSERVATION]. G&M's 2008
   "guaranteed" GZK-neutrino estimate was *unobserved* then; IceCube detected the
   astrophysical flux from 2013. Their own caveat (§8.1.2) — that the bound fails
   if the flux "doesn't exist" or neutrino-parton coupling is suppressed by brane
   separation — has weakened with data. **Live node: status improved since 2008.**
2. **Neutrino-parton BH production behaves like nucleon-parton** [CALCULATION] —
   not killed by higher-dimensional brane separation of neutrinos from quarks.
3. **Existence of Gyr-old neutron stars with known ages** [OBSERVATION, robust].

So the irreducible residual is P(GZK neutrinos don't make BHs the standard way) ×
P(stable neutral non-Hawking BHs exist at all) — both small, and the first is now
partly empirically anchored rather than purely assumed.

## Assumptions log
- Production rates are G&M Table 10 (ν) and Table 3 (binary), conservative flux;
  could be 10–100× higher (AGN/GRB neutrinos) or suppressed (heavy CR composition
  + brane effects). All "how often" numbers scale linearly with the flux.
- Stopping column comparison uses notes/05 values + eq-5.35 extrapolation to D=11;
  the D=11 stopping column (~few ×10¹⁷) is the least certain but still ≪ 2×10²⁰.
- Consumption uses non-relativistic 4D Bondi + steep-potential capture for
  degenerate/relativistic NS matter — crude; expect factor (not decade) errors.
  Validated OOM against G&M; not a precision result.
- All conditional on TeV gravity + stable neutral non-Hawking BH (the dangerous
  hypothesis); absent any of those, production rate is zero.
- "Typical NS": M = 1.4 M_⊙, R = 10 km, age ~Gyr.
