# Mistake: Delete node case where node is the head only returns original node

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self, head):
        self.head = head

    def new_head(self, newhead):
        self.head.data = newhead
        return newhead

    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def append(self, new_data):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                current_node.next = Node(new_data)
                return self.head
            current_node = current_node.next

    def delete(self, value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == value:
                if previous_node is None:
                    new_head = current_node.next
                    current_node.next = None
                    return new_head
                previous_node.next = current_node.next
                return self.head
            previous_node = current_node
            current_node = current_node.next
        return self.head


head = Node('10')
node1 = Node('14')
node2 = Node('17')

head.next = node1
node1.next = node2

llist = LinkedList(head)

print(llist.traversal())
llist.append('11')
print(llist.traversal())
llist.new_head('25')
print(llist.traversal())
