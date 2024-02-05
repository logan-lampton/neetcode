def knapsack(items, capacity):

    dp = {}

    dp[0] = 0

    def helper(current_capacity, items):
        if current_capacity in dp:
            return dp[current_capacity]
        
        if current_capacity < 0:
            return None
        
        max_value = float('-inf')

        for item in items:
            result = helper(current_capacity - item[0], items)
            if result is not None:
                current_value = result + item[1]
                if current_value > max_value:
                    max_value = current_value
                    dp[current_capacity] = max_value
        
        return dp[current_capacity]
    
    helper(capacity, items)
    return dp[capacity]

print(knapsack(5, [[2, 4], [1, 3], [3, 5]]))
