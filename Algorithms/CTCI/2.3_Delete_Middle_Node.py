class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return repr(self.val)

def delete_middle(node):
    if node.next:
        node.val = node.next.val
        node.next = node.next.next
    else:
        print('error')
        
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(20)
print(head, head.next, head.next.next, head.next.next.next)

ok = delete_middle(head.next)
print(head, head.next, head.next.next)

# current
# head
# 
# ListNode(10)  ->  ListNode(20)  ->  ListNode(30)  ->  ListNode(20)  ->   None
