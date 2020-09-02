class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        
        get the location of each server on the grid 
        add that row and column to a coordinates set 
        
        iterate over the servers in the grid 
            check if there is another server in that row or column 
                increment 1 if ture
            
        """
        
        servers = [] 
        coordinates = collections.defaultdict(list) 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    servers.append((row, col)) 
                    coordinates['R'+str(row)].append((row,col))
                    coordinates['C'+str(col)].append((row,col)) 
        count = 0 
        seen = set() 
        for (serverRow, serverCol) in servers: 
            
            if len(coordinates['R'+str(serverRow)]) > 1:
                count += 1
                
            elif len(coordinates['C'+str(serverCol)]) > 1:
                count += 1
                
        return count 
