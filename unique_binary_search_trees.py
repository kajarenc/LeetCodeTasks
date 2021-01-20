# https://leetcode.com/problems/unique-binary-search-trees/

class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)

        dp[0] = 1
        dp[1] = 1

        # dp[i] - number of unique trees with i nodes

        for i in range(2, n + 1):
            number_of_unique_trees = 0

            for k in range(1, i + 1):
                number_of_unique_trees += dp[k - 1] * dp[i - k]

            dp[i] = number_of_unique_trees

        print(dp)
        return dp[n]
