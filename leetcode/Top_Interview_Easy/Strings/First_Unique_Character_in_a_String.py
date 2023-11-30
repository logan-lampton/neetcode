# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
# Input: s = "leetcode"
# Output: 0

# Example 2:
# Input: s = "loveleetcode"
# Output: 2

# Example 3:
# Input: s = "aabb"
# Output: -1

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

def firstUniqChar(s) -> int:
    
    char_dict = {}

    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = [1, [i]]

        else:
            char_dict[s[i]][0] += 1
            char_dict[s[i]][1].append(i)
            
    for key, value in char_dict.items():
        if value[0] == 1:
            return value[1][0]
    
    return - 1