![Beneath the Benchmark: an underwater vision research record with a sonar visualization of the dataset audit](assets/cover.svg)

# Beneath the Benchmark

### Underwater vision, with the evidence left visible.

An independent research record by **Hamza Raheel**, developed during an approximately eight-week remote collaboration with the [Laboratory for Underwater Systems and Technologies (LABUST)](https://labust.fer.hr/) at FER, University of Zagreb, from July to September 2026.

The starting question was practical: how can an underwater object detector transfer from controlled imagery to open water? The most important answer was methodological. Before measuring that transfer, we had to establish what the delivered images, splits and annotations actually represented.

[Explore the visual case study](https://hamzamaverick51.github.io/Beneath-The-Benchmark/) · [Project atlas](docs/PROJECT_ATLAS.md) · [Evidence ledger](docs/EVIDENCE.md) · [Reproduce the audit](docs/REPRODUCE.md)

---

## The finding that changed the work

**2,646 outdoor exports represented 1,206 distinct source frames.** All **17 source videos** appeared on both sides of the delivered train/validation split. File count was not independent sample count, and the supplied export could not by itself demonstrate transfer to unseen recordings. This finding concerns that export, **not** any unpublished paper split.

We traced exports to source frames and built video-separated partitions. Later orientation and box-annotation concerns meant that even the revised target-domain comparisons could not be certified as accuracy results. The work became a case study in what a benchmark can—and cannot—support.

The record also includes **31 retained result records**, a **1,000-frame desktop inference burn-in**, and an offline review package flagging **704 candidate issues across 636 frames**. These document work completed, not a certified model gain or accepted label corrections.

---

## Five connected workstreams

### 01 / Reconstruct the data

Recreated the public-source preparation path, reconciled counts, and traced the delivered export back to video and frame identities. The [public audit tool](tools/audit_export.py) reproduces structural findings from filenames without opening image pixels.

### 02 / Repair the evaluation structure

Removed export-level duplication and assigned whole videos to separate development and held-out partitions. The provisional split was video-disjoint; image orientation and boxes were **not** certified.

### 03 / Study model behaviour

Under fixed protocols, investigated annotation budgets, sample selection, run variation, source retention, unlabelled views, checkpoint composition, resolution and small objects. The [experiment map](docs/EXPERIMENT_MAP.md) groups historical results by research question rather than advertising a “best model.”

### 04 / Build an edge-inference software path

Developed NCNN reference and Python-free C++ inference paths, ARM executables and integrity checks. Desktop stability and emulated-ARM execution were exercised. Exact per-detection parity was not reached, and no physical Raspberry Pi, ROV or field benchmark was run.

### 05 / Hand off reviewable uncertainty

Assembled an offline, full-corpus review package for **1,206 distinct frames**, with a **704-record candidate ledger** and a two-reviewer/adjudicator workflow. It enabled human decisions; it did not produce corrected ground truth.

[Read the detailed project atlas →](docs/PROJECT_ATLAS.md)

---

## What the evidence supports

**Established:** filename lineage, overlap in the delivered split, software checks, and delivery of the review queue.

**Provisional:** target-domain detector comparisons on images and labels that had not completed review.

**Not tested:** corrected-dataset accuracy, sustained physical-board runtime, and ROV/open-water performance.

A video-disjoint split fixes one structural leakage route. It cannot repair a mirrored image, missing object or imprecise box. That is why this repository does **not** present a model-performance multiplier as its headline. The [evidence ledger](docs/EVIDENCE.md) distinguishes each claim and limit.

## Reproduce one public finding

The tool reads filenames from a locally extracted copy of the [publisher's dataset](https://github.com/labust/PPE_underwater_dataset). It does not read image contents, upload files or modify the dataset.

~~~bash
python3 tools/audit_export.py /path/to/extracted-dataset
python3 -m unittest discover -s tests -v
~~~

For the export audited here, expect 2,646 outdoor exports, 1,206 distinct source frames and 17 source videos spanning the supplied splits. Other dataset versions may differ. See the [reproduction guide](docs/REPRODUCE.md) for interpretation and limitations.

## Explore the record

- [Project atlas](docs/PROJECT_ATLAS.md) — chronology, workstreams and deliverables.
- [Research story](docs/RESEARCH_STORY.md) — the methodological turn in brief.
- [Experiment map](docs/EXPERIMENT_MAP.md) — six questions behind 31 historical records.
- [Evidence ledger](docs/EVIDENCE.md) — checked facts, provisional results and untested claims.
- [Reproduction guide](docs/REPRODUCE.md) — repeat the public filename audit.
- [Credits and provenance](docs/CREDITS.md) — collaborators, institution and source-data attribution.

---

This account names the people and institution involved, but is **not an official LABUST publication or endorsement**. It contains no private correspondence, meeting content, unpublished manuscript, original LABUST imagery or labels, weights, binaries or personal contact details. Source media remain with the [dataset publisher](https://github.com/labust/PPE_underwater_dataset).

**Status:** collaboration concluded September 2026 · **Dataset:** orientation/annotation review unresolved · **Deployment:** software prototype, not field tested.
