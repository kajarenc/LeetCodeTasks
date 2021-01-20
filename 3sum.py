# https://leetcode.com/problems/3sum/submissions/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        results = []

        for i in range(len(nums) - 2):
            if (i != 0 and nums[i] == nums[i - 1]):
                continue

            if nums[i] > 0:
                break

            left_ptr = i + 1
            right_ptr = n - 1

            while left_ptr < right_ptr:
                if nums[left_ptr] + nums[right_ptr] == -nums[i]:
                    triple = [nums[i], nums[left_ptr], nums[right_ptr]]
                    results.append(triple)

                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr + 1]:
                        left_ptr += 1

                    while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr - 1]:
                        right_ptr -= 1

                    left_ptr += 1
                    right_ptr -= 1
                elif nums[left_ptr] + nums[right_ptr] < -nums[i]:
                    left_ptr += 1
                else:
                    right_ptr -= 1

        return results
