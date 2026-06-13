#!/usr/bin/env python3
"""
Part 4: fate of black holes produced AT THE LHC, cases A-D.

Key kinematic difference from cosmic rays: the lab IS the (nucleon-nucleon) CM
frame. A 10 TeV BH at sqrt(s)=14 TeV needs parton fractions x1*x2 >= 0.5, so
x1 ~ x2 ~ 0.7 and the longitudinal boost is small: typical |beta| ~ 0.1-0.3
(parton imbalance + balding-phase recoil). We model the slow tail as phase
space, P(beta < x) = (x / beta_typ)^3.

Capture logic per case (LHC ring is ~100 m underground):
  A, B: nothing in Earth can stop them (Parts 2-3) -> trapped only if BORN
        slower than v_esc. P = (beta_esc/beta_typ)^3 ~ 1e-11.
  C:    sigma ~ 40 mb. Non-relativistic stopping column from beta0 = 0.2:
        N = (M/2m_p) ln(beta0^2/beta_esc^2) collisions -> ~4e6 g/cm^2 ~ 14 km
        of rock. Downward hemisphere: trapped. Upward: only ~100 m rock +
        atmosphere (~3e4 g/cm^2) -> shed only ~0.1 e-fold -> ESCAPE TO SPACE
        at beta ~ 0.19. P_cap ~ 0.5.
  D:    Bethe dE/dx at beta = 0.2 is ~25x minimum-ionizing (~50 MeV cm^2/g).
        KE = M beta^2/2 = 200 GeV -> range ~ 4e3 g/cm^2 ~ 15 m of rock:
        stops in the cavern wall / first rock in ANY direction. P_cap ~ 1.

Consumption: identical accretion physics as capture_and_accretion.py (how the
BH arrived is irrelevant once it is at rest in the host) -- imported.
"""
import math
from capture_and_accretion import grow, fmt_mass, fmt_time, BODIES, AGE_S

# parameters
F_BH = 1e-8                 # BHs per inelastic collision (sigma_BH ~ 1 nb)
N_COLL = 2.4e17             # HL-LHC program inelastic collisions
BETA_TYP = 0.2              # typical production speed
BETA_ESC = 3.73e-5          # Earth
M_GEV = 1.0e4
M_P = 0.9383

N_BH = F_BH * N_COLL

def p_slow(beta_cut, beta_typ=BETA_TYP):
    return min(1.0, (beta_cut / beta_typ) ** 3)

if __name__ == "__main__":
    print(f"BHs produced over (HL-)LHC program: N = f_BH x {N_COLL:.1e} = {N_BH:.1e}")
    print(f"Production speed: beta_typ ~ {BETA_TYP} (x1~x2~0.7 kinematics); "
          f"P(beta<x) = (x/{BETA_TYP})^3\n")

    print("=" * 78)
    print("CAPTURE AT/NEAR THE COLLIDER, BY CASE")
    print("=" * 78)

    # A and B: only the born-slow tail
    pA = p_slow(BETA_ESC)
    print(f"\nA (gravity only) and B (+weak): unstoppable by Earth (Parts 2-3).")
    print(f"  P(born with beta < beta_esc) = ({BETA_ESC}/{BETA_TYP})^3 = {pA:.1e}")
    print(f"  expected trapped in Earth over whole program: {N_BH * pA:.1e}  (<< 1)")
    p_sol = p_slow(2.4e-4)   # bound to Sun: lab speed + 30 km/s orbital vs 42 km/s esc
    print(f"  (bound to SOLAR orbit, v_sun-frame < 42 km/s: ~{N_BH * p_sol:.0f} BHs ->")
    print(f"   harmless Earth-crossing orbits; entering the Sun needs further fine-tuning)")

    # C: stopping column from beta0
    n_stop = (M_GEV / (2 * M_P)) * math.log(BETA_TYP**2 / BETA_ESC**2)
    col_stop = n_stop * 1.66e-24 / 40e-27          # g/cm^2
    rock_km = col_stop / 2.7 / 1e5
    col_up = 100e2 * 2.7 + 1030                     # 100 m rock + atmosphere
    efolds_up = (col_up / 1.66e-24) * 40e-27 * (2 * M_P / M_GEV)
    print(f"\nC (+strong): stopping column from beta={BETA_TYP}: "
          f"{col_stop:.1e} g/cm^2 (~{rock_km:.0f} km rock)")
    print(f"  downward hemisphere -> trapped;  upward: only {col_up:.1e} g/cm^2 "
          f"-> sheds {efolds_up:.2f} e-folds, escapes to space at beta ~ 0.19")
    print(f"  P_cap ~ 0.5 -> expected trapped in Earth: {0.5 * N_BH:.1e}")

    # D: ionization range at beta = 0.2
    ke_mev = 0.5 * M_GEV * 1e3 * BETA_TYP**2
    dedx = 2.0 / BETA_TYP**2 * 0.5      # ~Bethe 1/beta^2 scaling from MIP, OOM
    rng = ke_mev / dedx
    print(f"\nD (+EM, charge e): KE = {ke_mev/1e3:.0f} GeV, dE/dx ~ {dedx:.0f} MeV cm^2/g")
    print(f"  range ~ {rng:.1e} g/cm^2 ~ {rng/2.7/100:.0f} m of rock: stops in the")
    print(f"  cavern wall in ANY direction. P_cap ~ 1 -> trapped: {N_BH:.1e}")

    print()
    print("=" * 78)
    print("CONSUMPTION (same accretion clock as Part 3 -- arrival mode irrelevant)")
    print("=" * 78)
    earth = BODIES["Earth"]
    print(f"\n  {'n':>2} | {'1 BH eats in 4.5 Gyr':>20} | {'consume Earth':>15} | total for N_trapped(C) = {0.5*N_BH:.0e}")
    for n in range(1, 8):
        m_age, t_con = grow(n, earth)
        tot = fmt_mass(m_age * 0.5 * N_BH) if m_age else "-"
        print(f"  {n:>2} | {fmt_mass(m_age):>20} | {fmt_time(t_con):>15} | {tot}")

    print()
    print("=" * 78)
    print("RISK CLOSURE, CASE BY CASE (LHC vs nature's pre-existing population)")
    print("=" * 78)
    nat_earth_C = 2.5e22 * F_BH
    print(f"""
  C: LHC adds {0.5*N_BH:.0e} trapped BHs to the {nat_earth_C:.0e} identical ones cosmic
     rays already put in Earth -- each of which has had 4.5 Gyr (vs our decades).
     If ANY n made case-C accretion dangerous on < Gyr timescales, Earth would
     have been eaten ~4.5e9/1.2e5 ~ 40,000 times over (n=2 clock). Earth's
     existence closes case C directly; LHC multiplies the exposure by ~1e-5.

  D: same closure, via the ~{0.1*nat_earth_C:.0e} charged BHs resident in Earth and
     ~3e+18 in the Sun. LHC increment again ~1e-5 of nature's population.

  A, B: the LHC traps ~0.01 expected BHs -- with ~99% probability the entire
     program traps NONE of the dangerous kind. But this is a probabilistic
     statement, not an exclusion, and Earth/Sun history says nothing (Part 3).
     Conditional danger still requires n <= 3 (else accretion >> Hubble);
     n <= 2 flat is excluded by lab/astro gravity tests; n = 3-4 is covered
     only by the white-dwarf/neutron-star argument. The ENTIRE residual safety
     case for A/B therefore rests on: (i) the born-slow tail being ~1e-11,
     (ii) the WD/NS stopping analysis at n = 3-4. Same audit target as before.
""")
