# Given a string s, return the number of segments in the string.

# A segment is defined to be a contiguous sequence of non-space characters.

# Example 1:
# Input: s = "Hello, my name is John"
# Output: 5
# Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

# Example 2:
# Input: s = "Hello"
# Output: 1
 
# Constraints:
# 0 <= s.length <= 300
# s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
# The only space character in s is ' '.


class Solution:
    def countSegments(self, s: str) -> int:

        num_segments = 0
        inside_segment = False

        for char in s:
            if char != " " and not inside_segment:
                num_segments += 1
                inside_segment = True
            elif char == " " and inside_segment:
                inside_segment = False
            
        return num_segments


solution = Solution()
print(solution.countSegments(s = "Hello, my name is John"))
print(solution.countSegments(s = "Hello"))
print(solution.countSegments(s = "                "))
print(solution.countSegments(s = "Of all the gin joints in all the towns in all the world,   "))