# Suggested Submission Form Answers

These are draft answers for the FLF/LessWrong submission form.

## Submission Type

Preferred, if available:

```text
Integrated system / workflow
```

Fallback:

```text
Workflow document
```

Add in the description that the repository is the supporting artifact/prototype.

## Layers Addressed

Select all that apply:

```text
ingestion
structure
assessment
integrated
```

If only one is allowed, choose:

```text
integrated
```

## 2-5 Sentence Description

Draft:

```text
This submission is a workflow and knowledge artifact for decomposing a
settled-but-complex safety argument into claims, assumptions, calculations,
source dependencies, correction history, and update triggers. The prototype
applies the method to the LHC microscopic black-hole safety case, showing how
the conclusion depends on cosmic-ray exposure, stopping, accretion,
white-dwarf/neutron-star survival, direct-search coverage, and model-specific
loopholes. The repository includes reproducible order-of-magnitude checks and
structured notes; the primary document gives a guided tour of the representative
slices judges should inspect first. The current early-feedback version is a
working prototype; the final version will add a machine-readable claim graph and
cleaner reuse instructions.
```

## Primary Document URL

Use a hosted version of:

```text
contest_submission/early_feedback_core.md
```

For final submission, this can become a PDF or Google Doc if preferred.

## Repository URL

```text
https://github.com/valentinslepukhin/Black-holes-CERN
```

## Extra Context

Draft:

```text
The Python calculations are intentionally retained as reference artifacts, even
where later comparison with the primary literature corrected part of their
interpretation. The project began as an attempt to update the numerical safety
margins, but as modern inputs generally weakened rather than strengthened old
dangerous branches, the work shifted toward surfacing qualitative model
assumptions and adversarial loophole classes. This correction trail is part of
the intended methodology.
```

## Early Feedback Checkbox

For June 21:

```text
Yes, this is for early feedback.
```

## Follow-On Funded Work

Suggested:

```text
Yes.
```

Possible expansion:

```text
We would be interested in developing the claim-graph format, adding a second
case study, and turning the current repository into a reusable template for
AI-assisted epistemic audits.
```

## Short Bio / Team Context

Keep this compact. Suggested version:

```text
The project combines two paths. Valentin Slepukhin led much of the coding and
conceptual decomposition work in Claude Code, bringing a modeling background
that now sits closer to soft condensed matter and biophysics. Andrey Sadofyev
then added a particle-physics expert pass using Codex; his current work is
mainly QCD jets, jet quenching, and heavy-ion physics rather than TeV-gravity
model building, but the old BSM/LHC-safety literature was a natural adjacent
domain from earlier high-energy-theory training. The workflow explicitly uses
this division: automated reconstruction and calculation first, then
domain-adjacent expert pressure-testing for qualitative loopholes.
```

Optional shorter version:

```text
The team combines a coding/modeling path with a particle-physics expert pass:
Valentin Slepukhin led the Claude Code/repository path, while Andrey Sadofyev
added domain-adjacent particle-physics review through Codex, especially around
QCD, heavy-ion, medium-induced radiation, and older BSM assumptions.
```
