class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return repr(self.val)

def remove_dups(root):
    current = root

    seen = set()
    
    while current:
        
        if current.val in seen:
            # Remove the node
            prev.next = current.next
            current = current.next
            
        else:
            seen.add(current.val)
            prev = current
            current = current.next
            
    return root

head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(20)
print(head, head.next, head.next.next, head.next.next.next)

head = remove_dups(head)
print(head, head.next, head.next.next, head.next.next.next)

# current
# head
# 
# ListNode(10)  ->  ListNode(20)  ->  ListNode(30)  ->  ListNode(20)  ->   None
