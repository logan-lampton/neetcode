# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them. 

# Example 1:
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.

# Example 2:
# Input: x = 3, y = 1
# Output: 1

# Constraints:
# 0 <= x, y <= 231 - 1


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        def add_zeros(bin_num, length):
            return bin_num.zfill(length)

        hamming_dist = 0
        
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]

        max_len = max(len(bin_x), len(bin_y))

        formatted_bin_x = add_zeros(bin_x, max_len)
        formatted_bin_y = add_zeros(bin_y, max_len)

        for i in range(max_len):
            if formatted_bin_x[i] != formatted_bin_y[i]:
                hamming_dist += 1

        return hamming_dist
    

solution = Solution()
print(solution.hammingDistance(x = 1, y = 4))
print(solution.hammingDistance(x = 93, y = 73))
print(solution.hammingDistance(x = 680142203, y = 1111953568))