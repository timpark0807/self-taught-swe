class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None 
        

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapping = [None] * 1000
        self.num = 1000
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashed_key = key % self.num 
        node = Node(key, value) 
        if not self.mapping[hashed_key]:
            self.mapping[hashed_key] = node
        else:
            curr = self.mapping[hashed_key]
            prev = None 
            while curr:
                if curr.k == key: # update value 
                    curr.v = value
                    return 
                prev = curr
                curr = curr.next
                
            prev.next = node # add the value 

            
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashed_key = key % self.num 
        if self.mapping[hashed_key]:
            curr = self.mapping[hashed_key]
            while curr:
                if curr.k == key:
                    return curr.v 
                curr = curr.next
        return -1 
    

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashed_key = key % self.num 
        curr = self.mapping[hashed_key]

        if not curr:
            return 
        
        if curr.k == key:
            self.mapping[hashed_key] = curr.next
            return 
        
        prev = None 
        while curr:
            if curr.k == key:
                prev.next = curr.next
                break 
            prev = curr
            curr = curr.next
                    

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)















