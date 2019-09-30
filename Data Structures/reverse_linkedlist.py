class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None 

def reverse_linkedlist(root):
    curr = root
    prev = None

    while curr:
        temp = curr 
        curr = curr.next
        temp.next = prev
        prev = temp

    root = prev

    return root

if __name__ == '__main__':
    root = ListNode(3)
    root.next = ListNode(2)
    root.next.next = ListNode(1)
    
    print(root.data)
    print(root.next.data)
    print(root.next.next.data)

    print('reverse it:')
    
    root = reverse_linkedlist(root)
    print(root.data)
    print(root.next.data)
    print(root.next.next.data)
    #                                     prev
    #                                     temp 
    #                                              curr 
    # None <-   (3)    <-    (2)    <-    (1)   -> None
