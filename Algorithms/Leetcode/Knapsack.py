def solve_knapsack(profits, weights, capacity):
    """

    weights = [2, 3, 1, 4]
    profits = [4, 5, 3, 7]
    
    [0, 3, 4, 7, 0, 0]
     0  1  2  3  4, 5


     
    """

    dp = [0] * (capacity + 1)

    for capacity in range(len(dp)):
        for index, weight in enumerate(weights):
            if weight < capacity:
                dp[capacity] = max(profits[index], profits[index] + dp[capacity-index])

    return dp[-1]

fruits = ['apple', 'orange', 'banana', 'melon']
weights = [2, 3, 1, 4]
profits = [4, 5, 3, 7]
print(solve_knapsack(profits, weights, 5))
