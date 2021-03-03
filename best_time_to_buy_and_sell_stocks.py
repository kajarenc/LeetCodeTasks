# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        current_min = prices[0]
        max_profit = 0

        for price in prices:
            if price - current_min > max_profit:
                max_profit = price - current_min

            if price < current_min:
                current_min = price

        return max_profit
