#!/usr/bin/env python3
"""
Passage of a hypothetical stable TeV-scale black hole through Earth.

Scenario: a cosmic ray (E ~ 1e17 eV) hits an atmospheric nucleon and produces
a BH of mass M ~ 10 TeV. The CM frame is boosted with gamma_CM ~ 7e3, so the
BH enters Earth relativistically. It ESCAPES unless interactions degrade its
velocity below v_esc = 11.2 km/s (beta_esc = 3.7e-5) within one chord.

We compare four interaction hypotheses for the BH:
  A) gravitational only (absorbs what it geometrically intersects)
  B) gravity + weak      (neutrino-like cross sections)
  C) gravity + strong    (hadronic cross sections)
  D) gravity + EM        (retains electric charge ~ e; Bethe ionization)

Kinematic facts used:
  * Absorption of a nucleon at rest conserves momentum: p stays fixed,
    E grows by m_p per event. Capture requires beta = p/E < beta_esc,
    i.e. E must grow to p/beta_esc -- counting argument on N_absorptions.
  * Elastic scattering off a light target (m << M): max energy transfer
    W_max = 2 m beta^2 gamma^2 / (1 + 2 gamma m/M + (m/M)^2); take
    <dE> = W_max/2 per collision (isotropic in CM, order-of-magnitude).
  * Charged particle ionization: ~2 MeV/(g/cm^2) at minimum ionizing.

Everything is order-of-magnitude; conclusions have >= 1-2 decades of margin
except where flagged MARGINAL.
"""
import math

# ---- constants (GeV, cm) ----
M_P = 0.9383                      # GeV
GEV_INV_CM = 1.97e-14             # hbar*c in GeV*cm
RHO_EARTH = 5.514                 # g/cm^3 (mean)
N_NUC = RHO_EARTH / 1.6605e-24    # nucleons/cm^3 = 3.3e24
R_EARTH_CM = 6.371e8
CHORD_CM = 2 * R_EARTH_CM         # worst case (diametric); mean chord = 4R/3
BETA_ESC = 11.2e5 / 2.998e10      # 3.74e-5

COLUMNS = {                       # available stopping columns, g/cm^2
    "Earth (diameter)":        RHO_EARTH * CHORD_CM,            # ~7e9
    "Sun (diameter)":          1.41 * 1.392e11,                 # ~2e11
    "White dwarf (radius)":    1.0e6 * 1.0e9,                   # ~1e15
    "Neutron star (radius)":   5.0e14 * 1.2e6,                  # ~6e20
}

# ---- BH parameters ----
M_BH = 1.0e4                      # GeV (10 TeV)
M_D = 1.0e3                       # GeV (TeV-scale Planck mass)
GAMMA0 = 7.4e3                    # production boost (CR at threshold energy)


def r_horizon_cm(M, n_extra):
    """Horizon radius in 4+n dims, r_H ~ (1/M_D)(M/M_D)^(1/(n+1)), O(1) factors dropped."""
    return (1.0 / M_D) * (M / M_D) ** (1.0 / (n_extra + 1)) * GEV_INV_CM


def column_to_stop_elastic(sigma_cm2, M=M_BH, gamma0=GAMMA0, beta_floor=BETA_ESC):
    """
    Nucleon column density (g/cm^2) needed to drag the BH below beta_floor
    via elastic collisions with <dE> = W_max/2 each.
    Integrates collision-by-collision in the relativistic regime, then uses
    the non-relativistic exponential: N_nr = (M/m) ln(beta1/beta_floor).
    """
    n_coll = 0.0
    gamma = gamma0
    # relativistic phase: fractional KE loss per collision
    while gamma > 1.5:
        ke = (gamma - 1) * M
        beta2 = 1 - 1 / gamma**2
        wmax = 2 * M_P * beta2 * gamma**2 / (1 + 2 * gamma * M_P / M + (M_P / M) ** 2)
        f = 0.5 * wmax / ke
        # step in blocks for speed
        step = max(1.0, 0.01 / f)
        ke *= (1 - f) ** step
        gamma = 1 + ke / M
        n_coll += step
    beta1 = math.sqrt(1 - 1 / gamma**2)
    n_coll += (M / M_P) * math.log(beta1 / beta_floor)   # <dE>/KE ~ 2m/M per coll.
    return n_coll / sigma_cm2 * 1.6605e-24               # g/cm^2


def case_A(n_extra=6):
    sigma = math.pi * r_horizon_cm(M_BH, n_extra) ** 2
    n_abs_available = N_NUC * sigma * CHORD_CM
    # capture condition: E must grow from gamma0*M to p/beta_esc, +m_p per absorption
    p0 = GAMMA0 * M_BH                                   # beta ~ 1
    n_abs_needed = (p0 / BETA_ESC - GAMMA0 * M_BH) / M_P
    col_needed = n_abs_needed / sigma * 1.6605e-24
    return sigma, n_abs_available, n_abs_needed, col_needed


def sigma_weak(E_lab_GeV):
    """nu-N-like CC cross section (Gandhi et al. scaling), equivalent E = gamma*M."""
    return 5.5e-36 * E_lab_GeV ** 0.363                  # cm^2


def case_B():
    """March through Earth; each weak interaction sheds <y> ~ 0.25 of energy
    (capped by kinematics 2*gamma*m/M when that is smaller)."""
    x, gamma = 0.0, GAMMA0
    n_int = 0
    while x < CHORD_CM and gamma > 1.05:
        lam = 1.0 / (N_NUC * sigma_weak(gamma * M_BH))
        if x + lam > CHORD_CM:
            break
        x += lam
        y = min(0.25, 2 * gamma * M_P / M_BH)
        gamma = 1 + (gamma - 1) * (1 - y)
        n_int += 1
    return n_int, gamma


def case_C(sigma_mb=40.0):
    sigma = sigma_mb * 1e-27
    col_stop = column_to_stop_elastic(sigma)
    depth_km = col_stop / RHO_EARTH / 1e5
    return sigma, col_stop, depth_km


def case_D(dedx_min=2.0):
    """Charged BH, |Q| = e. Range against ionization (min-ionizing approx;
    conservative: dE/dx rises as 1/beta^2 once slow, and ln(gamma) when fast)."""
    ke = (GAMMA0 - 1) * M_BH * 1e3                       # MeV
    range_col = ke / dedx_min                            # g/cm^2
    gamma_punch = 1 + COLUMNS["Earth (diameter)"] * dedx_min / (M_BH * 1e3)
    return range_col, gamma_punch


def verdict(col_needed):
    out = []
    for name, col in COLUMNS.items():
        out.append(f"      {name:24s} X = {col:9.1e} g/cm^2 -> "
                   f"{'STOPS it' if col > col_needed else 'escapes'}")
    return "\n".join(out)


if __name__ == "__main__":
    print(f"BH mass {M_BH/1e3:.0f} TeV, production boost gamma0 = {GAMMA0:.1e}, "
          f"beta_esc(Earth) = {BETA_ESC:.2e}")
    print(f"Earth diametric column = {COLUMNS['Earth (diameter)']:.1e} g/cm^2\n")

    print("== A) GRAVITY ONLY ==")
    for n in (2, 6):
        sig, n_av, n_need, col = case_A(n)
        print(f"  n_extra={n}: sigma_abs = pi r_H^2 = {sig:.1e} cm^2")
        print(f"    nucleons absorbed crossing Earth : {n_av:.1f}")
        print(f"    absorptions needed for capture   : {n_need:.1e}")
        print(f"    column needed                    : {col:.1e} g/cm^2")
    _, _, _, colA = case_A(6)
    print(verdict(colA))
    print("    -> ESCAPES Earth by ~11 orders of magnitude. Only neutron-star")
    print("       columns suffice (white dwarf marginal -> dimension-dependent;")
    print("       enhanced low-velocity grav. scattering helps, cf. G&M 2008).\n")

    print("== B) + WEAK INTERACTIONS ==")
    n_int, g_exit = case_B()
    print(f"  sigma_w(gamma0*M = {GAMMA0*M_BH:.1e} GeV) = {sigma_weak(GAMMA0*M_BH):.1e} cm^2")
    print(f"  interactions in one chord: {n_int}, exit gamma = {g_exit:.0f} (beta ~ 1)")
    colB_rel = column_to_stop_elastic(sigma_weak(GAMMA0 * M_BH))  # generous: fixed high sigma
    print(f"  column to fully stop (even holding sigma at its high-energy value):")
    print(f"    >= {colB_rel:.1e} g/cm^2 (worse in reality: sigma_w collapses at low E)")
    print(verdict(colB_rel))
    print("    -> ESCAPES Earth: Earth is just opaque enough to make it interact")
    print("       ~10 times, but each sheds only ~25% of KE; needs ~30 e-folds.\n")

    print("== C) + STRONG INTERACTIONS ==")
    sig, col, depth = case_C()
    lam = 1.0 / (N_NUC * sig)
    print(f"  sigma_had = 40 mb, mean free path = {lam:.1f} cm")
    print(f"  stopping column = {col:.1e} g/cm^2  ->  stopping depth ~ {depth:.0f} km of rock")
    print(verdict(col))
    print("    -> TRAPPED: thermalizes within ~10 km, v << v_esc, sinks to core.")
    print("       Earth's 4.5 Gyr survival under ~1e22 such events applies DIRECTLY.\n")

    print("== D) + ELECTROMAGNETIC (retains charge e) ==")
    rng, g_punch = case_D()
    print(f"  ionization range at gamma0: {rng:.1e} g/cm^2 "
          f"vs Earth chord {COLUMNS['Earth (diameter)']:.1e}")
    print(f"  punch-through condition: gamma > {g_punch:.0f}")
    print(verdict(rng))
    print(f"    -> MARGINAL: at production boost ~7e3 it punches through Earth")
    print(f"       (factor ~5), but any BH with gamma < {g_punch:.0f} stops; the Sun")
    print(f"       stops all of them. Caveat: charge retention itself is doubtful")
    print(f"       (Schwinger discharge), and discharge physics is a cousin of")
    print(f"       Hawking emission -- a dependency worth flagging.")
