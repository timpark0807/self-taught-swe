import unittest

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
