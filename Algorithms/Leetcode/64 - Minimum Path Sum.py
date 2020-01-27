class Solution(object):
    def minPathSum(self, grid):
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        for i in range(1, len(dp)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for i in range(1, len(dp[0])):
            dp[0][i] = dp[0][i-1] + grid[0][i]

        for row in dp:
            print(row)
            
        for x in range(1, len(dp)):
            for y in range(1, len(dp[0])):
                dp[x][y] = min(dp[x][y-1], dp[x-1][y]) + grid[x][y]
        print("*" * 30)
        for row in dp:
            print(row)
        return dp[-1][-1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

s = Solution()
print(s.minPathSum(grid))
