# Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

# You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

# Example 1:
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.

# Example 2:
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed output.

# Constraints:
# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:

        name_index = 0
        typed_index = 0

        while name_index < len(name) and typed_index < len(typed):
            if name[name_index] == typed[typed_index]:
                name_index += 1
                typed_index += 1
            elif typed_index > 0 and typed[typed_index] == typed[typed_index - 1]:
                typed_index += 1
            else:
                return False
        
        if name_index != len(name):
            return False
        
        while typed_index < len(typed):
            if typed[typed_index] != name[-1]:
                return False
            typed_index += 1
        
        return True
    
solution = Solution()
print(solution.isLongPressedName(name = "alex", typed = "aaleex"))
print(solution.isLongPressedName(name = "saeed", typed = "ssaaedd"))