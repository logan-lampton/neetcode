# return the second greatest number
# [3, 1, 8, 2, 8, 3, 7, 1] => 7
# [8, 9, 1, 2, 6, 3, 1] => 8
# [0, 1, 2, 3, 4, 5, 6, 7, 7, 9] => 7

nums1 = [3, 1, 8, 2, 8, 3, 7, 1]
nums2 = [8, 9, 1, 2, 6, 3, 1]
nums3 = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9]

# my method:
def second_greatest_number(array):
    greatest = 0
    second_greatest = 0
    for i in range(len(array)):
        if array[i] > greatest:
            greatest = array[i]
    for i in range(len(array)):
        if second_greatest < array[i] < greatest:
            second_greatest = array[i]
    return second_greatest


# better
def better_second_greatest_number(array):
    greatest = 0
    second_greatest = 0
    for num in array:
        if num > greatest:
            second_greatest = greatest
            greatest = num
        elif num > second_greatest and num != greatest:
            second_greatest = num
    return second_greatest


print(second_greatest_number(nums1))
print(second_greatest_number(nums2))
print(second_greatest_number(nums3))
