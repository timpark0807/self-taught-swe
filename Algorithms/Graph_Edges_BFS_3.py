import unittest
import collections

class Solution:

    def bfs(self, edges, source, destination):
        """
        Input  : list of edges [x, y]
                 Undirected graph thus [x, y] == [y, x]
        Output : Integer representing the length of the shortest path
        
    x   1. Convert edges to adjacency list
    x   2. Initialize queue and a seen set with source
    x   3. Dequeue, check neighbors, enqueue and add to source
    x   4. Backtrack, keeping track of counts
    x   5. Return counts inside loop
    x   6. Else return False (No path from source to destination)
        """
        adj_list = self.edge_to_adj_list(edges)

        queue = [source]
        seen = set([source])
        backtrack = {source : None}

        while queue:
            current = queue.pop(0)
            if current == destination:
                count = 0
                while current is not None:
                    current = backtrack[current]
                    count += 1
                return count - 1
                    
            for neighbor in adj_list[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
                    backtrack[neighbor] = current
    
        return False

    def edge_to_adj_list(self, edges):
        adj_list = collections.defaultdict(list)

        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        return adj_list 


class TestSolution(unittest.TestCase):
    def test_bfs_edge_list(self):
        edges = [[0,1],
                 [0,2],
                 [0,3],
                 [2,4],
                 [4,5]]
        
        s = Solution()
        answer = s.bfs(edges, 0, 5)
        self.assertEqual(answer, 3)

if __name__ == '__main__':
    unittest.main()
