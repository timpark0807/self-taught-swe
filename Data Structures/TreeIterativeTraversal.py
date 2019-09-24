class Node: 
      
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def inorder(head):
    stack = []
    current = head
    stack.append(current)
    current = current.left
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.data)
            current = current.right


def preorder(head):
    stack = []
    current = head
    stack.append(current)
    while stack:
        current = stack.pop()
        print(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        
    """
                 (10)
                /    \
              (8)   (11)
              / \ 
            (4) (9)
        
    """
    
if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(11)
    root.left.left = Node(4)
    root.left.right = Node(9)
    print('inorder')
    inorder(root)
    print('preorder')
    preorder(root)
