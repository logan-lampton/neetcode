# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


def intersect(nums1, nums2):
    output = []
    num_counts = {}

    for num in nums1:
        if num not in num_counts:
            num_counts[num] = 1
        else:
            num_counts[num] += 1

    for num in nums2:
        if num in num_counts:
            if num_counts[num] > 0:
                output.append(num)
                num_counts[num] -= 1

    return output
