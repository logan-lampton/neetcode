# Reverse bits of a given 32 bits unsigned integer.

# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.

# Constraints:
# The input must be a binary string of length 32


class Solution:
    def reverseBits(self, n: int) -> int:
        binary_num = bin(n)[2:]
        backwards_binary = ""
        for i in range(len(binary_num) - 1, -1, -1):
            backwards_binary += binary_num[i]
        num_zeros = 32 - len(backwards_binary)
        zeros = ""
        while num_zeros:
            zeros += "0"
            num_zeros -= 1
        full_num = backwards_binary + zeros
        return int(full_num, 2)

solution = Solution()
print(solution.reverseBits(n = int("00000010100101000001111010011100", 2)))
print(solution.reverseBits(n = int("11111111111111111111111111111101", 2)))