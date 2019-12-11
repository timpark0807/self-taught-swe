# Doubly Linked List

A doubly linked list is a string of nodes with each node containing data, and a reference to the previous and next node.

## Pros and Cons
### Pros:
- Traversal and search available in both directions 

### Cons:
- Nodes require more memory to store previous pointer 

## Implementation
Define a Node class
```
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None    
```
Define a Doubly Linked List Class 
```
class DoublyLinkedList:
    def __init__(self):
        self.head = None
```
## Operations
Insert at beginning
```
def insert_start(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node 
```