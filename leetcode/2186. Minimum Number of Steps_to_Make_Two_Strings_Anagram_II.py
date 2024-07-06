# You are given two strings s and t. In one step, you can append any character to either s or t.

# Return the minimum number of steps to make s and t anagrams of each other.

# An anagram of a string is a string that contains the same characters with a different (or the same) ordering.

# Example 1:
# Input: s = "leetcode", t = "coats"
# Output: 7
# Explanation: 
# - In 2 steps, we can append the letters in "as" onto s = "leetcode", forming s = "leetcodeas".
# - In 5 steps, we can append the letters in "leede" onto t = "coats", forming t = "coatsleede".
# "leetcodeas" and "coatsleede" are now anagrams of each other.
# We used a total of 2 + 5 = 7 steps.
# It can be shown that there is no way to make them anagrams of each other with less than 7 steps.

# Example 2:
# Input: s = "night", t = "thing"
# Output: 0
# Explanation: The given strings are already anagrams of each other. Thus, we do not need any further steps.

# Constraints:
# 1 <= s.length, t.length <= 2 * 105
# s and t consist of lowercase English letters.


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        moves = 0
        for key, value in s_dict.items():
            if key not in t_dict:
                moves += value
            elif t_dict[key] > value:
                moves += (t_dict[key] - value)
        for key, value in t_dict.items():
            if key not in s_dict:
                moves += value
            elif s_dict[key] > value:
                moves += (s_dict[key] - value)
        return moves

solution = Solution()
print(solution.minSteps(s = "leetcode", t = "coats"))
print(solution.minSteps(s = "night", t = "thing"))