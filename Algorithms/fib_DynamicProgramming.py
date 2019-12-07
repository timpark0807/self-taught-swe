# Step 1. Naive Recursive Solution
def fib_top_down_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_top_down_naive(n-1) + fib_top_down_naive(n-2)


# Step 2. Introduce memoization for repeated subproblems
def fib_memo(n):
    memo = [-1] * (n+1)
    return dfs(n, memo)

def dfs(n, memo):
    if memo[n] != -1:
        return memo[n]
    
    if n == 0:
        memo[n] = 0
        return memo[n]
    elif n == 1:
        memo[n] = 1
        return memo[n]
    
    memo[n] = dfs(n-1, memo) + dfs(n-2, memo)
    return memo[n]


# Step 3. Remove recursion by using memozied table to solve problem
#         - Reduced recursive: memo[n] = dfs(n-1, memo) + dfs(n-2, memo)
#         - To table: memo[n] = memo[index-1] + memo[index-2]
def fib_tabulation(n):
    memo = [-1] * (n+1)
    memo[0], memo[1] = 0, 1
    
    for index in range(2, len(dp)):
        memo[index] = memo[index-1] + memo[index-2]
        
    return dp[-1]

print(fib_top_down_naive(198))
print(fib_memo(198))
print(fib_tabulation(198))
    
