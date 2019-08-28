
class Heap:
    def __init__(self, heap=[]):
        self.heap = heap
        self.size = len(heap)
            
    def build_max_heap(self):
        for index in reversed(range(0, self.size // 2)):
            self.heapify(index)
            
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        return True
    
    def heapify(self, root):   
        left = root * 2 + 1
        right = root * 2 + 2
        largest = root
        if left < self.size:
            # If the value of the root's left child is greater than root
            if self.heap[left] > self.heap[root]:
            # Largest is reassigned to the value of the root's left child
                largest = left
            # Else if the value of the root's right child is greater than the largest value,
        if right < self.size:
            if self.heap[right] > self.heap[largest]:
                # Assign largest to value of right child
                largest = right 
        if largest != root:
            self._swap(largest, root)
            self.heapify(largest)
            
# max_heap

#size = 5
#index =  0  1  2  3   4
#arr =  [15, 12, 6, 4, 8]

arr = [8, 4, 6, 15,12] 
heap = Heap(arr)
heap.build_max_heap()
print(heap.heap)

# build_max_heap:                       stack =     | heapify(1) |
#   for index in [2. 1, 0]:                         | heapify(0) |
#       max_heapify(0)                              --------------


# heapify(1):
#   size = 5
#   root = 1
#   heap[root] = 8
#   left = 3
#   heap[left] = 4
#   right = 4
#   heap[right] = 12

#   largest = 4
#   heap[largest] = 12


#         15
#       /    \ 
#      12     6
#     / \
#    4   8

