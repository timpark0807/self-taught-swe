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
- pop(): remove the top item from the stack
- push(item): add an item to the top of the stack
- peek(): return the top of the stack
- isEmpty(): returns true if stack is empty

## Big O:
- Access   :  O(n)
- Search   :  O(n)
- Insertion :  O(1)
- Deletion  :  O(1)