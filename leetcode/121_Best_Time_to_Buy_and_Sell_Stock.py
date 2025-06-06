# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                cur_profit = price - min_price
                if cur_profit > max_profit:
                    max_profit = cur_profit
        
        return max_profit


solution = Solution()
print(solution.maxProfit(prices = [7,1,5,3,6,4]))
print(solution.maxProfit(prices = [7,6,4,3,1]))

# practice, slightly different approach:
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                cur_profit = prices[right] - prices[left]
                if max_profit < cur_profit:
                    max_profit = cur_profit
                right += 1
            else:
                left = right
                right += 1
        
        return max_profit

# Practice
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                cur_profit = prices[right] - prices[left]
                if max_profit < cur_profit:
                    max_profit = cur_profit
            else:
                left = right
            right += 1

        return max_profit

# Practice with dp
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        dp = [0] * len(prices)
        dp[0] = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                dp[i] = prices[i] - min_price
        
        return max(dp)

# Practice:
class Solution:
    def maxProfit(self, prices: [int]) -> int:

        dp = [0] * len(prices)
        min_price = prices[0]
        
        for i in range(1,len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                dp[i] = prices[i] - min_price
        
        return max(dp)