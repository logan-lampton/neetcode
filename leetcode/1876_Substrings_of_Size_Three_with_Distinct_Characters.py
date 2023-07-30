# A string is good if there are no repeated characters.
#
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
#
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
#
# A substring is a contiguous sequence of characters in a string.
#
#
#
# Example 1:
#
# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
# The only good substring of length 3 is "xyz".
# Example 2:
#
# Input: s = "aababcabc"
# Output: 4
# Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
# The good substrings are "abc", "bca", "cab", and "abc".

class Solution(object):
    def countGoodSubstrings(self, s):
        good_number = 0

        for element in range(len(s) - 2):
            # create a substring that is a slice of string (s) from the element's index to the element's index + 3
            substring = s[element: element + 3]
            # if we convert the substring into a set, if will automatically remove any elements that are the same
            # if the length of the set is 3, it means there are 3 unique elements; if so, add 1 to good_number
            if len(set(substring)) == 3:
                good_number += 1

        return good_number
