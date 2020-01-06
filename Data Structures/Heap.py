import unittest

class Heap:
    """
    Implementation of a Max Heap.

    We initialize this class with an array of integers.
    If an array is not provided, we initialize with an empty array.

    This object supports the following:
    +------------------+------+-------+
    |   Operation      | Time | Space |
    +------------------+------+-------+
    | Insert           | O(1) |  O(1) |
    | Pop Max          | O(1) |  O(1) |
    | Get Max          | O(1) |  O(1) |
    | Heap Sort        | O(n) |  O(1) |
    +------------------+------+-------+
    """
    
    def __init__(self, heap=[]):
        self.heap = heap
        self.size = len(self.heap)
   
    def heapsort(self):
        """
        Input  :  None
        Output :  None
        
        Description:
            - Builds a max heap from an unsorted array by calling max_heapify on the specified indicies.
            - We use size // 2 because all indicies greater than half the size are leaves.
        """
        for index in reversed(range(0, self.size // 2)):
            self.max_heapify(index)
            
    def max_heapify(self, index):
        """
        Input  :  None
        Output :  None
        
        Description:
            - Swaps largest value between index, left child, and right child into the index position.
            - Recursively calls max_heapify on the index until the largest value is already in the index position.
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
        Input  :  None
        Output :  None
        
        Description:
            - Internal helper function to swap the values at two indices.
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):
        """
        Input  :  None
        Output :  None
        
        Description:
            - Allows us to insert new values into an existing max heap.
            - Heaps must be complete by definition, so we insert the value into the last position of the array.
            - We call bubble up to place the value in the correct position. 
        """
        self.heap.append(value)
        self._bubble_up(self.size)
        
    def _bubble_up(self, index):
        """
        Input  :  None
        Output :  None
        
        Description:
            - Helper function to swap the newly inserted value into the correct max position 
        """
        while index > 0:
            parent = (index-1)//2
            if self.heap[index] > self.heap[parent]:
                self._swap(index, parent)
            index = parent

    def pop_max(self):
        """
        Input  :  None
        Output :  int
        
        Description:
            - Returns the max value from the heap.
            - Swaps the last index of the array to the root index and bubbles it down to the correct position.
        """
        self._swap(0, self.size)
        value = self.heap.pop()
        self._bubble_down(0)
        return value

    def _bubble_down(self, index):
        """
        Input  :  None
        Output :  None
        
        Description:
            - Helper function that swaps the max value of index, left, and right into the index position.
        """
        while (index * 2) + 2 < self.size:
            max_value = self._get_max_child(index)
            self._swap(index, max_value)
            index = max_value
    
    def _get_max_child(self, index):
        """
        Input  :  None
        Output :  int
        
        Description:
            - Helper function that returns the max index between the current index, the left, and the right child.
        """
        if index * 2 + 1 > self.size:   # if index has no chidren, return index
            return index
        else:
            if self.heap[index] < self.heap[index * 2 + 1]:       # if left is greater than right, return left
                return index * 2 + 1
            else:
                return index * 2 + 2


class TestSolution(unittest.TestCase):
    def setUp(self):
        arr = [i for i in range(1,10,2)]
        self.h = Heap(arr)
        self.h.heapsort()

    def tearDown(self):
        self.h = None

    def test_build_max_heapify(self):
        self.assertEqual(self.h.heap, [19, 13, 15, 17, 11, 5, 1, 7, 3, 9])
        
    def test_insert(self):
        self.h.insert(55)
        self.assertEqual(self.h.heap, [55, 7, 9, 1, 3, 5])

if __name__ == '__main__':
    unittest.main()
