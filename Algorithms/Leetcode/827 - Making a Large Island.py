class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
         [1, 1]
         [1, 0]
        
        # preprocess 
             - key: coordinates  value: island id
             - key: island id    value: size of island
             
        # iterate over the grid (rows then columns) 
            - if the current coordinate is a zero: "create" an island here 
                -> init a local seen set 
                -> init a current count at 1 
                -> for each of the 4 directions 
                    - look at the mapping of coordinate to island id 
                    - add the size of the island id to current count 
                    - add island to locally seen 
                -> update globalMax
        
        return globalMax
        
        """
        self.moves = [(0,1),(0,-1),(1,0),(-1,0)]
        coordToId, IdToSize = self.getMapping(grid)
        globalMax = max(IdToSize.values()) if len(IdToSize) >= 1 else 0 
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                
                if grid[row][col] == 0:
                    localSeen = set() 
                    currCount = 1 
                    
                    for move in self.moves:
                        newRow, newCol = row + move[0], col + move[1]
                        if self.isValid(grid, newRow, newCol) and coordToId[(newRow, newCol)] not in localSeen:
                            localSeen.add(coordToId[(newRow, newCol)])
                            currCount += IdToSize[coordToId[(newRow, newCol)]]
                        
                    globalMax = max(globalMax, currCount) 
                        
                        
        return globalMax 
    
    def getMapping(self, grid):
        coordToId = collections.defaultdict(int)
        IdToSize = collections.defaultdict(int)
        currId = 1 
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in coordToId:
                    IdToSize[currId] = self.dfs(grid, row, col, coordToId, currId) 
                    currId += 1
        return coordToId, IdToSize
        
        
    def dfs(self, grid, row, col, coordToId, currId):
        stack = [(row, col)]
        coordToId[(row, col)] = currId 
        size = 1 
        
        while stack:
            currRow, currCol = stack.pop() 
            for move in self.moves:
                newRow, newCol = currRow + move[0], currCol + move[1]
                if self.isValid(grid, newRow, newCol) and (newRow, newCol) not in coordToId and grid[newRow][newCol] == 1:
                    stack.append((newRow, newCol))
                    coordToId[(newRow, newCol)] = currId 
                    size += 1
                    
        return size
    
    
    def isValid(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
