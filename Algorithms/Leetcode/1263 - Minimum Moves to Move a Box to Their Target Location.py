import collections

class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        
        grid = ["#","#","#","#","#","#"],
               ["#","T","#","#","#","#"],
               ["#",".",".","B",".","#"],
               ["#",".","#","#",".","#"],
               ["#",".",".",".","S","#"],
               ["#","#","#","#","#","#"]
    
        Pass 0 - Find coordinates of B, S and T 
               - Check that there is a path from S to B 
               
        BFS 
        queue = [(row, col, dist)]
        seen = set()
        moves = {
                 (0,1)  : (1,0),
                 (1,0)  : (0,1),
                 (-1,0) : (0,-1)
                 (0,-1) : (-1,0)
                 }
        
        while there are elements in the queue
            - dequeue r,c,d from queue 
            - check if r,c == tr, tc: return d 
            - for new_position, push_position in moves.items():
                - if the both positions are valid
                    - add new_position to the queue, increment d by 1 
                    - add new_position to seen
        return -1 
        
        
        is_valid()
        Is the new position inbound and unblocked
        Is the push position inbound and unblocked 
        Is the new position not in seen 

        is_inbound()
        check that row and col are in bounds 
        
           [["#",".",".","#","#","#","#","#"]
            ["#",".",".","T","#",".",".","#"]
            ["#",".",".",".","#","B",".","#"]
            ["#",".",".",".",".",".",".","#"]
            ["#",".",".",".","#",".","S","#"]
            ["#",".",".","#","#","#","#","#"]]
                 
        """
        if not grid: 
            return -1 
        
        t_coord, s_coord, b_coord = self.get_coordinates(grid)
        grid[b_coord[0]][b_coord[1]] = '.'
        min_push = self.bfs(grid, b_coord, s_coord, t_coord)
        return min_push 
    
    
    def bfs(self, grid, b_coord, s_coord, t_coord):
        queue = collections.deque([(b_coord, s_coord, 0)])
        seen = set([(b_coord, s_coord)]) 
        
        # new position : push position 
        self.moves = {(0,1)  : (0 ,-1),
                      (1,0)  : (-1,0),
                      (-1,0) : (1,0),
                      (0,-1) : (0 ,1)}   
        
        while queue: 
            (box_row, box_col), (person_row, person_col), curr_push = queue.popleft() 
            if (box_row, box_col) == t_coord:
                return curr_push 

            for new_pos, push_pos in self.moves.items():
                new_row, new_col = box_row + new_pos[0], box_col + new_pos[1]
                push_row, push_col = box_row + push_pos[0], box_col + push_pos[1]
                if not self.is_path(grid, person_row, person_col, push_row, push_col, box_row, box_col):
                    continue 
                if self.is_valid(grid, new_row, new_col, push_row, push_col) and ((box_row, box_col), (new_row, new_col)) not in seen:
                    queue.append(((new_row, new_col), (box_row, box_col), curr_push+1))
                    seen.add(((box_row, box_col), (person_row, person_col)))
    
        return -1
    
    def is_path(self, grid, sr, sc, tr, tc, br, bc):
        stack = [(sr, sc)]
        seen = set()
        while stack:
            curr_row, curr_col = stack.pop(0)
            if (curr_row, curr_col) == (tr, tc):
                return True
            for move in self.moves.keys():
                new_row, new_col = curr_row + move[0], curr_col + move[1]
                if self.inbound(grid, new_row, new_col) and (new_row, new_col) not in seen and (new_row, new_col) != (br, bc):
                    seen.add((new_row, new_col))
                    stack.append((new_row, new_col))
        return False
        
    def is_valid(self, grid, nr, nc, pr, pc):
        return self.inbound(grid, nr, nc) and self.inbound(grid, pr, pc) 
           
    def inbound(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != '#'
        
    def get_coordinates(self, grid):
        t_coord, s_coord, b_coord = None, None, None
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 'T':
                    t_coord = (row, col)
                elif grid[row][col] == 'B':
                    b_coord = (row, col)
                elif grid[row][col] == 'S':
                    s_coord = (row, col)         
        return t_coord, s_coord, b_coord
                    
                    
grid = [["#",".",".","#","#","#","#","#"],
        ["#",".",".","T","#",".",".","#"],
        ["#",".",".",".","#","B",".","#"],
        ["#",".",".",".",".",".",".","#"],
        ["#",".",".",".","#",".","S","#"],
        ["#",".",".","#","#","#","#","#"]]
s= Solution()
print(s.minPushBox(grid))

grid = [ ["T","#","#","#"],
         [".",".","B","."],
         [".","#","#","."],
         [".",".",".","S"]]
print(s.minPushBox(grid))
