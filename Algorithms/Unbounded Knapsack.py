def max_ribbon(lengths, n):
    
    dp = [[float('-inf') for _ in range(n+1)] for _ in lengths]

    for row in dp:
        row[0] = 0

    for index in range(len(lengths)):
        for ribbon_size in range(len(dp[0])):
            if ribbon_size - lengths[index] >= 0:
                cut_it = dp[index][ribbon_size - lengths[index]] + 1
                leave_it = dp[index-1][ribbon_size]
                dp[index][ribbon_size] = max(cut_it, leave_it)
            else:
                dp[index][ribbon_size] = dp[index-1][ribbon_size]

    return dp[-1][-1]



print(max_ribbon([2,3,5], 5))
print(max_ribbon([2,3], 7))
print(max_ribbon([3,5,7], 13))
