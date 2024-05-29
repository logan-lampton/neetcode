# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

# Return the number of special letters in word.

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters in word are 'a', 'b', and 'c'.

# Example 2:
# Input: word = "abc"
# Output: 0
# Explanation:
# No character in word appears in uppercase.

# Example 3:
# Input: word = "abBCab"
# Output: 1
# Explanation:
# The only special character in word is 'b'.

# Constraints:
# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen_upper = set()
        seen_lower = set()
        special_amount = 0
        for char in set(word):
            if char.islower():
                seen_lower.add(char)
            else:
                seen_upper.add(char)
        for char in seen_upper:
            if char.lower() in seen_lower:
                special_amount += 1

        return special_amount

solution = Solution()
print(solution.numberOfSpecialChars(word="aaAbcBC"))
print(solution.numberOfSpecialChars(word="abBCab"))