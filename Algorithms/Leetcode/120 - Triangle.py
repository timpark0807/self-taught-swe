class Solution:
    def minimumTotal(self, triangle):
        self.memo = {}
        return self.dp(triangle, 0, 0, 0)
    
    def dp(self, triangle, row, col, path):
        if (row, col) in self.memo:
            return self.memo[(row, col)]
        
        if row == len(triangle):
            return 0
        
        elif col < 0 or col == len(triangle[row]):
            return float('inf')
        
        else:
            self.memo[(row, col)] = min(self.dp(triangle, row+1, col+1, path) + triangle[row][col],
                                        self.dp(triangle, row+1, col, path) + triangle[row][col])
            return self.memo[(row, col)]
