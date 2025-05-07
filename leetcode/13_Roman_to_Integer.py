# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Constraints:
# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        answer = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and s[i] == "I":
                if s[i + 1] == "V":
                    answer += 4
                    i += 2
                elif s[i + 1] == "X":
                    answer += 9
                    i += 2
                else:
                    answer += roman_dict[s[i]]
                    i += 1
            elif i < len(s) - 1 and s[i] == "X":
                if s[i + 1] == "L":
                    answer += 40
                    i += 2
                elif s[i + 1] == "C":
                    answer += 90
                    i += 2
                else:
                    answer += roman_dict[s[i]]
                    i += 1
            elif i < len(s) - 1 and s[i] == "C":
                if s[i + 1] == "D":
                    answer += 400
                    i += 2
                elif s[i + 1] == "M":
                    answer += 900
                    i += 2
                else:
                    answer += roman_dict[s[i]]
                    i += 1
            else:
                answer += roman_dict[s[i]]
                i += 1

        return answer
    
solution = Solution()
print(solution.romanToInt(s = "III"))
print(solution.romanToInt(s = "LVIII"))
print(solution.romanToInt(s = "MCMXCIV"))


# Practice
class Solution:
    def romanToInt(self, s: str) -> int:
        integer_answer = 0

        dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        index = 0

        while index < len(s):
            if s[index] == "I":
                if index < len(s) - 1:
                    if s[index + 1] == "V":
                        integer_answer += 4
                        index += 2
                    elif s[index + 1] == "X":
                        integer_answer += 9
                        index += 2
                    else:
                        integer_answer += dictionary[s[index]]
                        index += 1
                else:
                    integer_answer += dictionary[s[index]]
                    index += 1
            elif s[index] == "X":
                if index < len(s) - 1:
                    if s[index + 1] == "L":
                        integer_answer += 40
                        index += 2
                    elif s[index + 1] == "C":
                        integer_answer += 90
                        index += 2
                    else:
                        integer_answer += dictionary[s[index]]
                        index += 1
                else:
                    integer_answer += dictionary[s[index]]
                    index += 1
            elif s[index] == "C":
                if index < len(s) - 1:
                    if s[index + 1] == "D":
                        integer_answer += 400
                        index += 2
                    elif s[index + 1] == "M":
                        integer_answer += 900
                        index += 2
                    else:
                        integer_answer += dictionary[s[index]]
                        index += 1
                else:
                    integer_answer += dictionary[s[index]]
                    index += 1
            else:
                integer_answer += dictionary[s[index]]
                index += 1

        return integer_answer