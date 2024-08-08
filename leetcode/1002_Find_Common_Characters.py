# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


class Solution:
    def commonChars(self, words: [str]) -> [str]:
        dictionary = {}
        for letter in words[0]:
            if letter not in dictionary:
                dictionary[letter] = words[0].count(letter)
        
        for word in words[1:]:
            for letter in dictionary.keys():
                dictionary[letter] = min(dictionary[letter], word.count(letter))
        
        answer = []
        
        for key, value in dictionary.items():
            for _ in range(value):
                answer.append(key)
        return answer


solution = Solution()
print(solution.commonChars(words = ["bella","label","roller"]))
print(solution.commonChars(words = ["cool","lock","cook"]))