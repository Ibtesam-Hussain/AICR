# tests/task_29_tests.py
# Task: Write a function that truncates a string to a max length without cutting a word in half.

import unittest

# --- Import snippets (adjust import paths to your actual folder structure) ---
from response_generated.gpt.task_29_gpt import truncate_string as gpt_truncate
from response_generated.claude.task_29_claude import truncate_string as claude_truncate_raw
from response_generated.cursor.task_29_cursor import truncate_without_breaking_words as cursor_truncate

# Wrapper: Claude's version adds a "..." suffix by default, which the original
# task never asked for. Neutralize suffix="" so all three are compared on the
# same basis (plain truncation at a word boundary, no suffix).
def claude_truncate(text, max_length):
    return claude_truncate_raw(text, max_length, suffix="")


class TestTruncateString(unittest.TestCase):

    def run_case(self, func, text, max_length, description):
        result = func(text, max_length)
        self.assertLessEqual(len(result), max_length,
            f"{description}: result exceeds max_length ({len(result)} > {max_length})")
        return result

    def test_1_normal_case(self):
        # Normal sentence, should cut at a word boundary
        text, max_length = "Hello world this is a test", 11
        for name, func in [("gpt", gpt_truncate), ("claude", claude_truncate), ("cursor", cursor_truncate)]:
            result = self.run_case(func, text, max_length, f"{name} normal case")
            self.assertNotIn(result[-1:], [" "], f"{name}: trailing space left in result")

    def test_2_empty_string(self):
        text, max_length = "", 10
        for name, func in [("gpt", gpt_truncate), ("claude", claude_truncate), ("cursor", cursor_truncate)]:
            result = func(text, max_length)
            self.assertEqual(result, "", f"{name}: empty input should return empty string")

    def test_3_single_long_word_no_spaces(self):
        # No space to break on — original task doesn't specify behavior here,
        # but result should still respect max_length or at least not crash.
        text, max_length = "Supercalifragilisticexpialidocious", 10
        for name, func in [("gpt", gpt_truncate), ("claude", claude_truncate), ("cursor", cursor_truncate)]:
            result = func(text, max_length)
            self.assertTrue(isinstance(result, str), f"{name}: did not return a string")
            # Note in ground_truth.json: whether this counts as "fragile" (fine, since
            # no word boundary exists) or the model handles it another way.

    def test_4_string_shorter_than_max_length(self):
        text, max_length = "Hi", 50
        for name, func in [("gpt", gpt_truncate), ("claude", claude_truncate), ("cursor", cursor_truncate)]:
            result = func(text, max_length)
            self.assertEqual(result, "Hi", f"{name}: should return original string unchanged")

    def test_5_zero_max_length(self):
        # Malformed/boundary input
        text, max_length = "Hello world", 0
        for name, func in [("gpt", gpt_truncate), ("claude", claude_truncate), ("cursor", cursor_truncate)]:
            try:
                result = func(text, max_length)
                self.assertLessEqual(len(result), max_length,
                    f"{name}: result exceeds zero max_length")
            except Exception as e:
                self.fail(f"{name}: raised exception on max_length=0 -> {e}")


if __name__ == "__main__":
    unittest.main()