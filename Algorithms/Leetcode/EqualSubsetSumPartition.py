def equal_partition_subset_sum(subset):
    if sum(subset) % 2 != 0:
        return False

    target = sum(subset) // 2

    dp = [[False for _ in range(target+1)] for _ in subset]

    for row in dp:
        row[0] = True
        
    for i in range(len(subset)):
        for curr_sum in range(len(dp[0])):
            exclude = dp[i-1][curr_sum]
            include = dp[i-1][curr_sum-subset[i]]
            dp[i][curr_sum] = exclude or include

    return dp[-1][-1]

subset = [1,2,3,4]
print(equal_partition_subset_sum(subset))
