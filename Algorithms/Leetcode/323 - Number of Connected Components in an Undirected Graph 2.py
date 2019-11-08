import collections
import unittest

class Solution(object):
    """
    Runtime: 72 ms, faster than 99.63% of Python online submissions for Number of Connected Components in an Undirected Graph.
    Memory Usage: 13.3 MB, less than 69.23% of Python online submissions for Number of Connected Components in an Undirected Graph.
    """
    def countComponents(self, n, edges):
        adj_list = self.get_adj_list(edges)
        seen = set()
        count = 0
        
        for node in range(n):
            if node not in seen:
                count += self.bfs(adj_list, seen, node)

        return count # Number of connected 

    def bfs(self, adj_list, seen, node):
        queue = [node]
        seen.add(node)
        
        while queue:
            current = queue.pop(0)
            for neighbor in adj_list[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
                    
        return 1

        

    def get_adj_list(self, edges):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)
        return adj_list
    


class TestSolution(unittest.TestCase):
    def test_two(self):
        n = 5
        edges = [[0, 1], [1, 2], [3, 4]]

        s = Solution ()
        answer = s.countComponents(n ,edges)
        self.assertEqual(answer, 2)


if __name__ == '__main__':
    unittest.main()
