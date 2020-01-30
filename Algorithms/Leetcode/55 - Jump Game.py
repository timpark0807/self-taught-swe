class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True 
        return self.backtrack(nums, 0)
        
        
    def backtrack(self, nums, curr_index):
        if curr_index == len(nums) - 1:
            return True
        
        for jump in range(1, nums[curr_index]+1):
            if curr_index + jump < len(nums):
                if self.backtrack(nums, curr_index + jump):
                    return True
        return False

s = Solution()
nums = [2,3,1,1,4]
s.canJump(nums)
