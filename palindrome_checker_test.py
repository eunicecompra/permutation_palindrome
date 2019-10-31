import pytest

from palindrome_checker import PalindromeChecker


def test_palindrome_checker_class():
    assert isinstance(PalindromeChecker(), PalindromeChecker)


def test_check_palindrome():
    result = PalindromeChecker.check_palindrome("civic")
    assert result


def test_check_palindrome_false():
    result = PalindromeChecker.check_palindrome("civil")
    assert not result
