# You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

# You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

# Return the reformatted string or return an empty string if it is impossible to reformat the string.

# Example 1:
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

# Example 2:
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by digits.

# Example 3:
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by characters.

# Constraints:
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.

class Solution:
    def reformat(self, s: str) -> str:
        if len(s) == 1:
            return s

        answer = ""

        letters = []
        digits = []

        for char in s:
            if char.isalpha():
                letters.append(char)
            if char.isdigit():
                digits.append(char)
        
        if len(letters) > len(digits) + 1 or len(digits) > len(letters) + 1:
            return ""
        
        min_length = min(len(letters), len(digits))

        for i in range(min_length):
            answer += letters[i]
            answer += digits[i]
        
        if len(letters) > len(digits):
            if answer[-1].isalpha():
                answer = letters[-1] + answer
            else:
                answer += letters[-1]
        elif len(digits) > len(letters):
            if answer[-1].isdigit():
                answer = digits[-1] + answer
            else:
                answer += digits[-1]
        
        return answer

solution = Solution()
print(solution.reformat(s = "a0b1c2"))
print(solution.reformat(s = "leetcode"))
print(solution.reformat(s = "1229857369"))