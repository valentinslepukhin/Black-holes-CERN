# Summary from AS

Date: 2026-06-14

This note captures the current working context for the Black-holes-CERN project
from the AS/Codex handoff. It is meant as a short bridge for future work, not a
replacement for `README.md`, `PROJECT_SUMMARY.md`, `CLAUDE.md`, or the layer
notes in `notes/`.

## Project frame

This repository is an entry for the Future of Life Foundation epistemic case
study competition. The judged object is the methodology and knowledge artifact:
a navigable, honest, updateable claim/evidence structure demonstrated on the
question, "Will the LHC create a dangerous black hole?"

The project should not become just another LHC safety essay. The physics is the
testbed for a more general workflow: extracting claims, representing dependency
structure, tracking evidence, preserving assumptions, reproducing calculations,
logging corrections, and identifying update triggers.

## Current understanding

The primary literature spine is Giddings and Mangano 2008, "Astrophysical
implications of hypothetical stable TeV-scale black holes" (arXiv:0806.3381),
plus the 2008 LSAG safety report (arXiv:0806.3414). The repository has already
implemented five order-of-magnitude layers:

1. Cosmic-ray vs. LHC collision rates.
2. Earth passage and stopping for cosmic-ray-produced black holes under several
   interaction hypotheses.
3. Capture statistics and accretion clocks.
4. Collider-produced black-hole fate and the "LHC first" probability.
5. A direct comparison against Giddings-Mangano.

The most important epistemic point is that "cosmic rays prove the LHC is safe"
is too compressed. Earth/Sun survival closes branches where produced black holes
are stopped in ordinary matter, especially strong or electromagnetic
interaction cases. The dangerous neutral, gravity-only stable branch is not
closed by ordinary Earth cosmic-ray survival, because ultra-relativistic
cosmic-ray-produced black holes pass through the Earth. That branch is handled
by accretion slowness plus white-dwarf and neutron-star survival.

Compact dependency structure:

```text
fast danger -> astrophysically testable -> excluded
not astrophysically excluded -> too slow to be dangerous
```

The project should keep this branch structure explicit, with observation-backed
nodes distinguished from calculation-backed and assumption-backed nodes.

## Guardrails for future edits

- Keep all calculations order-of-magnitude and flag marginal results.
- Validate load-bearing claims against primary sources, citing section, page,
  equation, or table where possible.
- Append corrections instead of silently rewriting superseded findings.
- Preserve the corrected lesson from Giddings-Mangano Appendix F: LHC capture is
  not impossible for light stable black holes; the safety argument rests on
  accretion slowness and astrophysical exclusions, not on capture improbability.
- Treat IceCube as a partial update to the old neutrino-flux node, not as a
  blanket settlement of every UHE/cosmogenic neutrino assumption.
- Treat modern LHC limits as an update node that shrinks parameter space, not as
  a substitute for the pessimistic stable-black-hole safety argument.

## Near-term work

1. Verify whether Giddings-Mangano Appendix H already covers the bound-solar-
   orbit decay-into-Sun channel noted in `notes/04-lhc-first-probability.md`.
2. Build the machine-readable claim graph with fields for status,
   supersession, source references, code references, assumptions, and update
   triggers.
3. Add a concise methodology write-up aimed at the competition deliverable.
4. Run the 2008-to-2026 update pass:
   - IceCube and high-energy neutrino flux status.
   - Gaia-era white-dwarf demographics, ages, masses, and magnetic-field
     systematics.
   - Run 2/Run 3 ATLAS/CMS constraints on microscopic black holes and
     extra-dimensional Planck scales.
   - Modern UHECR spectrum and composition inputs.

## Push/publishing note

As of this note, the local workspace has been checked out from
`https://github.com/valentinslepukhin/Black-holes-CERN.git`. Future publishable
outputs can be added on a branch, checked by running the existing stdlib Python
scripts, committed, and pushed to GitHub when credentials permit.
