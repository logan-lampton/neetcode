# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

# Example 1:
# Input: nums = [18,43,36,13,7]
# Output: 54
# Explanation: The pairs (i, j) that satisfy the conditions are:
# - (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
# - (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
# So the maximum sum that we can obtain is 54.

# Example 2:
# Input: nums = [10,12,19,14]
# Output: -1
# Explanation: There are no two numbers that satisfy the conditions, so we return -1.

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109


class Solution:
    def maximumSum(self, nums: [int]) -> int:
        # find all indexes that have two different indexes where the sum of the integers are equal to each other
        # track which is the largest and make sure to update if a larger value is found

        digit_sums = {}

        for i in range(len(nums)):
            string_i = str(nums[i])
            digit_sum = 0
            for char in string_i:
                digit_sum += int(char)
            if digit_sum not in digit_sums:
                digit_sums[digit_sum] = [nums[i]]
            else:
                digit_sums[digit_sum].append(nums[i])
        
        max_sum = -1
        
        for key, value in digit_sums.items():
            if len(value) >= 2:
                value.sort()
                cur_sum = value[-1] + value[-2]
                if max_sum < cur_sum:
                    max_sum = cur_sum
        
        return max_sum
    

solution = Solution()
print(solution.maximumSum(nums = [18,43,36,13,7]))
print(solution.maximumSum(nums = [10,12,19,14]))