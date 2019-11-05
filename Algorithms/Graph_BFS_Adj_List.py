import unittest
import collections


class Solution:
    
    def is_path(self, edges, start, stop):
        adj_list = self.get_adj_list(edges)

        queue = [start]

        while queue:
            
            current = queue.pop(0)
            
            if current == stop:
                return True
            
            for neighbor in adj_list[current]:
                queue.append(neighbor)

        return False
    
    def get_path(self, edges, start, stop):
        adj_list = self.get_adj_list(edges)

        queue = [start]
        parent = {start : None}
        
        while queue:
            
            current = queue.pop(0)
            
            if current == stop:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path
            
            for neighbor in adj_list[current]:
                queue.append(neighbor)
                parent[neighbor] = current
                
        return False
    
    def get_adj_list(self, edges):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)

        return adj_list


class Test(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def test_is_path(self):
        edges = [
                [1, 2],
                [1, 3],
                [2, 4],
                [4, 5]
                ]
        answer = self.s.is_path(edges, 1, 5)
        self.assertTrue(answer)

    def test_get_path(self):
        edges = [
                [1, 2],
                [1, 3],
                [2, 4],
                [4, 5]
                ]
        answer = self.s.get_path(edges, 1, 5)
        self.assertEqual(answer, [1, 2, 4, 5])


    def test_no_path(self):
        edges = [
                [1, 2],
                [1, 3],
                [2, 4],
                [4, 5],
                [3, 6]
                ]
        answer = self.s.is_path(edges, 3, 5)
        self.assertFalse(answer)
        
if __name__ == '__main__':
    unittest.main()
