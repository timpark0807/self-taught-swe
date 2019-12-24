# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        
        elif root.val < L:
            if root.right:
                return self.rangeSumBST(root.right, L, R)
            else:
                return 0 
        elif root.val > R:
            if root.left:
                return self.rangeSumBST(root.left, L, R)
            else:
                return 0
            
        total = 0 
        if L <= root.val <= R:
            left = self.rangeSumBST(root.left, L, R)
            right = self.rangeSumBST(root.right, L, R)
            total += root.val + left + right
            

        return total
     
