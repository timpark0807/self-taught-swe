class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head

    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, item):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                current_node.next = StackNode(item)
                return self.head
            current_node = current_node.next

    def pop(self):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.next is None:
                previous_node.next is None
                return self.head
            
            previous_node = current_node
            current_node = current_node.next

head = StackNode('1')
stack = Stack(head)
print("*" * 30)
stack.traversal()
stack.push('2')
stack.push('3')
print("*" * 30)
stack.traversal()
stack.pop()
print("*" * 30)
stack.traversal()
