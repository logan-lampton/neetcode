# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

# The frequency of a letter x is the number of times it occurs in the string.

# Example 1:
# Input: word1 = "aaaa", word2 = "bccb"
# Output: false
# Explanation: There are 4 'a's in "aaaa" but 0 'a's in "bccb".
# The difference is 4, which is more than the allowed 3.

# Example 2:
# Input: word1 = "abcdeef", word2 = "abaaacc"
# Output: true
# Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
# - 'a' appears 1 time in word1 and 4 times in word2. The difference is 3.
# - 'b' appears 1 time in word1 and 1 time in word2. The difference is 0.
# - 'c' appears 1 time in word1 and 2 times in word2. The difference is 1.
# - 'd' appears 1 time in word1 and 0 times in word2. The difference is 1.
# - 'e' appears 2 times in word1 and 0 times in word2. The difference is 2.
# - 'f' appears 1 time in word1 and 0 times in word2. The difference is 1.

# Example 3:
# Input: word1 = "cccddabba", word2 = "babababab"
# Output: true
# Explanation: The differences between the frequencies of each letter in word1 and word2 are at most 3:
# - 'a' appears 2 times in word1 and 4 times in word2. The difference is 2.
# - 'b' appears 2 times in word1 and 5 times in word2. The difference is 3.
# - 'c' appears 3 times in word1 and 0 times in word2. The difference is 3.
# - 'd' appears 2 times in word1 and 0 times in word2. The difference is 2.

# Constraints:
# n == word1.length == word2.length
# 1 <= n <= 100
# word1 and word2 consist only of lowercase English letters.


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1_dict = {}
        word2_dict = {}

        def make_dict(string, dictionary):
            for char in string:
                if char not in dictionary:
                    dictionary[char] = 1
                else:
                    dictionary[char] += 1
        
        make_dict(word1, word1_dict)
        make_dict(word2, word2_dict)

        def compare_dicts(dictionary, other_dictionary):
            for key, value in dictionary.items():
                if key not in other_dictionary:
                    if value > 3:
                        return False
                else:
                    if abs(value - other_dictionary[key]) > 3:
                        return False 
            return True
        
        comparing_word1 = compare_dicts(word1_dict, word2_dict)
        comparing_word2 = compare_dicts(word2_dict, word1_dict)

        return comparing_word1 and comparing_word2

# class Solution:
#     def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
#         word1_dict = {}
#         for char in word1:
#             if char not in word1_dict:
#                 word1_dict[char] = 1
#             else:
#                 word1_dict[char] += 1
        
#         word2_dict = {}
#         for char in word2:
#             if char not in word2_dict:
#                 word2_dict[char] = 1
#             else:
#                 word2_dict[char] += 1
        
#         for key, value in word1_dict.items():
#             if key not in word2_dict and value > 3:
#                 return False
#             elif key in word2_dict:
#                 if word2_dict[key] > value + 3 or word2_dict[key] < value - 3:
#                     return False
        
#         for key, value in word2_dict.items():
#             if key not in word1_dict and value > 3:
#                 return False
        
#         return True
    
solution = Solution()
print(solution.checkAlmostEquivalent(word1 = "aaaa", word2 = "bccb"))
print(solution.checkAlmostEquivalent(word1 = "abcdeef", word2 = "abaaacc"))