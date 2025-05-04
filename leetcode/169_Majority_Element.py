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


# Practice
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        elements_dict = {}
        for num in nums:
            if num not in elements_dict:
                elements_dict[num] = 1
            else:
                elements_dict[num] += 1
        
        max_val = 0
        answer = 0

        for key, value in elements_dict.items():
            if value > max_val:
                max_val = value
                answer = key
        
        return answer

# Practice
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur_candidate = None

        for num in nums:
            if count == 0:
                cur_candidate = num
            if num == cur_candidate:
                count += 1
            else:
                count -= 1
        
        return cur_candidate