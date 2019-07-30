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
        return items == []

def is_reverse(string):
    s = Stack()
    for index in string:
        if index in '({[':
            s.push(index)
        else:
            top = s.pop()
            if is_match(top, index):
                continue
            else:
                return False
            
    return s.is_empty()
    

def is_match(top, index):
    if top == '[' and index ==']':
        return True
    elif top == '(' and index ==')':
        return True
    elif top == '{' and index =='{':
        return True
    else:
        return False
    
                
