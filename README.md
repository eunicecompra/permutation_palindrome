# Palindrome Checker in Python

Problem from [Interview Cake](https://www.interviewcake.com/)

> Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome. ↴
>
> You can assume the input string only contains lowercase letters.
>
>Examples:
>
>- "civic" should return True
>- "ivicc" should return True
>- "civil" should return False
>- "livci" should return False
>- "But 'ivicc' isn't a palindrome!"
>
>If you had this thought, read the question again carefully. We're asking if any permutation of the string is a palindrome. Spend some extra time ensuring you fully understand the question before starting. Jumping in with a flawed understanding of the problem doesn't look good in an interview.

## Solution
Use a set that tracks the character that doesn't have a match. If the set is empty or has at least one character left, it means that the word is a palindrome.

This works in the premise that a palindrome has either of the following:
- all of its characters are matching e.g. redder
- and only one character that doesn't match e.g. v in civic.

By iterating the characters of the given word, a character that is not in the set is added to the set and removed if a matching character is found in the next iterations.

## How to run the test

### Native
Prerequisite: pytest - for parametrized testing
```
pytest palindrome_checker_test.py
```
### Docker
```
docker image build -t palindrome_checker .
```

## Library Versions
- Python 3.7.0 or above
- pytest-5.2.1 or above

