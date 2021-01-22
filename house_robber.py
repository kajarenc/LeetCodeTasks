# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        n = len(nums)
        total_sum_arr = [0] * n

        total_sum_arr[0] = nums[0]
        total_sum_arr[1] = nums[1]

        for i in range(2, n):
            total_sum_arr[i] = max(total_sum_arr[:i - 1]) + nums[i]

        return max(total_sum_arr)