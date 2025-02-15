# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0] ** 2]
        
        answer = []
        negative_array = []
        positive_array = []
        final_index = 0

        for i, num in enumerate(nums):
            if num >=0:
                positive_array.append(num)
            elif num < 0:
                negative_array.append(num)

        if len(negative_array) == 0:
            for num in positive_array:
                answer.append(num ** 2)
            return answer

        if len(positive_array) == 0:
            for i in range(len(negative_array) - 1, -1, -1):
                answer.append(negative_array[i] ** 2)
            return answer

        negative_index = -1
        positive_index = 0

        while abs(negative_index) <= len(negative_array) and positive_index < len(positive_array):
            negative_value = negative_array[negative_index] ** 2
            positive_value = 0
            if positive_array[positive_index] == 0:
                answer.append(positive_value)
                positive_index += 1
                continue
            else:
                positive_value = positive_array[positive_index] ** 2
            
            if negative_value > positive_value:
                answer.append(positive_value)
                positive_index += 1
            elif negative_value < positive_value:
                answer.append(negative_value)
                negative_index -= 1
            else:
                answer.append(negative_value)
                answer.append(positive_value)
                negative_index -= 1
                positive_index += 1
        
        if abs(negative_index) <= len(negative_array):
            for i in range(len(negative_array) - abs(negative_index), -1, -1):
                answer.append(negative_array[i] **2)

        if positive_index <= len(positive_array):
            for i in range(positive_index, len(positive_array)):
                answer.append(positive_array[i] ** 2)

        return answer


solution = Solution()
print(solution.sortedSquares(nums = [-4,-1,0,3,10]))
print(solution.sortedSquares(nums = [-7,-3,2,3,11]))