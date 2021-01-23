# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def construct_sum(candidates, prev_nums, target):
            if target == 0:
                results.append(prev_nums)

            if target > 0:
                for i, num in enumerate(candidates):
                    if num <= target:
                        construct_sum(candidates[i:], prev_nums + [num], target - num)

        construct_sum(candidates, [], target)
        return results
