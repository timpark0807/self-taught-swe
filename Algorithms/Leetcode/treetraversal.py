class ListNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelorder(root):

    queue = [root]

    while queue:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

        print(current.data)

def inorder(root):
    stack = []
    current = root
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.data)
            current = current.right

def preorder(root):
    stack = [root]

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
            printing = stack.pop()
            print(printing.data)
    
#        (10)
#       /    \
#     (5)   (15)
#    /   \
#  (4)   (6)
#
# stack = [10, 15, 5, 6, 4
#
# print = [4, 5
#
# current = 5

root = ListNode(10)
root.left = ListNode(5)
root.right = ListNode(15)
root.left.left = ListNode(4)
root.left.right = ListNode(6)
postorder(root)
