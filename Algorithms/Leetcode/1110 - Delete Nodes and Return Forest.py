def delNodes(root, to_delete):
    """
    input  : root node, list of nodes to delete
    output : 2d array -> list of roots after deletion

    Variables Needed:
    result = []
    parent = dict
    
    
    Procedure:

    1. DFS - Keep track of parent
    2. If we encounter a node in the to_delete list, delete it
        2. Backtrack to its parent, set the .left or .right to None
        3. Add current_node.left and current_node.right to result

            1
         /                 
        2      3
      /       /  \
     4    5  6    7  

    to_delete = [3, 5]
    parent = {1 : None,
              2 : 1,
              4 : 2,
              5 : -1,
              3 : 1,
              6 : None,
              7 : None}

    stack = [
    curr = 3
    p = 1
    res = [1, 6, 7
    """
    # Get parent nodes 
    stack = [root]
    parent = {root:None}

    while stack:
        current = stack.pop()
        if current.right:
            parent[current.right] = current
            stack.append(current.right)
        if current.left:
            parent[current.left] = current
            stack.append(current.left)
            
        if current.val in to_delete:
            p = parent[current]
            if p:
                if p.left == current:
                    p.left = None
                else:
                    p.right = None
            parent[current] = -1
            
            if current.left:
                parent[current.left] = None
            if current.right:
                parent[current.right] = None

    stack = [root]
    res = [] 
    while stack:
        current = stack.pop()
                
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


        if current.val in to_delete:
            p = parent[current]
            if p:
                if p.left == current:
                    p.left = None
                else:
                    p.right = None
            parent[current] = -1
            
            if current.left:
                parent[current.left] = None
            if current.right:
                parent[current.right] = None
                
    for key, item in parent:
        if item == None:
            res.append(key.val)
    return res


            



            
