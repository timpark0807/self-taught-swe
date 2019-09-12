class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        boundary = 0
        fast = 1            
            
        while fast < len(nums):
            
            if nums[boundary] != nums[fast]:
                
                nums[boundary+1], nums[fast] = nums[fast], nums[boundary+1]
                boundary += 1
                
            fast += 1
                            
        return boundary+1
