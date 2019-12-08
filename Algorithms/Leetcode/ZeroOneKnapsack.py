def knapsack(profits, weights, capacity):
    
    dp = [[0 for _ in range(capacity+1)] for _ in profit]

    for index in range(len(profits)):
        for curr_capacity in range(1, capacity+1):
            if curr_capacity - weights[index] >= 0:
                take_it = profits[index] + dp[index-1][curr_capacity-weights[index]]
                leave_it = dp[index-1][curr_capacity]
                dp[index][curr_capacity] = max(take_it, leave_it)
            else:
                dp[index][curr_capacity] = dp[index-1][curr_capacity]                

    return dp[-1][-1]
    

profit = [1, 6, 10, 16]
weight = [1, 2, 3, 5]

print(knapsack(profit, weight, 7))
