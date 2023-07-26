# maxSubarraySum([100,200,300,400], 2) // 700
# maxSubarraySum([1,4,2,10,23,3,1,0,20], 4)  // 39
# maxSubarraySum([-3,4,0,-2,6,-1], 2) // 5
# maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2) // 5
# maxSubarraySum([2,3], 3) // null

def maxSubarraySum(array, integer):
    left = 0
    right = integer
    max_sum = 0
    current_sum = 0
    if len(array) < integer:
        return None
    for number in range(0, integer):
        current_sum += array[number]
    while right < len(array):
        # print("Current_sum:", current_sum, "max_sum:", max_sum)
        current_sum -= array[left]
        # print("c_sum_left", current_sum)
        current_sum += array[right]
        # print("c_sum_right", current_sum)
        if max_sum < current_sum:
            max_sum = current_sum
        right += 1
        left += 1
    return max_sum


print(maxSubarraySum([100, 200, 300, 400], 2))







