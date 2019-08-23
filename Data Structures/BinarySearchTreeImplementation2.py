class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)
    
class BinarySearchTree:
    
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def insert(self, root, value):
        if self.root is None:
            root = Node(value)
    
        elif value > root.data: # If value we are inserting is greater than its parents, append to right child of parent
            if root.right is None: # If the parent does not havea right child, its right child will be new node
                root.right = Node(value)
            else:                   # If there is a right child, recurse insert on right child 
                self.insert(root.right, value)

        elif value < root.data: # If value we are inserting is less than its parents, append to left child of parent
            if root.left is None:
                root.left = Node(value)
            else:
                self.insert(root.left, value)
        else:
            return False

    def preorder(self, root):
        if self:
            print(root.data)
            if root.left is not None:
                self.preorder(root.left)
            if root.right is not None:
                self.preorder(root.right)

    def inorder(self, root):
        if self:
            if root.left is not None:
                self.inorder(root.left)
            print(root.data)
            if root.right is not None:
                self.inorder(root.right)                
            

root = Node(12)
bst = BinarySearchTree(root)
bst.insert(root, 9)
bst.insert(root, 11)
bst.insert(root, 15)
bst.insert(root, 7)
bst.inorder(root)
print(bst.root)

# print
# 7
# 9 
# 11
# 12
# 15
##         12
##       /    \
##      9      15
##     / \       \
##    7   11      







