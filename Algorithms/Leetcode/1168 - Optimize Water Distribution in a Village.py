class Solution(object):
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        adjList = collections.defaultdict(list) 
        
        for index in range(len(pipes)):
            h1, h2, cost = pipes[index][0], pipes[index][1], pipes[index][2]
            adjList[h1].append((h2, cost))
            adjList[h2].append((h1, cost)) 
            
        for index in range(len(wells)): 
            adjList[0].append((index+1, wells[index])) 
        
        heap = [(cost, house) for house, cost in adjList[0]]
        heapq.heapify(heap) 
        
        globalCost = 0 
        seen = set([0]) 
        
        while heap and len(seen) < n+1:
            currCost, currHouse = heapq.heappop(heap) 
            
            if currHouse in seen:
                continue 
                
            seen.add(currHouse)
            globalCost += currCost 
            
            for neighbor, weight in adjList[currHouse]:
                if neighbor not in seen:
                    heapq.heappush(heap, (weight, neighbor))
                    
        return globalCost
