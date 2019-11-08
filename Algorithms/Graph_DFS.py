import collections
import unittest

class Solution:
    def bfs(self, edges, src, dst):
        adj_list = self.edge_to_adj_list(edges)

        stack = [src]
        seen = set([src])
        backtrack = {src: None}
        output = []

        while stack:
            current = stack.pop()
            
            if current == dst:
                while current is not None:
                    output.append(current)
                    current = backtrack[current]

                return output[::-1]
            
            for neighbor in adj_list[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)  
                    backtrack[neighbor] = current
        
        return -1 

    def edge_to_adj_list(self, edges):
        adj_list = collections.defaultdict(set)
        for node1, node2 in edges:
            adj_list[node1].add(node2)
        return adj_list


class Test(unittest.TestCase):
    def test_bfs(self):
        edges = [
                [1,2],
                [2,3],
                [3,4],
                [2,5],
                [5,6],
                [6,7]
                ]
        s = Solution()
        answer = s.bfs(edges, 1, 4)
        self.assertEqual(answer, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
    
