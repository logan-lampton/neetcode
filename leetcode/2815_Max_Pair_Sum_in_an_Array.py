# You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the largest digit in both numbers is equal.

# For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.

# Return the maximum sum or -1 if no such pair exists.

# Example 1:
# Input: nums = [112,131,411]
# Output: -1
# Explanation:
# Each numbers largest digit in order is [2,3,4].

# Example 2:
# Input: nums = [2536,1613,3366,162]
# Output: 5902
# Explanation:
# All the numbers have 6 as their largest digit, so the answer is 2536 + 3366 = 5902.

# Example 3:
# Input: nums = [51,71,17,24,42]
# Output: 88
# Explanation:
# Each number's largest digit in order is [5,7,7,4,4].
# So we have only two possible pairs, 71 + 17 = 88 and 24 + 42 = 66.

# Constraints:
# 2 <= nums.length <= 100
# 1 <= nums[i] <= 104


class Solution:
    def maxSum(self, nums: [int]) -> int:
        shared_dict = {}
        sorted_nums = sorted(nums, reverse=True)

        for num in nums:
            max_digit = 0
            for digit in str(num):
                int_digit = int(digit)
                if int_digit > max_digit:
                    max_digit = int_digit
            if max_digit not in shared_dict:
                shared_dict[max_digit] = [num]
            else:
                shared_dict[max_digit].append(num)
        
        max_sum = -1
        for shared_num, nums in shared_dict.items():
            if len(nums) > 1:
                cur_num_max = 0
                largest_num = 0
                second_largest_num = 0
                for num in nums:
                    if num > largest_num:
                        if largest_num > second_largest_num:
                            second_largest_num = largest_num
                        largest_num = num
                    elif num > second_largest_num:
                        second_largest_num = num
                cur_num_max = largest_num + second_largest_num
                if max_sum < cur_num_max:
                    max_sum = cur_num_max
    
        return max_sum


solution = Solution()
print(solution.maxSum(nums = [112,131,411]))
print(solution.maxSum(nums = [2536,1613,3366,162]))
print(solution.maxSum(nums = [51,71,17,24,42]))