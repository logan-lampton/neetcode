# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "hello"
# Output: "holle"

# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

# Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = 'aeiouAEIOU'

        found_vowels = ""

        for i in range(len(s)):
            if s[i] in vowels:
                found_vowels += s[i]

        answer = ""
        found_i = -1
        
        for i in range(len(s)):
            if s[i] in vowels:
                answer += found_vowels[found_i]
                found_i -= 1
            else:
                answer += s[i]

        return answer


solution = Solution()
print(solution.reverseVowels(s = "hello"))
print(solution.reverseVowels(s = "leetcode"))