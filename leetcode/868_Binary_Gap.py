# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

# Example 1:
# Input: n = 22
# Output: 2
# Explanation: 22 in binary is "10110".
# The first adjacent pair of 1's is "10110" with a distance of 2.
# The second adjacent pair of 1's is "10110" with a distance of 1.
# The answer is the largest of these two distances, which is 2.
# Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

# Example 2:
# Input: n = 8
# Output: 0
# Explanation: 8 in binary is "1000".
# There are not any adjacent pairs of 1's in the binary representation of 8, so we return 0.

# Example 3:
# Input: n = 5
# Output: 2
# Explanation: 5 in binary is "101".

# Constraints:
# 1 <= n <= 109


class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)
        bin_n = binary[2:]

        longest_distance = 0
        cur_distance = 0
        seen_1 = False
        
        for i in range(len(bin_n)):
            if bin_n[i] == "1" and seen_1 == False:
                seen_1 = True
            elif bin_n[i] == "0" and seen_1 == True:
                cur_distance += 1
            elif bin_n[i] == "1" and seen_1 == True:
                cur_distance += 1
                if cur_distance > longest_distance:
                    longest_distance = cur_distance
                cur_distance = 0

        return longest_distance
    

solution = Solution()
print(solution.binaryGap(n = 22))
print(solution.binaryGap(n = 8))
print(solution.binaryGap(n = 5))