class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        
        Build the adjacency list, number of outdegrees, and parents of nodes 
        
        Build a set strcuture 
        
        Starting with nodes with 0 outdegrees 
        for each parent of that node 
            Add the current nodes prereq set to the parent nodes prereq set 
            Remove 1 from the parent nodes outdegree count 
            if parent node has 0 outdegrees, add the parent node to the queue 
            
        run through all the queries 
            append the query result to answer array
            
        return answer array 
        """
        adjList = {i:[] for i in range(n)}
        outdegrees = {i:0 for i in range(n)}
        parents = {i:[] for i in range(n)}
        
        # O(p) where p = len(prerequisites)
        for node1, node2 in prerequisites:
            adjList[node1].append(node2) 
            outdegrees[node1] += 1 
            parents[node2].append(node1) 
            
        prereqs = {i:set([i]) for i in range(n)}
        zeroNodes = [node for node, count in outdegrees.items() if count == 0]
        
        while zeroNodes: # O(n) where n = number of nodes 
            currNode = zeroNodes.pop() 
            for parent in parents[currNode]:
                prereqs[parent] = prereqs[parent].union(prereqs[currNode]) 
                outdegrees[parent] -= 1
                if outdegrees[parent] == 0:
                    zeroNodes.append(parent) 
        
        answer = [] 
        for node1, node2 in queries:
            answer.append(node2 in prereqs[node1])
            
        return answer 
