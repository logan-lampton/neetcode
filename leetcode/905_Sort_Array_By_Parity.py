# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

# Example 1:
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# Example 2:
# Input: nums = [0]
# Output: [0]


class Solution:
    def sortArrayByParity(self, nums: [int]) -> [int]:
        even_answer = []
        odd_answer = []
        # Note to self! in my tests, using an index in range, rather than num in nums, had better run time
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_answer.append(nums[i])
            else:
                odd_answer.append(nums[i])
        return even_answer + odd_answer
