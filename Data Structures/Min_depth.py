class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
def min_depth(root):

    queue = [{'node':root, 'depth':1}]
    while queue:
        item = queue.pop(0)
        current = item['node']
        depth = item['depth']
        
        if current.left:
            queue.append({'node':current.left,'depth':depth+1})
        if current.right:
            queue.append({'node':current.right,'depth':depth+1})
            
        if current.left is None and current.right is None:
            return depth


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print(min_depth(root))
