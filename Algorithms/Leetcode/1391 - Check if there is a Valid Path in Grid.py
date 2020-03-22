class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        
        1 which means a street connecting the left cell and the right cell.
        2 which means a street connecting the upper cell and the lower cell.
        3 which means a street connecting the left cell and the lower cell.
        4 which means a street connecting the right cell and the lower cell.
        5 which means a street connecting the left cell and the upper cell.
        6 which means a street connecting the right cell and the upper cell.
        
        """
        self.moves = {1:[(0,1), (0,-1)], 
                      2:[(1,0),(-1,0)], 
                      3:[(1,0),(0,-1)], 
                      4:[(0,1),(1,0)],
                      5:[(-1,0),(0,-1)],
                      6:[(-1,0),(0,1)]}
        
        queue = collections.deque([(0,0,(0,0))])
        seen = set() 
        while queue:
            curr_row, curr_col, last_move = queue.popleft() 
            curr_direction = grid[curr_row][curr_col] 
            if curr_row == len(grid) - 1 and curr_col == len(grid[-1]) - 1:
                return True
            
            for move in self.moves[curr_direction]:
                new_row, new_col = curr_row + move[0], curr_col + move[1]
                if self.is_inbounds(grid, new_row, new_col, seen) and self.does_accept(grid, move, new_row, new_col):
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, move)) 
        return False 
    
    def does_accept(self, grid, move, row, col):
        opposite_move = (move[0] *-1, move[1] * -1) 
        curr_direction = grid[row][col]
        return opposite_move in self.moves[curr_direction] 
    
    
    def is_inbounds(self, board, row, col, seen):
        return 0 <= row < len(board) and 0 <= col < len(board[row]) and (row, col) not in seen
    
