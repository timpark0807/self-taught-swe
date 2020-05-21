class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        
        iterate over the preorder
            if current number is less than the last number in stack
                push to stack 
            if current number is less than left:
                return False 
            while current number is greater than the last number in stack
                pop from stack and keep as last value 
                this will be our new left bound 
                
        """
        stack = []
        left = None 
        
        for num in preorder:
            
            if left and num < left:
                return False
            
            while stack and num > stack[-1]:
                left = stack.pop()
            
            stack.append(num) 
            
        return True 
        
        
