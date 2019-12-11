class MinStack:

    def __init__(self):
        self.items = []
        self.min = []
        self.total = 0 
        self.size = 0 

    def push(self, value):
        self.size += 1
        self.items.append(value)
        if self.min == [] or value < self.min[-1]:
            self.min.append(value)
        self.total += value

    def pop(self):
        self.size -= 1
        if self.items == []:
            return print('Empty Stack')
        if self.items[-1] == self.min[-1]:
            self.min.pop()
        remove = self.items.pop()
        self.total -= remove
        
        return remove

    def get_min(self):
        return print(self.min[-1])
    
    def get_average(self):
        return self.total/self.size


if __name__ == '__main__':
    ms = MinStack()
    ms.push(5)
    ms.push(10)
    ms.push(15)
    ms.get_min()
    print(ms.get_average())
    ms.pop()
    ms.pop()
    ms.get_min()
    ms.pop()    
    ms.pop()   
    ms.pop()   
