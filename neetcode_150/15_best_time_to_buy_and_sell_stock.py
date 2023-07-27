# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            max_profit = max(max_profit, prices[right] - prices[left])
            right += 1

        if max_profit <= 0:
            return 0

        return max_profit
