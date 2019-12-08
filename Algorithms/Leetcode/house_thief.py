class DynamicProgramming:
    def housethief_naive(self, houses):
        index = len(houses) - 1
        curr_profit = 0
        return self.dfs_naive(houses, index, curr_profit)

    def dfs_naive(self, houses, index, curr_profit):
        """

         0  1  2  3  4
        [2, 5, 1, 3, 5]
                     i
        """
        if index < 0:
            return curr_profit

        take_it = self.dfs_naive(houses, index-2, curr_profit + houses[index])
        leave_it = self.dfs_naive(houses, index-1, curr_profit)

        return max(take_it, leave_it)
    
    def housethief_memo(self, houses):
        index = len(houses) - 1
        curr_profit = 0
        self.memo = {}
        return self.dfs_memo(houses, index, curr_profit)

    def dfs_memo(self, houses, index, curr_profit):
        if (index, curr_profit) in self.memo:
            return self.memo[(index, curr_profit)]
        
        if index < 0:
            return curr_profit

        take_it = self.dfs_memo(houses, index-2, curr_profit + houses[index])
        leave_it = self.dfs_memo(houses, index-1, curr_profit)
        self.memo[(index, curr_profit)] = max(take_it, leave_it)
        return max(take_it, leave_it)

    def housethief_table(self, houses):
        dp = [0 for len(houses+1)]
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])
        
        for index in len(2, dp):
            take_it = houses[index] + dp[index-2]
            leave_it = dp[index-1]
            dp[index] = max(take_it, leave_it)

        return dp[-1]
            

    
dp = DynamicProgramming()
houses = [2, 5, 1, 3, 6, 2, 4]
print(dp.housethief_memo(houses))









              
