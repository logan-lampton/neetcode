# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Example 2:
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1


# Practice:
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                haystack_index = i
                needle_index = 0
                while haystack_index <= len(haystack) - 1 and haystack[haystack_index] == needle[needle_index]:
                    if needle_index == len(needle) - 1:
                        return i
                    haystack_index += 1
                    needle_index += 1
        
        return -1