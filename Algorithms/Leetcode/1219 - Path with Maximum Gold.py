
class Solution(object):
    def getMaximumGold(self, grid):
        self.global_max = 0 
        self.moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] != 0:
                    self.backtrack(grid, set(), row, col, 0)
        
        return self.global_max
    
    def backtrack(self, grid, seen, row, col, curr_loot):
        if not 0 <= row < len(grid) or not 0 <= col < len(grid[row]) or grid[row][col] == 0 or (row, col) in seen:
            self.global_max = max(self.global_max, curr_loot)
            return 
        
        curr_gold = grid[row][col]
        grid[row][col] = 0
        
        for move in self.moves:
            new_row, new_col = row + move[0], col + move[1]
            self.backtrack(grid, seen, new_row, new_col, curr_loot + curr_gold)
        grid[row][col] = curr_gold
        
grid = [[0,0,0,0,0,0,32,0,0,20],[0,0,2,0,0,0,0,40,0,32],[13,20,36,0,0,0,20,0,0,0],[0,31,27,0,19,0,0,25,18,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,18,0,6],[0,0,0,25,0,0,0,0,0,0],[0,0,0,21,0,30,0,0,0,0],[19,10,0,0,34,0,2,0,0,27],[0,0,0,0,0,34,0,0,0,0]]
s = Solution()
print(s.getMaximumGold(grid))
