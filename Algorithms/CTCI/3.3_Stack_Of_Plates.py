class SetOfStacks:
    def __init__(self, size):
        self.stackset = []
        self.size = size

    def push(self, data):

        # If set of stacks is empty
        # Or last stack in the stack set is full
        # Create a new stack with the data
        if self.stackset == [] or len(self.stackset[-1]) >= 3:
            self.stackset.append([data])
        else:
            # Else, iterate backward through the set of stacks
            # Find the first stack in the set that isn't empty
            # And append the new data
            for stack in reversed(self.stackset):
                if stack != []:
                    stack.append(data)
                
    def pop(self):

        if self.stackset == []:
            return 'Error: Empty Set of Stacks'
        else:
            # Iterate backwards through the set of stacks
            # Find the first stack in the set that isn't empty
            # Pop the last value off that stack
            # If we encounter an empty stack, remove it from the set. 
            for stack in reversed(self.stackset):
                if stack != []:
                    current = stack.pop()
                    break
                else:
                    self.stackset.pop()
        
        return current


if __name__ == '__main__':
    s = SetOfStacks(3)
    s.push(10)
    s.push(8)
    s.push(9)
    print(s.pop())
    s.push(5)
    s.push(7)
    print(s.pop())
    print(s.pop())
    s.push(1)
    s.push(15)
    print(s.stackset)
