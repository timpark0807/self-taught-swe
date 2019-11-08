import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        current = root
        stack = []
        output = []

        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                output.append(current.data)
                current = current.right
                
        return output

    def r_inorderTraversal(self, root):
        output = []
        self.helper(root, output)
        return output
    
    def helper(self, root, output):
        if root.left:
            self.helper(root.left, output)
        output.append(root)
        if root.right:
            self.helper(root.right, output)

        
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None
        
    def test_valid_tree(self):
#            (10)
#          /      \ 
#         (5)     (15) 
#        /  \     /  \ 
#      (2)  (7)
#           /
#         (6)
#   output  =   [2, 5
#   stack   =   [10,  7
#   current = 7

# 1. Add current.right and current.left to stack
# 2. Set current to current.left
# 3. If current.left = None
#       -> current = stack.pop()

        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(2)
        root.left.right = Node(7)
        root.left.right.left = Node(6)
        answer = self.s.inorderTraversal(root)
        self.assertEqual(answer, [2, 5, 6, 7, 10, 15])

    def test_empty_tree(self):
        root = None
        answer = self.s.inorderTraversal(root)
        self.assertEqual(answer, [])

if __name__ == '__main__':
    unittest.main()
