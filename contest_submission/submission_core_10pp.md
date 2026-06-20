# Black Holes at the LHC as an Epistemic Audit

Subtitle:

```text
A claim-graph workflow for settled but complex safety arguments
```

## 1. What This Submission Is

This is an integrated workflow and knowledge artifact. If the submission form
requires a narrower label, classify it as:

```text
Workflow document, with repository artifact/prototype attached.
```

The submission is not mainly a physics essay about whether CERN is safe. The
scientific conclusion is already widely treated as settled: the LHC is safe. The
interesting task is methodological: show how a complex safety argument can be
decompressed into claims, assumptions, calculations, sources, corrections, and
update triggers.

The prototype applies the method to the LHC microscopic-black-hole question.

Repository:

```text
https://github.com/valentinslepukhin/Black-holes-CERN
```

## 2. Why This Case

The public version of the argument is often compressed to:

```text
Cosmic rays prove the LHC is safe.
```

That sentence is directionally useful but epistemically too coarse. It hides
several branches:

```text
Does the black hole Hawking-radiate?
Is it stable or a remnant?
Is it stopped in ordinary matter?
Is it neutral, charged, colored, magnetic, or hidden-sector?
Does Earth/Sun survival apply?
Do white dwarfs or neutron stars supply the relevant bound?
Do LHC direct searches cover the decay channel?
Does pp production transfer to cosmic neutrino-nucleon production?
```

A more accurate summary is:

```text
Earth/Sun cosmic-ray survival closes branches where produced black holes are
stopped in ordinary matter. The neutral gravity-only stable branch is not closed
by ordinary Earth cosmic-ray survival, because cosmic-ray-produced black holes
are ultra-relativistic and pass through ordinary matter. That branch is handled
by accretion slowness plus white-dwarf and neutron-star survival.
```

The compact safety structure is:

```text
fast danger -> astrophysically testable -> excluded
not astrophysically excluded -> too slow to be dangerous
```

This makes the case useful for a methodology competition: the goal is not to
generate a dramatic new conclusion, but to make the dependency structure visible
enough that a future investigator can inspect, challenge, update, or reuse it.

## 3. What The Repository Contains

The current artifact has four parts:

1. **Executable order-of-magnitude checks**

   Directory:

   ```text
   analysis/
   ```

   These scripts reproduce the main numerical branches at order-of-magnitude
   level. They are intentionally small and dependency-free.

2. **Layered notes**

   Directory:

   ```text
   notes/
   ```

   The notes decompose the physics argument into cosmic-ray exposure,
   stopping/capture, accretion, LHC-produced black holes, comparison with
   Giddings-Mangano, neutron-star bounds, and research gaps.

3. **Correction trail**

   The project keeps superseded first-pass estimates visible rather than
   silently overwriting them. One important example is the early LHC-capture
   estimate, later corrected after reading Giddings-Mangano Appendix F.

4. **Contest-facing documentation**

   Directory:

   ```text
   contest_submission/
   ```

   This folder contains the current submission draft, supporting material, form
   answers, artifact tour, and collaboration/provenance note.

## 4. How The Project Evolved

The project began as a numerical update/reproduction task:

```text
Re-run the old LHC black-hole safety argument, compare with 2026 inputs, and
see whether the safety margins changed.
```

That remains part of the artifact. The Python files are useful as a
reproducibility trail and as references for the calculation branches.

But the investigation changed shape. Along the old quantitative paths, modern
information generally makes the dangerous branches smaller rather than larger:

- direct LHC searches push visible benchmark scenarios upward in mass,
- higher thresholds are amplified by the high-x PDF cliff,
- compact-star observations refine rather than erase the old astrophysical
  survival argument,
- and ordinary Hawking-radiating branches are not dangerous in the first place.

The more valuable work became qualitative:

```text
Which assumptions would have to fail, and in what specific way, for the old
safety structure to stop working?
```

That led to a search for branch-breaking assumptions:

- pp production versus neutrino-nucleon production,
- invisible/stable/long-lived decay channels,
- exotic semiclassical gravity,
- Born-Infeld / higher-curvature / regular-black-hole variants,
- monopole-stabilized or magnetically charged black holes,
- heavy-ion magnetic-field production,
- slow neutron-star consumption,
- neutron-star superfluid/condensate suppression of stopping or accretion,
- and whether observed neutron stars could be replaced by exotic BH-like
  objects.

## 5. The Workflow

The workflow is:

1. **Start with a compressed claim.**

   Example:

   ```text
   Cosmic rays prove the LHC is safe.
   ```

2. **Split it into conditional branches.**

   Example:

   ```text
   stopped in ordinary matter
   not stopped in ordinary matter
   Hawking-radiating
   stable/remnant
   visible decay
   invisible/stable decay
   pp-like production
   neutrino-nucleon production
   ```

3. **Attach each branch to a status.**

   ```text
   observation
   calculation
   assumption
   model
   correction
   update-sensitive node
   ```

4. **Run small checks where possible.**

   The calculations are not precision simulations. They are transparent
   order-of-magnitude tests designed to reveal which dependencies matter.

5. **Compare against primary literature.**

   The main source spine is Giddings-Mangano 2008 and the LSAG report, with
   later checks against modern direct searches, neutrino/cosmic-ray literature,
   and compact-star updates.

6. **Record corrections explicitly.**

   A wrong first-pass calculation is useful if it shows where an intuitive
   argument failed.

7. **Search adversarially for qualitative loopholes.**

   Once ordinary numerical updates push danger lower, the interesting residual
   becomes model structure: which assumptions can be broken without breaking the
   LHC-production premise itself?

8. **Convert the result into a claim graph.**

   The final intended artifact is a machine-readable claim graph tying together
   claims, evidence, code, sources, corrections, and update triggers.

## 6. Representative Finding: Capture Is Not The Safety Argument

An early project estimate made LHC capture look extremely unlikely. Direct
comparison with Giddings-Mangano Appendix F corrected that. Low-velocity
accretion drag and the rapidity distribution can make trapping of light stable
LHC black holes much larger than the first-pass estimate suggested.

That correction changed the interpretation:

```text
Bad argument:
The LHC is safe because capture is unlikely.

Correct argument:
The LHC may trap light stable black holes in pessimistic branches. Safety rests
on accretion slowness and astrophysical exclusion of fast-accretion branches,
not on capture improbability.
```

This is the kind of correction trail the artifact is meant to preserve.

## 7. Representative Finding: The pp versus nu-N Crux

For higher-dimensional neutral gravity-only branches, neutron stars are a
load-bearing bound. The standard argument uses cosmic ultra-high-energy
neutrinos to make black holes inside neutron stars.

This introduces a nontrivial inference:

```text
If the LHC can make BHs in pp collisions,
then cosmic neutrino-nucleon collisions can make corresponding BHs in neutron
stars.
```

In minimal extra-dimensional gravity this is plausible because the hard process
is gravitational and approximately species-democratic. But brane-localization,
split-fermion, or bulk-neutrino models can suppress neutrino-quark production
relative to quark-quark production.

The artifact therefore separates:

```text
pp-like cosmic proton/nucleus production
neutrino-nucleon neutron-star production
proton-on-binary-companion fallback
```

This is a good example of the method: do not merely repeat the published
argument; identify the exact arrow where a model class could attack it.

## 8. Representative Finding: Direct Searches Are Strong But Not Exhaustive

Modern ATLAS/CMS searches strongly constrain prompt visible benchmark branches.
They do not cover every possible stable, invisible, or long-lived remnant.

The event-count equation is:

```text
N_seen = L_int * sigma_BH * BR_visible * A * epsilon
```

If `BR_visible` or acceptance is small, a direct search can miss a branch. This
does not mean the branch is dangerous; it means the astrophysical argument and
the direct-search argument cover different parts of the claim graph.

## 9. Representative Finding: Magnetic and Heavy-Ion Branches

The later expert pass looked for qualitative loopholes beyond the original ADD
story:

- magnetically charged or monopole-stabilized black holes,
- hidden-sector magnetic charge,
- heavy-ion magnetic-field production through a Schwinger-like mechanism,
- and the possibility that direct searches miss rare or unusual channels.

The current conclusion is not that these are likely hazards. It is that they are
distinct branches:

```text
ordinary magnetic charge -> strong stopping/capture; astrophysical survival
                            bounds are usually stronger, with detector searches
                            as an additional constraint
hidden magnetic charge   -> ordinary stopping/capture is not guaranteed, but
                            visible heavy-ion magnetic fields may also fail to
                            produce it efficiently
HIC B-field production   -> not covered by ordinary pp luminosity equivalence;
                            the live question is whether the production mode is
                            collider-specific while post-capture accretion
                            remains dangerous
```

This is the intended use of the artifact: turn vague "what about exotic
physics?" questions into specific nodes with assumptions and failure modes.

The same correction matters for future machines. For FCC-hh, visible charged or
magnetic stable BHs are not primarily a detector-invisibility loophole. If
nature also produces them, charge makes them easier to stop in Earth/Sun/WD/NS
matter. The distinctive FCC branch is instead coherent heavy-ion electromagnetic
production, where the natural astrophysical analogue may be absent or
rate-suppressed.

## 10. Representative Finding: Superfluid Accretion Is A Spectral Question

The latest branch concerns neutron-star condensates. Neutron-star interiors are
not simple gases; they likely contain neutron superfluidity, proton
superconductivity, and possibly more exotic paired phases. This matters because
the standard post-capture argument uses an accretion clock.

The useful formulation is:

```text
What operator does the black hole couple to, and what spectral weight does the
medium have at the required (q, omega)?
```

Stopping and accretion must be separated. Stopping is energy loss to
quasiparticles outside the horizon. Accretion is flux through an absorbing
boundary. If the BH is much smaller than the coherence length of paired matter,
the naive Bondi/gas estimate may need a suppression factor:

```text
dot M_NS = dot M_naive * S_cond
```

Possible regimes include:

```text
S_cond ~ 1                 hydrodynamic condensate limit
S_cond ~ (r_h/xi)^alpha    coherence-limited absorber
S_cond ~ exp(-Delta/T)     thermal quasiparticle limited only
S_cond ~ spectral integral correct many-body formulation
```

This is now tracked as:

```text
MODEL-NS-SUPERFLUID-SPECTRAL-ACCRETION
MODEL-NS-SUPERFLUID-SPECTRAL-STOPPING
```

## 11. What Is Missing Before Final Submission

The early-feedback version is a working prototype. The final submission should
add:

1. A machine-readable claim graph:

   ```text
   notes/claim_graph.yaml
   ```

2. Superseded-output warnings in:

   ```text
   analysis/lhc_bh_fate.py
   analysis/lhc_first_capture.py
   ```

3. Updated top-level docs, since the repo now has six layers rather than five.

4. Focused notes on:

   ```text
   production/PDF cliff
   direct-search coverage
   exotic semiclassical and magnetic branches
   neutron-star condensate accretion
   ```

5. A short reuse protocol for applying the workflow to a second case.

## 12. Why This Should Generalize

The workflow should transfer to cases where:

- the public claim is compressed,
- the conclusion depends on multiple disciplines,
- the primary literature is long or technical,
- direct empirical tests cover only some branches,
- old arguments contain update-sensitive nodes,
- and the residual risk is concentrated in correlated error rather than a
  single known parameter.

Possible target classes include:

- lab-leak evidence chains,
- AI model-evaluation claims,
- nuclear or accelerator safety cases,
- geoengineering risk arguments,
- controversial public-health evidence chains,
- and long-range environmental risk assessments.

The reusable product is not a single answer. It is a structured map of what the
answer depends on.

## 13. Early-Feedback Ask

We are especially interested in feedback on:

1. Whether the claim graph should be the central final artifact.
2. Whether the representative slices are readable enough.
3. Whether the correction trail is valuable or too distracting.
4. Whether the final version should include a second small case study.
5. Whether the submission should emphasize the workflow more and the physics
   less.
