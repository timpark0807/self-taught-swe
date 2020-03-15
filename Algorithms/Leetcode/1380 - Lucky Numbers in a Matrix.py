class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        matrix = [[3, 7, 8],
                  [9,11,13],
                  [15,16,17]]
                  
        matrix = [[ 1,10, 4, 2]
                  [ 9, 3, 8, 7] 
                  [15,16,17,12]]
        
        1. Find the minimum element in the row 
        2. Check that column maximum 
        
        """
        if len(matrix) == 1:
            return [min(matrix[0])]
        rows = len(matrix)
        cols = len(matrix[0]) 
        
        max_nums = {}
        
        for col in range(cols):
            local_max = 0 
            for row in range(rows):
                local_max = max(local_max, matrix[row][col])
                
            max_nums[col] = local_max
            
        
        lucky = [] 
        
        for row in matrix:
            curr_min = min(row) 
            min_index = row.index(curr_min)
            if curr_min == max_nums[min_index]:
                lucky.append(curr_min)
            
            
        return lucky 
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
