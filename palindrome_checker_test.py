import pytest

from palindrome_checker import PalindromeChecker


testdata = [
    ("civic", True),
    ("ivicc", True),
    ("BUB", True),
    ("10801", True),
    ("8racecar8", True),
    ("redder", True),
    ("", True),
    ("b", True),
    ("civil", False),
    ("livci", False),
    ("palindrome", False),
]


def test_palindrome_checker_class():
    assert isinstance(PalindromeChecker(), PalindromeChecker)


@pytest.mark.parametrize("word,expected", testdata)
def test_check_palindrome(word, expected):
    result = PalindromeChecker.check_palindrome(word)
    assert result == expected
