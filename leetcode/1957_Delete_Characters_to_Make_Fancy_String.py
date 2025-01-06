# A fancy string is a string where no three consecutive characters are equal.

# Given a string s, delete the minimum possible number of characters from s to make it fancy.

# Return the final string after the deletion. It can be shown that the answer will always be unique.

# Example 1:
# Input: s = "leeetcode"
# Output: "leetcode"
# Explanation:
# Remove an 'e' from the first group of 'e's to create "leetcode".
# No three consecutive characters are equal, so return "leetcode".

# Example 2:
# Input: s = "aaabaaaa"
# Output: "aabaa"
# Explanation:
# Remove an 'a' from the first group of 'a's to create "aabaaaa".
# Remove two 'a's from the second group of 'a's to create "aabaa".
# No three consecutive characters are equal, so return "aabaa".

# Example 3:
# Input: s = "aab"
# Output: "aab"
# Explanation: No three consecutive characters are equal, so return "aab".

# Constraints:
# 1 <= s.length <= 105
# s consists only of lowercase English letters.


class Solution:
    def makeFancyString(self, s: str) -> str:
        # start answer with the first letter
        answer = s[0]
        # count of the first letter set at 1
        count = 1

        for i in range(1, len(s)):
            # if the letter is the same as the latest letter, count goes up by 1
            if s[i] == answer[-1]:
                count += 1
                # if it's only the second of that letter in a row, we add it to the answer
                if count < 3:
                    answer += s[i]
            # if it's a different letter, add it to the answer and reset the count to 1
            else:
                answer += s[i]
                count = 1
        
        return answer
    

solution = Solution()
print(solution.makeFancyString(s = "leeetcode"))
print(solution.makeFancyString(s = "aaabaaaa"))
print(solution.makeFancyString(s = "aab"))
