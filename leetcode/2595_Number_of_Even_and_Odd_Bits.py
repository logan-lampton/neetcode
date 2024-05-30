# You are given a positive integer n.

# Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

# Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

# Return an integer array answer where answer = [even, odd].

# Example 1:
# Input: n = 17
# Output: [2,0]
# Explanation: The binary representation of 17 is 10001. 
# It contains 1 on the 0th and 4th indices. 
# There are 2 even and 0 odd indices.

# Example 2:
# Input: n = 2
# Output: [0,1]
# Explanation: The binary representation of 2 is 10.
# It contains 1 on the 1st index. 
# There are 0 even and 1 odd indices.

# Constraints:
# 1 <= n <= 1000

class Solution:
    def evenOddBit(self, n: int) -> [int]:
        bin_string = bin(n)
        binary_string = bin_string[2::]
        answer = [0,0]
        index = 0
        for i in range(len(binary_string) - 1, -1, -1):
            if binary_string[i] == "1":
                if index % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1
            index += 1
        return answer

solution = Solution()
print(solution.evenOddBit(n = 17))
print(solution.evenOddBit(n=2))