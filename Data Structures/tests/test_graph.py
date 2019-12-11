import unittest
from .Graph import Graph
    
class TestGraph(unittest.TestCase):

    def setUp(self):
        edges = [[0,1], [0,2], [1, 3], [3,4], [4,2]]
        self.g = Graph(edges)

    def tearDown(self):
        self.g = None

    def test_insert(self):
        self.g.insert_edge(0, 5)
        self.assertEqual(self.g.dfs(0), [0, 5, 2, 1, 3, 4])
        self.assertTrue(self.g.is_path(0, 5))
        self.assertRaises(LookupError, self.g.insert_edge, 99, 100)

    def test_delete(self):
        self.g.delete_edge(1, 3)
        self.assertEqual(self.g.dfs(0), [0, 2, 1])
        self.assertFalse(self.g.is_path(1, 3))
        self.assertRaises(LookupError, self.g.delete_edge, 99, 2)
        self.assertRaises(LookupError, self.g.delete_edge, 0, 100)

    def test_dfs(self):
        self.assertEqual(self.g.dfs(0), [0, 2, 1, 3, 4])
        self.assertEqual(self.g.dfs(1), [1, 3, 4, 2])
        self.assertRaises(LookupError, self.g.dfs, 99)
        
    def test_bfs(self):
        self.assertEqual(self.g.bfs(0), [0, 1, 2, 3, 4])
        self.assertEqual(self.g.bfs(1), [1, 3, 4, 2])
        self.assertRaises(LookupError, self.g.bfs, 99)

    def test_is_path(self):
        self.assertTrue(self.g.is_path(0, 4))
        self.assertTrue(self.g.is_path(1, 3))
        self.assertFalse(self.g.is_path(2, 1))

    def test_get_path(self):
        self.assertEqual(self.g.get_path(0, 4), [0, 1, 3, 4])
        self.assertEqual(self.g.get_path(1, 3), [1, 3])
        self.assertEqual(self.g.get_path(2, 1), [])
        
    def test_indegrees(self):
        self.assertEqual(self.g._get_indegrees(), {0:0, 1:1, 2:2, 3:1, 4:1})

    def test_topological_sort(self):
        self.assertEqual(self.g.topological_sort(0), [0, 1, 3, 4, 2])
        self.g.insert_edge(4, 5)
        self.assertEqual(self.g.topological_sort(0), [0, 1, 3, 4, 5, 2])

    def test_is_cycle(self):
        self.assertFalse(self.g.is_cycle(0))
        self.g.insert_edge(2, 3)
        self.assertTrue(self.g.is_cycle(0))

        
if __name__ == '__main__':
    unittest.main()
