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
