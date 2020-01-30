import collections
import unittest

class Solution:

    def detect_cycle(self, edges, start):
        if not edges:
            return False
        
        adj_list = self.get_adj_list(edges)
        seen = set([start])
        stack = [start]
        parent = {start:-1}
        
        while stack:
            current_node = stack.pop()
            
            for neighbor in adj_list[current_node]:
                if neighbor not in seen:
                    parent[neighbor] = current_node
                    seen.add(neighbor)
                    stack.append(neighbor)

                elif neighbor != parent[current_node]:
                    return True

        return False

            
    def get_path(self, edges, start, end):
        if not edges:
            return False
        
        adj_list = self.get_adj_list(edges)
        seen = set([start])
        stack = [start]
        parent = {start:-1}
        
        while stack:
            current_node = stack.pop()
            for neighbor in adj_list[current_node]:
                if neighbor not in seen:
                    parent[neighbor] = current_node
                    seen.add(neighbor)
                    stack.append(neighbor)
                elif neighbor != parent[current_node]:
                    return True

        return False
    
    def get_adj_list(self, edges):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        return adj_list

    
class TestSolution(unittest.TestCase):
                 
    def setUp(self):
        self.s =  Solution()
        
    def tearDown(self):
        self.s = None

    def test_cycle(self):
        edges = [[0,1],
                 [0,2],
                 [1,2],
                 [2,3]]
        self.assertTrue(self.s.detect_cycle(edges, 0))

    def test_nocycle(self):
        edges = [[0,1],
                 [2,3],
                 [0,2]]
        self.assertFalse(self.s.detect_cycle(edges, 0))

if __name__ == '__main__':
    unittest.main()
