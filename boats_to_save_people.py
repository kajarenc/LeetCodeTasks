# https://leetcode.com/problems/boats-to-save-people/

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()

        if people[-1] > limit:
            return -1

        boats = 0

        left = 0
        right = n - 1

        while left <= right:
            new_boat_weight = 0

            if new_boat_weight + people[right] <= limit:
                new_boat_weight += people[right]
                right -= 1

            if new_boat_weight + people[left] <= limit:
                new_boat_weight += people[left]
                left += 1

            boats += 1

        return boats

