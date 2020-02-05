class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        
        State
            - index
        
        Base Case
            - not boxes -return 0 
            - index = len(boxes) -> float('-inf') 
            
        Decision
            - Take this row of boxes
            - Don't take this row of boxes           
            
        [1, 3, 2, 2, 2, 3, 4, 3, 1]
               l        r
               
        """
        self.memo = {}
        return self.dp(boxes, 0, 0)
        
    def dp(self, boxes, left, right):
        
        if not boxes:
            return 0 
        
        if left > right or right >= len(boxes):
            return float('-inf')
        
        while right < len(boxes) and boxes[right] == boxes[left]:
            right += 1
            
        skip = 0
        
        take = self.dp(boxes[:left] + boxes[right:], 0, 0) + ((right-left) * (right-left))
        
     
        skip = self.dp(boxes, right, right)

        return max(take, skip)
    
    
    
s = Solution()
print(s.removeBoxes([1,2,3,4,5,6,7,8,9,10]))
#                      l
#                        r
  
#                   [2,3,4,5,6,7,8,9,10]
#                    l
#                      r 
    
print(s.removeBoxes([1,3,2,2,2,3,4,3,1]))
#                      l
#                      r
