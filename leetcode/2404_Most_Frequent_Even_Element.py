# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1.

# Example 1:
# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.

# Example 2:
# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.

# Example 3:
# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.

# Constraints:
# 1 <= nums.length <= 2000
# 0 <= nums[i] <= 105

class Solution:
    def mostFrequentEven(self, nums: [int]) -> int:
        smallest_key = float('inf')
        largest_value = -1
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        for key, value in dictionary.items():
            if key % 2 == 0:
                if value > largest_value:
                    smallest_key = key
                    largest_value = value
                elif value == largest_value:
                    if key < smallest_key:
                        smallest_key = key

        if smallest_key != float('inf'):
            return smallest_key
        return -1

solution = Solution()
print(solution.mostFrequentEven(nums = [0,1,2,2,4,4,1]))
print(solution.mostFrequentEven(nums = [4,4,4,9,2,4]))
print(solution.mostFrequentEven(nums = [29,47,21,41,13,37,25,7]))