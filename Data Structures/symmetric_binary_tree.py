class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def symmetry(root):

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
    root.left.left = newNode(5)  
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
