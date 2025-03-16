# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        left = 0
        result = ""

        while left < len(strs[0]):
            for word in strs:
                if left >= len(word) or word[left] != strs[0][left]:
                    return result
            result += strs[0][left]
            left += 1

        return result

# Practice
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        first_word = strs[0]
        min_prefix_len = len(strs[0])
        min_prefix = ""
        cur_prefix = ""

        for i in range(1, len(strs)):
            word = strs[i]
            cur_prefix = ""
            for i in range(min(len(word), len(first_word))):
                if first_word[i] == word[i]:
                    cur_prefix += word[i]
                else:
                    break
            if cur_prefix == "":
                return ""
            elif min_prefix == "":
                min_prefix = cur_prefix
            else:
                if len(cur_prefix) < len(min_prefix):
                    min_prefix = cur_prefix
        
        return min_prefix