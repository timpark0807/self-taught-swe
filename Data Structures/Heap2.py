class Heap:
    def __init__(self, heap=[]):
        self.heap = heap
        self.size = len(heap) - 1

    def min_heapify(self, index):
        left = 2 * index
        right = 2 * index + 1
        smallest = index

        if left < self.size and self.heap[index] > self.heap[left]:
            smallest = left
        if right <= self.size and self.heap[smallest] > self.heap[right]:
            smallest = right
        if smallest != index:
            self.swap(smallest, index)
            self.min_heapify(smallest)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        return

heap = Heap([0, 30, 5, 25, 2, 55])
heap.min_heapify(1)
print(heap.heap)
        
