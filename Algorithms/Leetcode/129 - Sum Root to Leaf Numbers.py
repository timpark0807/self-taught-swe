# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        BEAT.IO
        Brute Force
            -> 
        Edge Cases
            -> Empty root
        Assumptions
            -> Binary Tree -> Each node has 0, 1 or 2 Elements
            -> No cycles
            -> Only references to left and right child, no parent
        Toolbox
            -> DFS 
            -> Parent dictionary parent
        Input 
            -> Tree
        Output 
            -> Integer
            -> Keep track of all paths to root 
            
    Needed:
    parent = {4: None,
              9: 4,
              0: 4,
              5: 9,
              1, 9
              
    stack = [root]
    answers = []
    
    
                4
               / \
              9   0
             / \
            5   1
            
       temp = 9
       s = '9'+'5'
      
       1. DFS, keep track of every node's parent
       2. If current node does not have a left or right child it is a leaf
            -> Build the path using the parent dictionary and store it in answers
       3. Sum all paths and return  
        """
        if not root:
            return 0
        
        parent = {root:None}
        stack = [root]
        res = 0
        while stack:
            current = stack.pop()
            
            if current.right:
                parent[current.right] = current
                stack.append(current.right)
            
            if current.left:
                parent[current.left] = current
                stack.append(current.left)
                
            if not current.left and not current.right:
                temp = current
                s = ''
                while temp:
                    s = str(temp.val) + s
                    temp = parent[temp]
                res += int(s)
                            
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
