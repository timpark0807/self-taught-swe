class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def symmetry(root):
    """
         1
       /   \
      2     2
     / \   / \
    3   4 4   3

    Using a queue.
    
    Set left and right nodes to represent the side of the tree
    
    check that
        1. left.left == right.right
        2. left.right == right.right

    return False when
        1. either left or right do not have a node
        2. data in left or right are unequal

    queue: 
    (2) <- (2) <- (3) <- (3) <- (4) <- (4)
    
    1. root.left, root.right
    2. root.left.left, root.right.right
    3. root.left.right, root.right.left
    """
    if root is None:
         return False
        
    ln = root.left
    rn = root.right
    q = [ln, rn]
    
    while q:
        
        ln = q.pop(0)
        rn = q.pop(0)
        
        if ln.data != rn.data:
            return False
        
        if ln.left and rn.right:
            q.append(ln.left)
            q.append(rn.right)
        # elif (ln.left and not rn.right) or (rn.right and not ln.left):
        # Can be simplified to below. 
        elif ln.left or rn.right:
            return False

        if ln.right and rn.left:
            q.append(ln.right)
            q.append(rn.left)
        elif ln.right or rn.left:
            return False

    return True

if __name__ == '__main__':
    root = newNode(1)  
    root.left = newNode(2)  
    root.right = newNode(2)  
    root.left.left = newNode(3)  
    root.left.right = newNode(4)  
    root.right.left = newNode(4)  
    root.right.right = newNode(3)

    ans = symmetry(root)
    print(ans)

#         1
#       /   \
#      2     2
#     / \   / \
#    3   4 4   3
