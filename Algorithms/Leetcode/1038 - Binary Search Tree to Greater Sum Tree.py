# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        @description Modifies values to only contain values greater than it 
        @param1 root : TreeNode 
        @return root : TreeNode 
        
        
        BEATIO HD Checklist
        
        
        Highlevel
            Approach 1 :
                Traverse through BST, Get all values inside it 
                Traverse through the BST, Change the value to sum(values[index:])
                
                O(n) where n = number of nodes 
                
            Approach 2 : 
                ?? 
                
        Edge Cases
            Empty root 
            Skewed Tree 
            
        Assumptions
            - Access to parent pointer?
            - Balanced? Skewed? In between?
            - Perfect complete or full ? 
            - In place?
            
        Test cases
        Toolbox
        input/output

        
        Docstrings
        """
        answers = [] 
        stack = []
        curr = root
        curr_sum = 0 
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.right
            elif stack:
                curr = stack.pop()
                curr_sum += curr.val 
                curr.val = curr_sum
                curr = curr.left
        
        return root
    
    
    
    
