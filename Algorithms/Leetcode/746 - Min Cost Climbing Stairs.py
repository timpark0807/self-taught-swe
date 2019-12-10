class Solution:
    def minCostClimbingStairs(self, cost):
        if not cost:
            return 0
        
        dp = [float('inf') for _ in range(len(cost)+1)]
        dp[0] = 0
        dp[1] = 0
        for start in range(len(dp)):
            end = start + 1
            jumps = 2
            
            while end < len(dp) and jumps > 0:
                dp[end] = min(dp[start] + cost[start], dp[end])
                end += 1
                jumps -= 1
        
        return dp[-1]


s = Solution()
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
