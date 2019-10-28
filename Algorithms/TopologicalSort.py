import unittest

class Solution:
    def topological_sort(self, digraph):
        """
        A function to return an array with the topological order from a given digraph.

        The input is a directed graph, represented as an adjacency matrix.

            digraph = {node: [neighbors]}
        """

        indegrees = {node: 0 for node in digraph}
        for node in digraph:
            for neighbor in digraph[node]:
                indegrees[neighbor] += 1

        nodes_with_no_incoming_edges  = []

        for node in digraph:
            if indegrees[node] == 0:
                nodes_with_no_incoming_edges.append(node)

        topological_ordering = []

        while len(nodes_with_no_incoming_edges) > 0:
            current = nodes_with_no_incoming_edges.pop()

            topological_ordering.append(current)

            for neighbor in digraph[current]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    nodes_with_no_incoming_edges.append(neighbor)

        if len(topological_ordering) == len(digraph):
            return topological_ordering
        else:
            raise Exception("Graph has cycle! No topoogical ordering exists.")


class TestSolution(unittest.TestCase):
    def test_valid(self):
        digraph = {'A' : ['C', 'D'],
                   'B' : ['E', 'C'],
                   'C' : ['D'],
                   'D' : [],
                   'E' : ['A', 'C']}
        
        s = Solution()
        answer = s.topological_sort(digraph)
        self.assertEqual(answer, ['B', 'E', 'A', 'C', 'D'])


if __name__ == '__main__':
    unittest.main()
    
