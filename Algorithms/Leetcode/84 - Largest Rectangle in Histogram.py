class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        
        Brute Force:
            Time: O(n^2)
            Space: O(1) 
            
            For each height
                Expand as far left and right as possible with this as the max height  
        
        Optimal
            Time: O(n)
            Space: O(n) 
            
            Use a monotonically increasing stack to calculate left and right 
            Calculate maximum   
            
        """
        if not heights:
            return 0 
        
        left = [0] * len(heights)
        right = [0] * len(heights)
        
        stack = [] 
        for index, height in enumerate(heights):
            while stack and height < stack[-1][1]:
                sIndex, _ = stack.pop() 
                left[sIndex] = index - sIndex - 1
            stack.append((index, height)) 
            
        for index, height in stack:
            left[index] = len(heights) - index - 1 
            
        for index in reversed(range(len(heights))):
            while stack and heights[index] < stack[-1][1]:
                sIndex, _ = stack.pop()
                right[sIndex] = sIndex - index - 1
            stack.append((index, heights[index]))
            
        for index, height in stack:
            right[index] = index
            
        globalMax = 0 
        
        for index in range(len(heights)):
            width = left[index] + right[index] + 1 
            globalMax = max(globalMax, heights[index] * width) 
        return globalMax 
