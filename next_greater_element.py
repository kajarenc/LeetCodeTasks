# Leetcode 503 https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        n = len(nums)
        max_num = max(nums)
        max_index = nums.index(max_num)

        ans = [-1] * n
        stack = []

        for i in range(max_index, n):
            while stack and stack[-1][0] < nums[i]:
                value, ind = stack.pop()
                ans[ind] = nums[i]

            stack.append((nums[i], i))

        for i in range(max_index + 1):
            while stack and stack[-1][0] < nums[i]:
                value, ind = stack.pop()
                ans[ind] = nums[i]

            stack.append((nums[i], i))

        return ans