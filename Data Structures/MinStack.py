class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min == [] or x < self.min[-1]:
            self.min.append(x)
            
        self.items.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.items[-1] == self.min[-1]:
            self.min.pop()
            
        self.items.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(1)
obj.push(3)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
