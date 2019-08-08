"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution:
    
    def isValid(self, s):
        stack = Stack()
        for index in s:
            if index in '({[':
                stack.push(index)
            else:
                if not stack.is_empty():
                    top = stack.pop()
                else:
                    return False
                if self.is_match(top, index):
                    continue
                else:
                    return False
        return stack.is_empty()
    
    def is_match(self, top, index):
        if top == '[' and index ==']':
            return True
        elif top == '(' and index ==')':
            return True
        elif top == '{' and index =='}':
            return True
        else:
            return False
    
class Stack:

    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def push(self, value):
        return self.items.append(value)

    def is_empty(self):
        return self.items == []
