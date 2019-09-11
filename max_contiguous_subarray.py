from typing import List

# https://leetcode.com/problems/maximum-subarray/
# video explanation https://youtu.be/2MmGzdiKR9Y


def maxSubArray(nums: List[int]) -> int:
    n = len(nums)

    DP = [0] * n

    DP[0] = nums[0]

    for i in range(1, n):
        DP[i] = max([DP[i-1] + nums[i], nums[i]])

    return max(DP)
