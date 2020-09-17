class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        
        adjList = {i:[] for i in range(n+1)}
        
        for p1, p2, cost in pipes:
            adjList[p1].append((p2, cost))
            adjList[p2].append((p1, cost)) 
        
        for house, cost in enumerate(wells):
            adjList[0].append((house+1, cost))
            
        heap = [(cost, house) for house, cost in adjList[0]]
        heapq.heapify(heap)
        seen = set()
        answer = 0 
        
        while heap:
            currCost, currHouse = heapq.heappop(heap) 
            
            if currHouse in seen:
                continue
            answer += currCost
            seen.add(currHouse)
            
            for neighbor, neighCost in adjList[currHouse]:
                if neighbor not in seen:
                    heapq.heappush(heap, (neighCost, neighbor)) 
        
        return answer
