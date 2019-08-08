class Node:
    
    def __init__(self, data=None, next=None):
        self.data= data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def list_length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
            
    def new_head(self, newhead):
        new_head = Node(newhead)
        new_head.next = self.head
        self.head = new_head
        
    def insert_node(self, newdata):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                current_node.next = Node(newdata)
                return self.head
            current_node = current_node.next
        
    def delete_node(self, deletenode):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == deletenode:
                if previous_node is None: 
                    newHead = current_node.next
                    current_node.next = None
                    return newHead
                previous_node.next = current_node.next
                return self.head
            previous_node = current_node
            current_node = current_node.next
        return self.head


llist = LinkedList()

llist.head = Node('Mon')

llist.print_list()

print('*' * 30)

llist.insert_node('Tues')
llist.insert_node('Wed')
llist.insert_node('Thurs')
llist.insert_node('Fri')

llist.print_list()

print('*' * 30)

llist.delete_node('Thurs')

llist.print_list()

print('*' * 30)

llist.new_head('Sun')

llist.print_list()

print('*' * 30)
print(llist.head)

print('*' * 30)
print(llist.list_length())
