# Implementation of a Stack using an array

def create_stack():
    stack = []
    return stack

def get_size():
    return len(stack)

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def is_empty(stack):
    return len(stack) == 0

def peek(stack):
    return stack[len(stack) - 1]

stack = create_stack()
is_empty(stack)
push(stack, '1')
push(stack, '2')
push(stack, '3')
print(stack)
print(peek(stack))
pop(stack)
print(stack)
