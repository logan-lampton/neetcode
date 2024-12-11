# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

# Constraints:
# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def create_hashmap(string):
            hashmap = {}
            for char in string:
                if char not in hashmap:
                    hashmap[char] = 1
                else:
                    hashmap[char] += 1
            return hashmap
        s1_hashmap = create_hashmap(s1)

        s2_hashmap = {}
        
        for i in range(len(s2)):
            if s2[i] not in s2_hashmap:
                s2_hashmap[s2[i]] = 1
            else:
                s2_hashmap[s2[i]] += 1

            if i >= len(s1):
                char_to_remove = s2[i - len(s1)]
                s2_hashmap[char_to_remove] -= 1
                if s2_hashmap[char_to_remove] == 0:
                    del s2_hashmap[char_to_remove]
            
            if s2_hashmap == s1_hashmap:
                return True
        
        return False
    

solution = Solution()
print(solution.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(solution.checkInclusion(s1 = "ab", s2 = "eidboaoo"))