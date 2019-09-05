# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
                
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        prev, current = dummy_head, dummy_head.next
        
        while current:
            if current.val == val:
                prev.next = current.next 
                current = prev.next
            else:
                prev = current
                current = current.next
    
        return dummy_head.next 


#                                            prev  
#                                                     cur     
#   head      
#     1   ->    2    ->    3   ->   4   ->    5   ->   6   ->   None

# Use dummy head for cases where linked list is None or 1 element long ...
