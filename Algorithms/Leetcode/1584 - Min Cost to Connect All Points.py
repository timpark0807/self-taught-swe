class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        adjList = {i:[] for i in range(len(points))}
        
        for index1 in range(len(points)):
            for index2 in range(index1+1, len(points)):
                p1, p2 = points[index1], points[index2] 
                
                dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
                adjList[index1].append((dist, index2))
                adjList[index2].append((dist, index1))
                
        heap = [(0, 0)] 
        heapq.heapify(heap) 
        mst = set([]) 
        cost = 0 
        
        while heap and len(mst) < len(points):
            currDist, currNode = heapq.heappop(heap) 
            if currNode in mst:
                continue 
                
            mst.add(currNode)    
            cost += currDist
            
            for nDist, neighbor in adjList[currNode]:
                if neighbor not in mst:
                    heapq.heappush(heap, (nDist, neighbor)) 
        
        return cost 
    
