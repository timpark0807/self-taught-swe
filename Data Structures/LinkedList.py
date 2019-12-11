class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val}'

class LinkedList:
    """
    Class representation of a singly Linked List.

    We initialize this linked list with a head node.
    
    +----------------+------+-------+
    |   Operation    | Time | Space |
    +----------------+------+-------+
    | Search         | O(n) |  O(1) | 
    | Insert         | O(1) |  O(1) |
    | Delete         | O(1) |  O(1) |
    | Reverse        | O(n) |  O(1) | 
    | Is Cycle?      | O(n) |  O(1) |
    | Get Mid Node   | O(n) |  O(1) |
    +----------------+------+-------+
    """
    
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.size = 1

    def __len__(self):
        return self.size

    def __str__(self):
        return f'Linked List: {self._traverse()}'
    
    def search(self, val):
        """
        Input  : int
        Output : boolean
        
        Description:
            - Search a node by value.
        """
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def insert(self, val):
        """
        Input  : int
        Output : None
        
        Description:
            - Insert a new Node object to the end of the Linked List. 
        """
        current = self.tail
        current.next = Node(val)
        self.tail = current.next
        self.size += 1

    def delete(self, node_to_delete):
        """
        Input  : Node
        Output : None

        Description:
            - Delete a node by reference.
            - If the node to delete is the tail, deletion takes O(n).  
        """
        # Check if node is head
        if node_to_delete == self.head:
            self.head = self.head.next
            node_to_delete.next = None
            
        # Check if node is tail
        elif node_to_delete == self.tail:
            current = self.head
            while current.next != self.tail:
                current = current.next
            self.tail = current
            current.next = None
        else:
            temp = node_to_delete
            temp.val = temp.next.val
            temp.next = temp.next.next
            
        self.size -= 1

    def _traverse(self):
        """
        Input  : None
        Output : str

        Description:
            - Helper method for __str__ method. 
            - String representation of values in linked list
            
        Example:
            "0 -> 1 -> 2 -> 3 -> None" 
        """
        current = self.head
        temp = []
        while current:
            temp.append(str(current.val))
            current = current.next
            
        temp.append('None')
        output = ' -> '.join(temp)
        return output
        
    def is_cycle(self):
        """
        Input  : None
        Output : boolean

        Description:
            - Uses Floyd's algorithm to detect if there is a cycle in the Linked List.
        """
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
    
    def reverse(self):
        """
        Input  : None
        Output : Node

        Description:
            - Reverses the linked list in place and returns the new head.
            - THE ORIGINAL LIST WILL BE MODIFIED
        """
        self.tail = self.head
        prev = None
        current = self.head
        while current:
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        self.head = prev
        return self.head
            
    def get_mid(self):
        """
        Input  : None
        Output : Node

        Description:
            - Returns the mid point of the linked list.
        """   
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
