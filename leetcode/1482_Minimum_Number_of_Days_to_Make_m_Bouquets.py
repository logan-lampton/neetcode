# You are given an integer array bloomDay, an integer m and an integer k.

# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one
# bouquet.

# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible
# to make m bouquets return -1.

# Example 1:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not
# bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

# Example 2:
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
# Output: -1
# Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is
# impossible to get the needed bouquets, and we return -1.

# Example 3:
# Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
# Output: 12
# Explanation: We need 2 bouquets each should have 3 flowers.
# Here is the garden after the 7 and 12 days:
# After day 7: [x, x, x, x, _, x, x]
# We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three
# flowers that bloomed because they are not adjacent.
# After day 12: [x, x, x, x, x, x, x]
# It is obvious that we can make two bouquets in different ways.

def minDays(bloomDay, m, k):
    # Check to see if it's possible to make enough bouquets with the number of flowers in the bloomDay array
    if m * k > len(bloomDay):
        return -1

    # Use binary search
    # Identify the range of possible days by finding the minimum and maximum values in the bloomDay array.

    left = min(bloomDay)
    right = max(bloomDay)

    while left < right:
        # Calculate the middle day (it's the average of the left and right pointers)
        middle_day = (left + right) // 2
        # Reset the bouquet and flowers to count the amount on the current middle_day
        bouquets = 0
        flowers = 0
        # Determine if we can make 'm' bouquets on middle_day
        for i in bloomDay:
            if i <= middle_day:
                flowers += 1
                # When the flowers count reaches k, a bouquet is made, and the flowers count is reset.
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
        # Adjust the search interval based on the bouquets count
        if bouquets >= m:
            # If at least 'm' bouquets can be made, the right pointer is adjusted to middle_day to narrow down the
            # search interval.
            right = middle_day
        else:
            # If you can't make m bouquets on the middle_day, the left pointer is adjusted to middle_day + 1 to search
            # in the higher half of the interval.
            left = middle_day + 1

    return left
