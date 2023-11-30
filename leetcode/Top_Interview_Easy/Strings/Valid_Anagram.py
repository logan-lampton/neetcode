# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

def isAnagram(s: str, t: str) -> bool:
    
    s_dict = {}

    for letter in s:
        if letter not in s_dict:
            s_dict[letter] = 1
        else:
            s_dict[letter] += 1
    
    for letter in t:
        if letter not in s_dict:
            return False
        else:
            s_dict[letter] -= 1
            
    for value in s_dict.values():
        if value != 0:
            return False
    
    return True