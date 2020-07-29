class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        queue = collections.deque([(0, node, set([node]), set([node])) for node in range(len(graph))]) 
        while queue:
            currSteps, currNode, currSeen, currPath = queue.popleft() 

            if len(currPath) == len(graph):
                return currSteps 
            
            for neighbor in graph[currNode]:
                if (neighbor, tuple(currPath)) not in currSeen:
                    currSeen.add((neighbor, tuple(currPath))) 
                    newPath = currPath.copy() 
                    newPath.add(neighbor) 
                    queue.append((currSteps+1, neighbor, currSeen, newPath)) 
                    
        return -1 
    
