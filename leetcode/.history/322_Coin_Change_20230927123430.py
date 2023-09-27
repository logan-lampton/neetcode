# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins,
# return -1.

# You may assume that you have an infinite number of each kind of coin.

# Example 1:
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Example 3:
# Input: coins = [1], amount = 0
# Output: 0


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # greedy approach, which is not the most efficient way to do the problem
        # step:
        # amount - the largest amount of coin that fits in the amount
        # sort the coins
        # test if the last coin is larger than the amount
        # if it is larger than the amount, go to the next largest coin and test them
        # if it not larger, subtract the coin from the amount
        # move to the next step using the reduced amount

        # Example 1
        # coins = [1, 2, 5]
        # a = amount
        # f(a) = the fewest number of coins required to make amount a
        # f(6) = 2 (5 + 1)
        # f(9) = 3
        # f(10) = 2

        # f(a) = min(f(a - ci)) + 1

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] == float("inf"):
            return -1

        return dp[-1]
