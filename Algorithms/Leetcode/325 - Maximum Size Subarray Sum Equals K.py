class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ps = 0 
        seen = {}
        seen[0] = -1 
        globalMax = 0 
        for index, num in enumerate(nums):
            ps += num 
            need = ps - k 
            if need in seen:
                globalMax = max(globalMax, index - seen[need])
            if ps not in seen:
                seen[ps] = index
                
        return globalMax
