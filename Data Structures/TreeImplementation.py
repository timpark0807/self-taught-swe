class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def get_root(self):
        return self.data

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                

root = Node(12)

'''
The tree looks like this after above
       12
      /  \
   None  None
'''

root.insert(6)

'''
The tree looks like this after above
       12
      /  \
     6   None
'''

root.insert(7)

'''
The tree looks like this after above
       12
      /  \
     6    
      \
       7
'''
root.right = Node(13)
root.right.right = Node(15)
root.right.right.left = Node(14)

