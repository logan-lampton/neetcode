# write a function bestSum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments

# The function should return an array containing the shortest combination of numbers that add up 
# to exactly the targetSum

# If there is a tie for the shortest combination, you may return any one of the shortest.


def bestSum(targetSum, numbers):

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    shortest_combination = None

    for num in numbers:
        remainder = targetSum - num
        remainder_combination = bestSum(remainder, numbers)
        if remainder_combination is not None:
            if len(remainder_combination) < len(shortest_combination) or  shortest_combination == None:
                shortest_combination = remainder_combination
    
    return shortest_combination


bestSum(7, [5, 3, 4, 7])