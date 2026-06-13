# Black Holes at the LHC — an epistemic audit

An independent, quantitative audit of the safety argument for hypothetical stable
TeV-scale black holes at the LHC ("Will CERN generate a black hole?"), built as a
case study for the [FLF epistemic case study competition](https://www.lesswrong.com/posts/frizRHnA6AZpJSDqw/lab-leaks-black-holes-and-eggs-epistemic-case-study)
(deadlines: early feedback **June 21, 2026**, final **July 19, 2026**).

**Method:** re-derive the published safety case (Giddings–Mangano 2008,
arXiv:0806.3381; LSAG report) from first principles at order-of-magnitude level,
decompose it into a claim–dependency graph, identify the weakest links — then diff
against the primary source and log every validation and correction explicitly.

## Repository layout

```
analysis/   parameterized order-of-magnitude calculations (pure Python, no deps)
notes/      claims write-ups: findings, dependency graphs, assumptions logs
sources/    primary sources (G&M 2008 PDF, 97 pp)
```

## The five layers (chronological)

### 1. Cosmic rays vs. LHC — `analysis/cosmic_ray_flux.py`, `notes/01`
√s = 14 TeV requires a cosmic-ray proton of 1.0×10¹⁷ eV on an atmospheric nucleon.
Integrating the CR spectrum: **~1.8×10⁵ LHC-equivalent collisions/s on Earth,
2.5×10²² over its history** (matches G&M's ~10²²) vs. 2.4×10¹⁷ for the whole LHC
program. Caveat found: a pure-iron composition cuts Earth's margin from 10⁵× to
~10³× (initially mis-estimated as 17×, corrected in layer 5); the Sun restores it.

### 2. Does a CR-produced BH escape Earth? — `analysis/bh_earth_passage.py`, `notes/02`
CR-produced BHs enter at γ ~ 7×10³. Modeled traversal under four interaction
hypotheses; escape ⇔ stopping column > Earth's 7×10⁹ g/cm²:

| Case | Outcome |
|---|---|
| A: gravity only | escapes by many orders — nothing in the solar system stops it |
| B: + weak | escapes (Earth ≈ 1 interaction length, sheds ~25%/hit, needs ~30 e-folds) |
| C: + strong | **trapped in ~9 km of rock** |
| D: + EM (charge e) | marginal: trapped iff γ < 1.4×10³; the Sun stops all |

### 3. Capture statistics + accretion clock — `analysis/capture_and_accretion.py`, `notes/02`
Over 4.5 Gyr: cases C/D leave ~10¹⁴ BHs in Earth and ~3×10¹⁸ in the Sun (capture
certain); cases A/B leave **exactly zero** — Earth/Sun survival says *nothing* about
the dangerous (neutral, gravity-only) scenario. Once trapped, gravitational accretion
speed is set by extra dimensions n: Earth consumed in ~10⁵ yr (n=2), ~25 Gyr (n=3,
marginal), never (n≥4: 0.1 g per age-of-Earth). **Key structure: danger and empirical
testability switch on together** — fast accretion ⇔ strong stopping ⇔ white dwarfs
trap CR-made BHs, so the dangerous corner is exactly the observationally bounded one.
The pivot is n = 3–4 (D = 7–8).

### 4. Collider-produced BHs + "LHC-first" probability — `analysis/lhc_bh_fate.py`,
`analysis/lhc_first_capture.py`, `notes/03`, `notes/04`
At the LHC the lab is the CM frame: BHs are born slow (β ~ 0.2). Mirror image of the
CR case: C/D trapped copiously (~10⁹ — a 10⁻⁵ increment on nature's population),
A/B almost never. Joint Poisson probability P(nature trapped none AND LHC traps ≥1
in 50 yr): **identically ~0 for C/D** (μ_nat ~ 10¹⁸ — one cannot coherently believe
such BHs exist and observe Earth/Sun intact) vs. a real open window for A/B.
Includes a possibly-novel channel: LHC BHs in bound solar orbits decaying into the
Sun via repeated-passage accretion drag (~10²–10³ yr).

### 5. Diff against Giddings–Mangano — `sources/`, `notes/05`
Read the primary source directly (Table 1, §§4–5, 7–9, App. F).
**Validated:** D=6 accretion within ×2; D=7 (25 Gyr) inside their 6–80 Gyr; exact-zero
CR slow tail (E > M²/2m_p — identical formula); charged stopping thresholds;
Sun-core geometry to the digit; no-Eddington-limit stance; Schwinger⇔Hawking
correlation. **Corrected (ours):** LHC trapping probability is 10⁻⁵–10⁻³ per BH, not
10⁻¹² — 1/v accretion drag traps up to ~25× v_esc and the slow tail is linear (flat
rapidity), so "LHC-first capture" is near-certain for M ≲ 7 TeV at D ≥ 8, not 3%;
Fe margin ~10³ not 17×; neutral stopping column ~10¹⁶ not 10²¹ g/cm² (quantum
gravitational scattering). **Sharpest new dependency surfaced:** for D ≥ 8 the
safety case rests on the cosmic UHE neutrino flux (making BHs inside neutron stars)
— unobserved in 2008, since detected by IceCube: a calculation-node that became an
observation-node, demonstrating why knowledge bases must be living.

## Where the whole safety case bottoms out

```
no-Hawking worst case (assumed)
├── C/D (strong/EM-interacting): closed by Earth+Sun survival, margin ~1e18  [OBSERVATION]
├── A/B, R_C < 200 Å (incl. flat D≥8): Earth accretion >> solar lifetime    [CALCULATION]
├── A/B, D ≤ 7: white-dwarf survival; D=7 needs old, low-B, ≥1.1 M_sun WDs  [OBS + CALC]
└── A/B, D ≥ 8: neutron-star survival via cosmic-neutrino-made BHs          [OBS + CALC]
     └── depends on UHE neutrino flux: 2008 assumption → 2013+ IceCube data
Residual (Ord–Hillerbrand–Sandberg): P(correlated error in the calculations),
concentrated in WD astronomy and low-velocity accretion/stopping physics at D=7–8.
```

## Running

```bash
python3 analysis/cosmic_ray_flux.py
python3 analysis/bh_earth_passage.py
python3 analysis/capture_and_accretion.py
cd analysis && python3 lhc_bh_fate.py && python3 lhc_first_capture.py
```

No dependencies beyond the standard library. All numbers are order-of-magnitude;
every script documents its assumptions in the header, and each `notes/` file ends
with an assumptions log. Corrections are appended, not silently edited (see the
update box in `notes/04`).

## Status / next steps

- [x] Layers 1–5 (re-derivation, capture, accretion, LHC fate, primary-source diff)
- [ ] Verify App. H (background objects) re: the bound-orbit Sun channel novelty claim
- [ ] 2008 → 2026 update pass: IceCube flux, WD surveys, LHC Run 2/3 limits on M_D
- [ ] Build the competition artifact: machine-readable claim graph + ≤10 pp
      methodology write-up (early-feedback submission June 21, 2026)
