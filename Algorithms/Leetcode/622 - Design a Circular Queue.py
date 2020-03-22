class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None 

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.ring = Node(-1)
        self.ring.prev = self.ring.next = self.ring
        self.size = 0 
        self.capacity = k 
        
    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        new_node = Node(value) 
        temp = self.ring.prev
        temp.next = new_node
        new_node.prev = temp 
        new_node.next = self.ring
        self.ring.prev = new_node
        self.size += 1
        return True
        
    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        
        retval = self.ring.next
        temp = retval.next
        temp.prev = self.ring
        self.ring.next = temp 
        self.size -= 1
        
        return True 

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.ring.next.val 

    
    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.ring.prev.val
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.capacity
    

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
