# Decompressing a Settled Safety Argument

**A Structure-layer claim-graph workflow, demonstrated on the LHC
microscopic-black-hole case — with the neutron-star bound as the worked example.**

*Early-feedback working draft — FLF epistemic case study competition. Submitted
2026-06-21 for the optional early-feedback window; final due 2026-07-19. This is
a working draft on one case (LHC), with a second case (COVID-19 origins) planned
for the final submission (see §11).*

Repository: `https://github.com/valentinslepukhin/Black-holes-CERN`

---

## 1. Submission category

This is a **Structure** submission. The FLF stack defines the Structure layer as
*"resolve the inference structure: which claims and evidence support which other
claims."* That is precisely what the artifact does: it takes a compressed,
settled safety conclusion and exposes the full typed dependency graph underneath
it — claims, the assumptions they rest on, the calculations and observations that
back them, the corrections that revised them, and the triggers that would age
them.

We deliberately do **not** claim "integrated / all three layers." The rules
reward depth on one component (*"any submission that advances the state-of-the-art
on a component"*). Our honest layer map:

```text
PRIMARY    Structure   — the claim-dependency graph IS the deliverable
SECONDARY  Assessment  — reliability + gap-finding half (ranked gap register,
                         MARGINAL flags, residual-risk localization, correction
                         trail). The rhetorical-moves half is demonstrated more
                         naturally on a contested case → planned for COVID.
SUPPORTING Ingestion   — source discipline (primary-source-vs-web-summary
                         provenance), but not a built extraction pipeline.
```

---

## 2. Summary

The public form of the LHC safety argument compresses to *"cosmic rays prove the
LHC is safe."* That sentence is directionally right and epistemically too coarse:
it hides a branching structure in which one branch — neutral, gravity-only,
non-evaporating black holes — is **not** closed by ordinary cosmic-ray survival
at all. Earth and the Sun cannot close it, because cosmic-ray-made black holes
are ultra-relativistic and pass straight through them. **The branch is closed
instead by compact stars — and at the deepest (high-dimensional) end, by neutron
stars specifically.** The neutron-star bound is the load-bearing argument of the
entire safety case, and most of the interesting structure lives underneath it.

Our workflow turns the compressed claim into a navigable, typed, updateable claim
graph, then decomposes its single most important node — the neutron-star bound —
two levels deep to expose exactly which assumptions carry it and where each could
fail. The product judged here is **the method + the artifact it produces**, not a
new physics conclusion. The LHC is safe; that is not in question. What we expose
is *why the confidence is warranted and exactly where the argument is weakest.*

---

## 3. Why two cases, and why LHC first

The rubric's description of a strong Spec/Structure entry is *"demonstrate it on
multiple part(s) of at least two cases."* We are taking the two-case path, in a
deliberate order matched to (a) the team's expertise and (b) the stack layers
each case best exercises:

```text
Case 1  LHC microscopic black holes   (this draft)
  - a SETTLED, technical, multi-disciplinary safety argument
  - ideal for the STRUCTURE layer: a long inference chain to decompress
  - both collaborators have high-energy-physics background, so we can
    re-derive and adversarially stress the physics ourselves

Case 2  COVID-19 origins              (planned for final, 2026-07-19)
  - a CONTESTED, live, multi-source debate
  - ideal for the ASSESSMENT layer's second half: rhetorical moves that carry
    more persuasive weight than evidential weight
  - one author has a biology / biophysics background, giving the same
    domain-adjacent expert-pass capability we used on the physics
```

This is not a hedge. It is a layer-aware roadmap: the LHC case lets us show
Structure (and the reliability half of Assessment) cleanly because the answer is
known and the chain is long; COVID lets us show the rhetorical half of Assessment
because the answer is open and the persuasion is live. The **same workflow** runs
on both — which is the generalizability claim the competition asks us to make.

---

## 4. The case on one screen

The compressed claim, decompressed into typed branches:

```text
Hypothetical LHC black hole
├── Hawking-radiating ........................ evaporates; not the hazard branch
└── stable / remnant (worst case, ASSUMED)
    ├── strongly / EM-interacting ........... stopped in ordinary matter →
    │                                          Earth+Sun cosmic-ray survival closes it
    │                                          [OBSERVATION-backed, margin ~1e18]
    └── neutral, gravity-only (the dangerous branch)
        ├── cosmic-ray-made BHs are ultra-relativistic → pass THROUGH Earth
        │   so Earth/Sun survival says NOTHING here          [CALCULATION]
        ├── slow Earth/Sun accretion → not a practical hazard for most params
        ├── white-dwarf survival ............ closes lower-D branches (D ≤ 7) [OBS+CALC]
        └── NEUTRON-STAR survival ........... closes higher-D branches (D ≥ 8) [OBS+CALC]
            └── THE DECISIVE BOUND — decomposed in §7
```

The structural skeleton that makes the whole case work:

```text
fast danger  → astrophysically testable → excluded
not excluded → too slow to be dangerous
```

The single most important structural fact, surfaced by the decomposition:
**danger and empirical testability switch on together.** Fast accretion requires
few extra dimensions, which also means strong stopping, which means white dwarfs
and neutron stars trap the same objects — so the dangerous corner is exactly the
observationally bounded one. The case pivots on `n = 3–4` (`D = 7–8`), and the
`D ≥ 8` end — where white dwarfs no longer suffice — rests entirely on neutron
stars.

---

## 5. The workflow (the reusable product)

```text
1. Start from the compressed public claim.            ("cosmic rays prove safety")
2. Decompress into conditional branches.              (stopped / not-stopped;
                                                       Hawking-on / off; pp / νN …)
3. Type every node.                                   OBSERVATION | CALCULATION |
                                                       ASSUMPTION | MODEL
4. Run small, dependency-free OOM checks.             (transparent, not precision
                                                       sims; reveal which deps matter)
5. Diff against the PRIMARY literature, not summaries. (Giddings–Mangano 2008 PDF
                                                       is ground truth; web summaries
                                                       were wrong)
6. Record corrections as appended nodes, never        (a wrong node, kept visible,
   silent overwrites.                                  is part of the method)
7. Tag update triggers on every aging-prone node.     (new EeV ν flux; new LHC
                                                       limit; new WD/NS data)
8. Run an adversarial expert pass:                    (which MODEL class attacks
   which assumptions break the chain, and how?         which NODE, with what
                                                       failure mode)
9. Emit a machine-readable claim graph.               (claims ↔ evidence ↔ code ↔
                                                       sources ↔ corrections ↔ triggers)
```

The distinction in step 3 — **OBSERVATION-backed vs CALCULATION-backed nodes** —
is the central epistemic content: it tells a reader instantly which parts of
"settled" rest on a telescope and which rest on an order-of-magnitude argument.

---

## 6. The artifact

```text
analysis/   six dependency-free Python OOM checks (stdlib only) reproducing the
            numerical branches; retained even where later reading corrected their
            interpretation, as a reproducibility + correction trail.
notes/      one write-up per layer (01–06): findings, dependency graph, and an
            assumptions log; plus a ranked research-gap register and focused
            adversarial notes (production, condensates, exotic/magnetic branches).
sources/    the Giddings–Mangano 2008 primary source (the validated ground truth).
contest_submission/  this document and supporting material.
```

A judge's fastest path: `README.md` → `notes/06` (the decisive neutron-star
bound) → `notes/research-gaps.md` (the open structure beneath it) → `notes/04,05`
(the correction trail). Optional: run the four scripts (`python3 analysis/*.py`).

---

## 7. Worked example: the neutron-star bound, decomposed

This is the heart of the submission. The neutron-star bound is **the** decisive
node — the only thing that closes the dangerous neutral gravity-only branch at
`D ≥ 8`, where white-dwarf survival fails. It looks airtight as a one-liner.
Decomposing it is where the Structure method earns its keep: the single claim
resolves into **two distinct load-bearing assumptions**, each with its own
sub-graph of model-dependent loopholes, a backup, and a correction.

### 7.1 The bound in one line, and why it is decisive

```text
A neutron star would trap a neutral gravity-only BH and be consumed in
« its observed age → such BHs do not exist / are not produced → safe at D ≥ 8.
```

White dwarfs close `D ≤ 7`; only neutron stars reach `D ≥ 8`. So the deepest,
most speculative corner of the whole safety case rests here and nowhere else.

### 7.2 The sub-dependency graph

```text
CLAIM  neutral gravity-only stable BHs are excluded at D ≥ 8
  │
  ├── OBS   neutron stars are observed at Gyr ages (and in old X-ray binaries)
  │
  ├── CALC  a NS traps one such BH every ~16–220 yr        [G&M Table 10]
  │    │    capture efficiency ~1 (column 2e20 g/cm² ≫ needed; crust in ≲10 s)
  │    └── via cosmic UHE NEUTRINOS — neutral, so immune to the ≥1e8–1e15 G
  │         magnetic screening that deflects charged cosmic rays near a NS
  │         │
  │         └── ASSUMPTION-PRODUCTION-DEMOCRACY  (ν-N makes BHs like pp does)   §7.3
  │              ├── holds in minimal ADD/RS (formation is gravitational,
  │              │    species-democratic — only √ŝ and impact parameter enter)
  │              ├── BREAKS under brane-localized / bulk neutrinos — and the
  │              │    SAME mechanism elegantly explains small neutrino masses
  │              └── BACKUP  CALC-NS-PROTON-COMPANION-BOUND
  │                   protons on the NS's binary companion form BHs by the
  │                   IDENTICAL parton process as the LHC → far harder to evade
  │                   (G&M Table 3: 54/74/95/118 per Myr for D = 8/9/10/11)
  │
  └── CALC  once trapped, the NS is consumed in yr (D≤7) → ~10 Myr (D=11)       §7.4
       └── ASSUMPTION  naive Bondi/geometric accretion in NS matter
            └── MODEL-NS-SUPERFLUID-SPECTRAL-ACCRETION
                 the interior is a PAIRED CONDENSATE, not a gas; accretion is a
                 many-body spectral-absorption problem, not gas Bondi flow        §7.5
```

Two levels down, the airtight one-liner has become two assumptions
(`PRODUCTION-DEMOCRACY` and the `ACCRETION CLOCK`), each falsifiable in principle,
each with a specific model class that would attack it. That is the deliverable.

### 7.3 Load-bearing assumption #1 — production democracy (the `pp → ν-N` crux)

The bound needs cosmic neutrinos to make black holes the way LHC protons do. At
the hard subprocess this is gravitational and democratic, so `σ(ν q → BH) =
σ(q q → BH)` at equal `√ŝ`; neutrinos even reach *higher* `√ŝ` than the LHC, so
the argument is *a fortiori* — **conditional on democracy.** The dangerous
direction is specifically *ν-N suppressed while pp stays normal* (the LHC makes
something nature's neutrinos do not). That is exactly what **brane-localized or
bulk right-handed neutrinos** produce — and the same small wavefunction overlap
that suppresses `ν-q` formation is a *popular, independently motivated*
explanation for tiny neutrino masses. So the loophole is real, not contrived.

The backup is what makes the bound robust: cosmic-ray **protons** strike the
neutron star's **binary companion** (no magnetic screening there) and form black
holes by the *same quark-quark parton process the LHC uses*. Any theory that lets
the LHC make BHs must let the companion make them too — a far tighter equivalence
than `ν-N ↔ pp`. The residual danger therefore survives only in a theory that
(i) gives stable neutral non-Hawking BHs, (ii) suppresses `ν-q` formation, **and**
(iii) suppresses `q-q` formation on the companion while keeping it alive at the
LHC — and (iii) is nearly self-contradictory.

### 7.4 Load-bearing assumption #2 — the accretion clock

The "consumed in « its age" half of the bound assumes naive Bondi/geometric
accretion once a seed is trapped. But a neutron-star interior is **not a gas** —
it is a paired quantum condensate (neutron superfluid, proton superconductor,
possibly color-superconducting quark phases). The sharp question is not
"superfluid viscosity" but: *what operator does the BH couple to, and what
spectral weight does the medium have at the required `(q, ω)`?* Stopping (energy
loss to excitations outside the horizon) must be separated from accretion (flux
through an absorbing boundary). If the seed `r_h` is far below the pairing
coherence length, naive Bondi may overestimate growth:

```text
dot M_NS = dot M_naive × S_cond
to overturn the bound:  S_cond < t_naive / t_NS_age
                        D=11 (t_naive ~10 Myr): S_cond ≲ 1e-2 ... 1e-3
                        D=8  (t_naive ~4 kyr ): S_cond ≲ 1e-5 ... 1e-6
```

So a *modest* suppression only threatens the slowest, highest-`D` branch — which
is exactly the branch the neutron star is responsible for. This made the
condensate question the most active recent thread of the project.

### 7.5 The accretion-clock sub-graph, and a live correction trail

Decomposing assumption #2 further, we asked which condensate could actually
supply the needed suppression, and reached a clean criterion: a condensate can
suppress NS accretion only if it is **NS-specific**, carries **spectral weight at
`q ~ 1/r_h ~ TeV`**, **dominates the accretable energy density**, and is a
**Fermi-surface pairing** condensate. Running the candidate fields against it:

```text
neutron BCS / diquark pairing  → the only fields that pass — weak help, D=11 only
chiral QCD condensate          → vacuum order param; at q~1/r_h asymptotic
                                  freedom restores free-parton weight → ≈ no help
Higgs / electroweak condensate → UNIVERSAL (not NS-specific) + restored above v
                                  → null; cannot differentially protect the NS branch
cosmological-constant scalar   → ~44 decades too little energy density → null
```

The methodologically important part is the **correction trail** this produced —
the living-knowledge-base behavior the competition asks for:

- An early version of the condensate note invoked near-horizon "thermal melting"
  of the QCD condensate to dismiss the loophole. A collaborator pass showed this
  illegitimately imported thermal physics into the dangerous **Hawking-off**
  branch, which by assumption has *no* thermal bath: it must be treated as a
  zero-temperature absorbing sink. The note carries a **dated correction box**,
  not a silent edit, and records that the load-bearing argument (the
  asymptotic-freedom floor) survives because it was already a `T = 0` statement.
- Two independent derivations — the code-side note and the expert-side memo —
  **converged on the same fix**, and that convergence is itself logged as a
  cross-check. The exercise also surfaced the genuine open fork:
  `ASSUMPTION-NS-ACCRETION-UV-VS-SOFT-DOMINATED` (does the rate sample the
  TeV-scale horizon, where condensates are invisible, or the soft Bondi scale,
  where the dense-matter EOS re-enters?) — tracked as an explicit node, not
  silently decided.

This single worked example exercises the whole method: typed nodes, a two-level
dependency decomposition, an adversarial model-class search, a backup that ties a
fragile assumption to a robust one, and a kept-but-superseded correction trail.

---

## 8. Other representative results (briefer)

- **The top-level decompression (§4).** "Cosmic rays prove the LHC is safe"
  resolves into the typed tree; the structural correction to the public claim is
  that Earth/Sun survival is *silent* on the neutral gravity-only branch.
- **The LHC-capture correction.** An early script made LHC trapping look
  negligible (~10⁻¹²); reading Giddings–Mangano Appendix F corrected it to
  near-certain for light stable BHs at `D ≥ 8`. The argument shifted from *"safe
  because trapping is unlikely"* to *"trapping may happen; safety rests on
  accretion slowness + astrophysical exclusion."* Wrong node kept, marked
  superseded.
- **An aged node.** The `D ≥ 8` branch depends on the cosmic UHE neutrino flux —
  an *assumption* in 2008, an IceCube *observation* since 2013. A node that
  changed type over time: the cleanest argument for why a safety knowledge base
  must be living and update-triggered, not a static report.

---

## 9. How it maps to the FLF stack

```text
Ingestion   read the primary source directly; log where secondary summaries were
            wrong (web summaries mis-stated the D=7 timescale and the white-dwarf
            stopping direction); attach source_refs (page/section/equation) to
            nodes. → discipline, not a pipeline.

Structure   the whole artifact. Typed claim graph; OBSERVATION vs CALCULATION;
            depends_on / supports / contradicts; the two-level neutron-star
            decomposition; "which node does each adversarial scenario attack."
            ← PRIMARY

Assessment  reliability + gaps half: research-gap register ranked by leverage;
            MARGINAL flags; residual-risk localization (where correlated error
            concentrates); correction trail as an explicit reliability mechanism;
            update-sensitivity tags.  ← SECONDARY (rhetorical half → COVID)
```

---

## 10. Why it meets the judging bar

```text
Help someone reason better?  Yes — a reader sees instantly that the deepest part
                             of a "settled" conclusion rests on two falsifiable
                             assumptions under the neutron-star bound, and where
                             the residual risk sits.
Generalize?                  The 9-step workflow is domain-agnostic; the same
                             steps will run on COVID origins (§11).
Scale with AI / compute?     Decompression, OOM reproduction, source-diffing, and
                             adversarial branch-search are each AI-acceleratable;
                             a machine-readable claim graph is the natural output.
Compound?                    Typed, source-linked, update-triggered nodes let a
                             later investigator extend, challenge, or re-run the
                             graph rather than re-reading the literature.
```

---

## 11. Status and roadmap to the final submission

```text
neutron-star bound + sub-graph   substantial (the §7 worked example)
physics audit (LHC, layers 1–6)  substantial
calculation / OOM trail          substantial
primary-source diff              substantial (Giddings–Mangano 2008)
research-gap register            substantial
correction trail                 demonstrated (LHC capture; condensate melting)
machine-readable graph           planned, not yet emitted
second case (COVID)              planned
```

For the **final (2026-07-19)** we will add:
1. **Case 2 — COVID-19 origins**, the same workflow on a contested case,
   demonstrating the rhetorical-assessment half of the Assessment layer (author
   biology/biophysics background supplies the domain-adjacent expert pass).
2. **`notes/claim_graph.yaml`** — the machine-readable claim graph, with the
   neutron-star sub-graph of §7 as its showcase region (schema drafted; ~30 nodes
   already named across the notes).
3. **Superseded-output warnings** in the two corrected LHC capture scripts.
4. **Doc cleanup** (six layers, not five) and a one-page **reuse protocol**.

---

## 12. What we would value feedback on (early-feedback ask)

```text
1. Is the neutron-star sub-graph (§7) the right depth and the right showcase for
   the Structure layer, or should the machine-readable claim graph come first?
2. For a Spec/Structure entry on a SETTLED case, is depth on one case plus a
   credible second-case plan competitive, or is a completed second case required?
3. Is the OBSERVATION-vs-CALCULATION node typing legible and useful as the core
   epistemic content?
4. Is the correction trail (kept-but-superseded nodes) valuable, or noise?
5. Is COVID-19 origins the right second case to showcase rhetorical Assessment,
   or would the "eggs" case demonstrate transfer more cheaply?
```

---

## Collaboration note

The workflow uses two complementary passes. Valentin Slepukhin led the Claude
Code path — repository setup, first-principles OOM reproduction, and the
code-side claim decomposition — bringing a modeling background now closer to soft
condensed matter and biophysics (relevant to the planned COVID case). Andrey
Sadofyev added a particle-physics expert pass via Codex — PDF-threshold
sensitivity, `pp`-vs-`ν-N` production, direct-search coverage, the neutron-star
condensate accretion physics, and the exotic / magnetic / heavy-ion branches —
from an earlier high-energy-theory background. The intended structure is general:
**AI-assisted reconstruction and OOM checks first, then a domain-adjacent
expert/adversarial pass, then the claim graph.**
