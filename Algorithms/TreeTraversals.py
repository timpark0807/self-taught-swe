import unittest
import collections


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeTraversal:
    """
    Tree Traversal Implemenation
        - Preorder
        - Postorder
        - Inorder

    Time      : O(n)
    BFS Space : O(n)
    DFS Space : O(h)
    """
    def bfs(self, root):
        queue = collections.deque([root])
        answer = [] 
        while queue:
            current = queue.popleft()
            answer.append(current.data)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return answer 
    
    def preorder_iter(self, root):
        stack = [root]
        answer = []
        while stack:
            current = stack.pop() 
            answer.append(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return answer
    
    def preorder_recur(self, root, answer):
        answer.append(root.data)
        if root.left:
            self.preorder_recur(root.left, answer)
        if root.right:
            self.preorder_recur(root.right, answer)
        return answer
    
    def inorder_iter(self, root):
        stack = []
        current = root
        answer = []
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                answer.append(current.data)
                current = current.right
        return answer
        
    def inorder_recur(self, root, answer):
        if root:
            self.inorder_recur(root.left, answer)
            answer.append(root.data)
            self.inorder_recur(root.right, answer)        
        return answer
    
    def postorder_iter(self, root):
        stack1 = [root]
        stack2 = []
        answer = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            current = stack2.pop()
            answer.append(current.data)
            
        return answer
    
    def postorder_recur(self, root, answer):
        if root:
            self.postorder_recur(root.left, answer)
            self.postorder_recur(root.right, answer)
            answer.append(root.data)
        return answer


class TestTreeTraversal(unittest.TestCase):
    
    def setUp(self):
        self.t = TreeTraversal()
        self.root = Node(10)
        self.root.left = Node(5)
        self.root.left.left = Node(2)
        self.root.left.right = Node(7)
        self.root.left.right.left = Node(6)
        self.root.right = Node(15)
        self.root.right.left = Node(13)
        self.root.right.left.right = Node(14)

    def tearDown(self):
        self.t = None
        
    def test_tree_bfs(self):
        answer = self.t.bfs(self.root)
        self.assertEqual(answer, [10, 15, 5, 13, 7, 2, 14, 6])

    def test_tree_preorder_iter(self):
        answer = self.t.preorder_iter(self.root)
        self.assertEqual(answer, [10, 5, 2, 7, 6, 15, 13, 14])
        
    def test_tree_preorder_recur(self):
        answer = self.t.preorder_recur(self.root, [])
        self.assertEqual(answer, [10, 5, 2, 7, 6, 15, 13, 14])

    def test_tree_inorder_iter(self):
        answer = self.t.inorder_iter(self.root)
        self.assertEqual(answer, [2, 5, 6, 7, 10, 13, 14, 15])
        
    def test_tree_inorder_recur(self):
        answer = self.t.inorder_recur(self.root, [])
        self.assertEqual(answer, [2, 5, 6, 7, 10, 13, 14, 15])
        
    def test_tree_postorder_iter(self):
        answer = self.t.postorder_iter(self.root)
        self.assertEqual(answer, [2, 6, 7, 5, 14, 13, 15, 10])
        
    def test_tree_postorder_recur(self):
        answer = self.t.postorder_recur(self.root, [])
        self.assertEqual(answer, [2, 6, 7, 5, 14, 13, 15, 10])

 
if __name__ == '__main__':
    unittest.main()
