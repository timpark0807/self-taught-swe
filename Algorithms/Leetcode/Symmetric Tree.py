# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        Checklist: BEAT.IO HD
        
        Brute Force / Big O 
        Edge Cases
        Assumptions
        Test Case / Toolbox
        Input
        Output
        
        Highlevel
        Docstrings
        
            1
           / \
          2   2
         / \ / \
        3  4 4  3
        
        
        Level Order Traversal
            BFS 
         
        """
        if not root:
            return True
        
        queue = collections.deque([(root.left, root.right)])

        while queue: 
            left_, right_ = queue.popleft() 
            
            if (not left_ and right_) or (left_ and not right_):
                return False
            elif (not left_ and not right_):
                continue
            elif left_.val != right_.val: 
                return False  
            
            queue.append((left_.left, right_.right))
            queue.append((left_.right, right_.left))

        return True
