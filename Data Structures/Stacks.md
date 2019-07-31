# Stack
LIFO - Last In First Out

The most recent item added to the stack is the first item to be removed.

Can be implemented using an array or a linked list.
### Array
Pros:
- Easy to Implement
- Saves memory as pointers do not have to be stored

Cons:
- It is not dynamic 

### Linked List
Pros:
- Dynamic Sizing. Size of stack can grow and shrink easily.

Cons:
- Requires extra memory due to involvement of pointers


## Operations
When implementing a Stack using the linked list, we perform all push and pop operations on the head node. 
The examples below will reflect operations for a Linked List Stack. 

- pop(): remove the top item from the stack
```
def pop():
    value = self.head
    self.head = self.head.next
    return value 
```
- push(item): add an item to the top of the stack
```
def push(data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node 
```
- peek(): return the top of the stack
```
def peek():
    return self.head
```
- isEmpty(): returns true if stack is empty

## Big O:
- Access   :  O(n)
- Search   :  O(n)
- Insertion :  O(1)
- Deletion  :  O(1)