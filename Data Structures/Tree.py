

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data
    
class BinarySearchTree:
    
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        current = self.root 
        if self.root is None:
            self.root = Node(value)
        elif value < self.root:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.root:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
                    
    def search(self, value):
        current = self.root
        while current is not None:
            if value < current.data:
                current = current.left
            elif value > current.data:
                current = current.right
            else:
                return current



b = BinarySearchTree()
b.insert('5')
b.insert('2')
b.insert('6')
b.insert('3')
sear = b.search('2')
print(b.root.left)
print(b.root.right)
print(sear)    
