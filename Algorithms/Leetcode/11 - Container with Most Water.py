class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0 or len(height) == 1:
            return 0

        low = 0 
        high = len(height) - 1
        max_area = 0
        
        while low < high:
            shorter = min(height[low], height[high])
            curr_area = shorter * (high - low)
            max_area = max(max_area, curr_area)
            if shorter == height[low]:
                low += 1
            else:
                high -= 1 
    
        
        return max_area
