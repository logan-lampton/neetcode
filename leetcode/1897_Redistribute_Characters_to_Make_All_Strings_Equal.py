# You are given an array of strings words (0-indexed).

# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

# Return true if you can make every string in words equal using any number of operations, and false otherwise.

# Example 1:
# Input: words = ["abc","aabc","bc"]
# Output: true
# Explanation: Move the first 'a' in words[1] to the front of words[2],
# to make words[1] = "abc" and words[2] = "abc".
# All the strings are now equal to "abc", so return true.

# Example 2:
# Input: words = ["ab","a"]
# Output: false
# Explanation: It is impossible to make all the strings equal using the operation.

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


class Solution:
    def makeEqual(self, words: [str]) -> bool:
        
        len_words = len(words)
        
        if len_words == 1:
            return True
        
        hash_map = {}
        for word in words:
            for char in word:
                if char not in hash_map:
                    hash_map[char] = 1
                else:
                    hash_map[char] += 1
        
        for value in hash_map.values():
            if value % len_words != 0:
                return False
        return True


solution = Solution()
print(solution.makeEqual(words = ["abc","aabc","bc"]))
print(solution.makeEqual(words = ["ab","a"]))
print(solution.makeEqual(words = ["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]))