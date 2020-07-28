"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        self.answer = 0 
        self.dfs(root)
        return self.answer
    
    
    def dfs(self, root):
        if not root:
            return 0
        
        heap = [] 
        for child in root.children:
            curr = self.dfs(child)
            heapq.heappush(heap, curr)
            if len(heap) == 3:
                heapq.heappop(heap)
        
        self.answer = max(self.answer, sum(heap))   
        
        return max(heap) + 1 if heap else 1
