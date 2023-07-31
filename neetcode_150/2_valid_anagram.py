# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        # Convert strings to lists to enable element removal
        s_list = list(s)
        t_list = list(t)

        for char in s_list:
            if char in t_list:
                t_list.remove(char)
            else:
                return False

        # If t_list is empty, all characters in s have matched and they are anagrams
        if not t_list:
            return True
        else:
            return False
