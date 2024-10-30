# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...

# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# Example 3:
# Input: columnTitle = "ZY"
# Output: 701

# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"]


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        for char in columnTitle:
            # the number is worth the ord value of the character - the ord value of A + 1
            # For example, ord('A') - ord('A') would be 0, and we want 1 to represent that A is column 1
            cur_ord_num = (ord(char) - ord('A')) + 1
            # There are 26 letters in the alphabet. So ZY, means we got through AB, AC, AD, etc. each worth 26
            answer = answer * 26 + cur_ord_num
        return answer
    

solution = Solution()
print(solution.titleToNumber(columnTitle = "A"))
print(solution.titleToNumber(columnTitle = "AB"))
print(solution.titleToNumber(columnTitle = "ZY"))