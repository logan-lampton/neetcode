# Given an array of integers nums, you start with an initial positive value startValue.

# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

# Example 1:
# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2

# Example 2:
# Input: nums = [1,2]
# Output: 1
# Explanation: Minimum start value should be positive. 

# Example 3:
# Input: nums = [1,-2,-3]
# Output: 5

# Constraints:
# 1 <= nums.length <= 100
# -100 <= nums[i] <= 100

class Solution:
    def minStartValue(self, nums: [int]) -> int:
        sum_steps = {0: nums[0]}
        for i in range(1, len(nums)):
            sum_steps[i] = sum_steps[i - 1] + nums[i]
        min_value = min(value for value in sum_steps.values())
        if min_value >= 1:
            return 1
        else:
            return 1 + abs(min_value)

solution = Solution()
print(solution.minStartValue(nums = [-3,2,-3,4,2]))
print(solution.minStartValue(nums = [1,2]))
print(solution.minStartValue(nums = [1,-2,-3]))

# Practice/new method:
class Solution:
    def minStartValue(self, nums: [int]) -> int:
        lowest_value = 0
        cur_value = 0

        for num in nums:
            cur_value += num
            if lowest_value > cur_value:
                lowest_value = cur_value
        
        return abs(lowest_value) + 1
    
# Practice
class Solution:
    def minStartValue(self, nums: [int]) -> int:
        smallest_value = nums[0]
        running_total = 0

        for num in nums:
            running_total += num
            if running_total < smallest_value:
                smallest_value = running_total
        
        if smallest_value > 0:
            return 1
        else:
            return abs(smallest_value) + 1