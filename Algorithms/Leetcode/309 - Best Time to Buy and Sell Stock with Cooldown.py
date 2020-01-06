class Solution:
    def maxProfit(self, prices):
        if len(prices) == 2 and prices[1] > prices[0]:
            return prices[1] - prices[0]
        
        index = 0
        curr_stock = 0
        return self.dfs_naive(prices, index, curr_stock)
    
    
    def dfs_naive(self, prices, index, curr_stock):
        if index == len(prices):
            return 0
        if index > len(prices):
            return float('-inf')
        
        buy = 0
        if curr_stock == 0:
            buy = self.dfs_naive(prices, index + 1, prices[index])
            
        sell = 0
        if curr_stock != 0:
            sell = self.dfs_naive(prices, index + 2, 0) + curr_stock 
        
        return max(buy, sell)

s = Solution()
print(s.maxProfit([1, 2, 4]))
