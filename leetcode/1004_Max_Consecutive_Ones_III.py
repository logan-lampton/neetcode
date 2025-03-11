# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip
# at most k 0's.

# Example 1:
# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:
# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


def longestOnes(nums, k):
    left = 0
    right = 0
    flips_remaining = k
    max_count = 0
    current_count = 0

    while right < len(nums):
        if nums[right] == 1:
            current_count += 1
            right += 1
        else:
            if flips_remaining > 0:
                current_count += 1
                flips_remaining -= 1
                right += 1
            else:
                max_count = max(max_count, current_count)
                if nums[left] == 0:
                    flips_remaining += 1
                left += 1
                current_count -= 1

    return max(max_count, current_count)


print(longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))

# Practice/somewhat different approach:
class Solution:
    def longestOnes(self, nums: [int], k: int) -> int:
        max_length = 0
        cur_zeros = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                cur_zeros += 1
            while cur_zeros > k:
                if nums[left] == 0:
                    cur_zeros -= 1
                left += 1
            cur_length = right - left + 1
            if max_length < cur_length:
                max_length = cur_length
        
        return max_length


# Practice:
class Solution:
    def longestOnes(self, nums: [int], k: int) -> int:
        
        max_consecutive = 0
        cur_consecutive = 0
        flips = k

        left = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                cur_consecutive += 1
            else:
                flips -= 1
                cur_consecutive += 1

            while flips < 0:
                if nums[left] == 0:
                    flips += 1
                cur_consecutive -= 1
                left += 1
                
            if max_consecutive < cur_consecutive:
                max_consecutive = cur_consecutive
            
        return max_consecutive