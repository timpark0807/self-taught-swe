import collections

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
         [2,1,1]
         [1,1,0]
         [0,1,1]
         
         count = 1
         
         q
         
        Get all the coordinates of oranges in a queue 
        Expand outwards infecting orange until you can. 
        
        Check if there are any fresh oranges left  
        
         [2,2]
         [1,1]
         [0,0]
         [2,0]
        """
        if not grid:
            return 0 
        
        queue = self.get_queue(grid)        
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0 
        
        while queue: 
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                for move in moves:
                    new_row, new_col = curr_row + move[0], curr_col + move[1]
                    if self.is_valid(grid, new_row, new_col):
                        grid[new_row][new_col] = 2 
                        queue.append((new_row, new_col))
                        
            count += 1 
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
    
        return max(0, count - 1) 
    
    
    def is_valid(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1 
    
    def get_queue(self, grid):
        temp = collections.deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    temp.append((row, col))
        return temp 

    
    
    
    
    
    
    
    
    
    
    
    
    
            
