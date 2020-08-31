class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        
        find the path between top left and bottom right
        where the number of times we go negative is minimized 
        
        use a heap to keep track of 
            - coordinate
            - total damage taken 
            - health 
            
        
        """
        if not dungeon or not dungeon[0]: 
            return 0 
        
        if dungeon[0][0] < 0:
            damage = dungeon[0][0]
            health = 0 
        else:
            damage = 0 
            health = dungeon[0][0] 
            
        heap = [(-damage, -health, 0, 0)] # damage, health, row, col 
        seen = set() 
        
        while heap:
            
            currDamage, currHealth, currRow, currCol  = heapq.heappop(heap) 
            currHealth *= -1
            
            if [currRow, currCol] == [len(dungeon)-1, len(dungeon[0])-1]:
                return currDamage + 1
            
            for moveRow, moveCol in [(0,1),(1,0)]:
                
                newRow, newCol = currRow + moveRow, currCol + moveCol
                
                if self.inBounds(dungeon, newRow, newCol):
                    
                    newHealth = currHealth + dungeon[newRow][newCol] 
                    newDamage = currDamage 
                    
                    if newHealth < 0:
                        newDamage += -newHealth
                        newHealth = 0 
                    if (newDamage-newHealth, newRow, newCol) not in seen:
                        heapq.heappush(heap, (newDamage, -newHealth, newRow, newCol)) 
                        seen.add((newDamage-newHealth, newRow, newCol)) 
                    
        return -1 
    
    
    def inBounds(self, grid, row, col):
        return 0<=row<len(grid) and 0<=col<len(grid[0]) 
    
    
