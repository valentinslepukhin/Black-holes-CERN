# Contest Submission Documentation

This directory contains the contest-facing documentation for the FLF epistemic
case study submission.

The intended submission type is:

```text
Integrated system / workflow
```

If the form requires a single narrower category, use:

```text
Workflow document, with repository artifact/prototype attached
```

## Files

- `submission_core_10pp.md`
  - Current draft of the main submission document.
  - This is the file intended to fit inside the contest's ~10-page reading
    budget.

- `supporting_material_20pp.md`
  - Current draft of the optional supporting material.
  - This collects the artifact tour, representative findings, open gaps,
    source/correction logic, and collaboration/provenance notes.

- `early_feedback_core.md`
  - Draft core document for the June 21 early-feedback submission.
  - Kept as the earlier early-feedback draft; `submission_core_10pp.md` is the
    current sendable version.

- `form_answers.md`
  - Compact suggested answers for the submission form.

- `artifact_tour.md`
  - A short guide to what judges should inspect first in the repository.

- `collaboration_provenance.md`
  - Team/workflow background and a suggested compact version for the final
    submission.

## Submission Strategy

The repository began as a numerical update/reproduction project: re-run the
classic LHC black-hole safety argument, update inputs where 2026 data matter,
and check whether old numbers moved. As the work progressed, the main finding
became methodological rather than numerical:

```text
Most old dangerous branches become weaker under modern inputs. The more useful
work is to expose the claim graph, correction trail, model assumptions, and
qualitative loophole classes.
```

For that reason, the old Python calculations should stay in the repository as
reproducibility anchors and historical/correction references. Some scripts now
need superseded-output warnings, but they are still useful because they show how
the argument was reconstructed, checked, and corrected.

## Immediate Early-Feedback Package

For June 21, submit:

1. `submission_core_10pp.md` as the primary document.
2. GitHub repository URL as supporting artifact.
3. `supporting_material_20pp.md` as optional supporting material.
4. `form_answers.md` as the source for short form responses.

The final July submission should add a machine-readable claim graph and clean up
the stale script/readme warnings before submission.

All contest-facing material in this folder is kept in Markdown for now. Do not
create a separate PDF branch unless the final submission process requires it.
