class Solution(object):
    def maxSubArray(self, nums):
        """
        
        Input: [-2,1,-3,4,-1,2,1,-5,4]
                   i 
        
        current_max = 1
        global_max  = -2 
        
        1. Initialize pointers left and right
        2. Take current sum 
        
        """
        if len(nums) == 0:
            return 0 
        
        current_max, global_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            current_max = max(current_max + nums[i], nums[i])
            
            global_max = max(global_max, current_max)
            
        return global_max
            
        
