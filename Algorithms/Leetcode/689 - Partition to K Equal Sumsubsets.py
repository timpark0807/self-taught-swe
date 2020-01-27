class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k 
        seen = set() 
        buckets = [[] for _ in range(k)]
        sums = [0] * k
        return self.backtrack(nums, target, 0, k, seen, 0)

    def backtrack(self, nums, target, bucket_sum, k, seen, index):
        if k == 1:
            return True
        
        if bucket_sum == target: 
            return self.backtrack(nums, target, 0, k-1, seen, 0)
        
        for index_num, num in enumerate(nums, start = index):
            if index_num not in seen and bucket_sum + num <= target:
                seen.add(index_num)
                if self.backtrack(nums, target, bucket_sum + num, k, seen, index_num+1):
                    return True
                seen.remove(index_num)
                
        return False

    
s = Solution()
num1 = [4, 3, 2, 3, 5, 2, 1]
nums = [2,2,10,5,2,7,2,2,13]
k = 4

print(s.canPartitionKSubsets(num1, k))
