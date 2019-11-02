# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        
                             l1
        (10)  ->  (20)  ->  None
        
                                        l2
        (15)  ->  (20)  ->  (30)  ->  None
        
        
        new_val = 20
        
                                                                         curr 
        (0)   ->    (10)    ->   (15)   ->      (20)    ->  (20)    ->   (30)
        dum                                   
 
        """
        dummy = ListNode(0)
        current = dummy
        
        # Time: O(n + m)
        # Space: O(n + m) 
        # Where n is the length of list 1 and m is the length of list 2
        while l1 and l2:
            if l1.val <= l2.val:
                new_val = l1.val
                l1 = l1.next
            else:
                new_val = l2.val
                l2 = l2.next
            new_node = ListNode(new_val)
            current.next = new_node
            current = current.next
            
        if l1:
            while l1:
                current.next = ListNode(l1.val)
                l1 = l1.next
                current = current.next
        if l2:
            while l2:
                current.next = ListNode(l2.val)
                l2 = l2.next
                current = current.next
                
        return dummy.next
    
