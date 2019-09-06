class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return None

        i = 0 
        length = 1 
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i += 1
                length += 1
                
        return length



    def removeDuplicates_old(self, nums: List[int]) -> int:
        i, j = 0, 1

        if len(nums) == 0:
            return None
        
        length = 1 
        while j < len(nums):         # Ran a for loop with j since it will be incremented in either if or else statement
            if nums[i] == nums[j]:   # changed if case to else case
                j += 1
            else:                   
                nums[i+1], nums[j] = nums[j], nums[i+1]
                length += 1
                i += 1
                j += 1
                
        return length


##                         i       j
##[0,0,1,1,1,2,2,3,3,4]    0       1  
##[0,0,1,1,1,2,2,3,3,4]            2
##[0,0,1,1,1,2,2,3,3,4]            3
##[0,0,1,1,1,2,2,3,3,4]            4 
##[0,0,1,1,1,2,2,3,3,4]
##

arr = [0,0,1,1,1,2,2,3,3,4]
s = Solution()
print(s.removeDuplicates(arr))
