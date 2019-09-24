class linkedlist:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None
    
def cycle(head):

    p1 = head
    p2 = head.next

    while p2 and p2.next:
        if p1 == p2:
            return True
        else:
            p1 = p1.next
            p2 = p2.next.next
            
    return False

head = linkedlist(1)
head.next = linkedlist(2)
head.next.next = linkedlist(3)
head.next.next.next = linkedlist(4)
head.next.next.next.next = head


print(cycle(head))
