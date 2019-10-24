import unittest

from palindrome_checker import PalindromeChecker


class PalindromeCheckerTest(unittest.TestCase):
    def test_palindrome_checker_class(self):
        self.assertIsInstance(PalindromeChecker(), PalindromeChecker, "class exists")

    def test_check_palindrome_true(self):
        result = PalindromeChecker.check_palindrome("civic")
        self.assertTrue(result)

    def test_check_palindrome_false(self):
        result = PalindromeChecker.check_palindrome("civil")
        self.assertFalse(result)
