class DynamicProgramming:

    def rodcut_naive(self, lengths, profits, n):
        curr_length, curr_profit = 0, 0
        index = 0
        return self.dfs(lengths, profits, n, index, curr_length, curr_profit)


    def dfs(self, lengths, profits, n, index, curr_length, curr_profit):
        if curr_length == n:
            return curr_profit

        elif index >= len(profits) or curr_length > n:
            return 0

        cut_it = self.dfs(lengths, profits, n, index, curr_length+lengths[index], curr_profit + profits[index])
        
        leave_it = self.dfs(lengths, profits, n, index+1, curr_length, curr_profit)

        return max(cut_it, leave_it)
        
        

        


lengths = [1, 2, 3, 4, 5]
prices = [2, 6, 7, 10, 13]
dp = DynamicProgramming()
print(dp.rodcut_naive(lengths, prices, 5))
