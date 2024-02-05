# Top-Down Method

def knapsack(capacity, items):

    if not isinstance(items, list) or not all(isinstance(item, list) and len(item) == 2 for item in items):
        raise ValueError("Items should be a list of lists where each inner list represents an item with its weight and value.")

    dp = {}

    dp[0] = 0

    def helper(current_capacity, items):
        if current_capacity in dp:
            return dp[current_capacity]
        
        if current_capacity == 0:
            return 0
        
        if current_capacity < 0:
            return float('-inf')
        
        max_value = float('-inf')

        for item in items:
            weight, value = item
            if current_capacity - weight >= 0:
                result = helper(current_capacity - weight, items)
                current_value = result + value
                if current_value > max_value:
                    max_value = current_value
        
        dp[current_capacity] = max_value
        
        return max_value
    
    helper(capacity, tuple(items))
    return dp[capacity]

print(knapsack(5, [[2, 4], [1, 3], [3, 5]]))

print(knapsack(5, [
    [2, 4],
    [1, 3],
    [3, 5],
]))
