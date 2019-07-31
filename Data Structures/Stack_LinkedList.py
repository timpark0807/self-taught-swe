"""
Implementation of a Stack Data Structure using a Linked List for dynamic memory allocation.

Push and Pop operations are performed on the head of the linked list.

This provides O(1) time for insertion (push) and deletion (pop).

Reference: https://codereview.stackexchange.com/questions/193162/stack-implementation-with-singly-linked-list
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self, head):
        self.head = head
        self.size = 1

    def get_size(self):
        return self.size

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        value = self.head
        self.head = self.head.next
        self.size -= 1
        return value 

h = Node('3')
s = Stack('h')
s.push('2')
s.push('1')
lent = s.get_size()
print(lent)
