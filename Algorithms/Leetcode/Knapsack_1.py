def knapsack_unbounded(profits, weights, capacity):

    dp = [[0 for _ in range(capacity+1)] for _ in profits]

    for index in range(len(profits)):
        for curr_capacity in range(len(dp[0])):
            if curr_capacity - weights[index] >= 0:
                take_it = dp[index][curr_capacity-weights[index]] + profits[index]
                leave_it = dp[index-1][curr_capacity]
                dp[index][curr_capacity] = max(take_it, leave_it)
            else:
                dp[index][curr_capacity] = leave_it = dp[index-1][curr_capacity]

    return dp[-1][-1]


def knapsack_01(profits, weights, capacity):
    
    dp = [[0 for _ in range(capacity+1)] for _ in profit]

    for index in range(len(profits)):
        for curr_capacity in range(1, capacity+1):
            if curr_capacity - weights[index] >= 0:
                take_it = dp[index-1][curr_capacity-weights[index]] + profits[index] 
                leave_it = dp[index-1][curr_capacity]
                dp[index][curr_capacity] = max(take_it, leave_it)
            else:
                dp[index][curr_capacity] = dp[index-1][curr_capacity]                

    return dp[-1][-1]
