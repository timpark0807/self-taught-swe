class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        seen = set()
        shapes = set()
        count = 0 
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if self.is_valid(grid, row, col, seen):
                    curr_shape = self.bfs(grid, row, col, seen)
                    shapes.add(curr_shape)
                    
        return len(shapes)
    
    
    def bfs(self, grid, row, col, seen):
        queue = collections.deque([(row, col)])
        seen.add((row, col))
        curr_shape = ['00']
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
            curr_row, curr_col = queue.popleft()    
            for move in moves:
                new_row, new_col = curr_row + move[0], curr_col + move[1]
                if self.is_valid(grid, new_row, new_col, seen):
                    queue.append((new_row, new_col))
                    seen.add((new_row, new_col))
                    curr_shape.append((row-new_row, col-new_col))
        
        return tuple(curr_shape)
    
    def is_valid(self, grid, row, col, seen):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row]) and (row, col) not in seen and grid[row][col] == 1
