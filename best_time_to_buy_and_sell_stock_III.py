# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
#  Based on Best time to buy and sell stocks with cooldown explanation

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        dp = {}

        dp['A'] = [0] * n
        dp['B'] = [0] * n
        dp['C'] = [float("-inf")] * n
        dp['D'] = [float("-inf")] * n
        dp['E'] = [float("-inf")] * n

        dp['B'][0] = - prices[0]

        for i in range(1, n):
            dp['B'][i] = max(dp['B'][i - 1], dp['A'][i - 1] - prices[i])
            dp['C'][i] = max(dp['C'][i - 1], dp['B'][i - 1] + prices[i])
            dp['D'][i] = max(dp['D'][i - 1], dp['C'][i - 1] - prices[i])
            dp['E'][i] = max(dp['E'][i - 1], dp['D'][i - 1] + prices[i])

        return max(dp['A'][-1], dp['C'][-1], dp['E'][-1])