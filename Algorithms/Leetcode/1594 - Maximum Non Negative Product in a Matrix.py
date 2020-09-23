class Solution(object):
    def maxProductPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        Optimization problem 
            - Greedy 
            - Dynamic Programming
        ans = self.dp(grid, 0, 0) 
        return ans % (10**9 + 7) if ans >= 0 else -1
    
    def dp(self, grid, row, col):
        if (row, col) == (len(grid)-1, len(grid[0])-1):
            return grid[row][col]
        
        moveRight, moveDown = 0, 0
        
        
    
    def greedy():

           [1,-2,1]
           [1,-2,1]
           [3,-4,1]

        heap -> store the coordinate and the current product
                sort the heap based on the current product
                max heap 
                
        use a heap to do a greedy bfs 
        
        while elements in the heap
            remove coordinate and product 
            if current coordinate is target, return the current product             
            check down and right moves
                if in bounds
                    add to heap and update coordinate and product
        """
        self.memo = {} 
        ans = self.dp(grid, 0, 0, grid[0][0]) 
        return ans % (10**9 + 7) if ans >= 0 else -1
    
    
    def dp(self, grid, row, col, currProduct):
        if (row, col, currProduct) in self.memo:
            return self.memo[(row, col, currProduct)]
        if (row, col) == (len(grid)-1, len(grid[0])-1):
            return currProduct
        
        moveRight, moveDown = float('-inf'), float('-inf')
        
        if row + 1 < len(grid):
            moveDown = self.dp(grid, row+1, col, currProduct * grid[row+1][col]) 
            
        if col + 1 < len(grid[0]):
            moveRight = self.dp(grid, row, col+1, currProduct * grid[row][col+1]) 
         
        self.memo[(row, col, currProduct)] = max(moveRight, moveDown) 
        return max(moveRight, moveDown) 
    
        
        
        
        
    def greedy():
        
        heap = [(-grid[0][0], 0, 0)]  # product, row, col 
        targetRow, targetCol = len(grid)-1, len(grid[0])-1
        moves = [(0,1),(1,0)]
        ans = float('-inf') 
        seen = set() 
        
        while heap:
            currProduct, currRow, currCol = heapq.heappop(heap)
            currProduct *= -1 

            if (currRow, currCol, currProduct) in seen:
                continue 
            
            seen.add((currRow, currCol, currProduct))
            
            if (currRow, currCol) == (targetRow, targetCol):
                ans = max(ans, currProduct)
                continue 
                
            for moveRow, moveCol in moves:
                newRow, newCol = currRow+moveRow, currCol+moveCol 
                if 0<=newRow<len(grid) and 0<=newCol<len(grid[0]):  # if in bounds 
                    newProduct = currProduct * grid[newRow][newCol] 
                    heapq.heappush(heap, (-newProduct, newRow, newCol)) 

        return ans % (10**9 + 7) if ans >= 0 else -1
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
