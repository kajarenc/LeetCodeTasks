from typing import List

# 739. Daily Temperatures https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:

        n = len(T)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):

            while stack and T[i] >= stack[-1][0]:
                stack.pop()

            if stack:
                ans[i] = stack[-1][1] - i
            stack.append((T[i], i))

        return ans
