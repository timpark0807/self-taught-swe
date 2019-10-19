class Solution(object):
    def findErrorNums(self, nums):
        count = [0] * (len(nums)+1)
        
        for num in nums:
            count[num] += 1
            
        for num in range(1, len(count)):
            if count[num] == 2:
                x = num
            elif count[num] == 0:
                y = num 
                
        return [x, y]
        
        
        
    def findErrorNums3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        # Time: O(n)
        # Space: O(n)
        """
        
        output = []        
        d = dict()
        
        # Find duplicated number 
        # Time: O(n)
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                output.append(num)
                break
        
        # Find missing number 
        # Time: O(n)
        n = len(nums) 
                    
        for index in range(1, n+1):
            if index not in nums:
                output.append(index)
    
        return output    
    
    
    
    def findErrorNums2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        # Time: O(nlogn)
        # Space: O(1)
        
        """
        
        output = []
        nums = sorted(nums)    # Time O(nlogn)
        
        n = nums[-1]  
        
        # Find duplicated number 
        # Time: O(n)
        for index in range(2, n):
            if nums[index - 1] == nums[index]:
                output.append(nums[index])
                break
        
        # Find missing number 
        # Time: O(n)
        for index in range(1, n):  # [1, 2, 3, 4]
            if index not in nums:
                output.append(index)
                break
              
        return output
    
