import math

class Solution(object):
    def numSquares_recurse(self, n):
        """
        Unbounded knapsack.

        Create Squares Array

        States = remaining, index
        """
        squares = []
        for i in range(1, n//2):
            squares.append(i**2)
        self.memo = {}
        return self.dfs_naive(squares, n, len(squares)-1)

    def dfs_naive(self, squares, remain, index):
        if (remain, index) in self.memo:
            return self.memo[(remain, index)]
        if remain == 0:
            return 0
        if index < 0 or remain < 0:
            return float('inf')

        self.memo[(remain, index)] = min(self.dfs_naive(squares, remain-squares[index], index) + 1,
                                         self.dfs_naive(squares, remain, index-1))
        return self.memo[(remain, index)]

    def numSquares(self, n):
        squares = []
        temp = int(math.sqrt(n))
        for i in range(1, temp+1):
            squares.append(i**2)
        dp = [[float('inf') for _ in range(n+1)] for _ in range(len(squares))]
    
        for row in dp:
            row[0] = 0
        for index in range(len(dp)):
            for remain in range(len(dp[0])):
                if squares[index] > remain:
                    dp[index][remain] = dp[index-1][remain]
                else:
                    if remain - squares[index] >= 0:
                        take_it = dp[index][remain-squares[index]] + 1
                    else:
                        take_it = float('inf')
                    leave_it = dp[index-1][remain]
                    dp[index][remain] = min(take_it, leave_it)

        return dp[-1][-1]


        
s = Solution()
print(s.numSquares(7927))
