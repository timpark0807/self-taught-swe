class Solution:
    def uniquePaths(self, m, n):
        self.memo = {}
        return self.dfs(m, n, 0, 0)
        
    def dfs(self, m, n, curr_x, curr_y):
        if (curr_x, curr_y) in self.memo:
            return self.memo[(curr_x, curr_y)]
        if (curr_x, curr_y) == (m-1, n-1):
            return 1
        
        if curr_x == m or curr_y == n:
            return 0
        
        go_right = self.dfs(m, n, curr_x, curr_y+1)
        go_down = self.dfs(m, n, curr_x+1, curr_y)
        self.memo[(curr_x, curr_y)] = go_right + go_down
        return go_right + go_down
