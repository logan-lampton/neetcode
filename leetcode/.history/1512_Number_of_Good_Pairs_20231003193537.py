# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0


class Solution:
    def numIdenticalPairs(self, nums: [int]) -> int:
        counter_dict = {}

        for num in nums:
            if num not in counter_dict:
                counter_dict[num] = 1
            else:
                counter_dict[num] += 1

        good_pairs = 0
        for num in counter_dict:
            if counter_dict[num] > 1:
                counter = 0
                first = counter_dict[num] - 1
                while first > 0:
                    counter += first
                    first -= 1
                good_pairs += counter
        return good_pairs
