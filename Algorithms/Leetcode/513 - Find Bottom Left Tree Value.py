class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        
        while queue:
            current = queue.pop(0)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
                
        return current.val
