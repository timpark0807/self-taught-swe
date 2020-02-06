class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        
        Shortest, Unweighted = BFS
        
           0 1 2
        0 [1,0,-1]

        
        Variables Needed:
            queue
            island1
            island2 
            count 
            isvalid
            moves 
        
        1. Identify the coordinates of both islands in a set
            island1 = {(2, 2)}
            island2 = {(0,1)}

        2. Do a BFS, expanding outwards from coordinates in island1
            queue = [(0, 1, 0)]
            
            3. If our expansion hits a coordinate in island2, return count 

        """
        self.moves = [(0,1),(0,-1),(1,0),(-1,0)]

        island1, island2 = self.get_islands(A) # returns a set of coordinates
        queue = collections.deque(list(island1))
        count = 0 
        
        while queue:
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft()
                
                for move in self.moves:
                    new_row, new_col = curr_row + move[0], curr_col + move[1]
                    
                    if (new_row, new_col) in island2:
                        return count 
                    
                    if self.is_valid(A, island1, new_row, new_col, 0):
                        queue.append((new_row, new_col))
                        island1.add((new_row, new_col))
            count += 1
            
    def get_islands(self, grid):
        """
            0  1  2
        0 [-1,-1, 1]
        1 [ 1, 1, 1]
        2 [ 1, 1,-1]
        
        count = 2
        
        q = [, (2,1)
        
        iter1 = (1, 2)
 
        
        island1 = {(0,0), (0,1)
                   (1,0), (1, 1), (0, 2)
        }
        island2 = {(2,2)}
        
        """
        island1, island2 = set(), set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and len(island1) == 0:
                    self.add_coordinates(grid, island1, row, col)
                elif grid[row][col] == 1:
                    self.add_coordinates(grid, island2 , row, col)
                    return island1, island2
    
    def add_coordinates(self, A, island, row, col):
        queue = collections.deque([(row, col)])
        island.add((row, col))
        while queue:
            curr_row, curr_col = queue.popleft()
            A[curr_row][curr_col] = -1 
            for move in self.moves:
                new_row, new_col = curr_row + move[0], curr_col + move[1]    
                if self.is_valid(A, island, new_row, new_col, 1):
                    island.add((new_row, new_col))
                    queue.append((new_row, new_col))
        return island
    
                
    def is_valid(self, A, seen, row, col, value):
        return 0 <= row < len(A) and 0 <= col < len(A[0]) and (row, col) not in seen and A[row][col] == value
            
    
    
