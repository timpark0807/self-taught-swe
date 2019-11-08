class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return self.data

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.d = dict()

        self.head = Node('h')
        self.tail = Node('t')
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        curr = self.head.next
        answer = []
        while curr.next:
            answer.append(curr.data)
            curr = curr.next

        print(answer)
        return ''
    
            
    def __len__(self):
        return self.size

    def get(self, key):
        if key in self.d:
            # Find reference to key
            node = self.d[key]

            # Break nodes prev and next reference
            node.prev.next = node.next
            node.next.prev = node.prev

            # bring node to the front
            temp = self.head.next
            self.head.next = node
            node.prev = self.head
            node.next = temp
            temp.prev = node
            
            return node.data[1]
        
        return -1

    def put(self, key, value):
        if self.size == self.capacity:
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail

            self.size -= 1
            
        # Insert a node to the beginning of the list
        new_node = Node((key, value))

        temp = self.head.next    
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = temp 
        temp.prev = new_node

        # add its reference to the dict
        self.d[key] = new_node

        self.size += 1
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lru = LRUCache(3)
lru.put(10, 1)
print(lru)
lru.put(4, 2)
print(lru)
lru.put(6, 3)
print(lru)
lru.get(10)
print(lru)
lru.put(15, 4)
print(lru)
