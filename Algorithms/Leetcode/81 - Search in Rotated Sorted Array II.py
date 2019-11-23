class Solution:
    def search(self, nums: List[int], target: int) -> int:

"""

target = 1

             r
        l 
nums = [1, 3, 1, 1, 1]
        0  1  2  3  4 
              m 

"""


        
        if len(nums) == 0:
            return False
        
        arr = nums
        left = 0
        right = len(arr) - 1

        while left <= right:
            while right > 0 and arr[right] == arr[right-1]:
                right -= 1
            while left < len(arr) - 1 and arr[left] == arr[left+1]:
                left += 1

            
            mid = (left + right) // 2

            if arr[mid] == target:
                return True

            elif arr[mid] >= arr[left]:
                if target >= arr[left] and target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= arr[right] and target > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


