class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        
        order = self._get_order(forest) 
        steps = 0 
        start_row, start_col = 0, 0 
        
        while order: 
            _, target_row, target_col = heapq.heappop(order) 
            curr_steps = self.bfs(forest, start_row, start_col, target_row, target_col) 
            if curr_steps == float('inf'):
                return -1 
            steps += curr_steps
            start_row, start_col = target_row, target_col
        return steps
    
    
    def bfs(self, forest, start_row, start_col, target_row, target_col):
        queue = collections.deque([(0, start_row, start_col)])
        seen = set([(start_row, start_col)])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue:
            curr_dist, curr_row, curr_col = queue.popleft()
            
            if (curr_row, curr_col) == (target_row, target_col):
                return curr_dist
            
            for move in moves:
                new_row, new_col = curr_row + move[0], curr_col + move[1]
                if self._is_valid(forest, new_row, new_col, seen):
                    seen.add((new_row, new_col))
                    queue.append((curr_dist + 1, new_row, new_col))
                    
        return float('inf') 
    
    
    def _is_valid(self, forest, row, col, seen):
        return 0 <= row < len(forest) and 0 <= col < len(forest[row]) and (row, col) not in seen and forest[row][col] != 0 
            
        
    def _get_order(self, forest):
        temp = [] 
        
        for row in range(len(forest)):
            for col in range(len(forest[row])):
                if forest[row][col] != 0:
                    heapq.heappush(temp, (forest[row][col], row, col))
                        
        return temp     
    
            
            
        
