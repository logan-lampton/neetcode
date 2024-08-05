# Given an integer n, add a dot (".") as the thousands separator and return it in string format.

# Example 1:
# Input: n = 987
# Output: "987"

# Example 2:
# Input: n = 1234
# Output: "1.234"

# Constraints:
# 0 <= n <= 231 - 1

class Solution:
    def thousandSeparator(self, n: int) -> str:
        string_n = str(n)
        b_answer = ""
        answer = ""
        characters = 0
        for i in range(len(string_n) - 1, -1, -1):
            if characters == 3:
                b_answer += "."
                characters = 0
            b_answer += string_n[i]
            characters += 1
        for i in range(len(b_answer) -1, -1, -1):
            answer += b_answer[i]

        return answer
    
solution = Solution()
print(solution.thousandSeparator(n = 987))
print(solution.thousandSeparator(n = 1234))