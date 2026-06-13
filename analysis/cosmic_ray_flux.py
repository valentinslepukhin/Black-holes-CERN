#!/usr/bin/env python3
"""
Cosmic rays vs. LHC: center-of-mass energy comparison and event rates.

Question: how often does nature perform collisions at sqrt(s) >= LHC energy,
on Earth's atmosphere and elsewhere?

Kinematics: CR nucleus (mass number A, lab energy E) on a nucleon at rest.
Per nucleon-nucleon pair: s = 2 (E/A) m_p  (+ negligible mass terms)
=> threshold lab energy E_th = A * s / (2 m_p).

Spectrum model: piecewise power law J(E) [1/(eV m^2 s sr)], anchored at
E^3 J(E) = 1.5e24 eV^2 m^-2 s^-1 sr^-1 at E = 1e18 eV (Auger/TA scale).
Slopes approximate knee -> 2nd knee -> ankle -> GZK suppression.
All numbers are order-of-magnitude; uncertainties of factor ~2 do not
affect any conclusion (margins are 4-5 orders of magnitude).
"""
import math

M_P_GEV = 0.9383
R_EARTH_M = 6.371e6
R_SUN_OVER_R_EARTH = 109.1
SEC_PER_YR = 3.156e7
AGE_EARTH_S = 4.54e9 * SEC_PER_YR

# ---- spectrum: segments [E_lo, E_hi) with integral slope gamma ----
EDGES = [1.0e15, 1.58e17, 5.0e18, 4.0e19, 3.16e20]   # eV ('2nd knee', ankle, GZK)
SLOPES = [3.05, 3.28, 2.60, 4.50]                     # differential indices
ANCHOR_E, ANCHOR_J = 1.0e18, 1.5e24 / 1.0e18**3       # J(1e18) = 1.5e-30

def _norms():
    """Continuity-matched normalizations C_i with J = C_i E^-gamma_i."""
    C = [None] * len(SLOPES)
    i0 = 1  # anchor sits in segment 1
    C[i0] = ANCHOR_J * ANCHOR_E ** SLOPES[i0]
    for i in range(i0 - 1, -1, -1):           # extend downward
        E = EDGES[i + 1]
        C[i] = C[i + 1] * E ** (SLOPES[i] - SLOPES[i + 1])
    for i in range(i0 + 1, len(SLOPES)):      # extend upward
        E = EDGES[i]
        C[i] = C[i - 1] * E ** (SLOPES[i] - SLOPES[i - 1])
    return C

CNORMS = _norms()

def integral_flux(E_min):
    """I(>E_min) in m^-2 s^-1 sr^-1."""
    total = 0.0
    for i, g in enumerate(SLOPES):
        lo, hi = max(EDGES[i], E_min), EDGES[i + 1]
        if lo >= hi:
            continue
        total += CNORMS[i] / (g - 1) * (lo ** (1 - g) - hi ** (1 - g))
    return total

def threshold_energy_eV(sqrt_s_TeV, A=1):
    s_GeV2 = (sqrt_s_TeV * 1e3) ** 2
    return A * s_GeV2 / (2 * M_P_GEV) * 1e9

def report(sqrt_s_TeV, A, label):
    E_th = threshold_energy_eV(sqrt_s_TeV, A)
    I = integral_flux(E_th)
    area = 4 * math.pi * R_EARTH_M ** 2
    rate = I * math.pi * area          # pi sr = isotropic flux through a surface
    n_life = rate * AGE_EARTH_S
    gamma_cm = (E_th / A) / (sqrt_s_TeV * 1e12)  # boost of the NN CM frame
    print(f"--- {label}: sqrt(s_NN) = {sqrt_s_TeV} TeV, primary A = {A} ---")
    print(f"  threshold lab energy      E_th    = {E_th:.2e} eV")
    print(f"  integral flux I(>E_th)            = {I:.2e} /m^2/s/sr")
    print(f"  rate on Earth's atmosphere        = {rate:.2e} /s")
    print(f"  events over Earth history         = {n_life:.2e}")
    print(f"  events on Sun over Earth history  = {n_life * R_SUN_OVER_R_EARTH**2:.2e}")
    print(f"  CM-frame boost at threshold gamma = {gamma_cm:.1e}")
    return n_life

if __name__ == "__main__":
    # LHC reference: total inelastic pp collisions over the full (HL-)LHC program
    lumi_fb = 3000.0                  # fb^-1 (HL-LHC target)
    sigma_inel_fb = 80e-3 * 1e15      # 80 mb in fb
    n_lhc = lumi_fb * sigma_inel_fb
    print(f"LHC program total inelastic collisions ~ {n_lhc:.1e} "
          f"(3000 fb^-1 x 80 mb), all at sqrt(s) = 13.6-14 TeV\n")

    n_p = report(14.0, 1, "protons (most optimistic)")
    print()
    n_fe = report(14.0, 56, "iron primaries (most pessimistic composition)")
    print()
    print("=== Ratios: nature / LHC-program ===")
    print(f"  Earth only, proton CRs : {n_p / n_lhc:.1e}")
    print(f"  Earth only, iron CRs   : {n_fe / n_lhc:.1e}")
    print(f"  Sun, iron CRs          : {n_fe * R_SUN_OVER_R_EARTH**2 / n_lhc:.1e}")
    print(f"  (and ~1e11 stars per galaxy, ~1e11 galaxies, plus white dwarfs")
    print(f"   and neutron stars -- see bh_earth_passage.py for why those matter)")
