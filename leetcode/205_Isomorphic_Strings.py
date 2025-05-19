# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        memo_s = {}
        memo_t = {}

        for i in range(len(s)):
            if s[i] not in memo_s:
                memo_s[s[i]] = t[i]
            else:
                if memo_s[s[i]] != t[i]:
                    return False
            
            if t[i] not in memo_t:
                memo_t[t[i]] = s[i]
            else:
                if memo_t[t[i]] != s[i]:
                    return False
        
        return True
    

# Practice:
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}  # maps s → t
        t_to_s = {}  # maps t → s

        for char_s, char_t in zip(s, t):
            # Check s → t direction
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False  # s is mapped to a different t than expected
            else:
                s_to_t[char_s] = char_t

        # Check t → s direction
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False  # t is mapped to a different s than expected
            else:
                t_to_s[char_t] = char_s

        return True