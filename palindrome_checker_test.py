import pytest

from palindrome_checker import PalindromeChecker


testdata = [
    ("civic", True),
    ("ivicc", True),
    ("BUB", True),
    ("civil", False),
    ("livci", False)
]


def test_palindrome_checker_class():
    assert isinstance(PalindromeChecker(), PalindromeChecker)


@pytest.mark.parametrize("word,expected", testdata)
def test_check_palindrome(word, expected):
    result = PalindromeChecker.check_palindrome(word)
    assert result == expected
