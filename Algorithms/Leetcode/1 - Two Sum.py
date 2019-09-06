"""
Brute Force solution
O(n^2)
"""

def twoSum(nums, target):
    ans = []
    for index in range(0, len(nums)):
        for index2 in range(index+1, len(nums)):
            compare = nums[index] + nums[index2]
            if compare == target:
                ans.append(index)
                ans.append(index2)
    return ans


def two_sum_optimize(nums, target):
    index = {}
    for i, x in enumerate(nums):
        if target - x in index:
            return [index[target-x], i]
        index[x] = i


arr = [3,2,3]
ans = two_sum_optimize(arr, 6)
print(ans)
