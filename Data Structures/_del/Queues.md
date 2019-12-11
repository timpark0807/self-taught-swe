# Stack
FIFO - First In First Out

The most first item added to the queue is the first item to be removed.

Can be implemented using an array or a linked list.
### Array
Pros:
Cons:

### Linked List
Pros:
Cons:

## Implementation 
Define a Node
```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```
Define a Queue
```
class Queue:
    def __init__(self):
        self.head = head
        self.tail = head
```
## Operations
EnQueue: add an item to the end of the queue
1. Create a new node 
2. Point the current tail's next value to the new node 
3. Set the new tail equal to new node
```
def enQueue(self, data):
    self.tail.next = Node(data)
    self.tail = self.tail.next 
```
DeQueue: remove the first item in the queue
1. Set value of head to a new variable
2. Set head to the next node
3. Return value of step 1
```
def deQueue(self):
    value = self.head
    self.head = self.head.next
    return value 
```
Peek: return the top of the queue
```
def peek(self):
    return self.head 
```
Is Empty: Checks if queue is emtpy 
```
def is_empty(self):
    return self.head is None and self.tail is None
```

## Big O:
- Access   :  O(n)
- Search   :  O(n)
- Insertion :  O(1)
- Deletion  :  O(1)