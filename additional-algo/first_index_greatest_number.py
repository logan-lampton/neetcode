# return index of first instance of the greatest number
# nums0 = [3, 1, 8, 2, 8, 3, 7, 1] => 2
# nums1 = [8, 9, 1, 2, 6, 3, 1] => 1
# nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9] => 9

nums0 = [3, 1, 8, 2, 8, 3, 7, 1]
nums1 = [8, 9, 1, 2, 6, 3, 1]
nums2 = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9]

def first_index_greatest_number(array):
    biggest = 0
    index = 0
    for i in range(len(array)):
        if array[i] > biggest:
            biggest = array[i]
            index = i
    return index




print(first_index_greatest_number(nums0))
print(first_index_greatest_number(nums1))
print(first_index_greatest_number(nums2))
