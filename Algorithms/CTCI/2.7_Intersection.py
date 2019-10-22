class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def intersection(list1, list2):
    # If the linked lists are the same length AND intersect,
    # We can simply iterate through both lists at the same time
    
    # If they are not the same length, move the longer list's pointer forward
    # Until they are the same length.
    
    if does_intersect(list1, list2):
        
        # Get length of both lists
        length_1 = get_length(list1)
        length_2 = get_length(list2)

        difference = length_2 - length_1

        # If difference is positive, that means length_2 > length_1
        if difference > 0:
            while difference > 0:
                list2 = list2.next
                difference -= 1

        # If difference is negative, that means length_1 > length_2
        
        elif difference < 0:
            while difference < 0:
                list1 = list1.next
                difference += 1
                
        # When difference is 0, that means we can iterate through the list         
        if difference == 0:
            while list1 and list2:
                if list1 == list2:
                    return list1
                else:
                    list1 = list1.next
                    list2 = list2.next

def get_length(root):
    current = root
    count = 0
    
    while current:
        count += 1
        current =current.next
        
    return count
        

def does_intersect(list1, list2):

    current = list1
    current_2 = list2
    
    while current.next:
        current = current.next

    while current_2.next:
        current_2 = current_2.next
        
    last_1 = current
    last_2 = current_2

    return last_1 == last_2



if __name__ == '__main__':
    head = Node(8)
    head.next = Node(1)
    head.next.next = Node(0)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(2)

    print(head.data,
          head.next.data,
          head.next.next.data,
          head.next.next.next.data,
          head.next.next.next.next.data)
    
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = head.next.next.next
    print(head2.data,
          head2.next.data,
          head2.next.next.data,
          head2.next.next.next.data)

    answer = intersection(head, head2)
    print(answer.data)
