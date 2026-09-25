# Evidence and limitations

| Claim | Evidence level | Boundary |
| --- | --- | --- |
| 2,646 outdoor exports map to 1,206 distinct source frames from 17 videos. | Structural audit of the supplied export. | Counts describe that export, not all available LABUST footage. |
| All 17 videos crossed the supplied training/evaluation split. | Source-video IDs recovered from export filenames. | Video separation alone does not guarantee different scenes or reliable labels. |
| A provisional video-disjoint derivative was built. | Split manifest and independent checks in the private technical record. | Image orientation and box labels were later found to be uncertified. |
| Detector and annotation-budget studies were run. | Frozen protocols and retained result records. | Their target-domain accuracy and model-selection conclusions are historical diagnostics, not current validated performance. |
| NCNN/C++ inference and ARM builds were implemented. | Desktop functional/parity checks, 1,000-frame desktop stability test, and ARM executables run under QEMU. | No physical Raspberry Pi or ROV latency, camera integration, thermals, or field accuracy measured. The native C++ path did not achieve exact per-detection output parity. |
| 704 issues were placed in an offline review queue. | Read-only full-corpus audit and sent package dated 12 September. | These are **candidates** across 636 frames. Human decisions and final correction authority were not completed. |

## Claims deliberately not made

- No state-of-the-art result or multiplicative model-improvement headline.
- No certified corrected dataset, final test result, or production-ready detector.
- No physical ROV or Raspberry Pi deployment.
- No publication, accepted paper, or official LABUST endorsement of this independent case study.

## Why the hold matters

A video-disjoint split prevents one form of leakage. It does not fix a mislabeled object, an unannotated ROV, or a mirrored image. A model evaluated on uncertain ground truth can yield a precise-looking number without a trustworthy interpretation. The honest next step would be reviewed source footage, adjudicated corrections, a frozen dataset version, and a rerun of the experiments. That next step did not occur within this collaboration.
