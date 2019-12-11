class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def insert(self, value):
        new_node = Node(value)
        if value < self.data:
            if self.left is None:
                self.left = new_node
            else:
                return self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = new_node
            else:
                return self.right.insert(value)
        else:
            return False
        
    def find(self, value):
        if value == self.data:
            return True
        elif value > self.data and self.right is not None:
            return self.right.find(value)
        elif value < self.data and self.left is not None:
            return self.left.find(value)
        else:
            return False


    def preorder(self):
        if self:
            print(self.data)
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data)

    def inorder(self):
        if self:
            if self.left is not None:
                self.left.inorder()
            print(self.data) 
            if self.right is not None:
                self.right.inorder()

root = Node(10)
root.insert(6)
root.insert(15)
root.insert(9)
root.insert(7)
root.insert(5)
root.insert(4)
root.preorder()

#            10
#           /  \
#          6    15
#         / \
#        5   9
#       /   /
#      4   7
print('root data is', root.data)
print('left child is', root.left)
print('right child is', root.right)
print('find 15?', root.find(15))
print('find 25?', root.find(25))

