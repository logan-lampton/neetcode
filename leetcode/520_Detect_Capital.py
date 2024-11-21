# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# Example 1:
# Input: word = "USA"
# Output: true

# Example 2:
# Input: word = "FlaG"
# Output: false

# Constraints:
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        first_letter_capital = False
        if word[0].isupper():
            first_letter_capital = True
        lower_found = False
        second_capital_found = False

        for i in range(1, len(word)):
            if word[i].isupper():
                second_capital_found = True
                if first_letter_capital == False:
                    return False
                if lower_found:
                    return False
            elif word[i].islower():
                lower_found = True
                if second_capital_found:
                    return False
                    
        return True


solution = Solution()
print(solution.detectCapitalUse(word="USA"))
print(solution.detectCapitalUse(word = "FlaG"))
print(solution.detectCapitalUse(word="mL"))