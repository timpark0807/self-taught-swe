class Solution:
    def canPartition_naive(self, nums):
        """
        state
            curr sum

        recurrence
            take_it = f(remain - nums[index], index-1)
            leave_it = f(remain, index-1)
            f(target, index) =

        base case
            remain == 0
            run out of elements -> index < 0
        """
        if sum(nums)% 2 != 0:
            return False
        remain = sum(nums) // 2
        index = len(nums) - 1
        return self.dfs_naive(nums, remain, index)

    def dfs_naive(self, nums, remain, index):
        if remain == 0:
            return True
        if index < 0 or remain < 0:
            return False

        take_it = self.dfs_naive(nums, remain-nums[index], index-1)
        leave_it = self.dfs_naive(nums, remain, index-1)

        return take_it or leave_it

    def canPartition_memo(self, nums: List[int]) -> bool:
        if sum(nums)% 2 != 0:
            return False
        self.memo = {}
        remain = sum(nums) // 2
        index = len(nums) - 1
        return self.dfs_naive(nums, remain, index)

    def dfs_naive(self, nums, remain, index):
        if (remain, index) in self.memo:
            return self.memo[(remain, index)] 
        if remain == 0:
            return True
        elif index == -1 or remain < 0:
            return False

        self.memo[(remain, index)] = self.dfs_naive(nums, remain-nums[index], index-1) or self.dfs_naive(nums, remain, index-1)
        return self.memo[(remain, index)]
    
s = Solution()
s.canPartition_naive([1, 5, 11, 5])
