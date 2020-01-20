import collections

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        
        
        # Find every gate coordinate 
            # Add to queue
        
        # While there are gates in the queue
            # Deque everything in the queue per iteration
            # Set every room touching the gate to the distance
        
        # 
        """
        if not rooms:
            return rooms 
        
        queue = self.get_gate_coordinates(rooms)
        levels = 1 
        moves = [(0, 1), (0, -1), (1, 0), (-1,0)]
        
        while queue:
            for _ in range(len(queue)):
                curr_row, curr_col = queue.popleft() 
                for move in moves:
                    new_row, new_col = curr_row + move[0], curr_col + move[1]
                    if self.is_valid(rooms, new_row, new_col):
                        rooms[new_row][new_col] = levels
                        queue.append((new_row, new_col))
            levels += 1
            
    def is_valid(self, rooms, row, col):
        if 0 <= row < len(rooms) and 0 <= col < len(rooms[0]) and rooms[row][col] == 2147483647:
            return True
        
    
    def get_gate_coordinates(self, rooms):
        q = collections.deque()
        
        for row in range(len(rooms)):
            for col in range(len(rooms[row])):
                if rooms[row][col] == 0:
                    q.append((row, col))
                    
        return q
    
        
