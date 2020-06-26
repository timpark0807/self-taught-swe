class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
             R 
           L
        [1,2,1,2,1,2,1]
         0 1 2 3 4 5 6
           I   J   K
           
        currSum = 3 
        [1,2,2,1,2,2,1,2,2,1,2]
         0 1 2 3 4 5 6 7 8 9 
             I     
             
        remain = 2
        [1,2,2,1,2,2,1,2]]
             I
             
        remain = 1
        [1,2,2,1,2]]
             I
             
        remain = 0 
        [1, 2]

               
             v 
        [1,2,2,3,2,3,1,3]
         0 1 2 3 4 5 6 7 8 9 
             I   J   K             
             
        Iterate over the array with index
            - try placing points down on I,
            - check if we can build that sum with triplets
            
        """
        
        for index in range(len(nums)-4): 
            currSum = sum(nums[:index])
            if index !=0 and nums[index-1] == 0 and nums[index] == 0:
                continue
            if self.dfs(nums, index+1, 2, currSum):
                return True
        return False 
    
    def dfs(self, nums, left, remain, currSum):
        if remain == 0:
            return sum(nums[left:]) == currSum 
        if left == len(nums):
            return False 
        for right in range(len(nums)+1):
            if sum(nums[left:right]) == currSum and self.dfs(nums, right+1, remain-1, currSum):
                return True
            
        return False 
    
