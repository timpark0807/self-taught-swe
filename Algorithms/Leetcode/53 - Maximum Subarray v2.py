class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

          
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
          0  1   2  3   4  5  6   7  8 
              ^ 
    dp= [-2, 1, -2, 4, 3 , 5, 6, 1 
    
    global_max = 6 
    
        """
        ans = [nums[0] for _ in range(len(nums))]
        
        for index in range(1, len(nums)):
            ans[index] = max(nums[index], ans[index-1] + nums[index])
    
        return max(ans) 
    
    
    
    
    
    
    
            
