# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
                
        brute force / Big o 
            - best conceivable run 
                time -> O(n) check every node in the tree
                space -> O(h) stack frame 
            
        edge cases
            - Empty root
            - Skewed Tree 
            
        assumptions
            - Skewed? Balanced? In between? 
            - A single node is max
            - Do we have parent points?
            - Is this a BST? 
            - Binary tree? Nary? 
            - rooted 
                - all nodes have a singl
        test cases
        toolbox
        
        input/output
            @description finds the maximum average subtree in a tree 
            @param1 root : TreeNode
            @return ans  : float  
        
        highlevel
            
            Base Case
                if not root : 
                    return avg, number of nodes
            
            States
                current root node
                number of nodes in the subtree 
            
            Work performed
                Check if adding the current node the the subtrees value a new max value           

        
         (2)
            \ 
            (1)
        
        ls, ln = 0, 0
        rs, rn = 1, 0 
        
        docstrings
        
        """
        self.answer = 0
        self.dfs(root)
        return self.answer 
    
    
    def dfs(self, root):
        if not root:
            return 0, 0 
        
        left_sum, left_num = self.dfs(root.left)
        right_sum, right_num = self.dfs(root.right)
        
        curr_sum = left_sum + right_sum + root.val
        curr_num = left_num + right_num + 1 
        
        curr_avg = float(curr_sum) / float(curr_num)
        self.answer = max(self.answer, curr_avg)
        
        return curr_sum, curr_num 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
