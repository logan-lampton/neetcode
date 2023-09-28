# You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

# If the character read is a letter, that letter is written onto the tape.
# If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
# Given an integer k, return the kth letter (1-indexed) in the decoded string.

# Example 1:
# Input: s = "leet2code3", k = 10
# Output: "o"
# Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
# The 10th letter in the string is "o".

# Example 2:
# Input: s = "ha22", k = 5
# Output: "h"
# Explanation: The decoded string is "hahahaha".
# The 5th letter is "h".

# Example 3:
# Input: s = "a2345678999999999999999", k = 1
# Output: "a"
# Explanation: The decoded string is "a" repeated 8301530446056247680 times.
# The 1st letter is "a".


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        # The constructed string will often be very long, so we want to use reverse traversal to grab the kth element, rather than building the string

        length = 0
        i = 0

        # solving the length of the string we are looking at
        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1

        # loop backwards from the last element to -1 (not inclusive), decrementing by 1 each time
        for j in range(i - 1, -1, -1):
            # set the char to be the current element in s at j index
            char = s[j]
            # if that char is a digit, divide the length by that digit (since the digit multiplied the original length)
            if char.isdigit():
                # floor division by the int of the digit (which is in a string)
                length //= int(char)
                # k == modulo of k / length
                k %= length
            # if the element isn't a digit, if k is 0 or k == our current length, return the char as the answer
            else:
                if k == 0 or k == length:
                    return char
                # if not k, then we reduce length by 1 and continue
                length -= 1

        # approach to build out the string will NOT work
        # tape = []

        # for char in s:
        #     if char.lower() in "abcdefghijklmnopqrstuvwxyz":
        #         tape.append(char)
        #     if char in "123456789":
        #         print(int(char))
        #         # print(char)
        #         # current_tape = tape
        #         # tape.append(current_tape)
        #     #     tape.extend(tape * (int(char) - 1))

        # print(tape)

        # if k > 0 and k <= len(tape):
        #     return tape[k - 1]
