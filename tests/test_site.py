"""Structural checks for the dependency-free public research site."""
from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []
        self.scripts = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        if tag == "script":
            self.scripts += 1
        for attribute in ("href", "src"):
            if values.get(attribute):
                self.references.append((tag, values[attribute]))


class PublicSiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.page = SiteParser()
        cls.page.feed((ROOT / "index.html").read_text(encoding="utf-8"))

    def test_local_references_and_anchors_exist(self) -> None:
        for _, reference in self.page.references:
            parsed = urlsplit(reference)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path:
                self.assertTrue((ROOT / parsed.path).is_file(), reference)
            if parsed.fragment:
                self.assertIn(parsed.fragment, self.page.ids, reference)

    def test_all_vector_assets_are_valid_xml(self) -> None:
        assets = sorted((ROOT / "assets").glob("*.svg"))
        self.assertGreaterEqual(len(assets), 1)
        for asset in assets:
            with self.subTest(asset=asset.name):
                ElementTree.parse(asset)

    def test_no_remote_runtime_assets_or_scripts(self) -> None:
        self.assertEqual(self.page.scripts, 0)
        for tag, reference in self.page.references:
            if tag in {"img", "link"} and not reference.endswith(".md"):
                self.assertFalse(urlsplit(reference).netloc, reference)


if __name__ == "__main__":
    unittest.main()
