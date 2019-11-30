# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
            
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        
        (3)
        / \
       (1) (4)
         \
         (2)
        
        """
        if not root:
            return None 
        
        current = root
        stack = []
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
                
            elif stack:
                current = stack.pop()
                
                if current.val == p.val:
                    if current.right:
                        current = current.right
                        while current.left:
                            current = current.left
                        return current
                    
                    elif stack:
                        ans = stack.pop()
                        return ans
                    else:
                        return None
                    
                current = current.right  
                
        return None
    
    
    
    
    
        
