class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        
             r 
        [5,6,7]
         0 1 2
         l 
         
        Two pointers
        
        Left and Right 
        
        Move right until the next number is not valid
            - Check that we won't have an index error first
        
        Create the current range
            - If right == left: str(nums[right])
            - else: str(nums[left]) + '->' + str(nums[right])

        right += 1
        left = right 
        """
        if not nums:
            return []
        
        left, right = 0, 0
        ans = [] 
        while right < len(nums):
            while right < len(nums)-1 and nums[right] + 1 == nums[right+1]:
                right += 1
            curr_string = self._get_curr_string(nums, left, right)
            ans.append(curr_string)
            right += 1
            left = right 
        return ans

    def _get_curr_string(self, nums, left, right):
        if left == right:
            return str(nums[left])
        else:
            return str(nums[left]) + '->' + str(nums[right])
        
