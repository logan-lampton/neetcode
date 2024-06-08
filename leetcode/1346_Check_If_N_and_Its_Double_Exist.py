# Given an array arr of integers, check if there exist two indices i and j such that:
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

# Constraints:
# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103

class Solution:
    def checkIfExist(self, arr: [int]) -> bool:

        dictionary = {}
        zero_count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                zero_count += 1
            else:
                dictionary[arr[i]] = i
            if zero_count >= 2:
                return True
        
        for key in dictionary.keys():
            if key * 2 in dictionary:
                return True
        
        return False

solution = Solution()
print(solution.checkIfExist(arr = [10,2,5,3]))
print(solution.checkIfExist(arr = [3,1,7,11]))