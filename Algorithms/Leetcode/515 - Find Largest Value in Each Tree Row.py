class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def largest_at_levels(root):
    level_dict = {}
    
    q = [
        {'node': root,
          'depth': 1}
         ]

    while q:
        current = q.pop(0)
        node = current['node']
        depth = current['depth']

        if node.right:
            q.append({'node': node.right,
                      'depth': depth + 1})
        if node.left:
            q.append({'node': node.left,
                      'depth': depth + 1})
        
        if depth in level_dict:
            level_dict[depth] = max(level_dict[depth], node.val)
        else:
            level_dict[depth] = node.val

    answer = list(level_dict.values())

    return answer


if __name__ ==  '__main__':
    root = Node(1) 
    root.left = Node(10) 
    root.right = Node(6) 
    root.left.left = Node(4) 
    root.left.right = Node(3)
    root.right.left = Node(5)
    print(largest_at_levels(root))

    
