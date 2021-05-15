# https://leetcode.com/problems/validate-stack-sequences/
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        stack = []

        n = len(pushed)

        while i < n:
            stack.append(pushed[i])

            while stack and stack[-1] == popped[j]:
                j += 1
                stack.pop()
            i += 1

        return i == j == n and not stack