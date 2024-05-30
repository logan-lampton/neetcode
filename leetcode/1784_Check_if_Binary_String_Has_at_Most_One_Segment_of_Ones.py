# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

# Example 1:
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.

# Example 2:
# Input: s = "110"
# Output: true

# Constraints:
# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_zero = 0
        for i in range(len(s)):
            if s[i] == "0":
                found_zero += 1
            if found_zero > 0 and s[i] == "1":
                return False
        return True

solution = Solution()
print(solution.checkOnesSegment(s="1001"))
print(solution.checkOnesSegment(s="110"))