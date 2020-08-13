class Solution(object):
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        
        seen
                
        use queue and store curr string and curr k 
        
            if curr string == B:
                return curr k
                
        
        bfs -> shortest path 

        we need neighbors 
        
        """
        
        queue = collections.deque([(A, 0)])
        seen = set() 
        
        while queue:
            currString, currCount = queue.popleft() 
            
            if currString == B:
                return currCount
            
            for neighbor in self._getNeighbors(currString, B):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, currCount + 1)) 
                    
        return -1 
    
    def _getNeighbors(self, A, B):
        
       
        neighbors = [] 
        for index1 in range(len(A)-1):
            if A[index1] != B[index1]:
                for index2 in range(index1+1, len(A)):
                    if A[index2] == B[index1] and A[index2] != B[index2]:
                        neighbors.append(A[:index1] + A[index2] + A[index1+1:index2] + A[index1] + A[index2+1:])
                break 
        return neighbors 
