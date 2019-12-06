class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data
    
class LinkedList:

    def __init__(self, head):
        self.head = head

    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next
        
    def add_to_end(self, data):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)

    
class Stack:

    def __init__(self, head):
        self.head = head
        
    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next
        


    def add(self, data):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = Node(data)

    def peek(self):
        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
        return current_node


h = Node('10')
llist = LinkedList(h)
llist.add_to_end('11')
llist.traversal()
