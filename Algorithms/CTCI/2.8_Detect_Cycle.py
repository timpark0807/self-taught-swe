class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def loop_detection(root):
    slow = root
    fast = root

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
        
    print(slow.data)
    slow = root

    while slow.data != fast.data:
        slow = slow.next
        fast = fast.next
        
    return slow.data

if __name__ == '__main__':
    head = Node(7)
    head.next = Node(1)
    head.next.next = Node(6)
    head.next.next.next = Node(10)
    head.next.next.next.next = head.next

    print(head.data,
          head.next.data,
          head.next.next.data,
          head.next.next.next.data,
          head.next.next.next.next.data)


    answer = loop_detection(head)

    print(answer)
