class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        [0,2]
        [1,3]
        
        path with the minimum maximum value 
        
        use a heap 
            -> store in a tuple
            -> (max value in this path, coordinate) 
            
        while there are elements in the heap 
            - remove from the heap
            
            if this coordinate is the bottom right
                - reutrn the min max value 
            for move in each 4 directions
                - if that move is valid
                    - update the min max value and push it to the heap 
                    
        return -1 
        
        """
        heap = [(grid[0][0], 0 , 0)]
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set() 
        
        while heap:
            currVal, currRow, currCol = heapq.heappop(heap) 
            
            if currRow == len(grid)-1 and currCol == len(grid[0])-1:
                return currVal 
            
            for moveRow, moveCol in moves:
                newRow, newCol = currRow + moveRow, currCol + moveCol 
                
                if 0<=newRow<len(grid) and 0<=newCol<len(grid[newRow]):
                    newVal = max(currVal, grid[newRow][newCol])
                    
                    if (newRow, newCol) not in seen:
                        heapq.heappush(heap, (newVal, newRow, newCol))
                        seen.add((newRow, newCol)) 
