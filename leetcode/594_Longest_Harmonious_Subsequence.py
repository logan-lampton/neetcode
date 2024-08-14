# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2

# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0

# Constraints:
# 1 <= nums.length <= 2 * 104
# -109 <= nums[i] <= 109


class Solution:
    def findLHS(self, nums: [int]) -> int:

        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1

        if len(hashtable) == 1:
            return 0

        max_length = 0
        
        for key, value in hashtable.items():
            if key + 1 in hashtable:
                max_length = max(max_length, value + hashtable[key + 1])
        
        return max_length


solution = Solution()
print(solution.findLHS(nums = [1,3,2,2,5,2,3,7]))
print(solution.findLHS(nums = [1,2,3,4]))
print(solution.findLHS(nums = [1,1,1,1]))