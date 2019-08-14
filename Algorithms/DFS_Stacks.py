# Iterative DFS
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def insert(self, value):
        new_node = Node(value)
        if value < self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                return self.left.insert(value)
        elif value > self.data:
            if self.right == None:
                self.right = Node(value)
            else:
                return self.right.insert(value)
        elif value == self.data:
            return False

    def preorder(self):
        if self:
            print(self.data)
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def dfs(self):
        stack = Stack()
        search = []
        stack.push(self.data)

        search.append(stack.pop())
        stack.push(self.right)
        stack.push(self.left)
        search.append(stack.pop())
        stack.push(self.left.right)
        stack.push(self.left.left)
        search.append(stack.pop())
        stack.push(self.left.left.left)
        search.append(stack.pop())
        return search


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)
    
class Stack:
    def __init__(self, head=None):
        self.head = head
        self.next = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.head == None

    def push(self, value):
        new_node = StackNode(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        
    def pop(self):
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value
    
"""
            10
           /  \ 
          5    11
         /  \
        4    7
       /
      3
"""

root = Node(10)
root.insert(5)
root.insert(7)
root.insert(4)
root.insert(3)
root.insert(11)
root.dfs()
root.preorder()

stack = Stack()
stack.push(root)





