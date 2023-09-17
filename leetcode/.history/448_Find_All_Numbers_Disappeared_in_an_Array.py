# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n]
# that do not appear in nums.

# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:
# Input: nums = [1,1]
# Output: [2]


class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        # create a list of the integers that should be in the full array
        # it should be 1 - the full length of the array
        full_array = [i for i in range(1, len(nums) + 1)]

        # only return the numbers needed
        # accomplished by making the full array and nums list into sets
        # then subtracting the resulting nums set from the full array set
        answer_numbers = set(full_array) - set(nums)

        # make the numbers into a list, then return the list
        answer_array = list(answer_numbers)

        return answer_array
