class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class Stack:
    
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.head is None

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        value = self.head
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        return self.head
    
    def getMin(self):
        current_min = self.head.data
        current_node = self.head
        
        while current_node is not None:
            if current_node.data < current_min:
                current_min = current_node.data
            current_node = current_node.next
            
        return current_min 

minStack = Stack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.peek())
print(minStack.getMin())



def is_valid(s):
    stack = Stack()
    for symbol in s:
        if symbol == "(":
            stack.push(symbol)
        elif symbol == ")":
            stack.pop()
            
    return stack.is_empty()

paren = "((())"
ans = is_valid(paren)
print(ans)
