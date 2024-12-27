# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# Example 1:
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.

# Example 2:
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.

# Example 3:
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

# Constraints:
# 1 <= s.length, goal.length <= 2 * 104
# s and goal consist of lowercase letters.


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            if len(set(s)) < len(s):
                return True
            return False
        
        different = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                different.append(i)
            if len(different) > 2:
                return False

        if len(different) == 2:
            if s[different[0]] == goal[different[1]] and s[different[1]] == goal[different[0]]:
                return True
        
        return False


solution = Solution()

print(solution.buddyStrings(s = "ab", goal = "ba"))
print(solution.buddyStrings(s = "ab", goal = "ab"))
print(solution.buddyStrings(s = "aa", goal = "aa"))