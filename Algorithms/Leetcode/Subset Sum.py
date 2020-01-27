class DynamicProgramming:

    def subset_naive(self, nums):
        if sum(nums) % 2 != 0:
            return False
        
        needed = sum(nums) // 2
        index = len(nums) - 1
        
        return self.dfs_naive(nums, needed, index)

    def dfs_naive(self, nums, needed, index):
        if needed == 0:
            return True
        elif index == -1:
            return False
        
        take_it = 0
        if needed - nums[index] >= 0:
            take_it = self.dfs_naive(nums, needed - nums[index], index-1)

        leave_it = self.dfs_naive(nums, needed, index-1)

        return take_it or leave_it

    def subset_memo(self, nums):
        if sum(nums) % 2 != 0:
            return False
        
        needed = sum(nums) // 2
        index = len(nums) - 1
        
        self.memo = {}
        
        return self.dfs_memo(nums, needed, index)


    def dfs_memo(self, nums, needed, index):
        if (needed, index) in self.memo:
            return self.memo[(needed, index)]
        
        if needed == 0:
            self.memo[(needed, index)] = True
            return self.memo[(needed, index)]

        elif index == -1:
            self.memo[(needed, index)] = False
            return False

        take_it = False
        if needed - nums[index] >= 0:
            if self.dfs_memo(nums, needed - nums[index], index-1):
                self.memo[(needed, index)] = True
                return self.memo[(needed, index)]

        leave_it = self.dfs_memo(nums, needed, index-1)

        self.memo[(needed, index)] = leave_it
        
        return self.memo[(needed, index)]


        

dp = DynamicProgramming()
print(dp.subset_memo(nums))
