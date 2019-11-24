"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import collections
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # Edge Cases
        if not root:
            return None
        
        # Define Variables
        queue = [(root, 0)]
        levels = collections.defaultdict(list)
        prev = root
        prev_depth = 0
        
        # BFS
        while queue:
            current = queue.pop(0)
            current_node = current[0]
            current_depth = current[1]
            
            if prev_depth == current_depth:
                prev_node.next = current_node.next
                
            prev = current_node 
            prev_depth = current_depth
            
            levels[current_depth].append(current_node)
            
            if current_node.left:
                queue.append((current_node.left, current_depth + 1))
            if current_node.right:
                queue.append((current_node.right, current_depth + 1))
        
        for level in levels.values():
            for index in range(1, len(level)):
                level[index-1].next = level[index]

        # Connect Nodes in each level
        
        return root
    
    
    
    
    
    
    
    
    
    
    
