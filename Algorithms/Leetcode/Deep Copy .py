def deep_copy(self, root):
    # 1a. Create copies of original nodes
    # 1b. Hash original node : copied node
    
    # 2.  Set copied node random pointers
    #     by looking up the current nodes
    #     random pointer in the hashtable.
    
    dummy = Node(0, None, None)
    current = root
    new_head = dummy
    d = dict()
    
    while current:
        new_head.next = Node(current.val, None, None)
        d[current] = new_head.next
        current = current.next
        new_head = new_head.next

    new_head = dummy.next
    current = root

    while current:
        if current.random:
            new_head.random = d[current.random]

        current = current.next
        new_head = new_head.next

    return dummy.next
