class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        
        # Case 1: Both heaps are same size
        
        [2, 3, 5, 8, 1, 29]
                     ^ 
         
        min =  5, 8, 29
        max = -3, -2
        
        if min heap is empty: 
            push to min heap
        
        if curr num > min heap:
            push to min heap
            
        elif curr num < min heap:
            push to max heap 
        
        balance() 
        

        
        """
        self.min_heap = []
        self.max_heap = [] 
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num) 
        
        elif num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num) 
        
        self._balance()

        
    def get_lengths(self):
        return len(self.min_heap), len(self.max_heap)
    
    def findMedian(self):
        """
        :rtype: float
        """
        min_length, max_length = self.get_lengths()
        if min_length == max_length:
            return float(self.min_heap[0] + -self.max_heap[0]) / 2 
        elif min_length > max_length:
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
        
    def _balance(self):
        min_length, max_length = self.get_lengths()
        
        if min_length - max_length == 2:
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -temp)
            
        elif max_length - min_length == 2:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -temp)
        

        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
