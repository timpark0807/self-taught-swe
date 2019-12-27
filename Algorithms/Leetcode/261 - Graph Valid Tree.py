import collections

class Solution(object):
    """
    validTree solutions using...
    1. Topological Sort
    2. Union Find
    """
     def validTree(self, n, edges):
        if len(edges) != n-1:
            return False
        
        indegrees = {n:0 for n in range(n)}
        adj_list = collections.defaultdict(list)
        
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
            indegrees[x] += 1
            indegrees[y] += 1
            
        nodes_with_one_indegree = [i for i in range(n) if indegrees[i] == 1]
        top_sort = []
        
        while nodes_with_one_indegree:
            curr = nodes_with_one_indegree.pop()
            top_sort.append(curr)
            
            for neighbor in adj_list[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 1:
                    nodes_with_one_indegree.append(neighbor)

        return len(top_sort) == n
    
    def validTree_unionfind(self, n, edges):
        if n - 1 != len(edges):
            return False
        
        self.parents = [-1] * n

        for x, y in edges: 
            if self.union(x, y):
                return False
            
        return True
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return True
        else:
            self.parents[rootX] = rootY
            return False
    
    def find(self, x):
        if self.parents[x] == -1:
            return x
        return self.find(self.parents[x])
        

