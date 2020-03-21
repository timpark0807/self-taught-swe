class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True 
        return self.dfs(root.left, root.right)
    
    
    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if (node1 and not node2) or (not node1 and node2) or (node1.val != node2.val):
            return False
        return self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)

    def isSymmetric_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        
        queue = collections.deque([(root.left, root.right)])
        
        while queue:
            node1, node2 = queue.popleft() 
            
            if not node1 and not node2:
                continue
            elif (node1 and not node2) or (not node1 and node2):
                return False
            elif node1.val != node2.val:
                return False
            
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
            
            
        return True
