class Heap:
    
    def __init__(self, heap=[]):
        self.heap = heap
        self.size = len(heap) - 1

    def __len__(self):
        return self.size

    def build_min_heap(self):
        for i in reversed(range(1, len(self.heap) // 2)):
            self.min_heapify(i)

    def min_heapify(self, index):
        """
        The index that we pass into this function is the index of the parent.
        We compare this parent node, to it's left and right child.
        Which ever child is smaller, will be swapped with the index.

        heap = [5, 10, 3]          heap = [3, 10, 5]
        
             5                          3 
           /   \          ---->       /   \ 
          10    3                    10    5
        """

        # Find index of left and right children for comparison 
        left = 2 * index
        right = 2 * index + 1
        smallest = index

        # Find the smaller of the children
        # If the left/right < self.size comparison fails, it means that the index has no children 
        if left < self.size and self.heap[index] > self.heap[left]:         # if the value at the current index is greater than left child
            smallest = left                                                 # smallest index = left 

        if right <= self.size and self.heap[smallest] > self.heap[right]:   # if previous if statement did not execute, smallest is parent index. 
            smallest = right                                              

        # Swap the smaller child with the parent 
        if smallest != index:                                               # if smallest is NOT index, swap values
            self.swap(smallest,index)
            self.min_heapify(smallest)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        return

heap = Heap([0, 30, 5, 25, 2, 55, 35])
heap.build_min_heap()
print(heap.heap)
        
