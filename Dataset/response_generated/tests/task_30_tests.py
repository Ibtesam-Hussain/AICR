# tests/task_30_tests.py
# Task: Write a function that compares two version strings (like "1.2.3" vs "1.10.0") to see which is newer.

import unittest

from response_generated.gpt.task_30_gpt import compare_versions as gpt_compare
from response_generated.claude.task_30_claude import compare_versions as claude_compare
from response_generated.cursor.task_30_cursor import compare_versions as cursor_compare

# NOTE: Claude's file defines compare_versions() twice. Python silently uses
# only the second definition (the manual tuple-based one) — the first
# (packaging.version-based) implementation is dead code and never executes.
# Flag this as a code-quality issue in ground_truth.json notes, independent
# of whether the active implementation passes these tests.


class TestCompareVersions(unittest.TestCase):

    ALL_FUNCS = [
        ("gpt", gpt_compare),
        ("claude", claude_compare),
        ("cursor", cursor_compare),
    ]

    def test_1_multi_digit_segment_bug(self):
        # Classic version-compare bug: naive string comparison would say
        # "1.2.3" > "1.10.0" because "2" > "1" as characters. Correct answer:
        # 1.10.0 is newer, so compare_versions("1.10.0", "1.2.3") == 1
        for name, func in self.ALL_FUNCS:
            result = func("1.10.0", "1.2.3")
            self.assertEqual(result, 1, f"{name}: failed multi-digit segment comparison")

    def test_2_equal_versions(self):
        for name, func in self.ALL_FUNCS:
            result = func("1.2.3", "1.2.3")
            self.assertEqual(result, 0, f"{name}: equal versions should return 0")

    def test_3_different_segment_lengths(self):
        # "1.2" vs "1.2.0" should be treated as equal (missing segments = 0)
        for name, func in self.ALL_FUNCS:
            result = func("1.2", "1.2.0")
            self.assertEqual(result, 0, f"{name}: different segment lengths should normalize to equal")

    def test_4_simple_lesser(self):
        for name, func in self.ALL_FUNCS:
            result = func("1.2.3", "2.0.0")
            self.assertEqual(result, -1, f"{name}: failed simple lesser-version comparison")

    def test_5_malformed_version_string(self):
        # Non-numeric segment (e.g. "1.2.x") — original task never specified
        # this, so the meaningful check is that it doesn't crash unhandled,
        # or at least fails predictably rather than silently returning a
        # wrong answer.
        for name, func in self.ALL_FUNCS:
            try:
                result = func("1.2.x", "1.2.3")
                # If it didn't raise, just confirm it returned an int (didn't corrupt logic)
                self.assertIsInstance(result, int, f"{name}: returned non-int on malformed input")
            except ValueError:
                # Raising ValueError on non-numeric input is acceptable/expected behavior
                pass
            except Exception as e:
                self.fail(f"{name}: raised unexpected exception type on malformed input -> {e}")


if __name__ == "__main__":
    unittest.main()