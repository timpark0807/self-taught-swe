# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head  
        
        mid = self._get_mid(head)
        head2 = self._reverse(mid)
        new_head = self._merge(head, head2)
        return new_head 
    
    
    def _get_mid(self, head):
        slow = head
        fast = head 
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        if not fast:
            prev.next = None 
            return slow 
        elif fast:
            node = slow.next
            slow.next = None 
            return node
        
    
    def _reverse(self, head):
        prev = None
        
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp 
        
        return prev 
    
    
    def _merge(self, head, head2):
        dummy = ListNode('DUMMY')
        curr = dummy
        
        while head and head2:
            
            curr.next = head
            head = head.next
            curr = curr.next
            
            curr.next = head2
            head2 = head2.next
            curr = curr.next
        
        if head:
            curr.next = head
        if head2:
            curr.next = head2 
        return dummy.next
     
