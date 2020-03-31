class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        [0,2]
        [1,3]
        """

        heap = [(grid[0][0], 0, 0)]
        seen = set([(0,0)]) 
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while heap: 
            
            curr_dist, curr_row, curr_col = heapq.heappop(heap) 

            if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                return curr_dist 
        
            for move in moves:
                new_row, new_col = curr_row + move[0], curr_col + move[1]
                if self._isValid(grid, seen, new_row, new_col): 
                    seen.add((new_row, new_col))
                    new_dist = max(grid[new_row][new_col], curr_dist)
                    heapq.heappush(heap, (new_dist, new_row, new_col))
            
    def _isValid(self, grid, seen, row, col):
        return 0 <= row <len(grid) and 0 <= col < len(grid[0]) and (row, col) not in seen 
