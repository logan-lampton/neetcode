# You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

# Return all lonely numbers in nums. You may return the answer in any order.

# Example 1:
# Input: nums = [10,6,5,8]
# Output: [10,8]
# Explanation: 
# - 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
# - 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
# - 5 is not a lonely number since 6 appears in nums and vice versa.
# Hence, the lonely numbers in nums are [10, 8].
# Note that [8, 10] may also be returned.

# Example 2:
# Input: nums = [1,3,5,3]
# Output: [1,5]
# Explanation: 
# - 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
# - 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
# - 3 is not a lonely number since it appears twice.
# Hence, the lonely numbers in nums are [1, 5].
# Note that [5, 1] may also be returned.

# Constraints:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 106


class Solution:
    def findLonely(self, nums: [int]) -> [int]:
        if len(nums) == 1:
            return nums
        sorted_nums = sorted(nums)
        answer = []
        for i, num in enumerate(sorted_nums):
            if i == 0:
                if sorted_nums[i + 1] > num + 1:
                    answer.append(num)
            elif i == len(sorted_nums) - 1:
                if sorted_nums[i - 1] < num - 1:
                    answer.append(num)
            else:
                if sorted_nums[i - 1] < num - 1 and sorted_nums[i + 1] > num + 1:
                    answer.append(num)
        return answer
    
solution = Solution()
print(solution.findLonely(nums = [10,6,5,8]))
print(solution.findLonely(nums = [1,3,5,3]))