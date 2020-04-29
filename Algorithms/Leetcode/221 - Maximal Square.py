class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp = [[0 for _ in matrix[0]] for _ in matrix]
        max_square = 0 
        for row in range(len(dp)):
            for col in range(len(dp[row])):
                if matrix[row][col] == "1":
                    dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row][col-1]) + 1
                    max_square = max(max_square, dp[row][col]) 
        return max_square * max_square
    
    
