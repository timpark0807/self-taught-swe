import collections
import unittest

class Solution:
    def bfs(self, edges, src, dst):
        adj_list = self.edge_to_adj_list(edges)

        queue = [src]
        seen = set([src])
        # MISTAKE that i've been running into
        # set takes an argument of an iterable
        backtrack = {src: None}
        output = []

        while queue:
            current = queue.pop(0)
            
            if current == dst:
                while current is not None:
                    output.append(current)
                    current = backtrack[current]

                # Mistake here, when return output.reverse() gives us None
                return output[::-1]
            
            for neighbor in adj_list[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)  
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
                [6,7],
                [7,4]
                ]
        s = Solution()
        answer = s.bfs(edges, 1, 4)
        self.assertEqual(answer, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
    
