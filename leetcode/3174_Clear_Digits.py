# You are given a string s.

# Your task is to remove all digits by doing this operation repeatedly:

# Delete the first digit and the closest non-digit character to its left.
# Return the resulting string after removing all digits.

# Example 1:
# Input: s = "abc"
# Output: "abc"
# Explanation:
# There is no digit in the string.

# Example 2:
# Input: s = "cb34"
# Output: ""
# Explanation:
# First, we apply the operation on s[2], and s becomes "c4".
# Then we apply the operation on s[1], and s becomes "".

# Constraints:
# 1 <= s.length <= 100
# s consists only of lowercase English letters and digits.
# The input is generated such that it is possible to delete all digits.

class Solution:
    def clearDigits(self, s: str) -> str:
        s_list = list(s)
        i = 0
        while i < len(s_list):
            if s_list[i].isdigit():
                if i > 0:
                    s_list.pop(i - 1)
                    i -= 1
                s_list.pop(i)
            else:
                i += 1
        return "".join(s_list)

solution = Solution()
print(solution.clearDigits(s="abc"))
print(solution.clearDigits(s = "cb34"))
print(solution.clearDigits(s="c3po"))


# Practice
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        answer = ''

        for char in s:
            if char.isalpha():
                stack.append(char)
            else:
                if stack:
                    stack.pop()
        
        return ''.join(stack)