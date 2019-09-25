class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    stack = []
    current = root
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right 


def preorder(root):
    stack = []
    stack.append(root)
    while stack:
        current = stack.pop()
        print(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right = Node(12)
    inorder(root)
    print('preorder')
    preorder(root)

#       (10)
#       /   \
#     (5)   (12)
#     /  \
#   (3)  (7) 
#
#   stack = [12, 7
#   
#   current = 3
#
#   print = [10, 5, 3 

    
    
