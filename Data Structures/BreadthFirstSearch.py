class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs(root):
    queue = []
    queue.append(root)
    while queue:
        current = queue.pop(0)
        print(current.data)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    print(bfs(root))

# print
##         1
##       /    \
##      2      3
##     / \       \
##    4   5



## Queue
##
## 1, 2

##  3 <- 4 <- 5
