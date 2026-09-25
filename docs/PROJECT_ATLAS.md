# Project atlas

**Beneath the Benchmark** is Hamza Raheel's independent record of an approximately eight-week remote research collaboration with LABUST at FER, University of Zagreb (24 July–16 September 2026). It is not an official lab publication. This document maps the work and its evidence status; it is not a collection of private messages or a claim that every experiment succeeded.

## The research question

Could a detector developed around controlled underwater imagery generalize to a new open-water recording site, and how much correctly labelled target-site data would that require? The original task was model improvement. The research became broader because the delivered evaluation split and, later, the image/annotation validity needed attention before a model gain could be trusted.

## The sequence

| Period | Work performed | What it produced | What it did not prove |
| --- | --- | --- | --- |
| 24–28 July | Reconstruct source-data preparation and the training path; audit LABUST's delivered export. | Reconciled source counts, candidate class mappings, reproducible preparation steps and source-video/frame identities. | Exact reproduction of an unpublished source split or the paper's unpublished outdoor membership. |
| 27 July–early August | Deduplicate and assign whole videos to development and held-out partitions. | A provisional video-disjoint outdoor derivative; explicit overlap checks. | Correct image orientation or complete and precise boxes. |
| August | Complete a source baseline and bounded studies of target labels, seed variation, sample selection, retention, pseudo-labels, checkpoint combination and resolution. | Frozen protocols and 31 retained result records, including failed and ambiguous branches. | A final certified accuracy gain; the target-domain labels were later placed on hold. |
| Late August | Prototype inference outside the research notebook. | NCNN reference runtime, Python-free native C++ path, x86/ARM builds, desktop stability and emulated-ARM checks. | Physical Raspberry Pi latency, ROV integration, field accuracy, or exact native per-detection parity. |
| 8–12 September | Recheck image orientation and annotation completeness, then make the uncertainty reviewable. | Full 1,206-frame review package, 704 candidate issue records across 636 frames, offline two-reviewer/adjudicator workflow and validator. | Accepted corrections or a frozen corrected dataset. |
| 16 September | Collaboration concluded. | Private technical archive retained; public case study prepared separately. | Any additional model or deployment result after the handoff. |

## 1. Reconstructing and auditing the data

The source-domain baseline was reconstructed from the public [TrashCan](https://irvlab.cs.umn.edu/resources/trashcan) and [SeaClear Marine Debris](https://doi.org/10.4121/4f1dff25-e157-4399-a5d4-478055461689.v1) datasets. The preparation reconciled 12,953 source-training and 2,869 source-validation images, but matching counts did not establish identical membership or semantic mapping to the authors' original experiment. That distinction was recorded rather than hidden.

For the LABUST outdoor export, the first structural audit linked filenames back to source videos and frame indices:

- 2,646 delivered outdoor image exports represented 1,206 distinct source frames from 17 videos.
- All 17 source videos occurred in both sides of the delivered train/validation split.
- 351 distinct source frames themselves appeared across splits in the locally audited export.
- The original paper's separate 793/1,853 outdoor membership was not present in the delivered archive. The finding therefore applies to the **delivered export**, not to an unseen split.

The [public filename-only audit](../tools/audit_export.py) reproduces the structural counts from the publisher's extracted dataset. It neither reads pixels nor judges labels.

## 2. Rebuilding the evaluation structure

One canonical export was retained per source frame, and complete videos were assigned to separate partitions. The provisional derivative had 524 training frames from seven videos, 108 validation frames from five videos, 213 same-platform test frames from four videos and 361 held-out FiFish frames from one video. There was zero video overlap between these partitions.

That was a real improvement in **split structure**, not certification of the benchmark. Later review found examples of mirrored imagery and missing or imprecise annotations. A model tested on a video-disjoint but incorrectly labelled image can still produce a precise-looking number with an unsound interpretation.

## 3. The model research programme

The archive retains 31 result records across six questions. The [experiment map](EXPERIMENT_MAP.md) groups the methods without ranking them as validated wins:

1. **Evaluation control:** grouped-video baselines, run-to-run variance, frozen selection gates.
2. **Labelling efficiency:** nested label budgets, class- and scale-aware selection, diversity.
3. **Source retention:** replay, regularization, feature retention and response distillation.
4. **Unlabelled information:** enhanced/mixed views, Fourier-domain style and pseudo-labels.
5. **Checkpoint composition:** interpolation, source/target blends and averaging.
6. **Deployment constraints:** small-object features, resolution, class counts and native inference.

Protocols and negative results remain useful as engineering history. Accuracy claims based on the uncertified target labels are on hold. The project did not produce a new, corrected, certified detector benchmark.

## 4. From model to edge-inference software

The deployment work built a 416-pixel NCNN reference application with image, directory, video and camera input paths and structured detection output. A separate Python-free native C++ path and x86-64, AArch64 and ARMv7 executables were produced. Checks included export integrity, desktop inference, a continuous 1,000-frame desktop burn-in and emulated-ARM execution.

The reference path passed an exact-output comparison on 108 provisional validation frames; the native C++ path passed a metric-level parity check but **not** exact per-detection output parity. Both observations concern software behaviour on provisional data, not field model quality. No physical board, camera-connected ROV, sustained onboard thermals or real-water accuracy was measured.

The board benchmark protocol existed, but the exact target board and operating requirement were not fixed or tested during the collaboration. “Deployable” was therefore a prototype direction, not a completed field claim.

## 5. The final data-validity handoff

After image and annotation concerns surfaced, the work stopped treating new target-domain training as the next automatic step. A full-corpus review package covered all 1,206 distinct frames and their drawn labels. It contained 704 **candidate** issues across 636 frames, including suspected missing-object labels, orientation questions, empty-label review and box-geometry cues. Candidate counts are not counts of confirmed errors.

The offline browser workflow supported two independent reviewers and an adjudicator for disagreements. Its ledger recorded proposals, not accepted corrections. Validators and fail-closed gates were built so unreviewed data could not silently be presented as a new approved benchmark. The package was delivered, but reviewers did not complete adjudication or freeze a corrected dataset within the project.

## What exists publicly—and what stays private

This public repository contains an original visual case study, a bounded evidence record, high-level work map, source links and a reproducible filename-lineage audit with synthetic tests. It does **not** mirror LABUST imagery or labels, model weights, the private experiment archive, meeting material, correspondence, unpublished manuscript, review package, or deployment binaries. Those omissions protect source rights, collaborators and the interpretation of unfinished results; they do not mean the work was never done.

For precise claim boundaries, see [Evidence and limitations](EVIDENCE.md). For the public tool, see [Reproduction guide](REPRODUCE.md). For attribution, see [Credits and provenance](CREDITS.md).
