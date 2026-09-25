#!/usr/bin/env python3
"""Audit source-video lineage in the publisher's outdoor image export.

This program reads directory entries and filenames only. It does not open image
or label files, change the dataset, or claim annotation correctness.
"""
from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

BLUEYE = re.compile(r"video_(BYEDP\d+_[\d-]+_\d+)_mp4-(\d+)_jpg\.rf\.", re.IGNORECASE)
FIFISH = re.compile(r"(NORM\d+)_MP4-(\d+)_jpg\.rf\.", re.IGNORECASE)
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png"}
SPLIT_NAMES = ("train", "val", "valid", "test")


@dataclass(frozen=True)
class Export:
    split: str
    filename: str
    video: str
    frame: int


def parse_source(filename: str) -> tuple[str, int] | None:
    """Recover the source video and frame index encoded in an export filename."""
    match = BLUEYE.search(filename) or FIFISH.search(filename)
    if match is None:
        return None
    return match.group(1).upper(), int(match.group(2))


def collect(root: Path) -> list[Export]:
    """Read outdoor image filenames from standard split/images directories."""
    exports: list[Export] = []
    split_dirs = [root / split / "images" for split in SPLIT_NAMES]
    present_dirs = [directory for directory in split_dirs if directory.is_dir()]
    if not present_dirs:
        raise ValueError(f"No split/images directory found below {root}")

    unparsed: list[str] = []
    for directory in present_dirs:
        split = directory.parent.name
        for path in sorted(directory.iterdir()):
            if not path.is_file() or path.suffix.lower() not in IMAGE_SUFFIXES:
                continue
            if not path.name.lower().startswith("biograd_"):
                continue
            source = parse_source(path.name)
            if source is None:
                unparsed.append(str(path.relative_to(root)))
                continue
            exports.append(Export(split, path.name, source[0], source[1]))

    if unparsed:
        example = ", ".join(unparsed[:3])
        raise ValueError(
            f"{len(unparsed)} outdoor filenames do not encode a known source video "
            f"and frame; examples: {example}"
        )
    if not exports:
        raise ValueError(f"No outdoor exports found below {root}")
    return exports


def summarize(exports: list[Export]) -> dict[str, object]:
    """Count source identities and split overlap without inspecting image bytes."""
    video_splits: dict[str, set[str]] = defaultdict(set)
    frame_splits: dict[tuple[str, int], set[str]] = defaultdict(set)
    split_counts: dict[str, int] = defaultdict(int)
    for export in exports:
        video_splits[export.video].add(export.split)
        frame_splits[(export.video, export.frame)].add(export.split)
        split_counts[export.split] += 1

    spanning_videos = sorted(
        video for video, splits in video_splits.items() if len(splits) > 1
    )
    spanning_frames = sum(len(splits) > 1 for splits in frame_splits.values())
    return {
        "outdoor_exports": len(exports),
        "distinct_source_frames": len(frame_splits),
        "source_videos": len(video_splits),
        "split_counts": dict(sorted(split_counts.items())),
        "videos_spanning_splits": len(spanning_videos),
        "frames_spanning_splits": spanning_frames,
        "spanning_video_ids": spanning_videos,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Extracted dataset root")
    parser.add_argument("--json", action="store_true", help="Print a JSON report")
    parser.add_argument(
        "--require-video-disjoint",
        action="store_true",
        help="Fail if a source video occurs in more than one split",
    )
    args = parser.parse_args(argv)

    try:
        report = summarize(collect(args.root))
    except ValueError as exc:
        parser.error(str(exc))

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"Outdoor exports: {report['outdoor_exports']}")
        print(f"Distinct source frames: {report['distinct_source_frames']}")
        print(f"Source videos: {report['source_videos']}")
        print(f"Videos spanning splits: {report['videos_spanning_splits']}")
        print(f"Frames spanning splits: {report['frames_spanning_splits']}")
        for split, count in report["split_counts"].items():
            print(f"  {split}: {count}")
        print("Filename lineage does not certify labels, orientation, or model accuracy.")

    return 2 if args.require_video_disjoint and report["videos_spanning_splits"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
