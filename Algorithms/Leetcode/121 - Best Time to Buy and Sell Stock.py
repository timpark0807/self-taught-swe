class Solution(object):
    def maxProfit(self, prices):
        """
        States:
            - What variables will we need to keep track of to solve this problem?
            1. Index -> What day we are on 
            2. Curr_Stock

        What choices do we have:
            1. Buy = optimal(index + 1, curr_profit - prices[index])
            2. Do nothing = optimal(index+1, curr_profit) 
            3. Sell = optimal(index+1, curr_profit + prices[index])

        Base Case:
            
        """
        return self.dp(prices, 0, 0)
    
    
    def dp(self, prices, index, curr_profit):
        if index >= len(prices) or curr_profit > 0:
            return curr_profit
        
        buy, sell = float('-inf'), float('-inf')
        hold = self.dp(prices, index+1, curr_profit)
        if curr_profit == 0:
            buy = self.dp(prices, index+1, curr_profit - prices[index])
        elif prices[index] >= abs(curr_profit):
            sell = self.dp(prices, index+1, curr_profit + prices[index])
        
        return max(buy, sell, hold)

s = Solution()
print(s.maxProfit([2,1,2,1,0,1,2]))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
