
class PalindromeChecker:
    @staticmethod
    def check_palindrome(word):
        result = False
        odd_letter_set = set()
        for letter in word:
            if letter in odd_letter_set:
                odd_letter_set.remove(letter)
            else:
                odd_letter_set.add(letter)

        if len(odd_letter_set) <= 1:
            result = True

        return result
