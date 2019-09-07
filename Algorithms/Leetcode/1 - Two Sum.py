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
    
def twosum(arr, target):
    arr.sort()
    low, high = 0, len(arr) - 1
    while low < high:
        if arr[low] + arr[high] == target:
            return arr[low], arr[high]
        elif arr[low] + arr[high] < target:
            low += 1
        else:
            high -= 1
            
    return False

arr = [3,2,3]
ans = twosum(arr, 6)
print(ans)
