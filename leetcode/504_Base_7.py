# Given an integer num, return a string of its base 7 representation.

# Example 1:
# Input: num = 100
# Output: "202"

# Example 2:
# Input: num = -7
# Output: "-10"

# Constraints:
# -107 <= num <= 107


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        negative = False
        if num < 0:
            negative = True
            num = num * -1
        remainders = []
        while num:
            remainders.append(num % 7)
            num = num // 7
        
        answer = ""
        for i in range(len(remainders) - 1, -1, -1):
            answer += str(remainders[i])
        
        if negative:
            return "-" + answer
        return answer

solution = Solution()
print(solution.convertToBase7(num = 100))
print(solution.convertToBase7(num = -7))