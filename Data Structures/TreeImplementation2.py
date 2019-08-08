class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        # Binary Search Tree Insert

        # Values less than the root node will be on the left subtree
        if value < self.data:

            # If the current node does not have a left child, then its new left child will be the new Node
            if self.left is None:
                self.left = Node(value)
                
            # Else, there already is a left child and we recursively call insert on this left child 
            else:
                return self.left.insert(value)
            
        # Values greater than the root node will be on the right subtree
        elif value > self.data:

            # If the current node does not have a right child, then its new right child will be the new Node
            if self.right is None:
                self.right = Node(value)

            # Else, there already is a right child and we recursively call insert on this right child
            else:
                return self.right.insert(value)
        else:
            return False
        
    def find(self, value):
        
        # If the value we are looking for is equal to the current node's date, return True
        if value == self.data:
            return True
        
        # If the value we are looking for is less than the current node's value, it must be contained in it's left subtree 
        elif value < self.data:

            # if we reach the end of the left subtree, the value is not in the tree
            if self.left is None:
                return False
            
            # Else, continue by recursively searching the left subtree for the value
            else:
                return self.left.find(value)
            
        # If the value we are looking for is greater than the current node's value, it must be contained in it's right subtree
        elif value > self.data:

            # If we reach the end of the right subtree, the value is not in the tree
            if self.right is None:
                return False

            # Else, continue by recursively searching the right subtree for the value
            else:
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
print(root.find(2))
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
