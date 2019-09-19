# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True
        
        count_pointer = head
        count = 0 
        while count_pointer:
            count += 1
            count_pointer = count_pointer.next
        
        current = head
        prev = None
        for i in range(count//2):
            temp = current
            current = current.next
            temp.next = prev
            prev = temp
        
        if count % 2 != 0:
            current = current.next
            
        while current and prev:
            if current.val != prev.val:
                return False
            else:
                current = current.next
                prev = prev.next
        
        return current == None and prev == None
        
