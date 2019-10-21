class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def partition(head, x):
    if not head:
        return None
    
    current = head
    boundary = head
    
    while current:
        if current.data < x:
            temp = current.data
            current.data = boundary.data
            boundary.data = temp
            boundary = boundary.next
            
        current = current.next

    return head


# 1. Iterate through nodes of linked list
#      -> while current is not None:

# 2. If current.data is less than x
#      -> swap current.data with boundary.data
#      -> increment current and boundary

# 3. If current.data is NOT less than x
#      -> increment current
#

# 4. return head

#   x = 4
#   temp = 2

#   head
#   ListNode(8)  ->  ListNode(5)  -> ListNode(6)  -> ListNode(2)  -> None
#                                                    current
#                    boundary 

if __name__ == '__main__':
    head = Node(8)
    head.next = Node(1)
    head.next.next = Node(6)
    head.next.next.next = Node(2)

    print(head.data, head.next.data, head.next.next.data, head.next.next.next.data)

    answer = partition(head, 4)
    print(answer.data, answer.next.data, answer.next.next.data, answer.next.next.next.data)


