# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

# Example 1:
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.

# Example 2:
# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.

# Constraints:
# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105


class Solution:
    def replaceElements(self, arr: [int]) -> [int]:
        if len(arr) == 1:
            return [-1]
        final_array = [0] * len(arr)
        greatest_value = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > greatest_value:
                greatest_value = arr[i]
            if i <= len(arr):
                final_array[i - 1] = greatest_value
        final_array[-1] = -1
        return final_array
    
solution = Solution()
print(solution.replaceElements(arr = [17,18,5,4,6,1]))
print(solution.replaceElements(arr = [400]))