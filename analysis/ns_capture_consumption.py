#!/usr/bin/env python3
"""
Part 6: neutron stars, gravitational-interaction-only black holes.
  (i)  How often does a typical NS get a (neutral, gravity-only) BH stuck inside?
  (ii) Once stuck, how long until the NS is consumed?

This is the load-bearing node of the safety case for D >= 8 (n_extra >= 4),
where white dwarfs fail to stop/constrain (see notes/05).

PRODUCTION ("how often"):
  Neutral gravity-only BHs are made INSIDE the NS by ultra-high-energy cosmic
  NEUTRINOS hitting nucleons (G&M sec 8.1.2). Neutrinos are used, not charged
  cosmic rays, because the NS B-field (>=1e8 G) magnetically screens charged CRs
  (acceptance x1e-3); neutrinos are immune -- and for NEUTRAL BHs the field is
  irrelevant anyway. G&M Table 10 (R=10 km NS, M_min=14 TeV, M_D=M_min/3, y=0.5,
  conservative GZK-neutrino flux dPhi/dE = 1e-7 (GeV/E)^2 /m^2/s/sr/GeV):
      D    = 5     6     7     8     9     10    11
      N/Myr= 4.5e3 1.1e4 2.0e4 3.0e4 4.0e4 5.1e4 6.2e4
  (A second, independent channel -- CR protons scattering on a binary companion,
   G&M Table 3 -- gives ~50-630/Myr for D>=8; subdominant but field-independent.)

STOPPING (does it stay?):
  NS column density ~ rho * R ~ (2e14 g/cm^3)(1e6 cm) ~ 2e20 g/cm^2, i.e.
  ~2e20 g/cm^2 to escape from the centre. Compare the gravitational stopping
  column needed (G&M Table 1 + eq 5.35 extrapolation, our notes/05):
      D=5..8 at 14 TeV: (0.7, 6.5, 20, 40)e15 g/cm^2; D=11 ~ few e17 g/cm^2.
  Needed << available for ALL D up to 11 -> capture efficiency ~ 1.
  And G&M sec 8.2.1: even after slowdown the BH drifts through the ~1 km crust
  in t_crust <~ 10 s and reaches the neutron fluid. So produced ~ stuck.

CONSUMPTION ("how long"):
  Same accretion machinery as Part 3 (capture_and_accretion.grow), re-evaluated
  at NS conditions: rho ~ 2e17 kg/m^3, c_s ~ 0.1c (G&M sec 8.2). Compared against
  G&M sec 8.2.2 (D<=7: <~50 yr; D=11: ~10 Myr longest phase; warped ~20 yr;
  primordial 1e15 g BH: ~3e5 yr).

Caveats: OOM only; degenerate/relativistic NS matter is crudely modelled by 4D
Bondi + steep-potential capture (our model is non-relativistic) -- expect factor
discrepancies vs G&M, flagged inline. Everything is conditional on the dangerous
hypothesis (TeV gravity + stable NEUTRAL non-Hawking BH).
"""
import math
from capture_and_accretion import grow, fmt_mass, fmt_time

SEC_PER_YR = 3.156e7
MYR = 1e6 * SEC_PER_YR
NS_AGE_TYP = 1e9 * SEC_PER_YR          # Gyr-old NSs / X-ray binaries are observed

# G&M Table 10: neutrino-induced production, per Myr, per 10 km NS, M_min=14 TeV
PROD_NU_PER_MYR = {5: 4.5e3, 6: 1.1e4, 7: 2.0e4, 8: 3.0e4, 9: 4.0e4, 10: 5.1e4, 11: 6.2e4}
# G&M Table 3: binary-companion (proton CR) channel, per Myr, M_min=14 TeV
PROD_BIN_PER_MYR = {8: 54.0, 9: 74.0, 10: 95.0, 11: 118.0}

# NS as an accretion host (reuse capture_and_accretion.grow signature)
NS = dict(rho=2.0e17, vth=3.0e7, cs=3.0e7, mass=2.8e30, ncoll=0.0)  # 1.4 Msun, c_s~0.1c

# G&M consumption reference (sec 8.2.2)
GM_CONSUME = {5: "<~50 yr", 6: "<~50 yr", 7: "<~50 yr", 8: "~yr-kyr",
              9: "~kyr", 10: "~Myr", 11: "~10 Myr"}


def d_to_n(D):
    return D - 4


if __name__ == "__main__":
    print("=" * 84)
    print("(i) HOW OFTEN a typical neutron star traps a gravity-only black hole")
    print("=" * 84)
    print(f"{'D':>3} {'n':>2} | {'nu-channel /Myr':>15} {'mean gap':>12} | "
          f"{'binary /Myr':>11} | over {1e9:.0e} yr NS life")
    print("-" * 84)
    for D in range(5, 12):
        npm = PROD_NU_PER_MYR[D]
        gap_yr = 1e6 / npm
        binp = PROD_BIN_PER_MYR.get(D)
        binstr = f"{binp:>11.0f}" if binp else f"{'-':>11}"
        n_life = npm * 1e9 / 1e6
        print(f"{D:>3} {d_to_n(D):>2} | {npm:>15.1e} {gap_yr:>9.0f} yr | "
              f"{binstr} | {n_life:.1e} produced")
    print("\n  => A typical NS is hit by a stuck gravity-only BH every ~16-220 yr")
    print("     (neutrino channel alone). Capture efficiency ~1: NS column ~2e20")
    print("     g/cm^2 >> stopping column needed (<~few e17 even at D=11), and the")
    print("     crust is penetrated in <~10 s (G&M 8.2.1). So produced ~ stuck.")

    print()
    print("=" * 84)
    print("(ii) HOW LONG until the NS is consumed (one stuck BH at the core)")
    print("=" * 84)
    print(f"  NS: rho = {NS['rho']:.0e} kg/m^3, c_s ~ 0.1c, M = {NS['mass']:.1e} kg\n")
    print(f"  {'D':>3} {'n':>2} | {'our model: consume NS':>22} | {'G&M sec 8.2.2':>14}")
    print("  " + "-" * 60)
    for D in range(5, 12):
        _, t_con = grow(d_to_n(D), NS, t_max=1e25)
        print(f"  {D:>3} {d_to_n(D):>2} | {fmt_time(t_con):>22} | {GM_CONSUME[D]:>14}")
    print("\n  Both agree: consumption is fast (yr -> ~10 Myr) for ALL D. The high")
    print("  NS density (~1e3 x white dwarf) makes even the slow high-D accretion")
    print("  run to completion far inside a stellar lifetime. (G&M: a captured")
    print("  primordial 1e15 g BH consumes a NS in ~3e5 yr -- same ballpark.)")

    print()
    print("=" * 84)
    print("(iii) THE BOUND: NS birth -> destruction vs observed Gyr-old neutron stars")
    print("=" * 84)
    for D in (8, 11):
        gap = 1e6 / PROD_NU_PER_MYR[D] * SEC_PER_YR
        _, t_con = grow(d_to_n(D), NS, t_max=1e25)
        total = gap + (t_con if t_con else 0)
        print(f"  D={D:>2}: t_first_capture ~ {gap/SEC_PER_YR:.0f} yr  +  "
              f"t_consume ~ {fmt_time(t_con)}  =  destroyed in ~{fmt_time(total)}")
    print(f"\n  Observed: neutron stars and their X-ray binary companions live ~Gyr")
    print(f"  ({NS_AGE_TYP/SEC_PER_YR:.0e} yr). In the dangerous hypothesis a NS would be")
    print(f"  consumed ~10^2-10^7 x faster than that. Their continued existence")
    print(f"  therefore EXCLUDES stable neutral gravity-only TeV BHs across D=5-11,")
    print(f"  INCLUDING the D>=8 window where the white-dwarf bound fails.")
    print(f"  This is why neutron stars, not Earth/Sun/WD, are the decisive object")
    print(f"  for the gravity-only case (cf. notes/02-05).")

    print()
    print("  RESIDUAL DEPENDENCIES (where the Ord-style P(argument wrong) sits):")
    print("   - the cosmic UHE neutrino flux (G&M's 'guaranteed' GZK estimate;")
    print("     unobserved in 2008, IceCube-detected since 2013 -> node strengthened);")
    print("   - neutrino-parton BH production not suppressed by brane separation;")
    print("   - existence of Gyr-old NSs with known ages (well established).")
