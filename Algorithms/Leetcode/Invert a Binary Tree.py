class Solution:
    def invertTree(self, root):
        # Edge Cases
        if not root:
            return None
        if not root.left and not root.right:
            return root
        
        # Define Variables
        queue = [root]
        
        # BFS
        while queue:
            # Dequeue
            current = queue.pop(0)
            
            # Swap left / right children
            current.left, current.right = current.right, current.left
            
            # Add left / right children (if exist) to the queue
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
            
        return root            
        
        """
        Assumptions:
            - Binary Tree -> Every node has up to 2 nodes
            - We have references to children of node, not parent

        Edge Cases:
            - Null Root
            - Root.left and root.right == None

        Process:
            - Traverse the Tree
            - At each node swap it's left and it's right children
            - Check if left/right exist, if so, add it to queue
            
        q = [(3), (1), (6), (9)
        c = (7)
        
         4
       /   \
      7     2
     / \   / \
    9   6 3   1
        
        """
