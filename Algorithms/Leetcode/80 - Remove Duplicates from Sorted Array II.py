class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        if len(nums) < 3:
            return len(nums)+1
        
        
        for index in range(1,len(nums)-1):
            if nums[index-1] != nums[index+1]:
                nums[count] = nums[index]
                count += 1
                
        nums[count] = nums[-1]
        
        return count + 1
