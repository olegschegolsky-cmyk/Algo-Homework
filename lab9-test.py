import unittest
from lab9 import find_substring


class TestFSASearch(unittest.TestCase):
    def test_single_match(self):
        haystack = "hello world"
        needle = "world"
        self.assertEqual(find_substring(haystack, needle), [6])

    def test_multiple_matches(self):
        haystack = "абабабагаламага"
        needle = "аба"
        self.assertEqual(find_substring(haystack, needle), [0, 2, 4])

    def test_no_match(self):
        haystack = "its is first test"
        needle = "second"
        self.assertEqual(find_substring(haystack, needle), [])

    def test_empty_needle(self):
        haystack = "anything"
        needle = ""
        self.assertEqual(find_substring(haystack, needle), [])

    def test_needle_larger_than_haystack(self):
        haystack = "car"
        needle = "bus"
        self.assertEqual(find_substring(haystack, needle), [])

unittest.main()