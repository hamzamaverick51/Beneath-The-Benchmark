![Beneath the Benchmark: an underwater vision research record with a sonar visualization of the dataset audit](assets/cover.svg)

# Beneath the Benchmark

### Underwater vision, with the evidence left visible.

This is **Hamza Raheel's independent research record** of an approximately eight-week remote collaboration with the [Laboratory for Underwater Systems and Technologies (LABUST)](https://labust.fer.hr/) at FER, University of Zagreb, from July to September 2026. The work began with a practical objective: improve how an underwater object detector transfers from controlled imagery to a new open-water site. It ended with a more consequential finding: model progress could not be judged responsibly until the delivered data and annotations were made trustworthy.

**The outcome was a research system, not a single headline score:** source-data reconstruction, a video-lineage audit, video-separated evaluation, bounded detector studies, an edge-inference software prototype, and an offline human-review handoff. The collaboration concluded before a corrected dataset or physical ROV benchmark could be completed.

[Full work map](docs/PROJECT_ATLAS.md) · [Evidence and limitations](docs/EVIDENCE.md) · [Website source](index.html) (GitHub Pages setup pending)

## The project at a glance

| Evidence from the work | What it means |
| --- | --- |
| **2,646 exported outdoor images → 1,206 distinct source frames** | File count was not independent sample count. |
| **17 of 17 source videos crossed the delivered train/validation split** | The supplied export could not measure transfer to unseen recordings as-is. This finding does not establish leakage in an unpublished paper split. |
| **31 retained result records** | Model ideas, controls, failed branches and ambiguous results were documented; their target-domain accuracy conclusions are historical diagnostics after the data-validity hold. |
| **1,000-frame desktop inference burn-in** | The edge-inference *software* path was exercised. No physical Raspberry Pi, ROV or field performance was measured. |
| **704 candidate issues across 636 frames** | A full-corpus review package was delivered. Candidate flags are not accepted annotation corrections. |

![Five stages of the work and their evidence status](assets/research-path.svg)

## What was built

**01 · Reconstruct and audit.** Recreated the public-source preparation path and reconciled dataset counts, while distinguishing reconstruction from exact reproduction. Then traced the delivered outdoor export back to video/frame identities. The [public audit tool](tools/audit_export.py) reproduces the structural counts without opening image pixels.

**02 · Make evaluation structurally honest.** Removed export-level duplication and assigned whole videos to separate development and held-out partitions. The provisional split was video-disjoint; its image orientation and boxes were **not** certified.

**03 · Investigate model behaviour.** Used frozen protocols to study annotation budgets, sample selection, run-to-run variation, source retention, unlabelled views, checkpoint composition, resolution and small objects. The [experiment map](docs/EXPERIMENT_MAP.md) groups the retained records by question, not by claimed win.

**04 · Prototype edge inference.** Built NCNN reference and Python-free C++ inference paths, ARM executables and integrity checks. Desktop stability and emulated-ARM execution were demonstrated. The native path did not reach exact per-detection output parity; no physical-board benchmark was run.

**05 · Hand off reviewable uncertainty.** After orientation and annotation concerns surfaced, assembled an offline package covering all 1,206 distinct frames, a 704-record candidate ledger and a two-reviewer/adjudicator workflow. The package enabled human decisions; it did not make them or produce a corrected ground truth.

The [project atlas](docs/PROJECT_ATLAS.md) gives the chronology, deliverables and precise boundaries behind each stage.

## Why the model scores are not the headline

Separating videos fixes a structural leakage route. It does not repair a mirrored image, a missing object label or an imprecise box. Because those questions were unresolved at handoff, the target-domain accuracy and model-selection results remain **on hold**. Presenting a multiplier or “best model” from that benchmark as a certified outcome would misrepresent what the experiment measured.

This repository therefore distinguishes:

- **Established:** filename lineage, split overlap, software checks and the delivered review queue.
- **Provisional:** target-domain detector comparisons on uncertified images/labels.
- **Not tested:** final corrected-dataset accuracy, sustained physical-board runtime and ROV/open-water performance.

See the [claim-by-claim evidence ledger](docs/EVIDENCE.md).

## Reproduce a public finding

The included tool reads filenames from a locally extracted copy of the [publisher's dataset](https://github.com/labust/PPE_underwater_dataset). It does not read image contents, upload files or modify the dataset.

~~~bash
python3 tools/audit_export.py /path/to/extracted-dataset
python3 -m unittest discover -s tests -v
~~~

For the export audited here, expect 2,646 outdoor exports, 1,206 distinct source frames and 17 source videos spanning the supplied splits. Other versions may differ; see the [reproduction guide](docs/REPRODUCE.md). The tool cannot assess pixels, labels, model accuracy or deployment speed.

## Navigate the record

| Document | What it contains |
| --- | --- |
| [Visual case study](index.html) | A designed, accessible project narrative; publish the root directory with GitHub Pages to view it as a website. |
| [Project atlas](docs/PROJECT_ATLAS.md) | Detailed sequence, workstreams, outputs and evidence limits. |
| [Research story](docs/RESEARCH_STORY.md) | Short chronology and methodological turn. |
| [Experiment map](docs/EXPERIMENT_MAP.md) | Six questions across 31 historical result records. |
| [Evidence and limitations](docs/EVIDENCE.md) | A claim ledger: what was checked, what is provisional and what was never tested. |
| [Reproduction guide](docs/REPRODUCE.md) | Instructions and interpretation for the public filename audit. |
| [Credits and provenance](docs/CREDITS.md) | People, institutional context and source-data attribution. |

## Attribution and release boundary

This account names the people and institution involved, but is **not an official LABUST publication or endorsement**. It contains no meeting recordings, correspondence, unpublished manuscript, original LABUST footage or labels, model weights, private experiment outputs, review-package media, deployment binaries or personal contact details. Original figures and the small public audit tool were prepared for this showcase. Source media remain with the [dataset publisher](https://github.com/labust/PPE_underwater_dataset).

**Status:** collaboration concluded September 2026 · **Dataset:** annotation/orientation review unresolved · **Deployment:** software prototype, not field tested.
