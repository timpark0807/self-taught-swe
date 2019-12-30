import collections

"""
Solution to Youtube Video Example Phone Screen Question:
reference: https://www.youtube.com/watch?v=V0xjK_6ZoEY
"""

class Relation:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child

class Solution:
    
    def printTree(self, arr):
        adj_list = self.get_adj_list(arr)
        indegrees = self.get_indegrees(adj_list)
        return self.topological_ordering(adj_list, indegrees)
        

    def topological_ordering(self, adj_list, indegrees):
        nodes_with_zero_indegree = []
        for key, indegree in indegrees.items():
            if indegree == 0:
                nodes_with_zero_indegree.append((key, ''))
        
        spaces = ''
        
        while nodes_with_zero_indegree:
            curr, spaces = nodes_with_zero_indegree.pop()
            print(spaces, curr)
            for neighbor in adj_list[curr]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    nodes_with_zero_indegree.append((neighbor, spaces + ' '))
        

    def get_adj_list(self, arr):
        adj_list = collections.defaultdict(list)
        for r in arr:
            parent = r.parent
            child = r.child
            adj_list[parent].append(child)
        return adj_list

    def get_indegrees(self, adj_list):
        indegrees = {}
        
        for key, value in adj_list.items():
            if key not in indegrees:
                indegrees[key] = 0
                
            for v in value:
                if v not in indegrees:
                    indegrees[v] = 0
                indegrees[v] += 1
                
        return indegrees 
            

arr = [Relation('animal', 'mammal'),
       Relation('animal', 'bird'),
       Relation('lifeform', 'animal'),
       Relation('cat', 'lion'),
       Relation('mammal', 'cat'),
       Relation('animal', 'fish'),
       Relation('alien', 'bacteria'),
       Relation('bacteria', 'flu'),
       Relation('alien', 'ET')]

s = Solution()
s.printTree(arr)
