# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        
        a preorder traversal where we keep track of the maximum node that we've seen
        
            - If the current node is the max, add 1 to count
            
        """
        self.count = 0
        self.dfs(root, float('-inf'))
        return self.count
    
    
    def dfs(self, root, maximum):
        
        if not root:
            return  
        
        if root.val >= maximum:
            self.count += 1
        maximum = max(maximum, root.val)
        self.dfs(root.left, maximum)
        self.dfs(root.right, maximum)
        
        return 
        
        
    
        
