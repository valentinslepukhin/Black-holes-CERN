# Artifact Tour for Judges

This is the suggested first path through the repository.

## 1. Start Here

Read:

```text
README.md
PROJECT_SUMMARY.md
contest_submission/early_feedback_core.md
```

Purpose:

```text
Understand the submission as a workflow and knowledge artifact, not as a claim
that the authors discovered a new LHC-safety result.
```

## 2. See the Core Physics Decomposition

Read:

```text
notes/01-cosmic-ray-argument.md
notes/02-capture-and-accretion.md
notes/06-neutron-star-bound.md
```

The key idea:

```text
Earth/Sun survival closes stopped-in-ordinary-matter branches. Neutral
gravity-only branches require accretion slowness plus white-dwarf/neutron-star
survival.
```

## 3. Inspect the Correction Trail

Read:

```text
notes/04-lhc-first-probability.md
notes/05-comparison-giddings-mangano.md
```

Purpose:

```text
See a concrete example where the project corrected its own first-pass estimate
after checking the primary source.
```

Important caveat:

```text
analysis/lhc_bh_fate.py and analysis/lhc_first_capture.py still need explicit
superseded-output warnings before final submission.
```

## 4. Inspect the Open-Questions Register

Read:

```text
notes/research-gaps.md
```

This is the best current guide to the unresolved structure, especially:

```text
pp production versus neutrino-nucleon production
the proton binary-companion fallback
the PDF cliff
direct-search coverage
modern 2026 updates
neutron-star superfluid/condensate accretion
```

## 5. Inspect the Combined AS Memo

Read selected sections of:

```text
summary_from_AS.md
```

Recommended sections:

```text
7. PDF Cliff Algebra
9. pp Production Versus Neutrino-Nucleon Production
10. Direct Searches and Decay Channels
13. Nonlinear and Exotic Semiclassical Gravity
16. Magnetic Fields, Magnetic Charge, and Monopole-Stabilized BHs
19. Heavy-Ion Magnetic-Field Production
notes/superfluid-spectral-accretion.md
21. Current Implementation Problems
22. Claim Graph Schema
```

Purpose:

```text
See how the methodology moves from numerical updates to qualitative
model-branch search.
```

## 6. Run the Calculations

Optional commands:

```bash
python3 analysis/cosmic_ray_flux.py
python3 analysis/bh_earth_passage.py
python3 analysis/capture_and_accretion.py
python3 analysis/ns_capture_consumption.py
```

Treat these as order-of-magnitude checks, not precision simulations.

## 7. Missing Final Artifact

The final submission should add:

```text
notes/claim_graph.yaml
```

This should be the central machine-readable artifact tying together:

```text
claims
assumptions
sources
calculations
status
corrections
update triggers
```
