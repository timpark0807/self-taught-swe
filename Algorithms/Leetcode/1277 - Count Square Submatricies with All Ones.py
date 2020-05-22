class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        
        beatid hd
        
        bruteforce
        edge cases
        assumptions
        testcases
        input
        output
        
        highlevel
            keep track of count (set to 0) 
            iterate over the matrix
                check how many squares can be spawned from this point of the matrix
                    1. add the minimum of the 3 corners +1 to the count 
            return to 1 
        docstrings
        
        """
        count = 0 
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])): 
                if matrix[row-1][col-1] == 1:
                    dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                count += dp[row][col] 
    
        return count 
