class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None 

class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.capacity = k 
        self.size = 0 
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next, self.tail.prev = self.tail, self.head
        
    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False 
        temp = self.head.next
        newNode = Node(value) 
        newNode.next = temp 
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode
        self.size += 1
        return True 
        
    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False 
        temp = self.tail.prev
        newNode = Node(value)
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = temp 
        temp.next = newNode
        self.size += 1
        return True 
    
    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        temp = self.head.next.next
        self.head.next = temp
        temp.prev = self.head
        self.size -= 1
        return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        temp = self.tail.prev.prev
        temp.next = self.tail
        self.tail.prev = temp 
        self.size -= 1
        return True 
        
    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.head.next.val
    
    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1     
        return self.tail.prev.val 

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.size == 0 

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return self.size == self.capacity 
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
