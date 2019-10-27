import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        
class Solution:
    def __init__(self):
        self.output = []

    def create_minimal_bst(self, arr, start, stop):
        if stop < start:
            return None

        mid = (start + stop) // 2
        n = Node(arr[mid])
        n.left = self.create_minimal_bst(arr, start, mid-1)
        n.right = self.create_minimal_bst(arr, mid + 1, stop)

        return n
        

    def dfs_preorder(self, root):
        if root:
            self.output.append(root.data)
            if root.left:
                self.dfs_preorder(root.left)
            if root.right:
                self.dfs_preorder(root.right)    
        return self.output
    

class TestSolution(unittest.TestCase):
    
    def test_valid(self):
        s = Solution()
        arr = [10, 20, 30, 40, 50, 60]
        answer = s.create_minimal_bst(arr, 0, len(arr)-1)
        output = s.dfs_preorder(answer)
        self.assertEqual(output, [30, 10, 20, 50, 40, 60])

if __name__ == '__main__':
    unittest.main()
