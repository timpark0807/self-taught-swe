class ListNode:
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
        if not current:
            remove = stack.pop()
            print(remove.data)
        else:
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            current = current.left

        
#        (10)
#       /    \
#     (5)   (15)
#    /   \
#  (4)   (6)
#
# stack = [15, 
#
# print = [10, 5, 4, 6
#
# current = 6



root = ListNode(10)
root.left = ListNode(5)
root.right = ListNode(15)
root.left.left = ListNode(4)
root.left.right = ListNode(6)
#inorder(root)
#preorder(root)
postorder(root)
