# Reversing an integer means to reverse all its digits.

# For example, reversing 2021 gives 1202. Reversing 12300 gives 321 as the leading zeros are not retained.
# Given an integer num, reverse num to get reversed1, then reverse reversed1 to get reversed2. Return true if reversed2 equals num. Otherwise return false.

# Example 1:
# Input: num = 526
# Output: true
# Explanation: Reverse num to get 625, then reverse 625 to get 526, which equals num.

# Example 2:
# Input: num = 1800
# Output: false
# Explanation: Reverse num to get 81, then reverse 81 to get 18, which does not equal num.

# Example 3:
# Input: num = 0
# Output: true
# Explanation: Reverse num to get 0, then reverse 0 to get 0, which equals num.

# Constraints:
# 0 <= num <= 106


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        string_num = str(num)
        reversed1 = ""
        for i in range(len(string_num) - 1, -1, -1):
            if reversed1 == "" and string_num[i] == "0":
                continue
            else:
                reversed1 += string_num[i]
        if reversed1 == "":
            reversed1 = "0"

        reversed2 = ""
        for i in range(len(reversed1) - 1, -1, -1):
            reversed2 += reversed1[i]

        return str(num) == reversed2


solution = Solution()
print(solution.isSameAfterReversals(num=1800))
print(solution.isSameAfterReversals(num=52678))
