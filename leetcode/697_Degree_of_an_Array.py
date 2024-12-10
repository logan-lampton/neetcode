# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

# Constraints:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.


class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        
        hashtable = {}
        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        
        ordered_items = sorted(hashtable.items(), key=lambda item: item[1], reverse=True)

        highest_degree_nums = [ordered_items[0]]
        for i in range(1, len(ordered_items)):
            if ordered_items[i][1] == highest_degree_nums[0][1]:
                highest_degree_nums.append(ordered_items[i])

        min_len = len(nums)

        for num, freq in highest_degree_nums:
            first_index = nums.index(num)
            last_index = len(nums) - 1 - nums[::-1].index(num)
            cur_len = last_index - first_index + 1
            if min_len > cur_len:
                min_len = cur_len
        
        return min_len
    

solution = Solution()
print(solution.findShortestSubArray(nums = [1,2,2,3,1]))
print(solution.findShortestSubArray(nums = [1,2,2,3,1,4,2]))