class Item:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [[]] * (size + 1)

    def _hash(self, key):
        return key % self.size
    
    def put(self, key, value):
        hashIndex = self._hash(key)
        curr = self.table[hashIndex]
        for item in curr:
            if item.key == key:
                item.value == value
                return
        newItem = Item(key, value)
        curr.append(newItem) 

    def get(self, key):
        hashIndex = self._hash(key)
        curr = self.table[hashIndex]
        for item in curr:
            if item.key == key:
                return item.value
        return -1 

    def delete(self, key):
        hashIndex = self._hash(key)
        curr = self.table[hashIndex]
        for index, item in enumerate(curr):
            if item.key == key:
                curr = curr[:index] + curr[index+1:]
                return 
        
            
        
 
