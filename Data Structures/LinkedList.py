class Node:
    
    def __init__(self, data=None, next=None):
        self.data= data
        self.next = next

    def __str__(self):
        return str(self.data)

class LinkedList:
    
    def __init__(self):
        self.head = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def newHead(self, newhead):
        new_head = Node(newhead)
        new_head.next = self.head
        self.head = new_head
        
    def insertNode(self, newdata):
        current_node = self.head
        while current_node is not None:
            if current_node.next is None:
                current_node.next = Node(newdata)
                return self.head
            current_node = current_node.next
        
    def deleteNode(self, deletenode):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == deletenode:
                if previous_node is None: 
                    newHead = current_node.next
                    current_node.next = None
                    return newHead
                previous_node.next = current_node.next
                return self.head
            previous_node = current_node
            current_node = current_node.next
        return self.head


llist = LinkedList()

llist.head = Node('Mon')

llist.listprint()

print("*" * 30)

llist.insertNode('Tues')
llist.insertNode('Wed')
llist.insertNode('Thurs')

llist.listprint()

print("*" * 30)

llist.deleteNode('Thurs')

llist.listprint()

print("*" * 30)

llist.newHead('Sun')

llist.listprint()

print("*" * 30)

print(llist.head)
