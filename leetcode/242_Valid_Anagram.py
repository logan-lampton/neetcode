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


# Practice
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}

        def create_dictionary(string, dictionary):
            for char in string:
                if char not in dictionary:
                    dictionary[char] = 1
                else:
                    dictionary[char] += 1
        
        create_dictionary(s, s_hash)
        create_dictionary(t, t_hash)

        def compare_dicts(dictionary1, dictionary2):
            for key, value in dictionary1.items():
                if key not in dictionary2:
                    return False
                else:
                    if value != dictionary2[key]:
                        return False
            return True
        
        return compare_dicts(s_hash, t_hash) and compare_dicts(t_hash, s_hash)


# Practice:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def create_hash(string):
            new_hash = {}
            for char in string:
                if char not in new_hash:
                    new_hash[char] = 1
                else:
                    new_hash[char] += 1
            return new_hash
        
        s_hash = create_hash(s)
        t_hash = create_hash(t)

        def compare_hashmaps(hashmap1, hashmap2):
            for key, value in hashmap1.items():
                if key not in hashmap2:
                    print(key)
                    return False
                elif hashmap2[key] != value:
                    return False
            return True
        
        s_valid = compare_hashmaps(s_hash, t_hash)
        t_valid = compare_hashmaps(t_hash, s_hash)

        return s_valid & t_valid