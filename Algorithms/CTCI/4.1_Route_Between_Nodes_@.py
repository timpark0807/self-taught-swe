import unittest

def route_between_nodes(node1, node2, graph):
    queue = [node1]
    seen = set(node1)
    while queue:
        current = queue.pop(0)
        for child in graph.get(current, []):
            if child == node2:
                return True
            else:
                queue.append(child)
                seen.add(child)


class TestSolution(unittest.TestCase):
    def test_test(self):
        graph = {'A':['B', 'C'],
                 'B':['E', 'F'],
                 'C':['G', 'D'],
                 'D':['Z']}
        answer = route_between_nodes('A', 'Z', graph)
        self.assertTrue(answer)

if __name__ == '__main__':
    unittest.main()
