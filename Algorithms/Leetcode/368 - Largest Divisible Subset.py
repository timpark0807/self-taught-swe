class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        if not nums:
            return [] 
        nums.sort() 
        dp = [[num] for num in nums]
        for last in range(1, len(dp)):
            for inside in range(last):
                insideNum = dp[inside][-1]
                if nums[last] % insideNum == 0 or insideNum % nums[last] == 0:
                    dp[last] = max(dp[last], dp[inside]+[nums[last]], key=len) 

        
        return max(dp, key=len) 
