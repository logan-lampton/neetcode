# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s

class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        l1 = 0
        l2 = 0
        while l1 < len(word1) or l2 < len(word2):
            if l1 < len(word1):
                result += word1[l1]
                l1 += 1
            if l2 < len(word2):
                result += word2[l2]
                l2 += 1
        return result
