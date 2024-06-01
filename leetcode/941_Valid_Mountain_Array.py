# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

# Example 1:
# Input: arr = [2,1]
# Output: false

# Example 2:
# Input: arr = [3,5,5]
# Output: false

# Example 3:
# Input: arr = [0,3,2,1]
# Output: true

# Constraints:
# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

class Solution:
    def validMountainArray(self, arr: [int]) -> bool:
        if len(arr) < 3:
            return False
        
        if not arr[0] < arr[1]:
            return False
        
        if not arr[-1] < arr[-2]:
            return False
        
        peak = 0

        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False
            if arr[i] < arr[i + 1]:
                if peak > arr[i + 1]:
                    return False
                else:
                    peak = arr[i + 1]
            elif arr[i] > arr[i + 1]:
                if arr[i + 1] < peak:
                    if i + 1 < len(arr) - 1:
                        if arr[i + 1] < arr[i + 2]:
                            return False

        return True
    
solution = Solution()
print(solution.validMountainArray(arr = [3,5,5]))
print(solution.validMountainArray(arr = [0,3,2,1]))