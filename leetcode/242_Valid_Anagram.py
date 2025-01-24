# Given two strings s and t, return true if t is an 
# anagram
#  of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        def create_dict(string, dictionary):
            for char in string:
                if char not in dictionary:
                    dictionary[char] = 1
                else:
                    dictionary[char] += 1

        create_dict(s, s_dict)
        create_dict(t, t_dict)

        def compare_dicts(dictionary1, dictionary2):
            for key, value in dictionary1.items():
                if key not in dictionary2:
                    return False
                elif dictionary1[key] != dictionary2[key]:
                    return False
            return True
        
        return compare_dicts(s_dict, t_dict) and compare_dicts(t_dict, s_dict)
    

solution = Solution()
print(solution.isAnagram(s = "anagram", t = "nagaram"))
print(solution.isAnagram(s = "rat", t = "car"))