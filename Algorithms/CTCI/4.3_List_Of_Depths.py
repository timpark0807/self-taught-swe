import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)
    
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return repr(self.data)

def list_of_depths(root):

    # Initialize queue and dictionary
    # Begin queue with root node, at depth of 0
    # Our queue will receieve tuples with [0] = depth, [1] = node
    # Time: O(1) // Space: O(1)
    queue = [(0, root)]
    d = dict()
    
    # Time: O(n) // Space: O(n)
    # Where n is the number of nodes in the binary tree
    while queue:
        # dequeue a tuple
        # current_depth is the first item [0] of the tuple 
        # current_node is the second item [1] of the tuple
        current = queue.pop(0)
        current_depth = current[0]
        current_node = current[1]

        # check if the current node has children
        # if it does, enqueue a tuple containing
        # current depth incremented by 1 
        # left or right child  
        if current_node.left:
            queue.append((current_depth + 1, current_node.left))
        if current_node.right: 
            queue.append((current_depth + 1, current_node.right))

        # Add current node to our overall dict
        # Our dict will store values as lists
        # If current depth is in d, append the current_node
        # if it is not, create a new entry as a list
        if current_depth in d:
            d[current_depth].append(current_node)
        else:
            d[current_depth] = [current_node]

    output = []
    
    # Create our linked lists
    # Time: O(mn) // Space: O(n)
    # Where m is the depth (number of different keys)
    # and n is the number of nodes in each depth
    for key, values in d.items():
        root = LinkedListNode(values[0])
        current = root
        for value in values:
            current.next = LinkedListNode(value)
            current = current.next
        output.append(root.next)

    return output


class TestSolution(unittest.TestCase):
    def test_valid(self):
        root = Node(10)
        root.left = Node(5)
        root.right = Node(15)
        root.left.left = Node(1)
        root.left.right = Node(8)
        root.right.left = Node(12)
        root.right.right = Node(20)
        answer = list_of_depths(root)
        self.assertEqual(answer, [10, 5, 1])


if __name__ == '__main__':
    unittest.main()
    
#            (10)
#         /        \
#       (5)        (15)
#      /   \      /   \
#    (1)   (8)  (12)  (20)

# dict  = {
#           1 : [(10)] ,
#           2 : [(5), (15)],
#           3 : [(1), (8), (12), (20)]
#                                     }
# 
#  
#
#

