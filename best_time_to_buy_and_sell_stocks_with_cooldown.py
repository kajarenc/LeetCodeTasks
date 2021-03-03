# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# https://youtu.be/pkiJyNijgBw
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if not prices:
            return 0

        dp = [[0] * n for _ in range(3)]
        dp[1][0] = -prices[0]

        for j in range(1, n):
            dp[0][j] = max(dp[0][j - 1], dp[2][j - 1])
            dp[1][j] = max(dp[0][j - 1] - prices[j], dp[1][j - 1])
            dp[2][j] = dp[1][j - 1] + prices[j]

        return max(dp[0][-1], dp[1][-1], dp[2][-1])