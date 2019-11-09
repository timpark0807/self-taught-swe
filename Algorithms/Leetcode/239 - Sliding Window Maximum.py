class Solution:
    
    def maxSlidingWindow_bruteforce(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums == []:
            return None
        
        output = []
        
        left = 0
        right = k
        
        while right <= len(nums):
            curr_max = float('-inf')
            for index in range(left, right):
                curr_max = max(curr_max, nums[index])

            output.append(curr_max)
            
            right += 1
            left += 1
            
        return output
