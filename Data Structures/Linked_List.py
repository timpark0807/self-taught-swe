import unittest

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f'{self.val}'

class LinkedList:
    """
    Implementation of a singly Linked List.

    Provides the following methods in the associated time complexity:
    
    search   :  O(n)
    insert   :  O(1)
    delete   :  O(1)
    reverse  :  O(n)
    is_cycle :  O(n)
    get_mid  :  O(n)
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
        Input  : Integer
        Output : Bool
        
        Search by Key.
        """
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def insert(self, val):
        """
        Input  : Integer
        Output : None
        
        Insert a new Node object to the end of the Linked List. 
        """
        current = self.tail
        current.next = Node(val)
        self.tail = current.next
        self.size += 1

    def delete(self, node_to_delete):
        """
        Input  : Node
        Output : None

        Delete a node by reference. If node is tail, deletion takes O(n).  
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
        Output : String

        Helper method for __str__ method. 
        Iterate's through nodes in linked list and returns a string in format:

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
        Output : Bool

        Uses Floyd's algorithm to detect if there is a cycle in the Linked List.
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

        Reverses the linked list in place and returns the new head.
        ** WILL DESTROY ORIGINAL LIST **
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

        Returns the mid point of the linked list.
        """   
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.head = Node(0)
        self.linkedlist = LinkedList(self.head)
        for i in range(1, 6):
            self.linkedlist.insert(i)
            
    def tearDown(self):
        self.linkedlist = None

    def test_len(self):
        self.assertEqual(len(self.linkedlist), 6)
        for i in range(6, 50):
            self.linkedlist.insert(i)
        self.assertEqual(len(self.linkedlist), 50)

    def test_search(self):
        self.assertTrue(self.linkedlist.search(0))
        self.assertTrue(self.linkedlist.search(2))
        self.assertTrue(self.linkedlist.search(5))
        self.assertFalse(self.linkedlist.search(99))
        
    def test_delete_from_middle(self):
        self.linkedlist.delete(self.head.next.next.next)
        self.assertEqual(self.linkedlist._traverse(), '0 -> 1 -> 2 -> 4 -> 5 -> None')
        self.assertEqual(self.linkedlist.size, 5)
        
    def test_delete_head(self):
        self.linkedlist.delete(self.linkedlist.head)
        self.assertEqual(self.linkedlist._traverse(), '1 -> 2 -> 3 -> 4 -> 5 -> None')
        self.assertEqual(self.linkedlist.size, 5)
        
    def test_delete_tail(self):
        self.linkedlist.delete(self.linkedlist.tail)
        self.assertEqual(self.linkedlist._traverse(), '0 -> 1 -> 2 -> 3 -> 4 -> None')
        self.assertEqual(self.linkedlist.size, 5)

    def test_detect_cycle_false(self):
        self.assertFalse(self.linkedlist.is_cycle())
        
    def test_detect_cycle_true(self):
        self.linkedlist.tail.next = self.linkedlist.head
        self.assertTrue(self.linkedlist.is_cycle())

    def test_reverse(self):
        self.assertEqual(self.linkedlist._traverse(), '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None')
        self.linkedlist.reverse()
        self.assertEqual(self.linkedlist._traverse(), '5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None')
        
    def test_get_mid(self):
        self.assertEqual(self.linkedlist.get_mid().val, 3)
        self.linkedlist.delete(self.linkedlist.head)
        self.linkedlist.delete(self.linkedlist.head)
        self.linkedlist.delete(self.linkedlist.head)
        self.assertEqual(self.linkedlist.get_mid().val, 4)

if __name__ == '__main__':
    unittest.main()
