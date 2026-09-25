"""Synthetic fixtures: no LABUST media or annotations are committed here."""
from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from audit_export import collect, main, parse_source, summarize  # noqa: E402


class FilenameAuditTests(unittest.TestCase):
    def test_blueye_and_fifish_filenames(self) -> None:
        blueye = (
            "biograd_blueye_root__train__"
            "video_BYEDP000001_2020-01-01_000000_mp4-0008_jpg.rf.abc.jpg"
        )
        fifish = "biograd_fifish_root__valid__NORM0001_MP4-0012_jpg.rf.def.jpg"
        self.assertEqual(
            parse_source(blueye), ("BYEDP000001_2020-01-01_000000", 8)
        )
        self.assertEqual(parse_source(fifish), ("NORM0001", 12))
        self.assertIsNone(parse_source("indoor_frame_001.jpg"))

    def test_split_overlap_and_deduplication(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            train = root / "train" / "images"
            valid = root / "val" / "images"
            train.mkdir(parents=True)
            valid.mkdir(parents=True)
            stem = "biograd_blueye_root__train__video_BYEDP000001_2020-01-01_000000"
            (train / f"{stem}_mp4-0001_jpg.rf.a.jpg").touch()
            (train / f"{stem}_mp4-0001_jpg.rf.b.jpg").touch()
            (valid / f"{stem}_mp4-0002_jpg.rf.c.jpg").touch()
            (valid / "indoor_frame_003.jpg").touch()

            report = summarize(collect(root))
            self.assertEqual(report["outdoor_exports"], 3)
            self.assertEqual(report["distinct_source_frames"], 2)
            self.assertEqual(report["source_videos"], 1)
            self.assertEqual(report["videos_spanning_splits"], 1)
            self.assertEqual(report["frames_spanning_splits"], 0)
            with redirect_stdout(io.StringIO()):
                self.assertEqual(main([str(root), "--require-video-disjoint"]), 2)

    def test_cross_split_frame_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for split, suffix in (("train", "a"), ("val", "b")):
                directory = root / split / "images"
                directory.mkdir(parents=True)
                name = (
                    "biograd_fifish_root__train__NORM0001_MP4-0012_jpg.rf."
                    f"{suffix}.jpg"
                )
                (directory / name).touch()
            report = summarize(collect(root))
            self.assertEqual(report["frames_spanning_splits"], 1)

    def test_unparseable_outdoor_name_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            directory = root / "train" / "images"
            directory.mkdir(parents=True)
            (directory / "biograd_unknown.jpg").touch()
            with self.assertRaisesRegex(ValueError, "do not encode"):
                collect(root)


if __name__ == "__main__":
    unittest.main()
