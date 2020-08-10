class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
                    r
        [-1,3,5,1,4,2,-9]
                l
            
            
                r 
        [-2,6,6,3,5,4,1,2,8]
          l  
        """
        seen = set() 
        seen.add(0) 
        
        prefixSum = 0 
        answer = 0 
        
        for num in nums:
            
            prefixSum += num 
            need = prefixSum - target 
            
            if need in seen:
                answer += 1
                seen = set() 
                seen.add(0) 
                prefixSum = 0 
            else:
                seen.add(prefixSum) 
                
        return answer
