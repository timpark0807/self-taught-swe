class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return repr(self.val)

def return_kth_to_last(root, k):
    current = root
    fast = current
    
    # set fast pointer
    while k > 0:
        fast = fast.next
        k -= 1

    # Iterate until fast pointer hits None
    while fast:
        current = current.next
        fast = fast.next

    return current.val

head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)
head.next.next.next = ListNode(40)
print(head, head.next, head.next.next, head.next.next.next)

answer = return_kth_to_last(head, k=3)
print(answer)

# current
# head
# 
# ListNode(10)  ->  ListNode(20)  ->  ListNode(30)  ->  ListNode(20)  ->   None
