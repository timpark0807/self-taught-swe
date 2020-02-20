class DLLNode:
    
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None 
        
class LRUCache(object):

    """    
    Checklist: 
    Brute Force
    Edge Cases
    Assumptions
    Test Cases
    
    Toolbox
    
        - Doubly Linked List
            - key 
            - value 
            - prev
            - next
        
        CAPACTIY = 2
        
      LRU
     (head)  <-> (4) <-> (1) <-> (3) <-> (tail)
                                          MRU
        
        - Hashtable 
            {key:node}
            {3:(3), 4:(4), (1):1}
            
    Input
    Output
    
    Highlevel
    Docstrings
    
    Goal: Get
          - Return the value of the key we are looking for 
          - Note: We should reset the node to the most recently used value 
    to 
    
    Task 
          - Check if key is in the cache -> use a hashtable 
            - If not in cache: return -1
          - If key is in the cache:
            - get a reference to the actual node 
            - remove the node from the DLL 
            - add the node to the tail 
    
    

    """
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.capacity = capacity
        self.head = DLLNode(-1, 'head')
        self.tail = DLLNode(-1, 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head 
        
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 
        node.prev = None
        node.next = None
        del self.cache[node.key]
        
    def _add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev 
        self.tail.prev.next = node
        self.tail.prev = node
        self.cache[node.key] = node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
    
        Goal for Get
              - Return the value of the key we are looking for 
              - Note: We should reset the node to the most recently used value 
        to 

        Task 
              - Check if key is in the cache -> use a hashtable 
                - If not in cache: return -1
              - If key is in the cache:
                - get a reference to the actual node 
                - remove the node from the DLL 
                - add the node to the tail 
        
            """
        if key not in self.cache:
            return -1
        else:
            curr_node = self.cache[key]
            self._remove(curr_node)
            self._add(curr_node)
            return curr_node.val 
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        
        
        Goal: Put
               - Insert a node
               - Check capacity and evict
        Task: 
               - Check if the key exists in our cache
               - If it does
               - get a reference to the actual node as curr node 
               - Update the value of curr node 
               - remove the curr node from the DLL

               - else:
                    create a new node that is curr node 

               - Insert currnode to the tail of the DLL (most recently used)
               - Add currnode to the hashtable 


               - Check capacity, evict the head.next

        """
        # TODO: Check what happens when the list is empty 
        if key in self.cache:
            curr_node = self.cache[key]
            self._remove(curr_node)
            
        curr_node = DLLNode(key, value)
        self._add(curr_node)
        
        if len(self.cache) > self.capacity:
            self._remove(self.head.next)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
