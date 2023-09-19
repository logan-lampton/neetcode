# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard.

# In the American keyboard:
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

# Example 1:
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]

# Example 2:
# Input: words = ["omk"]
# Output: []

# Example 3:
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]


class Solution:
    def findWords(self, words: [str]) -> [str]:
        # create arrays of the keyboard rows
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        answer = []

        # loop through the words array and see if each letter is in a keyboard row
        for word in words:
            # change letters to lowercase to check against the lowercase letters in the rows
            word_lower = word.lower()
            # track what row we are on
            row = None
            # look at each character in a word
            for char in word_lower:
                # check if the character is in a row; if so, make set our current row to that row
                if char in row1:
                    if row is None:
                        row = row1
                    # if the character isn't in the row, we break, so as to not waste time checking the other characters in the word
                    elif row is not row1:
                        break
                elif char in row2:
                    if row is None:
                        row = row2
                    elif row is not row2:
                        break
                elif char in row3:
                    if row is None:
                        row = row3
                    elif row is not row3:
                        break
            else:
                # if the loop completed without breaking, meaning all characters are in the same row, append the word to the answer array
                answer.append(word)

        return answer
