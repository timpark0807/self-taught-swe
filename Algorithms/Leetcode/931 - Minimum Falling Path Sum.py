class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        
        [[1,2,3],
         [4,5,6],
         [7,8,9]]

        State: row, col

        Decision: Go Down Down, Down Left, or Down Right
        """
        global_max = float('inf')
        self.memo = {}

        for index in range(len(A[0])):
            global_max = min(global_max, self.dp(A, index, 0))
            
        return global_max
    
    
    def dp(self, A, index, row):
        if (row, index) in self.memo:
            return self.memo[(row, index)]
        
        if index < 0 or index >= len(A[0]):
            return float('inf')
        
        if row == len(A)-1:
            return A[row][index]
        
        go_down = self.dp(A, index, row+1) + A[row][index]
        go_left = self.dp(A, index-1, row+1) + A[row][index]
        go_right = self.dp(A, index+1, row+1) + A[row][index]
        self.memo[(row, index)] = min(go_down, go_left, go_right)
        return self.memo[(row, index)]
        
