#!/usr/bin/env python3
"""
Part 3: (i) How many cosmic-ray-produced BHs got stuck in Earth / Sun over
4.5 Gyr, per interaction case A-D?  (ii) If stuck, how fast is the host consumed?

CAPTURE (from bh_earth_passage.py results):
  A (gravity only): needs ~1e21 g/cm^2; Earth/Sun provide 7e9 / 2e11.
     Production-at-rest is kinematically impossible (the CM frame itself has
     gamma ~ 7e3; max backward boost of a 10 TeV BH in a 14 TeV collision is
     gamma* < 1.5, nowhere near canceling gamma_CM). -> P_capture ~ 0. EXACTLY ZERO bound.
  B (+weak): Earth sheds ~2.5 e-folds of ~30 needed; Sun column is 30x too thin
     even holding sigma_w at its high-energy value. -> P ~ 0.
  C (+strong): stops in 9 km rock. -> P ~ 1 in both bodies.
  D (+EM): stops if gamma < 1.4e3 (Earth) / 4e4 (Sun). Production boost ~7e3
     with ~unit rapidity spread -> Earth catches the low-gamma tail O(0.1);
     Sun catches ~all.

ACCRETION of a trapped BH at the host center (all cases share this; strong/EM
add only a tiny constant-sigma channel, see notes):
  Higher-dim BH (r_H < R_extra): steep potential V ~ -mc^2 (r_H/r)^(n+1) has no
  centrifugal barrier -> everything passing within b_c is swallowed:
      b_c ~ r_H (c/v)^(2/(n+1)),  capped at R_extra;
      beyond the cap, 4D focusing onto the R_extra sphere: sigma = pi R^2 (1 + 2GM/(R v^2)).
  4D BH (r_H > R_extra): Bondi, Mdot = 4 pi rho (GM)^2 / c_s^3.
  Mdot = rho * v * sigma, integrated numerically from M0 = 10 TeV.

Caveats: O(1) factors dropped everywhere; no radiation-pressure (Eddington)
throttling -> FAST results are lower bounds on consumption time; material
strength of solid Earth ignored (conservative); flat ADD geometry, M_D = 1 TeV.
n=1 (and largely n=2) flat scenarios are excluded by gravity/astrophysics
tests independently -- shown to exhibit why low-n was the scary corner (cf. warped RS).
"""
import math

# constants (SI)
C = 2.998e8
G = 6.674e-11
HBARC_M = 1.973e-16          # GeV^-1 in meters
KG_PER_GEV = 1.783e-27
MPL_GEV = 1.22e19
MD_GEV = 1.0e3               # TeV-scale Planck mass
M0_KG = 1.0e4 * KG_PER_GEV   # 10 TeV BH
AGE_S = 4.54e9 * 3.156e7
HUBBLE_S = 13.8e9 * 3.156e7

BODIES = {  # rho_center kg/m^3, v_thermal m/s, c_sound m/s, mass kg, N_coll>thresh over history
    "Earth": dict(rho=1.3e4, vth=1.6e3, cs=1.0e4, mass=5.97e24, ncoll=2.5e22),
    "Sun":   dict(rho=1.5e5, vth=5.9e5, cs=5.0e5, mass=1.99e30, ncoll=3.0e26),
}
F_BH = 1e-8   # BH production fraction per inelastic collision (sigma_BH ~ 1 nb / 80 mb);
              # all 'expected captured' numbers scale linearly with this.

def r_extra(n):
    return HBARC_M / MD_GEV * (MPL_GEV / MD_GEV) ** (2.0 / n)

def r_horizon_hd(M_kg, n):
    return HBARC_M / MD_GEV * (M_kg / KG_PER_GEV / MD_GEV) ** (1.0 / (n + 1))

def mdot(M, n, rho, vth, cs):
    R = r_extra(n)
    rH = r_horizon_hd(M, n)
    if rH < R:                                   # higher-dimensional BH
        b = rH * (C / vth) ** (2.0 / (n + 1))    # steep-potential capture radius
        if b < R:
            sigma = math.pi * b * b
        else:                                    # 4D focusing onto the R_extra sphere
            sigma = math.pi * R * R * (1 + 2 * G * M / (R * vth * vth))
        return rho * vth * sigma
    return 4 * math.pi * rho * (G * M) ** 2 / cs ** 3   # 4D Bondi

def grow(n, body, t_max=1e22):
    """Integrate M(t); return (mass at 4.5 Gyr, time to consume half the body)."""
    rho, vth, cs, M_body = body["rho"], body["vth"], body["cs"], body["mass"]
    M, t = M0_KG, 0.0
    m_at_age, t_consume = None, None
    while M < M_body / 2:
        dM = 0.05 * M
        dt = dM / mdot(M, n, rho, vth, cs)
        if m_at_age is None and t + dt >= AGE_S:
            m_at_age = M
        t += dt
        M += dM
        if t > t_max:
            return m_at_age if m_at_age else M, None
    return (m_at_age if m_at_age else M), t

def fmt_mass(m):
    if m is None: return "-"
    if m > 5.97e23: return f"{m/5.97e24:.2g} M_Earth"
    for u, s in [(1e9, "Mt"), (1e3, "t"), (1.0, "kg"), (1e-3, "g"), (1e-6, "mg")]:
        if m >= u: return f"{m/u:.2g} {s}"
    return f"{m:.1e} kg"

def fmt_time(t):
    if t is None: return ">> Hubble time"
    yr = t / 3.156e7
    for u, s in [(1e9, "Gyr"), (1e6, "Myr"), (1e3, "kyr"), (1.0, "yr")]:
        if yr >= u: return f"{yr/u:.2g} {s}"
    return f"{t:.1g} s"

if __name__ == "__main__":
    print("=" * 78)
    print("(i) EXPECTED NUMBER OF BHs CAPTURED OVER 4.5 Gyr  (scales with f_BH = %.0e)" % F_BH)
    print("=" * 78)
    for name, b in BODIES.items():
        nbh = b["ncoll"] * F_BH
        print(f"\n{name}: ~{b['ncoll']:.1e} collisions above LHC energy -> ~{nbh:.1e} BHs produced")
        print(f"  A (gravity only) : P_cap ~ 0 (needs 1e21 g/cm^2)      -> expected stuck:  0")
        print(f"  B (+ weak)       : P_cap ~ 0 (needs >5e13 g/cm^2)     -> expected stuck:  0")
        pc_D = 0.1 if name == "Earth" else 1.0
        print(f"  C (+ strong)     : P_cap ~ 1 (stops in 5e6 g/cm^2)    -> expected stuck:  {nbh:.0e}")
        print(f"  D (+ EM)         : P_cap ~ {pc_D:<4} (ionization range)    -> expected stuck:  {pc_D*nbh:.0e}")

    print("\n  => For C (and D in the Sun) capture is CERTAIN and ENORMOUS in number.")
    print("     For A and B the count is identically ~zero: Earth/Sun survival")
    print("     carries NO information about those scenarios. (The gap WD/NS must fill.)")

    print()
    print("=" * 78)
    print("(ii) CONSUMPTION CLOCK for one BH trapped at the center")
    print("     (gravitational accretion, flat ADD, M_D = 1 TeV; no Eddington throttle)")
    print("=" * 78)
    for name, b in BODIES.items():
        print(f"\n--- {name} (rho_c = {b['rho']:.1e} kg/m^3, v_th = {b['vth']:.1e} m/s) ---")
        print(f"  {'n':>2} {'R_extra':>10} | {'mass after 4.5 Gyr':>20} | {'time to consume':>16}")
        for n in range(1, 8):
            m_age, t_con = grow(n, b)
            flag = "  [flat n<3 excluded by gravity tests]" if n <= 2 else ""
            print(f"  {n:>2} {r_extra(n):>10.1e} | {fmt_mass(m_age):>20} | {fmt_time(t_con):>16}{flag}")

    print("\nConstant-sigma side channels (do not change the picture):")
    rho, vth = BODIES["Earth"]["rho"], BODIES["Earth"]["vth"]
    md_strong = rho * vth * 40e-31  # 40 mb in m^2
    print(f"  strong (40 mb): Mdot = {md_strong:.1e} kg/s -> "
          f"{fmt_mass(md_strong*AGE_S)} eaten in 4.5 Gyr (sigma is QCD-fixed, no growth)")
    print(f"  EM: a charged BH neutralizes by binding/eating an electron; no enhancement.")

    print()
    print("=" * 78)
    print("(iii) EMPIRICAL INVERSION: survival of host -> per-BH accretion bound")
    print("=" * 78)
    for name, b in BODIES.items():
        n_stuck = b["ncoll"] * F_BH          # case C
        bound = b["mass"] / (n_stuck * AGE_S)
        print(f"  {name}: {n_stuck:.0e} case-C BHs resident, host intact ->")
        print(f"     per-BH <Mdot> < {bound:.1e} kg/s  (model-independent, given capture)")
    print("\n  LHC perspective: the full LHC program adds ~%.0e BHs (f_BH x 2.4e17)," % (F_BH * 2.4e17))
    print("  a negligible increment on the 1e14 (Earth) / 1e18 (Sun) already resident")
    print("  in the strongly-interacting scenario. For gravity-only BHs even the LHC")
    print("  traps ~none: typical production beta ~ 0.1-0.3 >> beta_esc = 3.7e-5;")
    print("  P(beta < beta_esc) ~ (beta_esc/0.2)^3 ~ 1e-11 -> expected trapped < 0.01.")
