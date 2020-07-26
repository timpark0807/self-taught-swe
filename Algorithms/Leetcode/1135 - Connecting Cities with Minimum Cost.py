class Solution(object):
    def minimumCost(self, N, connections):
        """
        :type N: int
        :type connections: List[List[int]]
        :rtype: int       
        """
        
        adjList = self.getAdjList(N, connections) 
        heap = [(0, 1)]
        seen = set() 
        globalDist = 0 
        
        while heap:
            
            currPath, currNode = heapq.heappop(heap) 
            
            if currNode in seen:
                continue 
                
            globalDist += currPath 
            seen.add((currNode))
            if len(seen) == N:
                return globalDist 
            
            for neighbor, cost in adjList[currNode]:
                if neighbor not in seen:
                    heapq.heappush(heap, (cost, neighbor)) 
                    
        return -1 
    
    def getAdjList(self, N, connections):
        adjList = {i:[] for i in range(1, N+1)}
        for node1, node2, cost in connections:
            adjList[node1].append((node2, cost))
            adjList[node2].append((node1, cost))
        return adjList 
    
