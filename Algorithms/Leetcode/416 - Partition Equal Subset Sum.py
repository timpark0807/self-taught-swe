class Solution(object):
    def canPartition(self, nums):
        if not nums:
            return True
        elif max(nums) > sum(nums) // 2:
            return False
        elif sum(nums) % 2 != 0:
            return False
            
        target = sum(nums) // 2

        dp = [False for _ in range(target+1)]
        dp[0] = True
        
        for num in nums:
            for j in reversed(range(1, len(dp))):
                if j >= num:
                    dp[j] = dp[j] or dp[j-num]
                    

        return dp[-1]

s = Solution()
nums = [2, 2, 3, 5]
print(s.canPartition(nums))
