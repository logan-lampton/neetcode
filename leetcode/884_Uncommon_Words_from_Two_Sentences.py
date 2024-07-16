# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# Example 1:
# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]

# Constraints:
# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> [str]:
        s1_dict = {}
        s2_dict = {}
        s1_list = s1.split()
        s2_list = s2.split()
        for word in s1_list:
            if word not in s1_dict:
                s1_dict[word] = 1
            else:
                s1_dict[word] += 1
        for word in s2_list:
            if word not in s2_dict:
                s2_dict[word] = 1
            else:
                s2_dict[word] += 1

        answer = []
        for key, value in s1_dict.items():
            if key not in s2_dict and value == 1:
                answer.append(key)
        for key, value in s2_dict.items():
            if key not in s1_dict and value == 1:
                answer.append(key)
        
        return answer

solution = Solution()
print(solution.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(solution.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))