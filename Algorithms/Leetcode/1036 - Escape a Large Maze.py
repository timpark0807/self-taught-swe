class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        
        stack = [(row, col)] -> start with source 
        place blocked spots in a set -> to take advantage of O(1) containment 
        
        while there are elements in the stack
            remove from stack 
            if current coordinate is target: return True
            
            for direction in each 4 direction
                calculate the new direction
                if the new direction isValid aka (1) inbounds, (2) not in seen, and (3) not blocked 
                    add the new direction coordinate to stack to process 
                    add the new driection coordinate to seen 
            
        return False 
        
        """
        if not blocked:
            return True
        return self.bfs(blocked, source, target) and self.bfs(blocked, target, source)
     
    def bfs(self, blocked, source, target):
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        blockedSet = set([(bRow, bCol) for bRow, bCol in blocked]) 

        heap = [(0, 0, source[0], source[1])]
        seen = set((source[0], source[1]))
        
        while heap:
            currDist, currMoves, currRow, currCol = heapq.heappop(heap) 
            if [currRow, currCol] == target or len(seen) > 20000:
                return True
            for move in moves:
                newRow, newCol = currRow + move[0], currCol + move[1]
                if self._isValid(blockedSet, newRow, newCol, seen):
                    newDist = self.getNewDist(newRow, newCol, target) 
                    heapq.heappush(heap, (newDist+1, currMoves+1, newRow, newCol))
                    seen.add((newRow, newCol)) 
        return False 
    
    def getNewDist(self, row, col, target):
        return abs(row-target[0]) + (col-target[1]) 
    
    def _isValid(self, blockedSet, row, col, seen):
        return 0<=row<1000000 and 0<=col<1000000 and (row, col) not in seen and (row,col) not in blockedSet 
