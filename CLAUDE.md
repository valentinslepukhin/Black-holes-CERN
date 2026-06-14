# CLAUDE.md

Guidance for Claude Code working in this repository.

## What this project is

An entry for the **Future of Life Foundation epistemic case study competition**
(LessWrong post `frizRHnA6AZpJSDqw`, "Lab leaks, black holes, and eggs"). The
deliverable is a **generalizable AI-assisted methodology** for building a
navigable, honest, *updateable* knowledge base on a disputed topic — demonstrated
on the case study **"Will the LHC create a dangerous black hole?"**

The output that gets judged is the *methodology + the knowledge artifact it
produces*, NOT a physics essay. The physics is the testbed. Keep that framing.

- Deadlines: early-feedback submission **2026-06-21**, final **2026-07-19**.
- Final write-up cap: **≤ 10 pages** (code/examples excluded).
- The LHC case is "closed and uncontested." The competition's ask is to **expose
  the dependency structure of the settled safety argument and flag the weakest /
  most speculative links, accessibly** — not to relitigate the conclusion.
- Knowledge artifacts should: preserve nuance, track who-said-what-when + the
  supporting evidence, and remain living/updateable.

## Repository layout

```
analysis/   parameterized order-of-magnitude calculations (pure Python, stdlib only)
notes/      claims write-ups, one per layer: findings + dependency graph + assumptions log
sources/    primary sources (Giddings–Mangano 2008 = arXiv:0806.3381, the PDF)
README.md           technical overview of all five analysis layers
PROJECT_SUMMARY.md  plain-language summary for human collaborators
```

### The five layers (read `notes/` in order to get oriented)

1. `analysis/cosmic_ray_flux.py` → `notes/01` — cosmic-ray vs LHC collision rates.
2. `analysis/bh_earth_passage.py` → `notes/01`,`02` — does a black hole escape Earth,
   under four interaction hypotheses (A gravity-only, B +weak, C +strong, D +EM).
3. `analysis/capture_and_accretion.py` → `notes/02` — how many get trapped over
   4.5 Gyr, and the accretion clock vs. number of extra dimensions n.
4. `analysis/lhc_bh_fate.py`, `analysis/lhc_first_capture.py` → `notes/03`,`04` —
   collider-produced black holes; joint "LHC-traps-one-first" probability.
5. `notes/05` — diff of our independent re-derivation against the G&M paper.
6. `analysis/ns_capture_consumption.py` → `notes/06` — neutron-star bound: how
   often a NS traps a gravity-only BH (~every 16–220 yr, neutrino channel) and
   how fast it consumes the NS (yr → ~10 Myr); the decisive bound for D ≥ 8.

## How to run

```bash
python3 analysis/cosmic_ray_flux.py
python3 analysis/bh_earth_passage.py
python3 analysis/capture_and_accretion.py
cd analysis && python3 lhc_bh_fate.py && python3 lhc_first_capture.py
```

No dependencies beyond the Python standard library. `lhc_first_capture.py` imports
from `capture_and_accretion.py`, so run it from inside `analysis/`.

## Conventions — please follow these

- **Everything is order-of-magnitude.** Conclusions should hold with multi-decade
  margin; if a result is within a factor of a few of a threshold, flag it
  `MARGINAL`. Don't present OOM numbers as precision results.
- **Every script documents its assumptions in a header docstring**, and every
  `notes/` file ends with an **assumptions log**. Maintain both when you add code.
- **Corrections are appended, never silently overwritten.** When a later result
  overturns an earlier one, leave the original and add a dated correction box on
  top (see the update box at the top of `notes/04`). The correction trail *is*
  part of the methodology being showcased — it demonstrates the living knowledge
  base. Do not "clean up" by deleting superseded claims.
- **Validate against primary sources, and read them directly.** Web summaries of
  the G&M paper were unreliable (they mis-stated the D=7 timescale and the
  white-dwarf stopping direction); the PDF in `sources/` is ground truth. Cite
  page/section/equation when making a claim about what the paper says.
- **Distinguish OBSERVATION-backed nodes from CALCULATION-backed nodes** in any
  dependency graph — that distinction is the core epistemic content here.

## Current state (2026-06)

Layers 1–5 complete: independent re-derivation done and validated against G&M.
Key established findings:
- Cosmic-ray argument closes the strong/EM cases (C, D) by direct Earth/Sun
  survival; it says **nothing** about the dangerous neutral gravity-only case (A).
- Danger ⇔ testability: fast accretion needs few extra dimensions (n ≤ 3), which
  also means strong stopping → white-dwarf/neutron-star survival becomes the
  bound. The whole case pivots on **n = 3–4 (D = 7–8)**.
- We corrected our own LHC-trapping probability (was ~3%, actually near-certain
  for light BHs) after reading G&M App. F — see correction box in `notes/04`.
- The D ≥ 8 branch depends on the cosmic UHE neutrino flux: unobserved in 2008,
  IceCube-observed since 2013. A live "this node aged" example.
- Neutron stars are the decisive object for the gravity-only case (notes/06): a
  NS traps one every ~16–220 yr (neutrino channel) and is consumed in yr–10 Myr,
  vs. observed Gyr ages → excludes D = 5–11 including the D ≥ 8 WD gap.

## Open tasks (don't redo finished layers without reason)

1. Verify G&M Appendix H re: whether the "bound-solar-orbit decays into Sun"
   channel (in `notes/04`) is novel or already covered.
2. 2008 → 2026 update pass: IceCube neutrino flux, modern white-dwarf surveys,
   LHC Run 2/3 limits on M_D (now exclude the lightest scenarios).
3. Build the deliverable: machine-readable **claim graph** + ≤10-page methodology
   write-up; target a draft for the **2026-06-21** early-feedback window.

## What NOT to do

- Don't relitigate "is the LHC safe" — the answer (yes) is not in question; the
  task is mapping *why we're confident* and *where the argument is weakest*.
- Don't inflate OOM estimates into false precision.
- Don't delete or silently rewrite superseded findings — append corrections.
