# Reproduce the structural audit

This repository ships a small, dependency-free audit of **export filename lineage**. It does not ship the dataset, reproduce model training, or inspect pixels and labels.

1. Obtain the dataset from the [LABUST publisher repository](https://github.com/labust/PPE_underwater_dataset) and follow its own extraction and license instructions.
2. Locate the extracted directory containing train/images/ and val/images/.
3. From this repository's root, run:

~~~bash
python3 tools/audit_export.py /path/to/extracted
python3 tools/audit_export.py /path/to/extracted --json
python3 -m unittest discover -s tests -v
~~~

For the export audited during this project, the expected **outdoor-only** counts are 2,646 files, 1,206 distinct (video, frame) identities, 17 source videos, and 17 videos represented in both delivered splits. Other dataset versions may differ; a mismatch is a prompt to check provenance, not to force the expected result.

The tool ignores indoor images, reads no image bytes, and writes nothing unless redirected by the user. --require-video-disjoint exits unsuccessfully when any source video spans splits, which is useful for checking a *new* proposed split. The supplied export is expected to fail that strict check.

## Reproducibility boundary

The public tool checks only what filenames can establish. Pixel-level near-duplicates, orientation, annotation correctness, model accuracy, and device runtime require separate evidence. Do not treat a clean filename audit as a certified benchmark.
