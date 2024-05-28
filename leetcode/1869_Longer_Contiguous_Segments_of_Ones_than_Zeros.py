# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s, or return false otherwise.

# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

# Example 1:
# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.

# Example 2:
# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.

# Example 3:
# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.

# Constraints:
# 1 <= s.length <= 100
# s[i] is either '0' or '1'.

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_one = 0
        longest_zero = 0
        right = 0
        while right < len(s):
            if s[right] == "0":
                curr_zero = 0
                while right < len(s) and s[right] == "0":
                    curr_zero += 1
                    right += 1
                longest_zero = max(longest_zero, curr_zero)
            else:
                curr_one = 0
                while right < len(s) and s[right] == "1":
                    curr_one += 1
                    right += 1
                longest_one = max(longest_one, curr_one)

        return longest_one > longest_zero

solution = Solution()
print(solution.checkZeroOnes(s="1101"))
print(solution.checkZeroOnes(s="110100010"))