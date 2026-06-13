# Project summary for collaborators

*A plain-language overview of where this project stands. For the technical
details see `README.md`, the per-layer write-ups in `notes/`, and the
calculations in `analysis/`. For working with Claude Code on this repo, see
`CLAUDE.md`.*

## What we're doing and why

This is an entry for the **Future of Life Foundation epistemic case study
competition** (the LessWrong "Lab leaks, black holes, and eggs" post). The
competition isn't asking for an essay on whether the LHC is safe — it's asking
for a **generalizable, AI-assisted methodology** for building a navigable,
honest knowledge base about a disputed/complex topic, *demonstrated* on a case
study. We picked the LHC black-hole question.

Deadlines: **early-feedback submission June 21, 2026**; **final July 19, 2026**.
Deliverable is ≤ 10 pages of write-up (plus code/examples). Prize pool ~$200k.

The LHC case is officially "closed and uncontested," so the interesting task
(per the competition) is to **dissect the settled safety argument into its
dependency structure and honestly flag the weakest links** — in an accessible,
updateable form. That's exactly what we've been building.

## What we've actually done

We re-derived the published safety argument (mainly **Giddings–Mangano 2008**,
arXiv:0806.3381) from scratch at order-of-magnitude level, in five layers, then
diffed our results against the paper. Everything is small, dependency-free
Python you can run in seconds; every script has an assumptions log in its header.

The physics question we worked through, concretely: *if the LHC made a stable
black hole, would it eat the Earth — and why are we confident it wouldn't?* We
attacked it through four interaction hypotheses for the black hole (gravity only;
+weak; +strong; +electromagnetic), for both cosmic-ray-produced and
collider-produced black holes.

**The headline findings:**

1. **Cosmic rays do LHC-energy collisions constantly.** Nature has run
   ~2.5×10²² LHC-equivalent collisions on Earth over its lifetime vs. ~2.4×10¹⁷
   for the whole LHC program. (Our number matches G&M's.)

2. **The "cosmic rays prove it's safe" argument has a real hole, and it's
   specific.** Cosmic-ray-produced black holes are born ultra-relativistic
   (γ ~ 7000) and fly straight through the Earth — *unless* they interact
   strongly or electromagnetically. So Earth/Sun survival directly bounds the
   strong/EM cases (where nature has trapped ~10¹⁴–10¹⁸ of them), but says
   **literally nothing** about the dangerous case: a neutral, gravity-only,
   stable black hole. Zero get trapped. This is the gap G&M had to fill.

3. **Danger and testability switch on together.** A trapped black hole only eats
   the Earth quickly if there are few extra dimensions (n ≤ 3). But few
   dimensions also means strong stopping power — which is exactly when
   cosmic-ray black holes *do* get trapped in white dwarfs and neutron stars, so
   their continued existence becomes the bound. For many dimensions (n ≥ 4) a
   trapped black hole eats ~0.1 g in the age of the Earth. **The whole argument
   pivots on n = 3–4 (D = 7–8)** — and we confirmed this is exactly where G&M's
   white-dwarf/neutron-star analysis lives.

4. **We found (and corrected) our own mistakes by reading the primary source.**
   Our first estimate said the LHC has only a ~3% chance of ever trapping the
   dangerous kind of black hole. The paper showed this is wrong by orders of
   magnitude: low-velocity accretion drag lets the Earth trap black holes born
   at up to ~25× escape velocity, and the production spectrum is flat in rapidity
   (not the cubic tail we assumed). Corrected, trapping is near-*certain* for
   light black holes — which is precisely why the real safety case rests on
   accretion-slowness and white-dwarf/neutron-star survival, never on capture
   being improbable. (We left the wrong number in `notes/04` with a correction
   box on top, deliberately — the correction trail is part of the methodology
   we're showcasing.)

5. **One node has visibly aged since 2008 — the best possible advert for a
   "living" knowledge base.** For D ≥ 8, the safety case relies on cosmic
   ultra-high-energy neutrinos producing black holes *inside* neutron stars. In
   2008 that neutrino flux had never been observed; IceCube has since detected
   the astrophysical flux. A node that was a *calculation/assumption* in 2008 is
   now partly an *observation*.

## Where it bottoms out (the honest residual)

Stripped down: the strong/EM scenarios are closed by direct observation (Earth
and Sun are still here). The dangerous neutral/gravity-only scenario is closed by
a *chain of calculations* — accretion slowness, plus white-dwarf survival
(D ≤ 7), plus neutron-star survival via cosmic neutrinos (D ≥ 8). In
Ord–Hillerbrand–Sandberg terms, the residual risk isn't the tiny physics
probabilities — it's **P(the argument itself has a correlated error)**, and that
probability is concentrated in two places: white-dwarf astronomy (ages, masses,
magnetic fields) and the low-velocity stopping/accretion physics at D = 7–8.

## What's left to do

- [ ] Verify G&M Appendix H to confirm whether our "bound solar orbit decays into
      the Sun" channel is genuinely novel or already covered.
- [ ] **2008 → 2026 update pass** (high value): IceCube neutrino flux, modern
      white-dwarf surveys, and LHC Run 2/3 limits on the higher-dimensional
      Planck scale M_D (which now exclude the lightest scenarios outright and
      shrink the whole space).
- [ ] Build the actual competition deliverable: a machine-readable **claim
      graph** + the ≤10-page methodology write-up. Aim a draft at the **June 21**
      early-feedback window.

## How the repo is organized

| Folder | Contents |
|---|---|
| `analysis/` | Five standalone Python calculations (stdlib only) |
| `notes/` | One write-up per layer: findings, dependency graphs, assumptions logs |
| `sources/` | Primary sources (the Giddings–Mangano 2008 PDF) |
| `README.md` | Technical overview of all five layers |
| `CLAUDE.md` | Orientation for Claude Code (for either of us) |

To reproduce everything:

```bash
python3 analysis/cosmic_ray_flux.py
python3 analysis/bh_earth_passage.py
python3 analysis/capture_and_accretion.py
cd analysis && python3 lhc_bh_fate.py && python3 lhc_first_capture.py
```
