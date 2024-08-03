# You are given a 0-indexed array nums of length n.

# The distinct difference array of nums is an array diff of length n such that diff[i] is equal to the number of distinct elements in the suffix nums[i + 1, ..., n - 1] subtracted from the number of distinct elements in the prefix nums[0, ..., i].

# Return the distinct difference array of nums.

# Note that nums[i, ..., j] denotes the subarray of nums starting at index i and ending at index j inclusive. Particularly, if i > j then nums[i, ..., j] denotes an empty subarray.

# Example 1:
# Input: nums = [1,2,3,4,5]
# Output: [-3,-1,1,3,5]
# Explanation: For index i = 0, there is 1 element in the prefix and 4 distinct elements in the suffix. Thus, diff[0] = 1 - 4 = -3.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 3 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 3 - 2 = 1.
# For index i = 3, there are 4 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 4 - 1 = 3.
# For index i = 4, there are 5 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 5 - 0 = 5.

# Example 2:
# Input: nums = [3,2,3,4,2]
# Output: [-2,-1,0,2,3]
# Explanation: For index i = 0, there is 1 element in the prefix and 3 distinct elements in the suffix. Thus, diff[0] = 1 - 3 = -2.
# For index i = 1, there are 2 distinct elements in the prefix and 3 distinct elements in the suffix. Thus, diff[1] = 2 - 3 = -1.
# For index i = 2, there are 2 distinct elements in the prefix and 2 distinct elements in the suffix. Thus, diff[2] = 2 - 2 = 0.
# For index i = 3, there are 3 distinct elements in the prefix and 1 distinct element in the suffix. Thus, diff[3] = 3 - 1 = 2.
# For index i = 4, there are 3 distinct elements in the prefix and no elements in the suffix. Thus, diff[4] = 3 - 0 = 3.

# Constraints:
# 1 <= n == nums.length <= 50
# 1 <= nums[i] <= 50

class Solution:
    def distinctDifferenceArray(self, nums: [int]) -> [int]:
        difference = []
        left = 0
        right = 1
        while right < len(nums) + 1:
            cur_dif = len(set(nums[0:left + 1])) - len(set(nums[right:]))
            difference.append(cur_dif)
            left += 1
            right += 1
        return difference


# class Solution:
#     def distinctDifferenceArray(self, nums: [int]) -> [int]:

#         prefix = set()
#         suffix = set()
#         output = []

#         for i in range(len(nums)):
#             prefix = set(nums[0 : i + 1])
#             suffix = set(nums[i + 1 : len(nums)])
#             output.append(len(prefix) - len(suffix))

#         return output

solution = Solution()
nums = [1,2,3,4,5]

print(solution.distinctDifferenceArray(nums))