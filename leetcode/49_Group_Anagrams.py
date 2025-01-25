# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.


class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:

        strings_hashtable = {}

        for string in strs:
            sorted_string_array = sorted(string)
            sorted_string = ''.join(sorted_string_array)
            
            if sorted_string not in strings_hashtable:
                strings_hashtable[sorted_string] = []
            
            strings_hashtable[sorted_string].append(string)

        answer = []

        for value in strings_hashtable.values():
            answer.append(value)
        
        return answer


solution = Solution()
print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(solution.groupAnagrams(strs = [""]))
print(solution.groupAnagrams(strs = ["a"]))