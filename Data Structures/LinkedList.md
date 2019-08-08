# Linked List
A linked list is a string of nodes, with each node containing both data and a reference to the next node in the list. 

## Node
A node is a single list element that contains data and the address of the next node 

## Arrays vs. Linked Lists
Arrays store items sequentially in memory.

Lists store items at different memory segments, which you can find by following the pointers from one node to the next.

## Pros of Linked Lists
1. Dynamic Memory allocation
    - The size of an array is fixed. So we must know the upper limit of elements in advance. 
2. Ease of insertion/deletion 
    - Inserting elements into an array is expensive because the entire array must be shifted. 

## Cons of Linked Lists
1. No random access
    - We have to access elements in a linked list sequentially starting with the head, following the pointers until we reach the element
2. Extra memory space for the pointer

## Implementation 
1. Define a node class 
``` 
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
```
2. Define a linked list class
```
class LinkedList:

    def __init__(self):
        self.head = None
```
3. Initialize the Linked List with a head 
```
llist  = LinkedList()
llist.head = Node('Mon')
```
4. Create new nodes and link them to the head
```
second = Node('Tue')
third = Node('Wed')
fourth = Node('Thur')

llist.head.next = second
second.next = third 
third.next = fourth

```
## Linked List Operations
### Traversal
Begin with the head and access the next node until you reach Null
```
def traversal(self):
    current_node = self.head
    while current_node is not Null:
        print(current_node.data)
        current_node = current_node.next 
```
### Add to end
Traverse through list, once we reach the end, create a new node 
```
def add_to_end(self, new_value)
    current_node = self.head
    while current_node is not Null:
        if current_node.next is None:
            current_node.next = Node(new_value)
            return self.head 
        current_node = current_node.next
```
### Delete a node 
Keep track of previous and current node

- Traverse through the list
- If the node's value equals value we want to delete
    - point previous node's next to current_node's next 
- Handle case where we want to delete the head (previous_node is None)
    - the new head is the current head's next value
    - set current_node.next to none 
```
def delete_node(self, value):
    current_node = self.head
    previous_node = None
    while current_node is not Null:
         if current_node.data == value:
              if previous_node is None:
                  new_head = current_node.next
                  current_node.next = None 
                  return new_head
              previous_node.next = current_node.next
         previous_node = current_node
         current_node = current_node.next
```

### References
- https://www.geeksforgeeks.org/linked-list-set-1-introduction/
- https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html
- https://stackabuse.com/python-linked-lists/