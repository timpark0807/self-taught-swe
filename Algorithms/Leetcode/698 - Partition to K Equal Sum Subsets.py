class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0:
            return False
        
        self.subset_sum = sum(nums) // k 
        seen = set()
        nums.sort(reverse=True)
        return self.dfs(nums, seen, 0, k, 0)
    
    
    def dfs(self, nums, seen, currsum, k, start):
        if k == 1:
            return True
        if currsum == self.subset_sum:
            return self.dfs(nums, seen, 0, k-1, 0)
        for index in range(start, len(nums)):
            if index not in seen and nums[index] + currsum < self.subset_sum:
                seen.add(index)
                if self.dfs(nums, seen, currsum + nums[index], k, index+1):
                    return True
                seen.remove(index)

        return False 
s = Solution()


arr = [5,2,5,5,5,5,5,5,5,5,5,5,5,5,5,3]
target = 15
print(s.canPartitionKSubsets(arr, target))


arr = [2,2,2,2,3,4,5]
target = 4
print(s.canPartitionKSubsets(arr, target))
"""
arr = [1,1,1,1,1,1,1,1,1,1]
target = 5
print(s.canPartitionKSubsets(arr, target))

print(s.canPartitionKSubsets(arr, target))
arr = [2,2,10,5,2,7,2,2,13]
target = 3
print(s.canPartitionKSubsets(arr, target))

"""
