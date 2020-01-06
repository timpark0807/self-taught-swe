class Solution(object):
    def largestRectangleArea(self, heights):
        if not heights:
            return 0
        elif len(heights) == 1:
            return heights[0]
        
        left, right = 0, len(heights) - 1
        global_max = 0
        min_height = self.get_min_height(heights, left, right)
                
        while left <= right:
            left_height = heights[left]
            right_height = heights[right]
            distance = right - left + 1
            global_max = max(global_max, min_height * distance)

            if min_height == left_height:
                min_height = self.get_min_height(heights, left+1, right)
            elif min_height == right_height:
                min_height = self.get_min_height(heights, left, right-1)
                
            if left_height <= right_height:
                left += 1
            else:
                right -= 1

        return global_max
                

            
    def get_min_height(self, heights, left, right):
        global_min = float('inf')
        for index in range(left, right+1):
            global_min = min(global_min, heights[index])
        if global_min == float('inf'):
            return 0
        return global_min


            
items = [5,5,1,7,1,1,5,2,7,6]
s = Solution()
print(s.largestRectangleArea(items))
