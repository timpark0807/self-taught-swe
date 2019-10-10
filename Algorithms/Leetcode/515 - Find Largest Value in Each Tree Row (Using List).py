class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def largest_at_levels(root):
    answer = []
    
    q = [
        {'node': root,
          'depth': 0}
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

        if depth == len(answer):
            answer.append(node.val)
        else:
            answer[depth] = max(answer[depth], node.val)

    return answer


if __name__ ==  '__main__':
    root = Node(1) 
    root.left = Node(10) 
    root.right = Node(6) 
    root.left.left = Node(4) 
    root.left.right = Node(3)
    root.right.left = Node(5)
    print(largest_at_levels(root))

    
