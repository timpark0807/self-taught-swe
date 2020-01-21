class Solution:
    def countServers(self, grid):
        seen = set()
        number_of_servers = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    potential_servers = self.four_directional_search(grid, row, col, seen)
                    if potential_servers > 1:
                        number_of_servers += potential_servers 
        return number_of_servers

    def four_directional_search(self, grid, row, col, seen):
        count = 1
        for new_row in range(len(grid)):
            if (new_row, col) not in seen:
                seen.add((new_row, col))
                if grid[new_row][col] == 1:
                    count += self.four_directional_search(grid, new_row, col, seen)
    
        for new_col in range(len(grid[0])):
            if (row, new_col) not in seen:
                seen.add((row, new_col))
                if grid[row][new_col] == 1:
                    count += self.four_directional_search(grid, row, new_col, seen)
                    
        return count
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
