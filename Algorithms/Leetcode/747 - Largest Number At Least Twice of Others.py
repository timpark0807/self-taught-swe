class Solution(object):
    def dominantIndex(self, nums):
        """
        Clarify:
            - Returning the index of the max value
            - Index matters, so sorting probably won't help
            - If null, return -1
            - If len(nums) == 1, return 0 -> index of first element

        Breakdown:
            1. Find max element
                - Store max value and max index
                - One pass through the array
            2. Run second pass to check if nums > max_element  
                - If False, return - 1
                - If num == max_element, skip

        Complexity:
            1. Space O(1)
            2. Time O(2n) -> O(n)
        """
        
        max_value, max_index = nums[0], 0
        
        for index, num in enumerate(nums):
            if num > max_value:
                max_value = num
                max_index = index
        
        for num in nums:
            if num != max_value and num * 2 > max_value:
                return -1
            
        return max_index
            
