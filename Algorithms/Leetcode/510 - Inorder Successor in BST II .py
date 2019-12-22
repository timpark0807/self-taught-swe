"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None 
        
        if node.right:
            return self.find_leftmost(node.right)
        
        temp = node
        while temp.parent and temp.parent.val < node.val:
            temp = temp.parent 
            
        if temp.parent:
            return temp.parent
        else:
            return None
        
        
    def find_leftmost(self, node):
        if not node.left:
            return node
        return self.find_leftmost(node.left)
