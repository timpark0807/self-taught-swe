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
        elif value == self.data:
            return False

    def find(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.data:
            if self.right is None:
                return False
            else:
                return self.right.find(value)

    def preorder(self):
        if self:
            print(self.data)
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()
        else:
            return
        
    def postorder(self):
        if self:
            if self.left is not None:
                self.left.postorder()
            if self.right is not None:
                self.right.postorder()
            print(self.data)
        else:
            return
        
    def inorder(self):
        if self:
            if self.left is not None:
                self.left.inorder()
            print(self.data)
            if self.right is not None:
                self.right.inorder()
        else:
            return

"""
              10
            /     \
           4      13
          / \    /   \ 
         1   5  11  15

"""

root = Node(10)
root.insert(4)
root.insert(1)
root.insert(5)
root.insert(11)
root.insert(13)
root.insert(15)
print(root.find(4))
root.inorder()
