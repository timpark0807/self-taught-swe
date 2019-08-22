# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if val == root.val:
            return root
        if val > root.val and root.right:
            return self.searchBST(root.right, val)
        if val < root.val and root.left:
            return self.searchBST(root.left, val)
        
