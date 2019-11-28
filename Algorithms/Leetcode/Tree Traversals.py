class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        answer = []
        stack = []
        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
    
            elif stack:
                current = stack.pop()
                answer.append(current.val)
                current = current.right
        return answer
    
    def postorderTraversal(self, root):
        answer = []
        self.helper(root, answer)
        return answer
    
    def helper(self, root, answer):
        if root:
            self.helper(root.left, answer)
            self.helper(root.right, answer)
            answer.append(root.val)
        
    def postorderTraversal_iter(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        answer = []
        stack = [root]
        
        while stack:
            current = stack.pop()
            answer.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return answer[::-1]
    
    def preorderTraversal(self, root):
        answer = []
        self._helper(root, answer)
        return answer

    def _helper(self, root, answer):
        if root:
            answer.append(root.val)
            self._helper(root.left, answer)
            self._helper(root.right, answer)
        
    def preorderTraversal_iter(self, root):
        """
              1
            /   \
           0     2
          / \    /
         4  6   3

        stack = [2, 
        curr = 6
        
        answer = 1, 0, 4, 6
        
        """
        if not root:
            return []
        answer = []
        stack = [root]
        
        while stack:
            current = stack.pop()
            answer.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
                
        return answer
