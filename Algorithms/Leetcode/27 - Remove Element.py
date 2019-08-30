class Solution:
    def removeElement(self, nums, val):
    """
    O(n)

    2 Pointer solution

    Mistake: not using range(len(num)), swapped value at index (val) instead of index of current iteration
                -> for index in nums:
                       if index != val:
                            nums[index], nums[boundary] = nums[boundary], nums[index]
                            ....
                            
                -> for index in nums: -> [3, 2, 2, 3]
                -> When index == val, val = 3 therefore index = 3
                -> Kept swapping boundary position with 3rd index

        Correct: -> for index in range(len(nums)): -> [0, 1, 2, 3]
                    -> swaps boundary with index
    """
            
        count = 0 
        boundary = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[index], nums[boundary] = nums[boundary], nums[index]
                boundary += 1
                count += 1 
        
        return count

        
if __name__ == '__main__':
    s = Solution()
    s.removeElement([3,2,2,3], 3)
