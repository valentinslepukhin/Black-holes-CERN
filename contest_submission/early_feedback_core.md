# Early Feedback Core Draft

Working title:

```text
Black Holes at the LHC as an Epistemic Audit:
A Claim-Graph Workflow for Settled but Complex Safety Arguments
```

## 1. Submission Type

This is an integrated workflow and knowledge artifact. If the contest form
requires a single category, classify it as a workflow document with a repository
prototype attached.

The submission is not primarily a physics essay about whether CERN is safe. It
is a demonstration of a general method for turning a complex safety argument
into:

- explicit claims,
- assumptions,
- evidence links,
- order-of-magnitude checks,
- correction history,
- update triggers,
- and model-dependent loophole branches.

## 2. Case Study

The case study is the hypothetical production of stable microscopic black holes
at the LHC. The scientific conclusion is widely regarded as settled: the LHC is
safe. That makes the case useful for a methodology competition, because the goal
is not to manufacture suspense but to expose why confidence is warranted and
where the argument actually rests.

The core safety structure is:

```text
fast danger -> astrophysically testable -> excluded
not astrophysically excluded -> too slow to be dangerous
```

The slogan "cosmic rays prove the LHC is safe" is too compressed. A more precise
statement is:

```text
Earth/Sun cosmic-ray survival closes branches where produced black holes are
stopped in ordinary matter. The neutral gravity-only stable branch is not closed
by ordinary Earth cosmic-ray survival, because cosmic-ray-produced black holes
are ultra-relativistic and pass through ordinary matter. That branch is handled
by accretion slowness plus white-dwarf and neutron-star survival.
```

## 3. Current Artifact

The repository currently contains:

- dependency-free Python order-of-magnitude calculations,
- numbered notes for each physics layer,
- a direct comparison against Giddings-Mangano 2008,
- a research-gap register,
- a combined AS handoff memo,
- and a draft plan for a machine-readable claim graph.

Representative files:

```text
README.md
PROJECT_SUMMARY.md
analysis/
notes/01-cosmic-ray-argument.md
notes/02-capture-and-accretion.md
notes/03-lhc-produced-bh.md
notes/04-lhc-first-probability.md
notes/05-comparison-giddings-mangano.md
notes/06-neutron-star-bound.md
notes/research-gaps.md
summary_from_AS.md
```

The calculation scripts are deliberately retained even where later reading
corrected part of their interpretation. They are part of the audit trail: the
project shows how an initially plausible estimate was tested against the primary
source, found wrong, and demoted.

## 4. How the Project Evolved

The initial plan was to check updated numbers:

- modern cosmic-ray and neutrino inputs,
- modern direct LHC limits,
- white-dwarf and neutron-star data,
- and whether 2008 safety margins had changed.

As the investigation progressed, it became clear that along the old quantitative
paths the level of danger was generally getting lower, not higher. Direct LHC
searches push the production premise into a smaller window; modern compact-star
and multimessenger observations mostly refine rather than overturn the old
astrophysical argument.

The work therefore shifted toward the more valuable question:

```text
Which qualitative assumptions would have to fail for the old safety structure
to stop working?
```

This led to explicit branches for:

- pp versus neutrino-nucleon production,
- PDF-cliff sensitivity near threshold,
- stable or invisible decay channels,
- exotic semiclassical gravity,
- Born-Infeld / higher-curvature / regular-BH variants,
- monopole-stabilized or magnetically charged black holes,
- heavy-ion magnetic-field production,
- and the possibility that direct searches miss rare or nonstandard channels.

## 5. Method

The workflow is:

1. Start from a compact public claim.

   Example:

   ```text
   Cosmic rays show the LHC is safe.
   ```

2. Decompress it into conditional branches.

   Example:

   ```text
   stopped in ordinary matter
   not stopped in ordinary matter
   Hawking-radiating
   stable or remnant
   visible decay
   invisible/stable decay
   pp-like production
   neutrino-nucleon production
   ```

3. Attach each branch to a source, calculation, or assumption.

4. Run small reproducible OOM checks where possible.

5. Compare against the primary literature and record corrections explicitly.

6. Mark every node by status:

   ```text
   current
   superseded
   disputed
   marginal
   needs_update
   ```

7. Add update triggers.

   Example:

   ```text
   new EeV neutrino flux measurement
   new direct LHC high-mass search
   revised white-dwarf age/magnetic-field catalog
   new neutron-star EOS/population constraints
   ```

8. Use expert and adversarial passes to search for model classes that attack
   load-bearing assumptions rather than merely changing small numerical inputs.

## 6. Example Correction Trail

An early project estimate treated the probability that the LHC traps a stable
black hole as extremely small. Direct comparison with Giddings-Mangano Appendix
F showed this was wrong: low-velocity accretion drag and the rapidity
distribution make trapping of light stable LHC black holes much larger than the
first script implied.

The correction changed the interpretation:

```text
Bad argument:
The LHC is safe because trapping is unlikely.

Correct argument:
The LHC may trap light stable black holes in pessimistic branches, but branches
with dangerous accretion are excluded by astrophysical survival, while branches
not excluded are too slow to matter.
```

The older script remains useful as a reference point, but it should be marked as
superseded before final submission.

## 7. Current Load-Bearing Nodes

The most important nodes are:

1. Production threshold and PDF cliff.
2. Cosmic-ray fixed-target comparison.
3. Whether cosmic-ray-produced black holes stop in ordinary matter.
4. Whether LHC-produced black holes are slow enough to be captured.
5. Accretion time once captured.
6. White-dwarf survival for lower-dimensional branches.
7. Neutron-star survival for higher-dimensional branches.
8. Whether pp production transfers to neutrino-nucleon production.
9. The proton binary-companion fallback if neutrino production is suppressed.
10. Direct-search coverage of prompt visible versus invisible/stable channels.

## 8. What Is Missing Before Final

The final July submission should add:

1. A machine-readable claim graph, probably `notes/claim_graph.yaml`.
2. Superseded-output warnings in old LHC capture scripts.
3. README and PROJECT_SUMMARY cleanup: the repo now has six layers, not five.
4. A focused note on production/PDF-cliff algebra.
5. A focused note on direct-search coverage.
6. A focused note on exotic/magnetic/HIC branches.
7. A short "how to reuse this workflow on another case" section.

## 9. Why This Should Generalize

The workflow is not specific to black holes. It is meant for cases where:

- the public claim is compressed,
- the conclusion depends on several disciplines,
- direct experiments do not cover all branches,
- old arguments contain update-sensitive nodes,
- and the main residual risk is correlated error in the argument structure.

Examples where the same template could travel:

- lab-leak evidence chains,
- geoengineering risk arguments,
- AI model eval claims,
- controversial public-health claims,
- nuclear or accelerator safety cases,
- long-range environmental risk assessments.

The reusable output is not a single answer. It is a structured map of which
answers depend on which evidence.

## 10. Early-Feedback Ask

We are especially interested in feedback on:

1. Whether the claim-graph schema is the right central artifact.
2. Whether the representative slice is readable enough for judges.
3. Whether the submission should emphasize the LHC physics audit or the general
   workflow more strongly.
4. Whether the correction-trail approach is legible and valuable.
5. Whether the final version should include a second, smaller case study to
   demonstrate transfer.

## 11. Current Status

The repo is a working prototype, not a polished final submission. It already
contains enough structure for early feedback:

```text
physics audit: substantial
calculation trail: substantial
source comparison: partial but real
research-gap register: substantial
claim graph: planned, not yet implemented
final writeup: draft stage
```

The intended final submission is a concise workflow document plus a navigable
artifact, not a long physics report.
