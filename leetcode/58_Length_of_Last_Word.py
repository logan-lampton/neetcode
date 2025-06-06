# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
#  consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # add logic to handle if there is no s string
        if not s:
            return 0

        # split the s string into separate "words" in an array
        word_array = s.split()

        # using this new array, grab the last element in the array
        last_word = word_array[-1]

        # return the length of the last word
        return len(last_word)


# Practice
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_array = s.split()

        for i in range(len(s_array) - 1, -1, -1):
            return len(s_array[i])

# Practice:
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and length > 0:
                break
            elif s[i] != " ":
                length += 1

        return length