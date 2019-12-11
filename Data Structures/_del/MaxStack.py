class MaxStack:
    def __init__(self):
        self.items = []
        self.max_stack = []

    def push(self, data):
        if self.max_stack == [] or data > self.max_stack[-1]:
            self.max_stack.append(data)

        self.items.append(data)

    def pop(self):
        value = self.items.pop()
        if self.items is [] or self.max_stack is []:
            return 'Error'
        elif value == self.max_stack[-1]:
            self.max_stack.pop()

        return value

    def get_max(self):
        return print(self.max_stack[-1])


s = MaxStack()
s.push(10)
s.push(15)
s.push(8)
s.push(25)
s.get_max()
s.pop()
s.get_max()
