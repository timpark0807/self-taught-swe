class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        left = self.find(nums, target, 'L')
        right = self.find(nums, target, 'R')
        return [left, right]

    def find(self, nums, target, side):
        left, right = 0, len(nums)-1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                answer = mid
                if side == 'L':
                    right = mid - 1
                elif side == 'R':
                    left = mid + 1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return answer

s=Solution()
arr = [5, 7, 7, 8, 8, 10]
print(s.searchRange(arr, 8))



    
