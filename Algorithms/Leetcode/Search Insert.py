class Solution:
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid
                
            elif nums[mid] > target:
                high = mid 

        if nums[mid] < target:
            return mid + 1
        else:
            return mid
