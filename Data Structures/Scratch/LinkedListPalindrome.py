class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None 

def linked_list_palindrome(head):
    count = get_count(head)
    mid = count // 2
    current = head
    prev = None
    
    while mid > 0:
        temp = current
        current = current.next
        temp.next = prev
        prev = temp
        mid -= 1

    head1 = prev
    
    if count % 2 != 0:
        head2 = current.next
    else:
        head2 = current
    
    while head1 and head2:
        if head1.data != head2.data:
            return False
        else:
            head1 = head1.next
            head2 = head2.next

    return head1 is None and head2 is None


def get_count(head):
    count = 0 
    while head:
        count += 1
        head = head.next
    return count 


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(linked_list_palindrome(head))


#  Node(1)   ->   Node(2)   ->   Node(2)   ->   Node(1)  ->   None


#                                        head2
#                           head1
# None   <-  Node(1)   <-   Node(2)      Node(2)   ->   Node(1)  ->   None  
