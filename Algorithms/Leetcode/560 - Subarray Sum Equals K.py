class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        prefix = collections.defaultdict(int) 
        
        curr = 0
        count = 0 
        
        for num in nums:
            prefix[curr] += 1
            curr += num
            if curr - k in prefix.keys():
                count += prefix[curr-k]
            
        return count 
