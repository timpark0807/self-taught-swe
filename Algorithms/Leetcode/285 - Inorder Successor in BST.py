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

        1. If p has a right child
            - the successor is the leftmost node in that right subtree
        2. If p does not have a right child
            - Go up it's parent until we find a parent with a value greater than p
            - If we reach the root, return None
        """
        if not root or not p:
            return None
        
        if not p.right:
            return self.dfs(root, p)
        
        elif p.right:
            return self.dfs_leftmost(p.right)
        
        
    def dfs_leftmost(self, root):
        if root.left:
            return self.dfs_leftmost(root.left)
        return root
        
        
    def dfs(self, root, target):
        parent = {root:None}
        
        while root != target:
            if root.val > target.val:
                parent[root.left] = root
                root = root.left 
            else:
                parent[root.right] = root
                root = root.right
                
        while parent[root] and parent[root].val < target.val:
            root = parent[root]
            
        if parent[root] == None:
            return None
        
        return parent[root]
            
