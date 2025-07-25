class Solution:
    def final_attempt(self, word, last_i, last_j) -> bool:
        actual_i = last_i
        actual_j = last_j

        while actual_i <= actual_j:
            if word[actual_i] == word[actual_j]:
                actual_i += 1
                actual_j -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n - 1

        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.final_attempt(s, i, j - 1) or self.final_attempt(
                    s, i + 1, j
                )

        return True
