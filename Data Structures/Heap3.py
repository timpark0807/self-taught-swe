class Heap:
    """
    Implementation of a Heap Data Structure.


    Pros:
        - Easy access to the max or min value of the data
    """
    
    def __init__(self, heap=[]):
        self.heap=heap
        self.size = len(self.heap)
   
    def build_max_heapify(self):
        """
        Builds a max heap from an unsorted array

        max_heapify indexes less than half the arrays size.
        All indexes greater than half the array are leaves. 
        """
        for index in reversed(range(0, self.size // 2)):
            self.max_heapify(index)

            
    def max_heapify(self, index):
        """
        Swaps largest value between index, left child, and right child into the index position.
        Recursively calls max_heapify on the index until the largest value is already in the index position.
        """
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left 
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self._swap(largest, index)
            self.max_heapify(largest)

    def _swap(self, i, j):
        """
        Internal helper function to swap values of two indexes.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        return

    def insert(self, value):
        """
        Allows us to insert new values into an existing max heap.
        Heaps must be complete by definition, so we insert the value into the last position.
        We call bubble up to place the value in the correct position. 
        """
        self.heap.append(value)
        self._bubble_up(self.size)
        
    def _bubble_up(self, index):
        """
        Places the inserted value in the correct max position 
        """
        while index > 0:
            if self.heap[index] > self.heap[(index-1)//2]:
                self._swap(index, (index-1)//2)
            index = (index-1)//2

    def remove(self):
        """
        Allows us to remove the max value from the max heap.
        Swap the last value of the array to the root index, and bubble down into correct position.
        """
        self._swap(0, self.size)
        value = self.heap.pop()
        self._bubble_down(0)
        return value

    def _bubble_down(self, index):
        """
        Swaps the max value of index, left, and right into the index position.
        """
        while (index * 2) + 2 < self.size:
            max_value = self._get_max(index)
            self._swap(index, max_value)
            index = max_value
            print(max_value)
    
    def _get_max(self, index):
        if index * 2 + 1 > self.size:   # if index has no chidren, return index
            return index
        else:
            if self.heap[index] < self.heap[index * 2 + 1]:       # if left is greater than right, return left
                return index * 2 + 1
            else:
                return index * 2 + 2


if __name__ == '__main__':
    arr = [i for i in range(1,20,2)]
    heap = Heap(arr)
    heap.build_max_heapify()
    heap.insert(55)
    print(heap.heap)
    print(heap.remove())
    print(heap.heap)
