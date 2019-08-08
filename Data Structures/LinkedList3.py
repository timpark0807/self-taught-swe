class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return self.data

class DoublyLinkedList:

    def __init__(self, head):
        self.head = head
        self.tail = head
        
    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next
            
    def reverse_traversal(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node)
            current_node = current_node.prev

    def add(self, data):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)
        current_node.next.prev = current_node
        self.tail= current_node.next


        

    def delete(self, value):
        current_node = self.head
        previous_node = None
        while current_node.next is not None:
            if current_node.data == value:
                previous_node.next = current_node.next
                return self.head
            previous_node = current_node
            current_node = current_node.next

            
head = Node('1')
llist = DoublyLinkedList(head)
llist.add('2')
llist.add('3')

llist.traversal()
llist.reverse_traversal()
