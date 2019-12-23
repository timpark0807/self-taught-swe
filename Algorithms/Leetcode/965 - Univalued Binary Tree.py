# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        stack = [root]
        unival = root.val 
        while stack:
            current = stack.pop()
            if current.val != unival:
                return False
            
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return True
            
