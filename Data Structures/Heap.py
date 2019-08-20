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
            if self.heap[i] < self.heap[i//2]:
                self.swap(i, i//2)
            i = i // 2
            
    def swap(self, i, j):
        return self.heap[i], self.heap[j] == self.heap[j], self.heap[i]
         

heap = Heap()
heap.insert(10)
heap.insert(20)
heap.insert(30)
heap.insert(5)
print(heap.heap)
