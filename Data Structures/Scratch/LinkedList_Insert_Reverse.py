class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            current_node = self.root
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def reverse(self):
        prev = None
        head = self.root
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        self.root = prev
        return prev


    def traversal(self):
        head = self.root
        output =[]
        while head:
            output.append(head.data)
            head = head.next
        return output
        
        
ll = LinkedList()
ll.insert(10)
ll.insert(15)
ll.insert(20)
print(ll.traversal())
ll.reverse()
print(ll.traversal())



    
            
