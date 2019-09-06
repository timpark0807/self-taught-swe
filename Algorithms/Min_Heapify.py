class Heap:

    def __init__(self, heap=[0]):
        self.heap = heap
        self.size = len(heap) - 1

    def min_heapify(self, index):
        left = index * 2
        right = index * 2 + 1
        smallest = index

        if left <= self.size and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right <= self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.min_heapify(smallest)

    def build_min_heap(self):
        for index in reversed(range(1, len(self.heap) // 2)):
            self.min_heapify(index)

    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.bubble_up(self.size)

    def bubble_up(self, i):
        while i >= 1:
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
            i = i // 2

    def pop(self, i):
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        while (i * 2) <= self.size:
            mc = self.minchild(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc
        return self.heap.pop()

    def minchild(self, i):
        if i * 2 + 1 > self.size:           # if there is no left child, return that leaf
            return i * 2
        else:
            if self.heap[i] < self.heap[i * 2]:
                return i * 2
            else:
                return i * 2 + 1



heap = Heap([0,2,4,8,9,10])
heap.build_min_heap()
print(heap.heap)
heap.insert(1)
print(heap.heap)
heap.pop(1)
print(heap.heap)



        
