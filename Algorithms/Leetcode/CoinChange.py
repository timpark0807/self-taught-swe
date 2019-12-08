class DynamicProgramming:

    def coinchange_naive(self, coins, amount):
        index = len(coins) - 1
        remain = amount
        ans = self.dfs_naive(coins, index, remain)
        if ans == float('inf'):
            return -1 
        return ans

    def dfs_naive(self, coins, index, remain):
        if remain == 0:
            return 0
        elif index < 0 or remain < 0:
            return float('inf')

        take_it = self.dfs_naive(coins, index, remain-coins[index]) + 1
        leave_it = self.dfs_naive(coins, index-1, remain)

        return min(take_it, leave_it)

    
    def coinchange_memo(self, coins, amount):
        self.memo = {}
        ans = self.dfs_memo(coins, len(coins), amount)
        if ans == float('inf'):
            return -1 
        return ans

    def dfs_memo(self, coins, index, remain):
        if (index, remain) in self.memo:
            return self.memo[(index, remain)]
        
        if remain == 0:
            return 0
        elif remain < 0 or index < 0:
            return float('inf')
        
        take_it = self.dfs_memo(coins, index, remain - coins[index]) + 1          
        leave_it = self.dfs_memo(coins, index-1, remain)
        self.memo[(index, remain)] = min(take_it, leave_it)
        return min(take_it, leave_it) 

    
    def coinchange_table(self, coins, amount):
        dp = [[float('inf') for _ in range(amount+1)] for _ in coins]
        
        for row in dp:
            row[0] = 0

        for index in range(len(dp)):
            for remain in range(len(dp[0])):
                take_it = dp[index][remain]
                if remain - coins[index] >= 0:
                    take_it = dp[index][remain-coins[index]] + 1
                leave_it = dp[index-1][remain]
                dp[index][remain] = min(take_it, leave_it)
                
        return dp[-1][-1]
                            
                        

dp = DynamicProgramming()
print(dp.coinchange_naive([1,2,5], 6))
print(dp.coinchange_naive([2], 3))

c = [2, 3, 5]
t = 7
print(dp.coinchange_naive(c, t))
print(dp.coinchange_table([1,2,5], 6))
