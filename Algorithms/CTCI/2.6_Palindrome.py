class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def is_palindrome(root):
    length = get_length(root)
    num = length // 2

    current = root
    prev = None

    while num > 0:
        temp = current
        current = current.next
        temp.next = prev
        prev = temp 
        num -= 1

    if length % 2 != 0:
        current = current.next

    while prev and current:
        if prev.data == current.data:
            prev = prev.next
            current = current.next
        else:
            return False

    return True


def is_palindrome2(root):
    length = get_length(root)
    
    # Get left and right pointers in the correct position
    fast = root.next.next
    current = root
    
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        current = current.next

    left = current
    
    if fast is not None:
        right = left.next.next
    else:
        right = left.next

    # Reverse the left half of the linked list

    current = root
    prev = None

    while current:
        temp = current
        current = current.next
        temp.next = prev
        prev = temp 

    
def get_length(root):
    count = 0
    while root:
        count += 1
        root = root.next

    return count 
        

    

if __name__ == '__main__':
    head = Node('b')
    head.next = Node('a')
    head.next.next = Node('c')
    head.next.next.next = Node('c')
    head.next.next.next.next = Node('a')
    head.next.next.next.next.next = Node('b')
    print(head.data,
          head.next.data,
          head.next.next.data,
          head.next.next.next.data,
          head.next.next.next.next.data,
          head.next.next.next.next.next.data)

    answer = is_palindrome(head)
    print(answer)
