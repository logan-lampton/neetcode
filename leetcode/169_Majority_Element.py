# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):

        count_dict = {}

        for num in nums:
            if num not in count_dict:
                count_dict[num] = 0
            count_dict[num] += 1

        max_count = 0
        majority_num = None

        for num, count in count_dict.items():
            if count > max_count:
                majority_num = num
                max_count = count

        return majority_num


# Testing solution
solution = Solution()

print(solution.majorityElement([3, 2, 3]))
