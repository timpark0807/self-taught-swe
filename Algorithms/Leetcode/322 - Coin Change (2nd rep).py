class Solution(object):
    def coinChange(self, coins, amount):
        table = [float('inf')] * (amount + 1)
        table[0] = 0 
        
        for curr_change in range(len(table)):
            for curr_coin in coins:
                if curr_coin <= curr_change:
                    if_we_take_curr_coin = 1 + table[curr_change-curr_coin]            
                    table[curr_change] = min(table[curr_change],  1 + table[curr_change-curr_coin])
        
        if table[-1] == float('inf'):
            return - 1
        else:
            return table[-1]
        
