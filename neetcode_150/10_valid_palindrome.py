# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Solution One
# use the built-in method to check if the char is alphanumerical
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # creating a new string uses extra memory, as does reversing it later
#         newStr = ""
#         for char in s:
#             if char.isalnum():
#                 newStr += char.lower()
#         # syntax for reversing a string
#         return newStr == newStr[::-1]


# Solution Two
# Use pointers
# Uses constant extra memory
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_pointer = 0
        r_pointer = len(s) - 1
        while l_pointer < r_pointer:
            while l_pointer < r_pointer and not self.alphaNum(s[l_pointer]):
                l_pointer += 1
            while r_pointer > l_pointer and not self.alphaNum(s[r_pointer]):
                r_pointer -= 1
            if s[l_pointer].lower() != s[r_pointer].lower():
                return False
            l_pointer, r_pointer = l_pointer + 1, r_pointer - 1
        return True

    # uses the number associated with the alphanumerical ASCII symbols
    def alphaNum(self, char):
        # check if it is an uppercase letter OR a lowercase letter OR a number
        # with return it will return either true or false
        return (ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord('9'))


solution = Solution()
print(solution.isPalindrome(s="dad"))
