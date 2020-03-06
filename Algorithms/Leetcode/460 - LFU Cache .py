class Node:
    def __init__(self, key, val, freq=1):
        self.k = key
        self.v = val
        self.f = freq
        self.next = None
        self.prev = None 

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        
        Needed
            Dictionary to access nodes in O(1) 
            Dictionary to store frequency
            
        freq =  
                                 t 
            1 : (h) <-> (1) <-> (4) <->   (t)
                                      (5)->
            2 : (h) <-> (3) <-> (t)
            3 : LRU 
        
        nodes = 
            1 : (1)
            3 : (3) 
            
        """
        self.freq = {} 
        self.nodes = {} 
        self.capacity = capacity 
        
    def remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev 
        lru = self.freq[node.f]
        self.freq[node.f][2] -= 1 
        self.lru_is_empty(node.f)
        del self.nodes[node.k]

    def add(self, node, new_freq):
        self.lru_exists(new_freq)
        self.nodes[node.k] = node 
        lru = self.freq[new_freq]
        curr_tail = lru[1]
        temp = curr_tail.prev
        node.next = curr_tail 
        curr_tail.prev.next = node
        curr_tail.prev = node 
        node.prev = temp 
        lru[2] += 1 
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        0. If key doesn't exist, return -1 
        1. Get a reference to the node in the nodes dict()
        2. Remove this node from the current freq LRU
            -> If curr_freq LRU is len(2), delete the LRU from the freq dict() 
        3. Add this node to the curr_freq + 1 LRU 
            -> If curr_freq + 1 does not exist in freq
            -> Initialize a LRU head/tail structure  
        """
        if key not in self.nodes:
            return -1 
        
        curr_node = self.nodes[key] 
        curr_freq = curr_node.f
        new_freq = curr_freq + 1 
        
        self.remove(curr_node)
        self.add(curr_node, new_freq) 
        curr_node.f = new_freq 
        
        return curr_node.v 
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        
        1. Check if this key already exists
            -> If it does, remove the node from the current LRU
            -> Add the node to the curr_freq + 1 
            
        2. Else, node doesn't exist
            -> Check if we are at capacity
                -> If we are, evict the head.next node from the min LRU 
                -> If min LRU is len(2), delete the LRU from freq dict() 
            -> Add the current node to the 1 freq dict()
        """
        
        if key in self.nodes:
            curr_node = self.nodes[key]
            curr_freq = curr_node.f
            new_freq = curr_freq+1
            
            self.remove(curr_node) 
            self.add(curr_node, new_freq) 
            curr_node.f = new_freq
            curr_node.v = value 
            
        else:
            if self.is_capacity() and self.evict_lfu_lru():
                return
            new_node = Node(key, value)
            self.add(new_node, 1) 

    def evict_lfu_lru(self):
        if not self.freq.keys():
            return True
        min_freq = min(self.freq.keys())
        min_head, min_tail, f = self.freq[min_freq]
        self.remove(min_head.next)
        return False 
    
    def is_capacity(self):
        return len(self.nodes) == self.capacity 
    
    def lru_is_empty(self, curr_freq):
        if self.freq[curr_freq][2] == 2:
            del self.freq[curr_freq] 
            
    def lru_exists(self, new_freq):
        if new_freq not in self.freq:
            self.create_lru(new_freq) 
            
    def create_lru(self, new_freq):
        head = Node('head', 'head', new_freq)
        tail = Node('tail', 'tail', new_freq)
        head.next, tail.prev = tail, head
        self.freq[new_freq] = [head, tail, 2] 
        
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
