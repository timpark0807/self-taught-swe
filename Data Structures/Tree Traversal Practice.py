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
    stack = [root]
    current = root
    while stack:
        current = stack.pop()
        print(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)

def postorder(root):
    stack = [root]
    current = root
    
    while stack:
        if current:
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            current = current.left
        else:
            data = stack.pop()
            print(data.data)

def levelorder(root):
    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

            
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    postorder(root)
    
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.right = Node(5)
    levelorder(root2)
    
#       (10)
#      /    \
#    (5)    (15) 
#   /   \ 
# (2)  (7)
#
# q = [ 2 , 7]

