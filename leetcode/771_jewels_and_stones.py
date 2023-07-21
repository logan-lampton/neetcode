# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you
# have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also
# jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:
#
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: jewels = "z", stones = "ZZ"
# Output: 0

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        shared_jewels = 0
        jewels_set = set(jewels)
        for stone in stones:
            if stone in jewels_set:
                shared_jewels += 1
        return shared_jewels
