# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        n = len(s)
        p_l = len(p)

        pattern_counter = defaultdict(int)
        rolling_counter = defaultdict(int)

        if n < p_l:
            return []

        pattern_sum = 0
        for letter in p:
            pattern_sum += ord(letter)
            pattern_counter[letter] += 1

        result = []

        rolling_sum = 0
        for i in range(p_l):
            rolling_sum += ord(s[i])
            rolling_counter[s[i]] += 1

        if rolling_sum == pattern_sum:
            is_anagram = True

            for key in pattern_counter:
                if pattern_counter[key] != rolling_counter[key]:
                    is_anagram = False
                    break

            if is_anagram:
                result.append(0)

        for i in range(p_l, n):
            rolling_sum -= ord(s[i - p_l])
            rolling_sum += ord(s[i])

            rolling_counter[s[i - p_l]] -= 1
            rolling_counter[s[i]] += 1

            if rolling_sum == pattern_sum:
                is_anagram = True
                for key in pattern_counter:
                    if pattern_counter[key] != rolling_counter[key]:
                        is_anagram = False
                        break

                if is_anagram:
                    result.append(i - p_l + 1)

        return result
