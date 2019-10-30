class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_matrix = {i: set() for i in range(numCourses)}
        indegrees = {i : 0 for i in range(numCourses)}
        
        for edge in prerequisites:
            adj_matrix[edge[0]].add(edge[1])
            indegrees[edge[1]] += 1
        
        no_incoming_edges = []
        
        for node, count in indegrees.items():
            if count == 0:
                no_incoming_edges.append(node)
                
        top_ordering = []
        
        while len(no_incoming_edges) > 0:
            current = no_incoming_edges.pop()
            top_ordering.append(current)
            
            for neighbor in adj_matrix[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    no_incoming_edges.append(neighbor)
                    
        if len(top_ordering) == len(adj_matrix):
            return True
        else:
            return False


                
