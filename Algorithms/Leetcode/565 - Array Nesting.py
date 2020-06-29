class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        
        A = [5,4,0,3,1,6,2]
             0 1 2 3 4 5 6
        
        prev = None 
        
        index = 5
        conn = 6
        
        0 : [5]
        5 : [0]
        
        Create a graph 
            Iterate through the nodes and find the largest connected component
        
        return longest set 
        """
        
        graph = self.getGraph(nums)
        answer = 1 
        seen = set() 
        for node in range(len(nums)):
            if node not in seen:
                currSize = self.dfsTheSize(node, graph, seen)
                answer = max(answer, currSize) 
        return answer 
    
    def dfsTheSize(self, start, graph, seen):
        stack = [start]
        seen.add(start)
        size = 0 
        while stack:
            node = stack.pop()
            size += 1
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return size
    
    
    def getGraph(self, nums):
        adjList = collections.defaultdict(list) 
        prev = None 
        seen = set() 
        for index in range(len(nums)):
            while index not in seen: 
                seen.add(index)
                connect = nums[index]
                adjList[index].append(connect)
                adjList[connect].append(index) 
                index = connect

        return adjList
