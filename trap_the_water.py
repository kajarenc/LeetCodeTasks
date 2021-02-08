# https://leetcode.com/problems/trapping-rain-water/

# O(n^2) solution, O(1) memory

# class Solution:
#
#     def trap(self, height: List[int]) -> int:
#         result = 0
#         n = len(height)
#
#         for i in range(n):
#             left_max = 0
#             right_max = 0
#
#             for j in range(i):
#                 if height[j] > left_max:
#                     left_max = height[j]
#
#             for j in range(i + 1, n):
#                 if height[j] > right_max:
#                     right_max = height[j]
#
#             possible_water_level = min(left_max, right_max) - height[i]
#
#             if possible_water_level > 0:
#                 result += possible_water_level
#
#         return result


# O(n) solution with O(n) memory
# class Solution:
#
#     def trap(self, height: List[int]) -> int:
#         result = 0
#         n = len(height)
#
#         left_max_arr = [0] * n
#         right_max_arr = [0] * n
#
#         left_max = 0
#         right_max = 0
#
#         for i in range(n):
#             if height[i] > left_max:
#                 left_max = height[i]
#             left_max_arr[i] = left_max
#
#         for i in range(n - 1, -1, -1):
#             if height[i] > right_max:
#                 right_max = height[i]
#             right_max_arr[i] = right_max
#
#         for i in range(n):
#             result += max(min(left_max_arr[i], right_max_arr[i]) - height[i], 0)
#         return result


# O(n) solution with O(1) memory
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)

        if n < 3:
            return 0

        left_ptr = 0
        right_ptr = n - 1

        left_max = height[left_ptr]
        right_max = height[right_ptr]

        while left_ptr <= right_ptr:
            if left_max <= right_max:
                left_max = max(left_max, height[left_ptr])
                result += left_max - height[left_ptr]
                left_ptr += 1
            else:
                right_max = max(right_max, height[right_ptr])
                result += right_max - height[right_ptr]
                right_ptr -= 1

        return result
