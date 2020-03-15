# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        
        
        [1, 2, 3, 4]
        
        (2)
       /   \ 
     (1)    (3)  
               \
                (4) 
        """
        inorder = self._get_inorder(root)
        root = self.build_tree(inorder)
        return root
    
    
    def build_tree(self, arr): 
        if not arr:
            return None
        
        mid = (0 + len(arr)-1) // 2
        root = TreeNode(arr[mid])
        
        root.left = self.build_tree(arr[:mid])
        root.right = self.build_tree(arr[mid+1:])
        
        
        return root 
        
        
    def _get_inorder(self, root):
        stack = []
        curr = root
        answer = [] 
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                answer.append(curr.val)
                curr = curr.right
                
        return answer
        
