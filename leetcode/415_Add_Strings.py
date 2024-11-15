# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"

# Example 2:
# Input: num1 = "456", num2 = "77"
# Output: "533"

# Example 3:
# Input: num1 = "0", num2 = "0"
# Output: "0"

# Constraints:
# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        def char_to_int(char):
            # Map character to integer without using int()
            return ord(char) - ord('0')

        def string_to_int(num):
            int_num = 0
            for char in num:
                # Shift previous digits left by multiplying by 10
                int_num = int_num * 10 + char_to_int(char)
            return int_num

        def int_to_string(num):
            if num == 0:
                return "0"

            result = []
            while num > 0:
                # Get the last digit and convert it to a character
                result.append(chr((num % 10) + ord('0')))
                num //= 10

            # Reverse the result to get the correct order
            return ''.join(result[::-1])

        # Convert strings to integers, perform the addition, then back to string
        full_sum = string_to_int(num1) + string_to_int(num2)
        return int_to_string(full_sum)

solution = Solution()
print(solution.addStrings(num1 = "11", num2 = "123"))
print(solution.addStrings(num1 = "456", num2 = "77"))
print(solution.addStrings(num1 = "0", num2 = "0"))