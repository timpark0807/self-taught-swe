import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:   
    def check_balanced(self, root):
        if root is None:
            return True

        queue = [(0, root)]
        levels_with_leaf = set()
        
        while queue != []:
            current = queue.pop(0)
            current_depth = current[0]
            current_node = current[1]
                
            if current_node.left is None and current_node.right is None:
                check_depth = current_depth - 2
                if check_depth in levels_with_leaf:
                    return False
                else:
                    levels_with_leaf.add(current_depth)    
            else:
                if current_node.left:
                    queue.append((current_depth + 1, current_node.left))
                if current_node.right:
                    queue.append((current_depth + 1, current_node.right))

        return True
                       
"""  
    # do a bfs to find all leaf nodes

x    # initialize a queue with depth and root
x        # queue will contain tuples
x        # (depth, current_node)

x    # while queue is not empty: 
x        # pop first off queue,as current
x            # ******REMEMBER************
x            # to set current_depth and current_node as [0] and [1] of popped item 
            
x        # if current_node.left: add (depth + 1, current_node)
x        # if current_node.right: add (depth + 1, current_node)
        
x        # if current_node.left and current_node.right are both None
x            # if depth of leaf node is > 2 of any other leaf nodes
x            # if current_depth - 2 or current_depth + 2 in dict:
x                # return False
                
x            # Save its depth in a data structure
x                # -> What DS should we use?
x                # -> We must ensure fast lookups O(1) 
            
    # return Boolean

"""
# depth 
#   0          (10)  
#             /    \
#   1       (5)    (15)
#          /   \    
#   2    (3)   (8)
#             /   \
#   3        (7)   (9)
#              \              
#   4          (4)

#        queue = [(4, 4)
#
#        current_depth = 3
#        current_node = 9
#
#        levels_with_leafs = {1, 2, 3
#
#        current_depth - 2 = 1
#        current_depth + 2 = 5
#


class TestSolution(unittest.TestCase):

    def test_unbalanced(self):
        s = Solution()
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(3)
        root.left.right = Node(8)
        root.left.right.left = Node(7)
        root.left.right.right = Node(9)
        root.left.right.left.right = Node(4)

        self.assertFalse(s.check_balanced(root))

    def test_balanced(self):
        s = Solution()
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.right.right = Node(20)
        root.left.left = Node(3)
        root.left.right = Node(8)
        root.left.right.left = Node(7)
        root.left.right.right = Node(9)

        self.assertTrue(s.check_balanced(root))

if __name__ == '__main__':
    unittest.main()
