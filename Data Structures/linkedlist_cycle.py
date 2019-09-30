class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None 

def cycle(root):
    slow = root
    fast = root.next

    while fast:
        if slow.data == fast.data:
            return True
        else:
            slow = slow.next
            fast = fast.next.next
            
    return False

if __name__ == '__main__':
    root = ListNode(3)
    root.next = ListNode(2)
    root.next.next = ListNode(1)
    root.next.next.next = ListNode(0)
    root.next.next.next.next = root.next
    print(root.data)
    print(root.next.data)
    print(root.next.next.data)
    print(root.next.next.next.data)
    print('cycle?')
    print(cycle(root))
    

    
    #                            slow
    #                fast                                                
    #   (3)    ->    (2)    ->    (1)   ->    (0)  -|
    #                                               |
    #                 ^------------------------------
