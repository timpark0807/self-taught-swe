class QueueTwoStacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())

            if self.stack2 == []:
                return "Error"

        return self.stack2.pop()


if __name__ == '__main__':
    q = QueueTwoStacks()
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    q.enqueue('go')
    print(q.stack1)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
