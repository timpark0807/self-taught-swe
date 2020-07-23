class Solution(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        heap = [(-A[0][0], 0, 0)] # min value in path, curr coordinate
        seen = set([(0,0)])
        moves = [(0,1),(1,0),(-1,0),(0,-1)]
        
        while heap:
            currMin, currRow, currCol = heapq.heappop(heap) 
            if currRow == len(A)-1 and currCol == len(A[0])-1:
                return -currMin
            for moveRow, moveCol in moves:
                newRow, newCol = currRow + moveRow, currCol + moveCol
                if (newRow, newCol) not in seen and self.inBounds(A, newRow, newCol):
                    seen.add((newRow, newCol))
                    newMin = min(-currMin, A[newRow][newCol])
                    heapq.heappush(heap, (-newMin, newRow, newCol))
                    
        return 
    
    def inBounds(self, A, row, col):
        return 0<=row<len(A) and 0<=col<len(A[row]) 

    def canVisitAllRooms(self, rooms):
        seen = set([0])
        stack = [0]
        
        while stack:
            currRoom = stack.pop() 
            if len(rooms) == len(seen):
                return True
             
            for keyRoom in rooms[currRoom]:
                if keyRoom not in seen:
                    seen.add(keyRoom)
                    stack.append(keyRoom) 
                    
        return len(seen) == len(rooms)

    def countComponents(self, n, edges):
        seen = set()
        adjList = self.getAdjList(n, edges) 
        answer = 0 
        for node in range(n):
            if node not in seen:
                answer += self.dfs(node, seen, adjList)
        return answer
    
    def dfs(self, node, seen, adjList):
        stack = [node]
        seen.add(node)
        while stack:
            currNode = stack.pop() 
            for neighbor in adjList[currNode]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return 1
     
    
    def getAdjList(self, n, edges):
        adjList = {i:[] for i in range(n)}
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1) 
        return adjList 
    
