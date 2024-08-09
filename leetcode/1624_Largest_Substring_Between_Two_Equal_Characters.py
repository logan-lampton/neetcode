# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.

# Example 2:
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".

# Example 3:
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.

# Constraints:
# 1 <= s.length <= 300
# s contains only lowercase English letters.


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dictionary = {}
        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = [i]
            else:
                dictionary[s[i]].append(i)
        
        longest = 0
        longest_val = 0
        for value in dictionary.values():
            longest_val = max(longest_val, len(value))
            longest = max(longest, max(value) - min(value) - 1)
        if longest_val == 1:
            longest = -1
        return longest


solution = Solution()
print(solution.maxLengthBetweenEqualCharacters(s = "aa"))
print(solution.maxLengthBetweenEqualCharacters(s = "abca"))
print(solution.maxLengthBetweenEqualCharacters(s = "cbzxy"))