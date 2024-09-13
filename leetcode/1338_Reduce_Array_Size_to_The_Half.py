# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

# Return the minimum size of the set so that at least half of the integers of the array are removed.

# Example 1:
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.

# Example 2:
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.

# Constraints:
# 2 <= arr.length <= 105
# arr.length is even.
# 1 <= arr[i] <= 105


class Solution:
    def minSetSize(self, arr: [int]) -> int:
        hashmap = {}
        half_array_len = len(arr) // 2

        for num in arr:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        sorted_by_frequency = sorted(hashmap.items(), key=lambda x: (x[1], x[0]), reverse=True)
        
        amount_in_set = 0
        remaining = len(arr)

        for key, value in sorted_by_frequency:
            amount_in_set += 1
            remaining -= value
            if remaining <= half_array_len:
                return amount_in_set


solution = Solution()
print(solution.minSetSize(arr = [3,3,3,3,5,5,5,2,2,7]))
print(solution.minSetSize(arr = [7,7,7,7,7,7]))
