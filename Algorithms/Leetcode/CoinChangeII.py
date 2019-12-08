class DynamicProgramming:
    """
    Dynamic Programming
    1. State
        - index, remaining
    2. Recurrence Relation
        - Leave Current Coin = change(index-1, remaining)
        - Take Current Coin = change(index, remaining-coins[index])
        - change(index, remaining) = change(index-1, remaining) + change(index, remaining-coins[index])
    3. Base Case
        - remaining == 0
            -> return 1
        - index < 0 or remaining < 0
            -> return 0 
    3. Naive Recursive Solution
    4. Memoized Recursive Solution
    5. Tabulated Solution
    """
    def change_naive(self, amount, coins):
        return self.dfs_naive(coins, len(coins)- 1, amount)

    def dfs_naive(self, coins, index, remain):
        if remain == 0:
            return 1
        elif remain < 0 or index < 0:
            return 0

        leave_it = self.dfs_naive(coins, index-1, remain)
        take_it = self.dfs_naive(coins, index, remain - coins[index])

        return take_it + leave_it 

    def change_memo(self, amount, coins):
        self.memo = {}
        return self.dfs_memo(coins, len(coins)- 1, amount)
    
    def dfs_memo(self, coins, index, remain):
        if (index, remain) in self.memo:
            return self.memo[(index, remain)]
        if remain == 0:
            return 1
        elif remain < 0 or index == -1:
            return 0

        leave_it = self.dfs_memo(coins, index-1, remain)
        take_it = self.dfs_memo(coins, index, remain - coins[index])
        self.memo[(index, remain)] = leave_it + take_it 
        return take_it + leave_it 

    def change_table(self, amount, coins):
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins)+1)]
            
        for index in range(1, len(dp)):
            dp[index][0] = 1
            for remain in range(1, len(dp[0])):
                if remain < coins[index-1]:
                    dp[index][remain] = dp[index-1][remain]
                else:
                    take_it = 0
                    if remain-index >= 0:
                        take_it = dp[index][remain-coins[index-1]]
                    leave_it = dp[index-1][remain]
                    dp[index][remain] = take_it + leave_it

        for row in dp:
            print(row)
            
        return dp[-1][-1]
    
dp = DynamicProgramming()
print(dp.change_table(5, [1, 2, 5]))

print(dp.change_table(100, [1, 101, 102, 103]))


















