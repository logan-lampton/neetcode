# return sum of numbers
# [8, 2, 1, 0, 3] => 14
# [2, 2, 2, 2, 2, 2] => 12

nums1 = [8, 2, 1, 0, 3]
nums2 = [2, 2, 2, 2, 2, 2]


def findTotal(array):
    total_sum = 0
    for num in array:
        total_sum += num
    return total_sum


print(findTotal(nums1))
print(findTotal(nums2))
