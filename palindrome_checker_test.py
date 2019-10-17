import unittest

from palindrome_checker import PalindromeChecker


class PalindromeCheckerTest(unittest.TestCase):
    def test_palindrome_checker_class(self):
        self.assertIsInstance(PalindromeChecker(), PalindromeChecker, "class exists")
