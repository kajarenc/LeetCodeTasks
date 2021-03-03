# https://leetcode.com/problems/word-break/

class Solution:
    def __init__(self):
        self.memo = dict()

    def remember(self, s: str, my_dict, my_set):
        if s not in self.memo:
            self.memo[s] = self.backtrack(s, my_dict, my_set)
        return self.memo[s]

    def backtrack(self, s: str, my_dict, my_set):
        if s in my_set:
            return True

        for l in my_dict:
            if l < len(s):
                if s[:l] in my_dict[l]:
                    if self.remember(s[l:], my_dict, my_set):
                        return True

        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        my_dict = dict()
        my_set = set()

        for word in wordDict:
            my_set.add(word)
            if len(word) not in my_dict:
                my_dict[len(word)] = {word}
            else:
                my_dict[len(word)].add(word)

        return self.backtrack(s, my_dict, my_set)
