class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        self.memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.dfs(obstacleGrid, m, n, 0, 0)
        
    def dfs(self, obstacleGrid, m, n, curr_x, curr_y):
        if (curr_x, curr_y) in self.memo:
            return self.memo[(curr_x, curr_y)]
        
        if curr_x == m or curr_y == n or obstacleGrid[curr_x][curr_y] == 1:
            return 0

        if (curr_x, curr_y) == (m-1, n-1):
            return 1
        
        go_right = self.dfs(obstacleGrid, m, n, curr_x, curr_y+1)
        go_down = self.dfs(obstacleGrid, m, n, curr_x+1, curr_y)
        self.memo[(curr_x, curr_y)] = go_right + go_down
        return go_right + go_down
    
    
    
