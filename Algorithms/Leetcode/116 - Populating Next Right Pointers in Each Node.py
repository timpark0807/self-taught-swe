"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        
        
          (1) 
        /      \ 
      (2)       (3) 
    /   \      /    \  
  (4)   (5)   (6)  (7)   

                
        q = [(3, (4))]


        curr_node = (3)
        curr_depth = 2
        
        prev_node =  (2)
        prev_depth = 2
        
        
        Level Order Traversal
        
        prev_node, curr_depth = None, 0 
        
        while there are nodes in the queue
            Keep track of curr node, curr depth
            
            if prev_node and curr_depth equal to prev depth
                set prev_node.next to curr_node 

            check if curr_node has left
                add it to queue 

            check if curr_node has right
                add it to queue 
            set prev_node to curr_node
            set prev_depth to curr_depth

        return root 

        """
        
        return self.dfs(root)
    
    
    def dfs(self, curr):
        if not curr:
            return None
        
        if curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left 
        
        self.dfs(curr.left)
        self.dfs(curr.right)
        return curr
        
        
        
        
        
        
        
        
        
        
        
