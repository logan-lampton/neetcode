# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without
# disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # set two pointers to 0
        left = 0
        right = 0

        # while the left pointer is less than the length of s and the right pointer is less than the length of t, go through those lists
        while left < len(s) and right < len(t):
            # if s list at right pointer index is equal to t list at right pointer index, add one to the left pointer
            # this shows that the first letter in s, matched a letter in t, then we look for the second letter in s
            if s[left] == t[right]:
                left += 1
            # we always increase the right pointer by one, as we go through the full t list
            right += 1
        # if left pointer made it all the way through the length of list s, then we return True, False if left != len(s)
        return left == len(s)
