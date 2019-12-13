import unittest
from . import BinaryTree

class TestBinaryTree(unittest.TestCase):
    #
    #       (7)
    #      /   \
    #    (2)   (10)
    #    / \ 
    #  (1)  (5)
    #
    def setUp(self):
        root = Node(7)
        self.bt = BinaryTree(root)
        self.bt.insert(2)
        self.bt.insert(10)
        self.bt.insert(1)
        self.bt.insert(5)

    def tearDown(self):
        self.root = None
        self.bt = None
        
    def test_get_root(self):
        self.assertEqual(self.bt.get_root(), self.bt.root)
        
    def test_insert(self):
        self.bt.insert(8)
        self.bt.insert(12)
        self.bt.insert(0)
        self.assertEqual(self.bt.inorder(), [0, 1, 2, 5, 7, 8, 10, 12])

    def test_preorder(self):
        self.assertEqual(self.bt.preorder(), [7, 2, 1, 5, 10])

    def test_postorder(self):
        self.assertEqual(self.bt.postorder(), [1, 5, 2, 10, 7])

    def test_inorder(self):
        self.assertEqual(self.bt.inorder(), [1, 2, 5, 7, 10])

    def test_levelorder(self):
        self.assertEqual(self.bt.levelorder(), [7, 2, 10, 1, 5])
        
    def test_get_height(self):
        self.assertEqual(self.bt.get_height(), 2)
        
    def test_search(self):
        self.assertTrue(self.bt.search(2))
        self.assertTrue(self.bt.search(10))
        self.assertFalse(self.bt.search(99))

    def test_get_path(self):
        self.assertEqual(self.bt.get_path(5), [7, 2, 5])

if __name__ == '__main__':
    unittest.main()
