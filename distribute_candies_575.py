from collections import defaultdict


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        n = len(candyType)
        candyNumbers = defaultdict(int)

        for candy in candyType:
            candyNumbers[candy] += 1

        distinctTypes = len(candyNumbers.keys())

        if distinctTypes < n // 2:
            return distinctTypes
        else:
            return n // 2
