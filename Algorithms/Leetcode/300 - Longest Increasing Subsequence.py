class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0 
        
        longest = [1] * len(nums) 
        
        for outside in range(len(nums)):
            for inside in range(outside):
                if nums[outside] > nums[inside]:
                    longest[outside] = max(longest[outside], longest[inside]+1)
        return max(longest) 
