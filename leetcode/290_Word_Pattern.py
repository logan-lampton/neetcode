# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
 
# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()
        if len(pattern) != len(s_split):
            return False

        pattern_dict = {}
        word_dict = {}
        
        for i in range(len(s_split)):
            if pattern[i] not in pattern_dict:
                if s_split[i] in word_dict:
                    return False
                else:
                    pattern_dict[pattern[i]] = s_split[i]
                    word_dict[s_split[i]] = pattern[i]
            else:
                if pattern_dict[pattern[i]] != s_split[i]:
                    return False
        return True