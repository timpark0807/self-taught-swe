class Solution:

    def __init__(self):
        pass
    
    def findRedundantConnection(self, edges):
        parent = [-1] * (len(edges) + 1)
        for x, y in edges:
            if not self.union(parent, x, y):
                return [x, y]
        
    def find(self, parent, x):
        if parent[x] == -1:
            return x
        return self.find(parent, parent[x])

    def union(self, parent, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)
        if rootX == rootY:
            return False
        elif rootX != rootY: 
            parent[rootX] = rootY
            return True


edges = [[1,2], [1,3], [2,3]]
edges2 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
s = Solution()
print(s.findRedundantConnection(edges))
