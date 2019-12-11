class Heap:
    def __init__(self, heap=[0]):
        self.heap = heap
        self.size = 0

    def insert(self, value):
        if self.heap == []:
            self.heap.append(value)
            self.size += 1
        else:
            self.heap.append(value)
            self.size += 1
            self.bubble_up(self.size)

    def bubble_up(self, i):
        while i//2 >= 1:
            if self.heap[i] < self.heap[i//2]:      # If child node is less than parent node
                self.swap(i, i//2)                  # Swap child and parent node 
            i = i // 2
            
    def swap(self, i, j):
        return self.heap[i], self.heap[j] == self.heap[j], self.heap[i]

    def pop(self):
        value = self.heap[1]
        self.bubble_down(self.heap[1])
        return value

    def bubble_down(self):
        self.swap(1, self.size)
        self.heap.pop()
        
        return 


heap = Heap()
heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(5)
print(heap.heap)
