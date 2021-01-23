# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keyboard = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        results = []

        def craft_word(digits, prefix):
            if not digits:
                results.append(prefix)
                return

            current_digit, rest_digits = digits[0], digits[1:]

            for letter in keyboard[current_digit]:
                craft_word(rest_digits, prefix + letter)

        craft_word(digits, '')

        return results
