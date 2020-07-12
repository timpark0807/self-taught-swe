class Solution(object):
    def maxProbability(self, n, edges, succProb, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start: int
        :type end: int
        :rtype: float
        
        
        step 1. build an adjacency list
            - helps us traverse the graph
            - choose this over an adjacency matrix 
        
        
        step 2. place starting node in a heap (?)
            - we will store a tuple containing (current probability, current node) 
            
            - while there are elements in the heap 
                - pop from heap 
                - if this node is the end: return current probablity 
            
                - check all it's neighbors
                    - if neighbor hasn't been seen
                    - append to heap with probablity it takes to get there
        
        step 3. return 0 if we didn't find anything in step 2
                    
            
        """
        adjList = self.getAdjList(n, edges, succProb)
        heap = [(-1, start)]
        seen = set() 
        
        while heap:
            currProb, currNode = heapq.heappop(heap) 
            currProb *= -1 
            if currNode == end:
                return currProb
            for probability, neighbor in adjList[currNode]:
                if (currNode, neighbor) not in seen:
                    seen.add((currNode, neighbor))
                    newProb = currProb * probability
                    heapq.heappush(heap, (-newProb, neighbor)) 
        return 0 
    
    def getAdjList(self, n, edges, succProb):
        adjList = {i:[] for i in range(n)}
        for index, (node1, node2) in enumerate(edges):
            adjList[node1].append((succProb[index], node2))
            adjList[node2].append((succProb[index], node1)) 
        return adjList 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
