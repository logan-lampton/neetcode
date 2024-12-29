# You are given an integer array deck where deck[i] represents the number written on the ith card.

# Partition the cards into one or more groups such that:

# Each group has exactly x cards where x > 1, and
# All the cards in one group have the same integer written on them.
# Return true if such partition is possible, or false otherwise.

# Example 1:
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].

# Example 2:
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.

# Constraints:
# 1 <= deck.length <= 104
# 0 <= deck[i] < 104


class Solution:
    def hasGroupsSizeX(self, deck: [int]) -> bool:

        def greatest_common_denominator(value1, value2):
            while value2 != 0:
                tempval1 = value1
                value1 = value2
                value2 = tempval1 % value2
            return value1

        hashmap = {}
        for card in deck:
            if card not in hashmap:
                hashmap[card] = 1
            else:
                hashmap[card] += 1
        
        freq_gcd = None

        for value in hashmap.values():
            if freq_gcd is None:
                freq_gcd = value
            else:
                freq_gcd = greatest_common_denominator(freq_gcd, value)
        
        return freq_gcd > 1
    

solution = Solution()
print(solution.hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1]))
print(solution.hasGroupsSizeX(deck = [1,1,1,2,2,2,3,3]))