# Stack
The Stack data structure follows the LIFO (Last In First Out) principle. In other words, the most recent item added to the stack is the first item to be removed.

## Array vs. Linked List
The data structure can be implemented using an array or a linked list. When implementing a Stack using the linked list, we perform all push and pop operations on the head node. 

### Array
```
__Pros__
- Easy to Implement
- Saves memory as pointers do not have to be stored

__Cons__
- Memory allocation is not dynamic 
```
### Linked List
```
__Pros__
- Dynamic Sizing. Size of stack can grow and shrink easily.

__Cons__
- Requires extra memory due to involvement of pointers
```

## Linked List Implementation 
A Stack implementation using linked lists does not require you to implement a linked list and its different operations. 

Since a stack follows the principle of LIFO, so we do not care about anything other than the head node. We design our insertion and deletion operations around the head of the stack. 

Define a Node class
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   
```
Define a Stack class
```
class Stack:
    def __init__(self, head):
        self.head = head
        self.size = 1
```
### Operations
The operations below will be contained within the Stack class defined above, giving us access to initialized head and size variables.

__Pop__: remove the top item from the stack and return its value.
```
def pop(self):
    value = self.head
    self.head = self.head.next
    self.size -= 1    
    return value 
```
__Push__: Adds a new node to the top of the stack.
```
def push(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node 
    self.size += 1
```
__Peek__: Returns the value at the top of the stack. 
```
def peek(self):
    return self.head
```
__Is Empty__: Checks if Stack is empty and returns a boolean value.
```
def is_empty(self):
    return self.head is None 
```
__Size__ : Returns the size of the stack.
```
def get_size(self):
    return self.size
```

## Big O
Access   :  O(n)

Search   :  O(n)

Insertion :  O(1)

Deletion  :  O(1)

## Use Cases
1. Check is parenthesis are valid 
2. Check if all opening '<>' tags have matching closing '</>' tags
