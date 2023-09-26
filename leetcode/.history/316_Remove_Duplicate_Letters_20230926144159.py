# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
# the smallest in lexicographical order among all possible results.

# Example 1:
# Input: s = "bcabc"
# Output: "abc"

# Example 2:
# Input: s = "cbacdcbc"
# Output: "acdb"


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letter_dict = {}

        for letter in s:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter] += 1

        seen = set()

        stack = []

        for letter in s:
            letter_dict[letter] -= 1
            if letter in seen:
                continue
            while stack and letter < stack[-1] and letter_dict[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(letter)
            seen.add(letter)

        return "".join(stack)
