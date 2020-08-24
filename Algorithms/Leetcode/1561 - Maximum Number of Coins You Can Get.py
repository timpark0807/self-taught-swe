class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        
        
        [1, 2, 2, 4, 7, 8]
         0  1  2  3  4  5
         
        [9,8,7,6,5,1,2,3,4]
        
             l   r
        [1,2,3,4,5,6,7,8,9]
        
        
        8, 6, 4
        """
        piles.sort() 
        
        left, right = 0, len(piles)-1 
        coins = 0 
        
        while left < right:
            coins += piles[right-1]
            right -= 2
            left += 1

        return coins 
    
