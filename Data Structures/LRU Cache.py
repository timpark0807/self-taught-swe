class DLLNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 
        

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        
        Need a data structure that will support insert and deletes  
        
        
        Keep a hashtable that maps the key to the node in the LRU
        
        have 2 ends of the ds 
            - head -> LRU 
            - tail -> MRU 
            
        so any puts will be done on the tail 
            - as they will be the most recently used objects 
            
        any retirevals 
            - should remove the node from the dll and place it to the tail
            

        (h)   <->   (t) 
        
        What is our bottle neck here? well finding the node
            -> what will allow us to look up stuff in O(1) time? Hashtable 
            
        So our datastructure will..
        """
        self.mapping = {}
        self.capacity = capacity 
        self.head = DLLNode(-1, -1)
        self.tail = DLLNode(-1, -1)
        self.head.next = self.tail 
        self.tail.prev = self.head 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # check if node exists in our hashtable 
        if key not in self.mapping:
            return -1 
        
        currNode = self.mapping[key] 
        self._remove(currNode)      # REMOVE the node from the dll 
        self._add(currNode)         # APPEND the node to the tail as its MRU
        return currNode.val         # return the node value 

    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if the node exists
        if key in self.mapping:         # overwrite the node if it does exist
            currNode = self.mapping[key]
            currNode.val = value        # update the node's value
            self._remove(currNode)      # REMOVE the node from  the dll
            self._add(currNode)         # APPEND the node to the tail  
        else:            # if the node does not exist 
            if len(self.mapping) == self.capacity:  # check our current size of the dll
                self._remove(self.head.next)     # if it's at capacity evict the LRU node aka REMOVE head 
            newNode = DLLNode(key, value)
            self._add(newNode)            # APPEND our node to tail 

    def _remove(self, node):
        """
        pn                nn
        (h) <--> (1) <--> (2) <--> tail
                  r 
                  
        1. p
        """
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode 
        node.prev = None 
        node.next = None
        del self.mapping[node.key]
    
    def _add(self, node):
        """
                           pn 
        (h) <--> (1) <--> (2)  tail
                            <---> (3) 
        """
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node 
        self.mapping[node.key] = node 

        

        
        
        
        
        
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
