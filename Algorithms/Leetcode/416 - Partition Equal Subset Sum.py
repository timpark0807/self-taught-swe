class Solution(object):
    def canPartition(self, nums):
        """
        Explanation for memoization needs to be reviewed:
        
        1. https://leetcode.com/problems/partition-equal-subset-sum/discuss/90610/Python-Backtracking-with-Memoization-Solution
        2. https://leetcode.com/problems/partition-equal-subset-sum/discuss/90640/simple-dfs-python-with-memo-beats-98
        """
        if not nums:
            return True
        elif max(nums) > sum(nums) // 2:
            return False
        elif sum(nums) % 2 != 0:
            return False
        
        target = sum(nums) // 2
        seen = set()
        return self.dfs(nums, target, seen, 0, {})
        
    def dfs(self, nums, target, seen, curr_sum, d):
        if curr_sum in d: 
            return d[curr_sum]
        if curr_sum == target:
            d[curr_sum] = True
        else:
            d[curr_sum] = False
            for index in range(len(nums)):
                if index not in seen and curr_sum + nums[index] <= target:
                    seen.add(index)
                    if self.dfs(nums, target, seen, curr_sum + nums[index], d):
                        d[curr_sum] = True
                        break
                    seen.remove(index)

        return d[curr_sum]
