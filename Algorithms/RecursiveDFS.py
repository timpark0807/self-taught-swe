class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None
        self.right = None
        
def dfs_inorder(root):
    if root is None:
        if root.left:
            dfs_inorder(root.left)
        print(root.data)
        if root.right:
            dfs_inorder(root.right)
    return None

def dfs_preorder(root):
    if root:
        print(root.data)
        if root.left:
            dfs_preorder(root.left)
        if root.right:
            dfs_preorder(root.right)
    return None

def dfs_postorder(root):
    if root:
        if root.left:
            dfs_postorder(root.left)
        if root.right:
            dfs_postorder(root.right)
        print(root.data)
    return None

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    dfs_postorder(root)
