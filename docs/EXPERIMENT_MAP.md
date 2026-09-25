# Experiment map

The private research archive contains 31 result records written before the dataset-validity hold. They are grouped here by question, not ranked as model wins. All dataset-dependent accuracy and selection conclusions remain historical diagnostics until reviewed ground truth exists and the relevant study is rerun.

| Question | Methods and checks explored |
| --- | --- |
| Baseline and evaluation control | Seed-variance measurement; grouped-video baseline smoke; final-model selection gate. |
| How much and which local data? | Annotation-efficiency curve; 16-frame budget; class-balanced and diversity-based selection; active class/scale selection. |
| How to retain source behavior? | Retention-constrained replay; L2-SP; Fisher-weighted EWC; spatial feature retention; interference-selected replay; source-response distillation. |
| Can unlabeled views help? | Mixed original/enhanced views; Fourier-domain source style; low-resource pseudo-labeling; temporal-consistency pseudo-labeling. |
| Can checkpoints be combined? | Alpha-grid refinement; cross-branch and seed soups; per-class head interpolation; source-best blending; retention-headroom ascent; SWAD checkpoint averaging; uniform interpolation frontier. |
| What survives deployment constraints? | Small-object P2 pilot; native-resolution training; class-count analysis; 416-pixel deployment follow-up; NCNN/C++ handoff. |

## How to read this map

- “Explored” means a protocol and result record exist in the private archive; it does not mean the method improved a valid final benchmark.
- Failed and ambiguous branches were retained, rather than dropped from the record.
- Model comparisons are not collapsed into one score because datasets, folds, resolutions and target classes differ.
- The public, runnable component of this showcase is the filename-lineage audit. Full training outputs, source frames, weights, and original review package are deliberately not mirrored.

The final research conclusion is methodological: better model selection requires a reviewed dataset first.
