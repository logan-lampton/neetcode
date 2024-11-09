# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0

# Constraints:
# 0 <= num <= 231 - 1


class Solution:
    def addDigits(self, num: int) -> int:

        def reduce_num(number):
            new_sum = 0
            for digit in str(number):
                new_sum += int(digit)
            return new_sum

        while num >= 10:
            num = reduce_num(num)
        
        return num
    

solution = Solution()
print(solution.addDigits(num = 38))