# Review of `summary_from_AS.md` (coauthor contribution, 2026-06-14)

*Analysis of the 1070-line working memo pushed by AS (via Codex) in commits
`0de6279` + `d729daf`. Written by Claude from the analysis-side thread.
TL;DR: substantive and largely correct; it's complementary to ours (production
side vs. our astrophysical-fate side), not redundant. Verified the risky 2026
references — they're real. A few coordination fixes needed before merging.*

## What it is
A single markdown handoff memo (not code, not integrated `notes/` layers). It
overwrote the earlier short summary. Author tag `AS-via-Codex <codex@local>`,
workspace `/Users/sadofyev/Documents/BHs_compete`. It is explicitly a "working
memo for the next round," not a polished write-up. It read our repo (it correctly
lists layers 1–5 and absorbs our notes/04 correction) but adds no scripts and
does not actually create the claim-graph file it designs.

## Division of labor (the good news)
AS's memo covers the **production side and the forward-looking literature**;
our `notes/01–06` cover the **astrophysical-fate side**. Together they span
production → fate. The single most useful thing it adds is grounding for our
biggest hand-wave: we treated the BH production fraction `f_BH ~ 1e-8` as a free
knob; AS explains what actually sets it (PDF cliff + threshold + κ).

## Physics I checked — correct
- **PDF cliff (§6–7).** Black-disk σ ∝ M^{2/(D-3)} is a slow power; endpoint rate
  sensitivity comes from parton luminosity, not the geometric prefactor. Verified
  the algebra: S=13 TeV, M_min=10 TeV ⇒ τ_min=0.592; 2τ/(1−τ)=2.90; p=8 ⇒
  dlnσ/dlnM_min = −23.2; +5% threshold ⇒ ×0.31; +10% ⇒ ×0.10; 13.0→13.6 TeV
  (+4.6%) ⇒ ×2.9. All correct. This is a genuinely valuable node.
- **Hawking-while-flying (§8).** Isotropic rest-frame emission ⇒
  dP^μ/dτ = −(Γ_H/M)P^μ, so mass and lab momentum fall in the same proportion and
  the *velocity is unchanged* — Hawking loss shrinks the hole but does not brake
  it. Correct and subtle; it also bears on our escape analysis (a mass-losing
  flying BH keeps its β, so our "escapes Earth" conclusions are unaffected).
- **pp vs ν-N production (§10).** Two parton-luminosity penalties vs one;
  x_min = M_min²/(2 m_N E_ν κ²). Correct, and directly complements our Part 1
  (CR) and Part 6 (NS neutrino channel).
- **FCC comparator scaling (§15).** E_CR ≈ s/(2m_p); Φ(>E)∝E^{-2}∝s^{-2}... they
  write S^{-4} using S≡√s (so s=S²) — internally consistent; (100/14)^4≈2600.
  Correct: LHC margins must be recomputed for FCC, not copied.
- **Heavy-ion / pileup (§13).** Correctly notes neither coherently builds one
  microscopic BH; local √ŝ is what matters.

Notation caveat: AS uses `S` for √s throughout (so `S²`=s, `tau S^2`=ŝ).
Unconventional but consistent; worth normalizing to `s`/`√s` before publishing.

## References — verified (this was the main risk with an AI-written list)
- CMS 2026 [arXiv:2604.10732]: **real**; 8.4–11.4 TeV semiclassical-BH exclusion,
  138 fb⁻¹ Run 2 — matches the memo. (Note: legacy Run-2 dataset, not new data.)
- GWTC-5.0 [arXiv:2605.27226]: **real** (LVK, 390 events, May 2026).
- Remaining 2026 refs (ATLAS 2604.19495, GWTC-4 2508.18080, IceCube 2402.18026,
  Auger 2309.01259) not individually checked but the two riskiest verified true,
  so the list is trustworthy. Recommend a one-pass citation check before the
  final write-up anyway.

## Correct framing additions worth keeping
- **§12 direct-search loophole:** modern ATLAS/CMS constrain *prompt visible*
  benchmark decays; they do **not** cover the stable/invisible neutral-remnant
  branch — i.e. exactly our dangerous case A. This cleanly separates "collider
  hasn't seen one" from "the safety proof." Important and correct.
- **§16 guardrails** reproduce our notes/04 correction (3% trapping was wrong)
  and the "capture is not impossible; safety rests on accretion-slowness +
  dense-star exclusion" line. Good alignment.
- **§17 claim-graph schema** (id/type/status/depends_on/source_refs/code_refs/
  update_triggers/...) is a concrete, usable design — directly advances the
  competition deliverable. Adopt this as the artifact backbone.

## Coordination fixes needed before merging
1. **`notes/06` filename collision.** AS's task list (§19.4) assigns
   `notes/06-production-and-pdf-cliff.md`, but I just created
   `notes/06-neutron-star-bound.md`. Renumber: keep NS as 06; production/PDF-cliff
   → 07; radiation/stopping → 08; direct-searches → 09. Update README/CLAUDE TOCs.
2. **Memo is a plan, not artifacts.** The claim-graph JSON, `bh_geometry.py`,
   `pp_production.py`, `neutrino_bh_production.py` are all proposed but unbuilt.
   These are the natural next implementation items.
3. **`sources/` PDF.** AS flags it's "missing" — it's intentionally gitignored
   (copyright) in the public repo; locally fetch with the one-liner in
   `sources/README.md`. Worth a note so the coauthor isn't confused.
4. **Overwrite vs. append.** AS replaced the earlier summary (fine for a planning
   memo; git keeps history). But our repo convention is append-corrections; the
   claim-graph artifact itself must follow that, not be overwritten.
5. **Repo hygiene.** `summary_from_AS.md` sits at root; consider moving working
   memos under `notes/` or a `handoffs/` dir to keep root clean.

## Net assessment
High-quality, mostly-correct, and well-targeted at the gap in our work
(production-side rate physics). No physics errors found in the checkable claims;
references verified where risky. The main actions are coordination (renumber 06,
build the designed artifacts) rather than correction. Recommend adopting §17's
schema as the claim-graph backbone and turning §§6–7, 8, 10, 12 into proper
`notes/` layers + scripts.
