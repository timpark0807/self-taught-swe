def knapsack_01_topdown(weights, profits, capacity):

    memo = [[0 for _ in range(capacity+1)] for _ in weights]
    
    return backtrack(weights, profits, capacity, len(profits)-1, 0, memo)


def backtrack(weights, profits, capacity, index, curr_profit, memo):
    if capacity == 0 or index == -1:
        return curr_profit
    
    if memo[index][capacity] != 0:
        return memo[index][capacity]
    
    take_it = 0
    
    if capacity - weights[index] >= 0:
        take_it = backtrack(weights, profits, capacity-weights[index], index-1, curr_profit + profits[index], memo)

    leave_it = backtrack(weights, profits, capacity, index-1, curr_profit, memo)

    memo[index][capacity] = max(take_it, leave_it)
    
    return memo[index][capacity]



weights = [2, 3, 1, 4]
profits = [6, 5, 3, 7]
capacity = 5
print(knapsack_01_topdown(weights, profits, capacity))
