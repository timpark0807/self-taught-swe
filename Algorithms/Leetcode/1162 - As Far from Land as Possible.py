import collections

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[Lis
        t[int]]
        :rtype: int
         
         [[1,0,0],
          [0,0,0],
          [0,0,0]]
          
          
        Step 0. Store all the maximum distances in a variable
        
        Step 1. Iterate through the grid
            Step 1.1 If point is water, BFS and find the closest water cell 
            Step 1.2 If that curr distance is greater than max_distance, update max_distance 
            
        return max_distance
        
         [0,0,1,1,1],
         [0,1,1,0,0],
         [0,0,1,1,0],
         [1,0,0,0,0],
         [1,1,0,0,1]
        
        """
        m,n = len(grid), len(grid[0])
        q = collections.deque([(i,j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) == m * n or len(q) == 0: return -1
        level = 0
        moves = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            size = len(q)
            for _ in range(size):
                curr_row, curr_col = q.popleft()
                for move in moves:
                    new_row, new_col = curr_row + move[0], curr_col + move[1]
                    if not self.is_invalid(grid, new_row, new_col) and grid[new_row][new_col] == 0:
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 1

            for row in grid:
                print(row)
            print('*'*30)
            level += 1
            
        return level - 1
                    
    def is_invalid(self, grid, row, col):
        if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
            return True
        return False
    
    
            
            
grid = [[1,0,1],[0,0,0],[1,0,1]]
s = Solution()
s.maxDistance(grid)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
