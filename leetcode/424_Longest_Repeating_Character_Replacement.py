# You are given a string s and an integer k. You can choose any character of the string and change it to any other
# uppercase English character. You can perform this operation at most k times.
#
# Return the length of the longest substring containing the same letter you can get after performing the above
# operations.
#
#
#
# Example 1:
#
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
#
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exist other ways to archive this answer too.

def characterReplacement(s, k):
    # start index of the current substring
    length = 0
    # dictionary to store the frequency of the characters
    frequency = {}
    # variable that stores the length of the longest substring with the most "k" replacements
    max_count = 0

    # check for the frequency of each letter and save to the dictionary "frequency"
    for i in range(len(s)):
        # Check if "s[i]" is not in the frequency dictionary. If not, add it and set its frequency to 0.
        if not s[i] in frequency:
            frequency[s[i]] = 0
        # Increment the frequency of the current character in the frequency dictionary.
        frequency[s[i]] += 1

        # Calculate cells_count
        # For each character "s[i]", calculate the number of characters between the currenct position "i" and the
        # starting position "length". This represents the size of the currenct substring
        cells_count = i - length + 1

        # Check if the current substring is valid
        # if the range of the substring ("cells count") minus the frequency of the letter is less than or equal to "k",
        # we can replace the letters in the substring that are not the most frequent; OTHERWISE, we would not have
        # enough "k" to make the switch
        if cells_count - max(frequency.values()) <= k:
            # set the max_count to either stay the same, or become the new largest substring count
            max_count = max(max_count, cells_count)

        # If the substring is NOT valid
        else:
            # reduce the frequency of the character at index "length" in the "frequency" dictionary by 1
            frequency[s[length]] -= 1
            # If the frequency of the character becomes 0...
            if not frequency[s[length]]:
                # ...remove the character from the "frequency" dictionary
                frequency.pop(s[length])
            # Increment the "length" variable to move to the start of the substring one position to the right
            length += 1

    # After the loop, return "max_count" as the result
    return max_count


# Quick test call
print(characterReplacement(s="AABABBA", k=1))
