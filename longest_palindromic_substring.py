# https://leetcode.com/problems/longest-palindromic-substring/
# insight from https://youtu.be/UflHuQj6MVA
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        matrix = [[0] * n for _ in range(n)]

        current_max_i = 0
        current_max_j = 0
        current_max = 1

        for i in range(n):
            matrix[i][i] = 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                matrix[i][i + 1] = 1
                current_max_i = i
                current_max_j = i + 1

                current_max = 2

        for i in range(n - 3, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j] and matrix[i + 1][j - 1] == 1:
                    matrix[i][j] = 1

                    if j - i + 1 > current_max:
                        current_max = j - i + 1
                        current_max_i = i
                        current_max_j = j

        return s[current_max_i:current_max_j + 1]