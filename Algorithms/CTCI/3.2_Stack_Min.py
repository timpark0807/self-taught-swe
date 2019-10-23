class Stack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, data):
        if self.min == [] or data < self.min[-1]:
            self.min.append(data)
            
        self.stack.append(data)

    def pop(self):
        if self.stack == []:
            return 'Error'

        # Error: called function by self.get_min instead of self.get_min()
        if self.get_min() == self.stack[-1]:
            self.min.pop()

        answer = self.stack.pop()
        return answer

    def get_min(self):
        return self.min[-1]

s = Stack()
s.push(10)
s.push(8)
s.push(7)
s.push(12)
s.push(6)
ans = s.get_min()
s.pop()
ans2 = s.get_min()
print(ans, ans2)
