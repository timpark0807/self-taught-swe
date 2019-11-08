class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        
        Graph is directed edges
        Nodes are people
        Edges are trust 
        
        1. Build Adjacency List
        2. Build Indegrees map 
        3. Iterate through indegrees
            Find the person with n-1 indegrees
            -> check that this person has no neighbors 
            
        N = 3, 
        trust = [
                [1,3],
                [2,3]
                ]
            

        Adj_List = {
                     1 : {3},
                     2 : {3},
                     3 : {}
                    }

        InDegrees = {
                     1 : 0,
                     2 : 0,
                     3 : 2
                    }
        """
        
        # Build adjacency list and indegrees
        adj_list = {n : set() for n in range(1, N+1)}
        indegrees = {n : 0 for n in range(1, N+1)}

        for x, y in trust:
            adj_list[x].add(y)
            indegrees[y] += 1
        
        for person, num_of_trust in indegrees.items():
            if num_of_trust == N-1 and len(adj_list[person]) == 0:
                return person
            
        return -1
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
