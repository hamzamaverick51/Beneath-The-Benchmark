# Research story

This is the project sequence, not a diary of correspondence. Dates identify work milestones; they do not imply continuous day-to-day supervision.

| Period | Question and action | Durable outcome |
| --- | --- | --- |
| Late July 2026 | Reconstruct the released training and data path; audit the supplied outdoor export before comparing detectors. | Source-frame lineage and split-overlap findings. |
| Early August | Replace image-level random separation with video-grouped development and held-out splits. | A structurally video-disjoint derivative and explicit leakage checks. Later visual review showed its labels and orientation were not yet certified. |
| August | Study target-label budgets and run-to-run variation; test model, data-selection and adaptation ideas under written protocols. | Historical diagnostic results and negative results, not a final accuracy claim. |
| Late August | Translate the research model into an edge-inference path. | NCNN runtime, native C++ implementation, ARM builds, desktop stability checks and QEMU smoke tests. No physical-board result. |
| Early September | Re-examine source imagery after annotation and orientation concerns were raised. | Data-validity hold; no new model promoted from the affected benchmark. |
| 12 September | Deliver a way to review the suspected problems systematically. | Offline review package covering all 1,206 distinct frames, an evidence-linked candidate register, and a two-reviewer/adjudicator workflow. |
| 16 September | The lab ended this line of work. | No further training or physical deployment was completed under this collaboration. |

## The central methodological turn

The original outdoor export contained 2,646 image files, but only 1,206 distinct source frames from 17 videos. Frames from the same video appeared across training and evaluation. That makes image-level performance an unreliable answer to the question of transfer to a new recording environment. The first response was to preserve video provenance and assign whole videos to separate splits.

That solved one structural problem, not the whole benchmark. Later inspection found orientation and annotation issues in the derivative. Accordingly, the experiment scores are retained as a record of what was tried, but not presented here as certified model improvement. The last deliverable was a review workflow so corrections could be assessed by people with authority over the data.

## What this project illustrates

The useful result is not a single high metric. It is the sequence **audit → isolate → experiment → challenge the labels → stop unsupported claims → hand over reviewable evidence**. That sequence is transferable to other small, video-derived computer-vision datasets.
