# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:
# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Example 2:
# Input: stones = [1]
# Output: 1

# Constraints:
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000


class Solution:
    def lastStoneWeight(self, stones: [int]) -> int:
        while len(stones) > 1:
            stones.sort()
            heaviest_stone = stones.pop()
            second_heaviest = stones.pop()
            diff = heaviest_stone - second_heaviest
            if diff > 0:
                stones.append(diff)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0

        # -----Without using sort/ method using recursion-----

        # def smash_two_stones(stones):
        #     if len(stones) < 1:
        #         return 0
        #     elif len(stones) == 1:
        #         return stones[0]

        #     heaviest_val = -1
        #     heaviest_index = -1
        #     second_heaviest_val = -1
        #     second_heaviest_index = -1

        #     for i, stone in enumerate(stones):
        #         if stone > heaviest_val:
        #             second_heaviest_val = heaviest_val
        #             second_heaviest_index = heaviest_index
        #             heaviest_index = i
        #             heaviest_val = stone
        #         elif stone == heaviest_val:
        #             second_heaviest_val = stone
        #             second_heaviest_index = i
        #         elif stone > second_heaviest_val:
        #             second_heaviest_val = stone
        #             second_heaviest_index = i

        #     difference = heaviest_val - second_heaviest_val

        #     if heaviest_index >= 0 and second_heaviest_index >= 0:
        #         if difference > 0:
        #             stones.append(difference)
        #         if heaviest_index > second_heaviest_index:
        #             stones.pop(heaviest_index)
        #             stones.pop(second_heaviest_index)
        #         else:
        #             stones.pop(second_heaviest_index)
        #             stones.pop(heaviest_index)

        #     return smash_two_stones(stones)

        # return smash_two_stones(stones)
