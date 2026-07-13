#!/usr/bin/env python3
"""Regression tests for promo progressive disclosure and gate fixtures."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ROUTER = ROOT / "references" / "image" / "promo-router.md"
GOOD_FIXTURES = ROOT / "scripts" / "fixtures" / "good" / "promo_patterns.jsonl"


class PromoContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.router = ROUTER.read_text(encoding="utf-8")
        cls.records = [
            json.loads(line)
            for line in GOOD_FIXTURES.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    def test_router_links_exactly_one_file_per_pattern(self) -> None:
        links = re.findall(r"\(promo/(P[1-8]-[^)]+\.md)\)", self.router)
        self.assertEqual(8, len(links))
        self.assertEqual({f"P{index}" for index in range(1, 9)}, {name[:2] for name in links})
        for relative in links:
            self.assertTrue((ROUTER.parent / "promo" / relative).is_file(), relative)

    def test_fixtures_cover_all_patterns_and_keep_information_card_separate(self) -> None:
        promo = [record for record in self.records if record.get("cut_type") == "promo_poster"]
        self.assertEqual({f"P{index}" for index in range(1, 9)}, {record["promo_pattern"] for record in promo})
        info = next(record for record in self.records if record["id"] == "INFO-C7")
        self.assertEqual("C7", info["category"])
        self.assertEqual("sns_cover", info["cut_type"])
        self.assertNotIn("promo_pattern", info)

    def test_three_representative_compiles_are_self_contained_under_limit(self) -> None:
        representatives = {"PROMO-P3", "PROMO-P5", "PROMO-P7"}
        selected = {record["id"]: record for record in self.records if record["id"] in representatives}
        self.assertEqual(representatives, set(selected))
        for identifier, record in selected.items():
            prompt = record["full_prompt"]
            self.assertLessEqual(len(prompt), 2000, identifier)
            self.assertNotIn("/tmp/", prompt, identifier)
            self.assertRegex(prompt, r"AR\s+\d+:\d+$", identifier)
            self.assertRegex(record["look_preset"], r"^L[1-8]$")
            self.assertIn(record["promo_subject"], prompt)
            self.assertGreaterEqual(len(record["finishing_devices"]), 1)
            self.assertLessEqual(len(record["finishing_devices"]), 3)
            self.assertEqual(prompt.count(record["korean_copy"]), 1)

    def test_only_implemented_look_and_typography_ranges_are_routed(self) -> None:
        self.assertIn("L1~L8", self.router)
        self.assertIn("T1~T4", self.router)
        self.assertIn("L9", self.router)
        self.assertIn("T5", self.router)
        self.assertIn("추가하지 않는다", self.router)


if __name__ == "__main__":
    unittest.main(verbosity=2)
