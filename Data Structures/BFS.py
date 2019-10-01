class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def levelorder(root):
    if root is None:
        return

    queue = []

    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
def inorder(root):
    stack = [root]

    while stack:
        current = stack.pop()
        print(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


def preorder(root):
    stack = []
    current = root

    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right
            
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
            printing = stack.pop()
            print(printing.data)
            

            
root = Node(12)
root.left = Node(9)
root.right = Node(15)
root.left.left = Node(7)
root.left.right = Node(11)
print(postorder(root))

# print
##         12
##       /    \
##      9      15
##     / \       \
##    7   11      
