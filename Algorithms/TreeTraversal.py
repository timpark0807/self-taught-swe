import unittest
import collections


class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeTraversal:
    
    def tree_bfs(self, root):
        queue = [root]
        answer = [] 
        while queue:
            current = queue.pop(0)
            answer.append(current.data)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
        return answer 
    
    def tree_preorder_iter(self, root):
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
    
    def tree_preorder_recur(self, root, answer):
        answer.append(root.data)
        if root.left:
            self.tree_preorder_recur(root.left, answer)
        if root.right:
            self.tree_preorder_recur(root.right, answer)
        return answer
    
    def tree_inorder_iter(self, root):
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
        
    def tree_inorder_recur(self, root, answer):
        if root:
            self.tree_inorder_recur(root.left, answer)
            answer.append(root.data)
            self.tree_inorder_recur(root.right, answer)        
        return answer
    
    def tree_postorder_iter(self, root):
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
    
    def tree_postorder_recur(self, root, answer):
        if root:
            self.tree_postorder_recur(root.left, answer)
            self.tree_postorder_recur(root.right, answer)
            answer.append(root.data)
        return answer


class GraphTraversal:

    def graph_bfs(self, edges, start, end):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)

        queue = [start]
        parent = {start: None}
        path = []
        
        while queue:
            current = queue.pop(0)
            if current == end:
                while current:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path
            
            for neighbor in adj_list[current]:
                queue.append(neighbor)
                parent[neighbor] = current
                
        return False 
            
    def graph_dfs_iter(self, edges, start, end):
        adj_list = collections.defaultdict(list)
        for x, y in edges:
            adj_list[x].append(y)

        stack = [start]
        parent = {start : None}

        while stack:
            current = stack.pop()
            if current == end:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                path.reverse()
                return path
            for neighbor in adj_list[current]:
                stack.append(neighbor)
                parent[neighbor] = current
                
        return False
        
    def graph_dfs_recur(self, edges, start, stop):
        res = []
        adj_list = collections.defaultdict(list)
        parent = {start : None}
        
        for x, y in edges:
            adj_list[x].append(y)
        self._helper(adj_list, parent, res, start, stop)
        
        return res
    
    def _helper(self, adj_list, parent, res, curr, stop):
        if curr == stop:
            temp = []
            c = curr
            while c:
                temp.append(c)
                c = parent[c]
            temp.reverse()
            return res.append(temp)
        
        for neighbor in adj_list[curr]:
            parent[neighbor] = curr 
            self._helper(adj_list, parent, res, neighbor, stop)


class TestGraphTraversal(unittest.TestCase):
    
    def setUp(self):
        self.g = GraphTraversal()
        self.edges = [[1,2],
                     [1,3],
                     [1,4],
                     [2,5],
                     [5,6],
                     [4,7],
                     [5,7]]
        
    def tearDown(self):
        self.g = None
        
    def test_graph_bfs_path(self):
        answer = self.g.graph_bfs(self.edges, 1, 6)
        answer_2 = self.g.graph_bfs(self.edges, 3, 6)
        self.assertEqual(answer, [1, 2, 5, 6])
        self.assertFalse(answer_2)
        
    def test_graph_dfs_path(self):
        answer = self.g.graph_dfs_iter(self.edges, 1, 7)
        answer_2 = self.g.graph_dfs_iter(self.edges, 3, 7)
        self.assertEqual(answer, [1, 4, 7] )
        self.assertFalse(answer_2)
         
    def test_graph_dfs_recur(self):
        answer = self.g.graph_dfs_recur(self.edges, 1, 7)
        answer_2 = self.g.graph_dfs_recur(self.edges, 3, 7)
        self.assertEqual(answer, [[1, 2, 5, 7], [1, 4, 7]])
        self.assertFalse(answer_2)
               
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
        answer = self.t.tree_bfs(self.root)
        self.assertEqual(answer, [10, 15, 5, 13, 7, 2, 14, 6])

    def test_tree_preorder_iter(self):
        answer = self.t.tree_preorder_iter(self.root)
        self.assertEqual(answer, [10, 5, 2, 7, 6, 15, 13, 14])
        
    def test_tree_preorder_recur(self):
        answer = self.t.tree_preorder_recur(self.root, [])
        self.assertEqual(answer, [10, 5, 2, 7, 6, 15, 13, 14])

    def test_tree_inorder_iter(self):
        answer = self.t.tree_inorder_iter(self.root)
        self.assertEqual(answer, [2, 5, 6, 7, 10, 13, 14, 15])
        
    def test_tree_inorder_recur(self):
        answer = self.t.tree_inorder_recur(self.root, [])
        self.assertEqual(answer, [2, 5, 6, 7, 10, 13, 14, 15])
        
    def test_tree_postorder_iter(self):
        answer = self.t.tree_postorder_iter(self.root)
        self.assertEqual(answer, [2, 6, 7, 5, 14, 13, 15, 10])
        
    def test_tree_postorder_recur(self):
        answer = self.t.tree_postorder_recur(self.root, [])
        self.assertEqual(answer, [2, 6, 7, 5, 14, 13, 15, 10])

 
if __name__ == '__main__':
    unittest.main()
