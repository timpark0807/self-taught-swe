# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        Key insight was realizing we need to keep track of odd's head
        and then find even's tail and set its next odd head

        The rest will fall into place logically
        """
        if not head:
            return head
        
        eventail = head
        oddhead = head.next
        oddtail = head.next
        
        while oddtail and oddtail.next:
            eventail.next = oddtail.next
            eventail = eventail.next
            oddtail.next = eventail.next
            oddtail = oddtail.next
            eventail.next = oddhead
            
        return head
