# A word is considered valid if:

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.
# You are given a string word.
# Return true if word is valid, otherwise, return false.

# Notes:
# 'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
# A consonant is an English letter that is not a vowel.

# Example 1:
# Input: word = "234Adas"
# Output: true
# Explanation:
# This word satisfies the conditions.

# Example 2:
# Input: word = "b3"
# Output: false
# Explanation:
# The length of this word is fewer than 3, and does not have a vowel.

# Example 3:
# Input: word = "a3$e"
# Output: false
# Explanation:
# This word contains a '$' character and does not have a consonant.

# Constraints:
# 1 <= word.length <= 20
# word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.

class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        invalid_symbols = ['@', '#', "$"]
        contains_vowel = False
        contains_consonant = False
        for char in word:
            if char in invalid_symbols:
                return False
            elif char in vowels:
                contains_vowel = True
            elif char not in vowels and char.isalpha():
                contains_consonant = True
        return contains_vowel and contains_consonant
    
solution = Solution()
print(solution.isValid(word = "234Adas"))
print(solution.isValid(word = "b3"))
print(solution.isValid(word = "a3$e"))