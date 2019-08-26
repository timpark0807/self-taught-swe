class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self, root):
        self.root = root
    
    def reverse(self):
        head = self.root
        prev = None

        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        self.root = prev
        return self.root

    def traversal(self):
        head = self.root
        while head:
            print(head.data)
            head = head.next


root = Node(10)
ll = LinkedList(root)
root.next = Node(15)
root.next.next = Node(20)
ll.traversal()
a = ll.reverse()
ll.traversal()
