#!/usr/bin/env python3
"""
Part 5: P(nature trapped NOTHING in Earth+Sun over 4.5 Gyr  AND  the LHC traps
>= 1 in 50 years), per case A-D -- i.e. the probability that the LHC performs a
capture experiment nature never ran. Then the same with the SUN as the LHC target.

All probabilities are CONDITIONAL on the scenario being physical at all
(TeV gravity, BH production with f_BH ~ 1e-8 per collision, absolute stability).
Counts are Poisson; the two clauses are independent populations.

Nature's expected captures mu_nat (Earth + Sun, 4.5 Gyr), from Parts 2-3:
  A, B: EXACTLY zero -- every CR-produced BH has lab gamma >= ~5e3 (even the
        most backward-emitted BH: at production threshold the CM frame itself
        has gamma_CM = sqrt(E_th/2m_p) ~ 5e3), and nothing in the solar system
        provides the ~1e21 (A) / ~1e15 (B) g/cm^2 to stop that.
        CR-CR collisions (slow CM possible) have negligible luminosity.
  C:    2.5e14 (Earth) + 3.0e18 (Sun)
  D:    2.5e13 (Earth) + 3.0e18 (Sun)

LHC expected captures over 50 yr (N_BH = 4.8e9, i.e. 2x HL-LHC program):
  EARTH target:
    A, B: born-slow tail, P = (beta_esc/0.2)^3 = 6.5e-12     -> mu = 0.031
    C:    downward hemisphere stops in 14 km rock            -> mu = 2.4e9
    D:    30 m rock range, all directions                    -> mu = 4.8e9
  SUN target:
    A, B: bound-orbit channel: P(bound to solar system) ~ 4e-10 (|v_Earth-orbit
          + v_lab| < 42 km/s, direction-weighted) -> ~2 BHs in Earth-crossing
          orbits; loss-cone fraction with perihelion < R_sun: L < sqrt(2 G M_s R_s)
          -> v_transverse < 2.9 km/s at 1 AU -> ~0.007. Each solar passage at
          v ~ 1400 km/s sheds Delta-v/v ~ 0.1-0.5 by accretion drag (focusing
          (c/v)^(4/(n+1)) now bites: slow passes are draggy, the same effect that
          is absent at gamma 5e3) -> orbit decays into the Sun in ~1e2-1e3 yr.
    C:    upward-escaping half leaves at beta ~ 0.19; fraction hitting the Sun
          = solid angle pi R_s^2 / 4 pi AU^2 = 5.4e-6; Sun column 2e11 >> 4e6
          g/cm^2 stops them.
    D:    none escape Earth -> ~0.
"""
import math

N_BH_50YR = 4.8e9
MU = {
    # case: (mu_nature_EarthPlusSun, mu_LHC_Earth, mu_LHC_Sun)
    "A (gravity only)": (0.0, N_BH_50YR * 6.5e-12, 2.1 * 0.0066),
    "B (+ weak)":       (0.0, N_BH_50YR * 6.5e-12, 2.1 * 0.0066),
    "C (+ strong)":     (2.5e14 + 3.0e18, 0.5 * N_BH_50YR, 0.5 * N_BH_50YR * 5.4e-6),
    "D (+ EM)":         (2.5e13 + 3.0e18, 1.0 * N_BH_50YR, 0.0),
}

def fmt_p(p, mu_nat=None):
    if p == 0.0 and mu_nat:                     # underflow: report the exponent
        return f"10^(-{mu_nat / math.log(10):.1e})"
    if p > 1e-4:
        return f"{100*p:.1f}%"
    return f"{p:.1e}"

if __name__ == "__main__":
    print("P(joint) = exp(-mu_nature) x (1 - exp(-mu_LHC));  50 yr LHC, f_BH = 1e-8\n")
    hdr = f"{'case':<18} {'mu_nat':>9} {'mu_LHC,E':>9} {'mu_LHC,S':>9} | {'JOINT (Earth)':>14} {'JOINT (Sun)':>14}"
    print(hdr); print("-" * len(hdr))
    for case, (mn, me, ms) in MU.items():
        p_none = math.exp(-min(mn, 700.0)) if mn < 700 else 0.0
        joint_e = p_none * (1 - math.exp(-me))
        joint_s = p_none * (1 - math.exp(-ms))
        print(f"{case:<18} {mn:>9.1e} {me:>9.2e} {ms:>9.2e} | "
              f"{fmt_p(joint_e, mn):>14} {fmt_p(joint_s, mn):>14}")

    print(f"""
Reading the table:
  * C, D: the joint event is IMPOSSIBLE -- not small, but double-double-
    exponentially zero. If trappable BHs exist, nature trapped ~1e18 of them;
    'nature trapped none' fails with certainty. One cannot coherently hold
    'dangerous strongly-interacting/charged BHs exist' AND 'Earth+Sun intact'.
    (D-Sun is zero twice over: the LHC clause also fails -- no charged BH
    ever leaves the Geneva rock.)
  * A, B: the LHC-first window is REAL but small: ~3% (Earth) / ~1% (Sun).
    These are the scenarios where capture is harmless-by-slowness for n >= 4
    (0.1 g per 4.5 Gyr) and >= 25 Gyr even at the marginal n = 3.
    So: P(LHC-first capture AND capture matters) ~ 3% x P(n <= 3 | TeV gravity),
    and n <= 3 is exactly what the white-dwarf/neutron-star argument excludes.

Sensitivity (case A, Earth): joint = 1 - exp(-3.1 x f_BH/1e-8 x T/50yr):""")
    for f in (1e-10, 1e-9, 1e-8, 1e-7, 1e-6):
        print(f"    f_BH = {f:.0e}: {100*(1-math.exp(-0.031*f/1e-8)):8.3f}%")
    print("""
Caveats:
  * 'Stuck in the Sun' via the A/B bound-orbit channel completes ~1e2-1e3 yr
    AFTER the 50-yr production window (orbital decay time); counted as stuck.
  * Bound-orbit population estimate is the crudest number here (phase-space
    tail x loss cone, each ~order-of-magnitude); 1% could be 0.1-3%.
  * Planetary perturbations refill the loss cone AND can eject the bound
    population (Jupiter) on Myr timescales -- competing effects, OOM wash.
  * Everything scales with f_BH (unknown by orders of magnitude) and is
    conditional on absolute BH stability (no Hawking, no Schwinger).""")
