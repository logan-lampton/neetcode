# A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

# A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

# For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
# Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

# Example 1:
# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

# Example 2:
# Input: s = "Myself2 Me1 I4 and3"
# Output: "Me Myself and I"
# Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.

# Constraints:
# 2 <= s.length <= 200
# s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
# The number of words in s is between 1 and 9.
# The words in s are separated by a single space.
# s contains no leading or trailing spaces.

# First Attempt


class Solution:
    def sortSentence(self, s: str) -> str:

        word_dict = {}

        number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        left = 0
        right = 0

        for char in s:
            if char not in number:
                right += 1
            elif not word_dict:
                word_dict[int(char)] = s[left:right]
                right += 1
                left = right
            else:
                word_dict[int(char)] = s[left + 1 : right]
                right += 1
                left = right

        answer = ""

        sorted_dict = sorted(word_dict.items())

        for i, t_pair in enumerate(sorted_dict):
            answer += t_pair[1] + " "

        return answer[0:-1]


# Improved approach
class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()

        answer = [None] * len(words)

        for word in words:
            # index must start at 0, thus - 1 to the number in the word
            index = int(word[-1]) - 1
            answer[index] = word[:-1]

        return " ".join(answer)
