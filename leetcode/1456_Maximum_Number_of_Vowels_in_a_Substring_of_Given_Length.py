# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        vowels = "aeiou"
        cur_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                cur_vowels += 1
                max_vowels = max(max_vowels, cur_vowels)
        left = 0
        for right in range(k, len(s)):
            if s[right] in vowels:
                cur_vowels += 1
            if s[left] in vowels and k > 1:
                cur_vowels -= 1
            left += 1
            max_vowels = max(max_vowels, cur_vowels)
            if max_vowels == k:
                break
        return max_vowels

solution = Solution()
print(solution.maxVowels(s = "abciiidef", k = 3))
print(solution.maxVowels(s= "aeiou", k = 2))
print(solution.maxVowels(s = "leetcode", k = 3))