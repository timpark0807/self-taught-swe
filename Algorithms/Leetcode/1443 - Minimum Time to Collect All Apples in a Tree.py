class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        parents = self.getParents(n, edges) 
        seen = set([0]) 
        ans = 0
        
        for currNode in range(n):
            if hasApple[currNode]:
                ans += self.process(currNode, parents, seen) 
                
        return ans * 2 
    
    def getParents(self, n, edges):
        parents = {0:None}
        for parent, child in edges:
            parents[child] = parent 
        return parents
    
    def process(self, currNode, parents, seen): 
        steps = 0 
        while currNode not in seen:
            seen.add(currNode)
            currNode = parents[currNode] 
            steps += 1
            
        return steps 
