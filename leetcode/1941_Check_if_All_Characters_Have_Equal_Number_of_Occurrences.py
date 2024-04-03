# Given a string s, return true if s is a good string, or false otherwise.

# A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

# Example 1:
# Input: s = "abacbc"
# Output: true
# Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

# Example 2:
# Input: s = "aaabb"
# Output: false
# Explanation: The characters that appear in s are 'a' and 'b'.
# 'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = {}

        for char in s:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1

        starting_val = list(frequency.values())[0]

        for value in frequency.values():
            if value != starting_val:
                return False

        return True


solution = Solution()
print(solution.areOccurrencesEqual(s="abacbc"))
