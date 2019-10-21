class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sum_lists_opt(head1, head2):

    output = Node(0)
    current = output
    carry = 0 
    value = carry
    
    while head1 or head2:
        
        if carry > 0:
            value += carry
            carry = 0
            
        if head1 is not None:
            value += head1.data
            
        if head2 is not None:
            value += head2.data
            
        if value >= 10:
            value = value - 10
            carry = 1

        current.next = Node(value)
        current = current.next
        head1 = head1.next
        head2 = head2.next
        value = 0

    return output.next

def sum_lists(head1, head2):

    output = Node(0)
    current = output
    remainder = 0
    
    while head1 or head2:
        summed = head1.data + head2.data
        
        if summed >= 10:
            remainder = 1
            summed = summed - 10
            current.next = Node(summed)  
        elif remainder == 1:
            current.next = Node(summed + remainder)
            remainder = 0
        else:
            current.next = Node(summed)
            
        current = current.next
        head1 = head1.next
        head2 = head2.next
        
    return output.next
if __name__ == '__main__':
    head = Node(7)
    head.next = Node(1)
    head.next.next = Node(6)

    head2 = Node(5)
    head2.next = Node(9)
    head2.next.next = Node(2)

    output = sum_lists_opt(head, head2)

    print(output.data, output.next.data, output.next.next.data)



