# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].


class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        # Faster approach:
        # loop backward:
        # begin at the length of the digits - 1
        # continue until the 0 index (written as -1, as it excludes the last number)
        # decrease by 1 each loop
        for i in range(len(digits) - 1, -1, -1):
            # if the digit encountered is a 9, change it to 0
            if digits[i] == 9:
                digits[i] = 0
            # otherwise, the value of the digit is increased by 1; then the digits are returned
            else:
                digits[i] += 1
                return digits
        # if we ran into all 9s, so didn't yet return the digits, we would run this
        # this constructs a new list by concatenating two lists; a list of 1 + all the digits
        # in this way the return is 1 with an 0s behind it for each of the 9s in th digits
        return [1] + digits

        # ----------

        # Naive Approach:
        large_integer = 0

        right = len(digits)

        while right > 0:
            for i in range(len(digits)):
                large_digit = digits[i] * (10 ** (right - 1))
                large_integer += large_digit
                right -= 1

        final_integer = large_integer + 1

        solution = []

        for num in str(final_integer):
            solution.append(int(num))

        return solution
