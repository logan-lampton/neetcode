# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Example 1:
# Input: nums = [3,2,3]
# Output: [3]

# Example 2:
# Input: nums = [1]
# Output: [1]

# Example 3:
# Input: nums = [1,2]
# Output: [1,2]


class Solution:
    def majorityElement(self, nums: [int]) -> [int]:
        n = len(nums)
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        return_array = []
        for key, value in num_dict.items():
            if value > n / 3:
                return_array.append(key)
        return return_array
