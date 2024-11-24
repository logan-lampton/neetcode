# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

# Constraints:
# 1 <= s.length <= 104
# s consists of only lowercase English letters.
# 1 <= k <= 104


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        formatted_s = ""

        for i in range(0, len(s), k + k):
            substring = s[i: i + k + k]
            formatted_s += substring[0:k][::-1] + substring[k:]

        return formatted_s


solution = Solution()
print(solution.reverseStr(s = "abcdefg", k = 2))
print(solution.reverseStr(s = "abcdefg", k = 4))