class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                return self.left.insert(value)
        elif value > self.data:
            if self.right is None:
                self.right = Node(value)
            else:
                return self.right.insert(value)
        else:
            return False
        
    def find(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            return self.left.find(value)
        elif value > self.data:
            return self.right.find(value)

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
root.insert(5)
root.insert(7)
root.insert(15)
root.insert(12)
root.insert(1)
root.insert(23)
print('preorder')
root.preorder()
print('postorder')
root.postorder()
print('inorder')
root.inorder()
"""

         10
       /    \
      5     15
     / \    / \
    1   7  12  23
    
"""

## print(root.data)
## print(root.left.data)
## print(root.left.left.data)
## print(root.left.right.data)
## print(root.right.data)
